import json
import sys
import requests


def deleteRepository():
#  get_URL = 'https://dev.azure.com/'+Organization_Name+'/'+Project_Name+'/_apis/git/repositories/'+Repository_Name+'?api-version=5.1'
  get_URL = 'https://dev.azure.com/guptashreya21/deleteRepo/_apis/distributedtask/variablegroups?groupName='+sys.argv[1]+'&api-version=5.0-preview.1'
  get_ID_request = requests.get(url = get_URL , auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'))
  data = get_ID_request.json()
  print(data)
  variables_data = data["value"][0]["variables"]
  print(variables_data)

  POST_URL= " https://dev.azure.com/guptashreya21/test/_apis/distributedtask/variablegroups?api-version=5.1-preview.1"
  post_data = {  "variables": variables_data, "type": "Vsts", "name": "TryPost", "description": "A test variable group"}
  header = {"Content-type": "application/json"}
  post_request = requests.post(url = POST_URL, auth = ('guptashreya21','o6vnjl3lehhcv6brzatndur7u2jhcu6o5mbmsm2ia3put46vdy3q'), headers=header, data=json.dumps(post_data))
  dataa = post_request.json()
  print(dataa)
try:

  deleteRepository()
except KeyError:
  print("URL Incorrect. Check values for Repository/Organization/Project Name")
except ValueError:
  print("Incorrect Credentials")
except Exception as error:
  print(error)
