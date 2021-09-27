
    
# Installation Guide:

## Clone project:
  - https : `$ git clone https://gitlab.com/prsttn/yottab-cli.git`
  - ssh : `$ git clone git@gitlab.com:prsttn/yottab-cli.git`
  
## Running virtual environment:

  1. Chack if you have installed "virtualenv":

      `$ virtualenv --version`

  2. If you dont have virtualenv installed, install it:

      `$ pip install virtualenv --user`

     One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:

      `$ sudo apt-get install python-virtualenv`

  3. Once you have virtualenv installed, go to project directory, open a shell and create your own environment. 
  
      `$ virtualenv venv`

  4. whenever you want to work on the project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

      `$ . venv/bin/activate`

     If you are a Windows user, the following command is for you:

      `$ venv\scripts\activate`

     Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).
    And if you want to go back to the real world, use the following command:

      `$ deactivate`
        
## Install the project packages:

  `$ pip install --editable .`
    
   type `$ yb --help`.
   
