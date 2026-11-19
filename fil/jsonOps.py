import json
# # Read from file and parse JSON
# jsonFile = open("files/test.json", "r")
# data = json.load(jsonFile)
# print(data)
# print(type(data)) # a list

# json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
# data_2 = json.loads(json_str) 
# print(data_2)
# print(type(data_2))#converts to a dict
# jsonFile = open("files/test.json", "r")
# out_all_as_string = jsonFile.read()
# data_3 = json.loads(out_all_as_string) 
# print(data_3)

# jsonFile = open("files/new_sample_b.json", "w")
# data_toSave_2= {"name":"mandy", "fav_col":"blue", "fav_city":["list",3,4,True,"abc"]}
# json.dump(data_toSave_2,jsonFile, indent =4)

jsonFile = open("files/new_sample_b.json", "r+")
data = json.load(jsonFile)
# print(data['fav_city'])
# print(type(data['fav_city']))
# #go to beginning of file
jsonFile.seek(0)
data['fav_city'].append("another element")
data["newKey"] = 1234
#output to the file
json.dump(data,jsonFile, indent =4)