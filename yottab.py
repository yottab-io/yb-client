from click.decorators import pass_context
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
@click.pass_context
def workspace(ctx):
  ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  ctx.obj['cookies'] = data['cookies']
  ctx.obj['user'] = data['user']


@workspace.command()
@click.argument('name')
@click.argument('plan')
@click.pass_context
def create(ctx, name, plan):
  #result = api.createWorkspace(ctx.obj['cookies'], ctx.obj['user'], name, plan)
  click.echo('create workspace: cookies=%s user=%s name=%s plan=%s' % (ctx.obj['cookies'], ctx.obj['user'], name, plan))

@workspace.command()
@click.pass_context
def list(ctx):
  #result = api.workspaceList(ctx.obj['cookies'], ctx.obj['user'])
  click.echo('list workspace: cookie=%s user=%s' % (ctx.obj['cookies'], ctx.obj['user']))

@workspace.command()
@click.argument('workspace')
@click.pass_context
def detail(ctx, workspace):
  #result = api.workspaceDetail(ctx.obj['cookies'], ctx.obj['user'], workspace)
  click.echo('workspace detail: cookie=%s user=%s workspace=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace))

@workspace.command()
@click.argument('workspace')
@click.pass_context
def restart(ctx, workspace):
  #result = api.restartWorkspace(ctx.obj['cookies'], ctx.obj['user'], workspace)
  click.echo('restart workspace: cookie=%s user=%s workspace=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace))

@workspace.command()
@click.argument('workspace')
@click.pass_context
def delete(ctx, workspace):
  #result = api.deleteWorkspace(ctx.obj['cookies'], ctx.obj['user'], workspace)
  click.echo('delete workspace: cookie=%s user=%s workspace=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace))

@workspace.command()
@click.argument('workspace')
@click.pass_context
def update(ctx, workspace):
  #result = api.deleteWorkspace(ctx.obj['cookies'], ctx.obj['user'], workspace)
  click.echo('update workspace: cookie=%s user=%s workspace=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace))

#****************************APP**********************
@cli.group()
@click.pass_context
def app(ctx):
  ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  ctx.obj['cookies'] = data['cookies']
  ctx.obj['user'] = data['user']

@app.command()
@click.argument('workspace')
@click.argument('product')
@click.pass_context
def create(ctx, workspace, product):
  #result = api.createApp(ctx.obj['cookies'], ctx.obj['user'], workspace, product)
  click.echo('create app: cookie=%s user=%s workspace=%s product=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace, product))

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def start(ctx, workspace, appid):
  #result = api.startApp(ctx.obj['cookies'], ctx.obj['user'], workspace, appid)
  click.echo('start app: cookie=%s user=%s workspace=%s appid=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace, appid))

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def stop(ctx, workspace, appid):
  #result = api.stopApp(ctx.obj['cookies'], ctx.obj['user'], workspace, appid)
  click.echo('stop app: cookie=%s user=%s workspace=%s appid=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace, appid))

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def delete(ctx, workspace, appid):
  #result = api.deleteApp(ctx.obj['cookies'], ctx.obj['user'], workspace, appid)
  click.echo('delete app: cookie=%s user=%s workspace=%s appid=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace, appid))

@app.command()
@click.argument('workspace')
@click.pass_context
def deleteServer(ctx, workspace):
  #result = api.deleteServer(ctx.obj['cookies'], ctx.obj['user'], workspace)
  click.echo('delete server: cookie=%s user=%s workspace=%s' % (ctx.obj['cookies'], ctx.obj['user'], workspace))

if __name__=='__main__':
  cli()