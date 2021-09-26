from setuptools import setup, find_packages

setup(
  name='YottabCLI',
  version='1.0.0',
  py_modules=['yottab'],
  install_requires=[
    'Click',
    'tabulate',
    'requests'
  ],
  entry_points='''
    [console_scripts]
    yb=yottab:cli
  ''',
)