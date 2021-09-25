import json

class result :
  def __init__(self, result):
    if result.ok:
      jsonResult = result.json()
      print(jsonResult)
      self.statusCode = jsonResult['code']
      self.msg = jsonResult['msg']
      try :
        self.data = jsonResult['data']
      except:
        pass
        
      self.ok = True
    else:
      print(result.reason)
      self.statusCode = result.status_code
      self.msg = result.reason
      self.ok = False
  def getData(self):
    return self.data
  def getStatusCode(self):
    return self.statusCode
  def getMsg(self):
    return self.msg
  def isOk(self):
    if self.ok:
      return 'Ok'
    return 'Err'
  