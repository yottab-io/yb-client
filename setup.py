from setuptools import setup

setup(
  name = 'yb-client',
  version = '1.0.0',
  license = 'GNU General Public License v3.0',
  description = 'Yottab-Client is a command-line interface to interact with the Yottab server to create and manage workspaces and applications.',
  author = 'Yottab',
  author_email = 'admin@yottab.io',
  py_modules=['yb_client','yb_client.commands'],
  keywords = ['yottab', 'yottab client', 'command-line'],
  install_requires=[
    'Click',
    'tabulate',
    'requests'
  ],
  entry_points = {
    'console_scripts': ['yb=yb_client.commands:cli'],
  },
)