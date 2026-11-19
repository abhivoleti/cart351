import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';


const MODEL_PATH = 'cookies.glb';

const canvas = document.getElementById('scene');
const info = document.getElementById('info');

// Basic scene setup
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 1.5, 4);

const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;

scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 2));
const sun = new THREE.DirectionalLight(0xffffff, 2);
sun.position.set(5, 10, 7);
scene.add(sun);

let mixer = null;
const clock = new THREE.Clock();


new GLTFLoader().load(
  MODEL_PATH,
  (gltf) => {
    const animations = gltf.animations;

    console.log('Number of animations:', animations.length);
    animations.forEach((clip, i) => console.log(`  ${i}: ${clip.name || '(unnamed)'}`));

    info.innerHTML = `Animations: ${animations.length}`
      + animations.map((clip, i) => `<br>${i}: ${clip.name || '(unnamed)'}`).join('');

    scene.add(gltf.scene);
    frameModel(gltf.scene);


    mixer = new THREE.AnimationMixer(gltf.scene); //doesnt play animations until clicked 

    // Stops the other animation and plays this one from the start
    function playOnly(action) {
      if (!action) return;
      mixer.stopAllAction();
      action.setLoop(THREE.LoopOnce); // play one time only
      action.clampWhenFinished = true; // hold the last frame instead of snapping back
      action.reset().play();
    }

    // One button per animation, in the order they appear in the file
    const controls = document.getElementById('controls');
    animations.forEach((clip, i) => {
      const action = mixer.clipAction(clip);
      const name = clip.name || `Animation ${i + 1}`;

      const button = document.createElement('button');
      button.textContent = name.charAt(0).toUpperCase() + name.slice(1); // captialize first letter i guess
      button.addEventListener('click', () => playOnly(action));
      controls.appendChild(button);
    });
  },
  undefined,
  (error) => {
    console.error('Error loading GLB:', error);
    info.textContent = `Couldn't load ${MODEL_PATH}. Check the console.`;
  }
);

// Points the camera at the model, whatever its size; might want to fuck around with this 
function frameModel(object) {
  const box = new THREE.Box3().setFromObject(object);
  const size = box.getSize(new THREE.Vector3()).length();
  const center = box.getCenter(new THREE.Vector3());

  controls.target.copy(center);
  camera.position.copy(center).add(new THREE.Vector3(0, size * 0.3, size * 1.2));
  camera.near = size / 100;
  camera.far = size * 100;
  camera.updateProjectionMatrix();
}

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

renderer.setAnimationLoop(() => {
  if (mixer) mixer.update(clock.getDelta());
  controls.update();
  renderer.render(scene, camera);
});