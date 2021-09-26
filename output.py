from tabulate import tabulate

def register(output):
  return output['msg']

def login(output):
  return output['msg']

def logout(output):
  return output['msg']

def createWorkspace(output):
  if output['type'] == 'table':
    table = []
    headers = ['name', 'state', 'plan']
    for workspace in output['data']:
      table.append([workspace['name'], workspace['state'], workspace['plan']])
    return tabulate(table, headers=headers, tablefmt="pretty")
  else:
    return output['msg']

def workspaceList(output):
  if output['type'] == 'table':
    table = []
    headers = ['name', 'state', 'plan']
    for workspace in output['data']:
      table.append([workspace['name'], workspace['state'], workspace['plan']])
    return tabulate(table, headers=headers, tablefmt="pretty")
  else:
    return output['msg']

def workspaceDetail(output):
  if output['type'] == 'table':
    wTable = []
    aTable = []
    wHeaders = ['worskspace_name', 'state', 'plan']
    aHeaders = ['app_name', 'id']
    for workspace in output['data']:
      wTable.append([ workspace['name'], workspace['state'], workspace['plan']])
      for app in workspace['apps']:
        aTable.append([app['name'], app['id']])
    wTable = tabulate(wTable, headers=wHeaders, tablefmt="pretty")
    aTable = tabulate(aTable, headers=aHeaders, tablefmt="pretty")
    return '%s \n %s' % (wTable, aTable)
  else:
    return output['msg']

def restartWorkspace(output):
  return output['msg']

def stopWorkspace(output):  
  return output['msg']
  pass

def deleteWorkspace(output): 
  return output['msg']

def updateWorkspace():
  pass

def createApp():
  pass

def appList():
  pass

def startApp():
  pass

def stopApp():
  pass

def deleteApp():
  pass

def deleteServer():
  pass