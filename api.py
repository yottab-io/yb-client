import requests as request
import json
import result
from file import FileManagment

url = 'http://dezh.yottab.io/v1'

def register(user, email, password):
  response = request.post(url + '/user/register', json=json.dump({user: user, email:email, password:password}))
  response = result(response)
  return result

def login(user, password):
  response = request.post(url + '/user/token', json=json.dump({user: user, password:password}))
  fileM  = FileManagment()
  fileM.writeFile(result.cookies[0].yb)
  return result.cookies

def logout(user, password):
  response = request.post(url + '/user/token', json=json.dump({user: user, password:password}))
  response = result(response)
  fileM  = FileManagment()
  fileM.clearFile()
  return result

def createWorkspace(cookies, user, name, plan):
  response = request.post(url + '/server/action/' + user , json=json.dump({name: name, plan:plan}),cookies=cookies)
  response = result(response)
  return result

def workspaceList(cookies, user):
  response = request.get(url + '/server/action/'+ user, cookies=cookies)
  response = result(response)
  return result

def workspaceDetail(cookies, user, workspace):
  response = request.get(url + '/server/action/'+ user + workspace, cookies=cookies)
  response = result(response)
  return result

def restartWorkspace(cookies, user, workspace):
  response = request.post(url + '/server/restart/'+ user + workspace, cookies=cookies)
  response = result(response)
  return result

def deleteWorkspace(cookies, user, workspace):  
  response = request.post(url + '/server/delete/'+ user + workspace, cookies=cookies)
  response = result(response)
  return result

def updateWorkspace(cookies, user, workspace):
  response = request.post(url + '/server/setting/'+ user + workspace, cookies=cookies)
  response = result(response)
  return result

def createApp(cookies, user, workspace, product):
  response = request.post(url + '/server/app_create/'+ user + workspace, json=json.dump(product), cookies=cookies)
  response = result(response)
  return result

def startApp(cookies, user, workspace, app_id):
  response = request.post(url + '/server/app_start/'+ user + workspace+ app_id, cookies=cookies)
  response = result(response)
  return result

def stopApp(cookies, user, workspace, app_id):
  response = request.post(url + '/server/app_stop/'+ user + workspace+ app_id, cookies=cookies)
  response = result(response)
  return result

def deleteApp(cookies, user, workspace, app_id):
  response = request.post(url + '/server/app_delete/'+ user + workspace+ app_id, cookies=cookies)
  response = result(response)
  return result

def deleteServer(cookies, user, workspace):
  response = request.post(url + '/server/'+ user + workspace, cookies=cookies)
  response = result(response)
  return result
