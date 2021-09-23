from file import FileManagment
import click
import api

@click.group()
def cli():
  pass

#*****************USER****************
@cli.group()
def user():
  pass



@user.command()
@click.argument('user')
@click.argument('email')
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True, help='Account password'
)
def register(user, email, password):
  """Register user in Yottab"""
  #result = api.register(user, email, password)
  click.echo('user register: name= %s email=%s password=%s' % (user, email, password))



@user.command()
@click.argument('user')
@click.option(
    "--password", prompt=True, hide_input=True, help='Account password'
)
def login(user, password):
  #result = api.login(user, password)
  click.echo('user logged in. name=%s password=%s' % (user,password))




@user.command()
@click.argument('user')
@click.option(
    "--password", prompt=True, hide_input=True, help='Account password'
)
def logout(user, password):
  #result = api.logout(user, password)
  click.echo('user logged out. name=%s password=%s' % (user,password))

#*****************WORKSPACE****************

@cli.group()
def workspace():
  """ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  print('dataaaaaaaaaa',data)
  print('data.cookie', data['cookies'])
  ctx.obj['cookies'] = data['cookies']
  ctx.obj['user'] = data['user']"""
  pass


@workspace.command()
@click.argument('name')
@click.argument('plan')
def create(name, plan):
  #result = api.createWorkspace(ctx.obj['cookies'], ctx.obj['user'], name, plan)
  click.echo('create workspace: name=%s plan=%s' % ( name, plan))

@workspace.command()
def list():
  click.echo('list workspace')

@workspace.command()
def detail():
  click.echo('workspace detail')

@workspace.command()
def restart():
  click.echo('restart workspace')

@workspace.command()
def delete():
  click.echo('delete workspace')

@workspace.command()
def update():
  click.echo('update workspace')

#****************************APP**********************
@cli.group()
def app():
  pass

@app.command()
def create():
  click.echo('create')

@app.command()
def start():
  click.echo('start app')

@app.command()
def stop():
  click.echo('stop app')

@app.command()
def delete():
  click.echo('delete app')

@app.command()
def deleteServer():
  click.echo('delete server')

if __name__=='__main__':
  cli()