import json
import sys
import requests
import ast

def deleteRepository():
#  get_URL = 'https://dev.azure.com/'+Organization_Name+'/'+Project_Name+'/_apis/git/repositories/'+Repository_Name+'?api-version=5.1'
  get_URL = 'https://dev.azure.com/guptashreya21/deleteRepo/_apis/distributedtask/variablegroups?groupName='+sys.argv[1]+'&api-version=5.0-preview.1'
  get_ID_request = requests.get(url = get_URL , auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'))
  data = get_ID_request.json()
  print(data)
  print("------------------------------------")
  check = data["value"][0]["variables"]
  check["org"]["value"]= "HCL"
  print(check)
  print(data["value"][0]["id"])
  del data["value"][0]["variables"]

  print(data)

#  check = {u'name': {u'value': u'Shreya'}}
  data["value"][0]["variables"]= check
  print("-----------------------------")
  print(data)
#  for inner_dict in data["value"][0]:
#      for dict in inner_dict:
#          del dict["variables"]
#          print(dict)
 # a =  type(check)
 # print(a)
#  dict = json.loads(data)
#  print(dict)

#  data.pop("count")
#  print(data)


#  dict = json.loads(data)
#  if 'dict["value"][0]["variables"]' in dict:
#      del dict["value"][0]["variables"]
#      print(dict)
 # print("------------------------------")
 # json_string = json.dumps(data)
 # strObj= str.replace(json_string,"u'","'")
 # print(strObj)
 # typee =  type(strObj)
 # print(typee)
 # x = json.loads(strObj)
#  print(x["value"])


try:

  deleteRepository()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
