class FileManagment:
  def __init__(self):
    try:
      file=open('config.txt', 'x')
      file.close()
    except:
      pass

  def writeFile(self, ybCookie, user):
    file=open('config.txt', 'w')
    file.write("cookies='%s' \nuser='%s'" % (ybCookie, user))
    file.close()
    return 'successful writing'

  def clearFile(self):
    file=open('config.txt', 'w')
    file.write("")
    file.close()
    return 'successful clearing'

  def readFile(self):
    file = open('config.txt', 'r')
    firstLine = file.readline().rsplit('=')[1]
    user = file.readline().rsplit('=')[1]
    cookies =firstLine.rsplit('\n')[0]
    file.close()
    return {'cookies':cookies, 'user':user}
