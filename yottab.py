from file import FileManagment
import click
import api
import output

@click.group()
def cli():
  pass

#*****************USER****************
@cli.group()
@click.pass_context
def user(ctx):
  ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  ctx.obj['token'] = data['token']
  ctx.obj['user'] = data['user']



@user.command()
@click.option('--user', '-u',help='Username.')
@click.option('--email', '-e', help='Email address.')
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True, help='Account password.'
)
def register(user, email, password):
  """Register user in Yottab"""
  result = api.register(user, email, password)
  click.echo(output.register(result))



@user.command()
@click.option('--user', '-u',help='Username.')
@click.option(
    "--password", prompt=True, hide_input=True, help='Account password'
)
def login(user, password):
  result = api.login(user, password)
  click.echo(output.login(result))




@user.command()
@click.pass_context
def logout(ctx):
  if not ctx.obj['token']:
    exception = click.ClickException('You are not logged in.')
    raise exception
  result = api.logout(ctx.obj['token'])
  click.echo(output.logout(result))

#*****************WORKSPACE****************

@cli.group()
@click.pass_context
def workspace(ctx):
  ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  ctx.obj['token'] = data['token']
  ctx.obj['user'] = data['user']
  if not ctx.obj['token']:
    exception = click.ClickException('Please login first: yb user login -u <username>')
    raise exception


@workspace.command()
@click.option('-n', '--name', help='Workspace name.')
@click.option('-p', '--plan', help='Workspace plan')
@click.pass_context
def create(ctx, name, plan):
  result = api.createWorkspace(ctx.obj['token'], ctx.obj['user'], name, plan)
  click.echo(output.createWorkspace(result))

@workspace.command()
@click.pass_context
def list(ctx):
  result = api.workspaceList(ctx.obj['token'], ctx.obj['user'])
  click.echo(output.workspaceList(result))

@workspace.command()
@click.option('-w', '--workspace', help='Workspace name.')
@click.pass_context
def detail(ctx, workspace):
  result = api.workspaceDetail(ctx.obj['token'], ctx.obj['user'], workspace)
  result = output.workspaceDetail(result)
  click.echo(result)

@workspace.command()
@click.option('-w', '--workspace', help='Workspace name.')
@click.pass_context
def restart(ctx, workspace):
  result = api.restartWorkspace(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo(output.restartWorkspace(result))

@workspace.command()
@click.option('-w', '--workspace', help='Workspace name.')
@click.pass_context
def stop(ctx, workspace):
  result = api.stopWorkspace(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo(output.stopWorkspace(result))

@workspace.command()
@click.option('-w', '--workspace', help='Workspace name.')
@click.pass_context
def delete(ctx, workspace):
  result = api.deleteWorkspace(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo(output.deleteWorkspace(result))

@workspace.command()
@click.option('-w', '--workspace', help='Workspace name.')
@click.pass_context
def update(ctx, workspace):
  result = api.updateWorkspace(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo('result: %s' % result.isOk())

#****************************APP**********************
@cli.group()
@click.pass_context
def app(ctx):
  ctx.ensure_object(dict)
  fileM  = FileManagment()
  data = fileM.readFile()
  ctx.obj['token'] = data['token']
  ctx.obj['user'] = data['user']
  if not ctx.obj['token']:
    exception = click.ClickException('Please login first: yb user login -u <username>')
    raise exception

@app.command()
@click.argument('workspace')
@click.argument('productid')
@click.argument('name')
@click.pass_context
def create(ctx, workspace, productid, name):
  result = api.createApp(ctx.obj['token'], ctx.obj['user'], workspace, productid, name)
  click.echo('result: %s' % result.isOk())

@app.command()
@click.argument('workspace')
@click.pass_context
def list(ctx, workspace):
  result = api.appList(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo('result: %s' % result.getData())

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def start(ctx, workspace, appid):
  result = api.startApp(ctx.obj['token'], ctx.obj['user'], workspace, appid)
  click.echo('result: %s' % result.isOk())

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def stop(ctx, workspace, appid):
  result = api.stopApp(ctx.obj['token'], ctx.obj['user'], workspace, appid)
  click.echo('result: %s' % result.isOk())

@app.command()
@click.argument('workspace')
@click.argument('appid')
@click.pass_context
def delete(ctx, workspace, appid):
  result = api.deleteApp(ctx.obj['token'], ctx.obj['user'], workspace, appid)
  click.echo('result: %s' % result.isOk())

@app.command()
@click.argument('workspace')
@click.pass_context
def deleteServer(ctx, workspace):
  #result = api.deleteServer(ctx.obj['token'], ctx.obj['user'], workspace)
  click.echo('delete server: cookie=%s user=%s workspace=%s' % (ctx.obj['token'], ctx.obj['user'], workspace))

if __name__=='__main__':
  cli()