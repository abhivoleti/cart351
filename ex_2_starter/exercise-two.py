from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)

NASA_URL = "https://images-api.nasa.gov/search"

# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
# Task-1: GET REQUEST
@app.route("/t1", methods=["GET"])
def t1():
    return render_template("t1.html", have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():
    app.logger.info(request.args)
    user_input = request.args.get("searchCriteria", "")

    data = requests.get(NASA_URL, params={"q": user_input, "media_type": "image"}).json()
    items = data["collection"]["items"]

    if not items:
        return render_template("t1.html", have_results=False)

    imgFromNasa = items[0]["links"][0]["href"]
    description = items[0]["data"][0].get("description", "No description available.")

    return render_template("t1.html",
                           have_results=True,
                           description=description,
                           imgPath=imgFromNasa)

#*************************************************
#Task-2: GET REQUEST
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():
    app.logger.info(request.args)
    user_input = request.args.get("search_query", "")

    data = requests.get(NASA_URL, params={"q": user_input, "media_type": "image"}).json()

    encoded_image_links = []
    for item in data["collection"]["items"]:
        if "links" in item:
            encoded_image_links.append(item["links"][0]["href"].replace(" ", "%20"))

    return render_template("t2.html", images=encoded_image_links)
#*************************************************

#run

app.run(debug=True)