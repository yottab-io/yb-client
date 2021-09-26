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

def createApp(output):
  return output['msg']

def appList(output):
  if(output['type'] == 'table'):
    message = ''
    headTable = []
    optionTable = []
    optionHeaders = ['option_name', 'option_value']
    headHeaders = ['name', 'state', 'id', 'product_id']
    for app in output['data']:
      headTable = [[app['name'], app['state'], app['id'], app['product_id']]]
      message = message + tabulate(headTable, headers=headHeaders, tablefmt="pretty", colalign=("right",)) + '\n'
      optionTable = []
      for option , value in app['options'].items():
        optionTable.append([option , value["val"]])
      message = message + tabulate(optionTable, headers=optionHeaders, tablefmt="pretty",  colalign=("left","left")) + '\n'
    return message
  else:
    return output['msg']
  
def startApp(output):
  return output['msg']

def stopApp(output):
  return output['msg']

def deleteApp(output):
  return output['msg']

def deleteServer():
  pass

def productList(output):
  if(output['type'] == 'table'):
    message = ''
    headTable = []
    optionTable = []
    optionHeaders = ['option_name', 'option_value']
    headHeaders = ['name', 'id', 'type']
    for app in output['data']:
      headTable = [[app['name'], app['id'], app['type']]]
      message = message + tabulate(headTable, headers=headHeaders, tablefmt="pretty") + '\n'
      optionTable = []
      for option , value in app['opt'].items():
        optionTable.append([option , value["val"]])
      message = message + tabulate(optionTable, headers=optionHeaders, tablefmt="pretty",  colalign=("left","left")) + '\n'
    return message
  else:
    return output['msg']