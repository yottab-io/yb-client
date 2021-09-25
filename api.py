import requests as request
import json
from result import result
from file import FileManagment

url = 'http://dezh.yottab.io/v1'

def register(user, email, password):
  response = request.post(url + '/user/register?format=json', json={'user': user, 'email':email, 'password':password})
  response = result(response)
  return response

def login(user, password):
  response = request.post(url + '/user/token?format=json', json={'user': user, 'password':password})
  response = result(response).getData()
  print(response)
  fileM  = FileManagment()
  fileM.writeFile(response['value'], user)
  return response

def logout(token):
  if token:
    response = request.get(url + '/user/token?format=json', headers={"X-Request-Token": '%s' % token})
    response = result(response)
    fileM  = FileManagment()
    fileM.clearFile()
  return 'logged out successfully'

def createWorkspace(token, user, name, plan):
  response = request.get(url + '/server/action/'+ user + '?format=json', json={'name': name, 'plan':plan}, headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def workspaceList(token, user):
  u = url + '/server/action/'+ user + '?format=json'
  response = request.get(u , headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def workspaceDetail(token, user, workspace):
  response = request.get(url + '/server/action/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def restartWorkspace(token, user, workspace):
  response = request.post(url + '/server/restart/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def stopWorkspace(token, user, workspace):
  response = request.post(url + '/server/stop/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def deleteWorkspace(token, user, workspace):  
  response = request.post(url + '/server/delete/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def updateWorkspace(token, user, workspace):
  response = request.post(url + '/server/setting/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def createApp(token, user, workspace, productid, name):
  response = request.post(url + '/server/app_create/'+ user + '/' + workspace + '?format=json', json={'product_id': productid, 'name':name}, headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def appList(token, user, workspace):
  response = request.get(url + '/server/apps/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def startApp(token, user, workspace, app_id):
  response = request.post(url + '/server/app_start/'+ user + '/' + workspace + '/' + app_id + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def stopApp(token, user, workspace, app_id):
  response = request.post(url + '/server/app_stop/'+ user + '/' + workspace + '/' + app_id + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def deleteApp(token, user, workspace, app_id):
  response = request.post(url + '/server/app_delete/'+ user + '/' + workspace + '/' + app_id + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response

def deleteServer(token, user, workspace):
  response = request.post(url + '/server/'+ user + '/' + workspace + '?format=json', headers={"X-Request-Token": '%s' % token})
  response = result(response)
  return response
