import json

class result :
  def __init__(self, result):
    self.statusCode = result.status_code
    if result.ok:
      self.status = 'Done'
      self.detail = result.content
    else:
      self.status = 'Error'
      self.detail = result.reason
  def json(self):
    json.dump(self)
  