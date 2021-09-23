from setuptools import setup

setup(
  name='Yottab CLI',
  version='1.0.0',
  py_modules=['yottab'],
  install_requires=[
    'Click'
  ],
  entry_points='''
    [console_scripts]
    yb=yottab:cli
  ''',
)