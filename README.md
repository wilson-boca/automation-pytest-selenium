# Learning PyTest

Following the course Elegant Automation Frameworks with Python and Pytest.
It's a Packt Video class.

## Install

Let's install <a href="https://virtualenvwrapper.readthedocs.io/en/latest/" target="_blank">virtualenvwrapper</a> it will make your life easier.

    $sudo pip install virtualenvwrapper

Add these lines into your bash profile:

    $export WORKON_HOME=$HOME/.virtualenvs
    $source /usr/local/bin/virtualenvwrapper.sh

Restart your terminal then type:

    $source /usr/local/bin/virtualenvwrapper.sh

### Create your ENV environment

    ### Create your ENV environment

Activate it with the command:

    $workon base-api

### To run pytest use

    $pytest or 
    $pytest -v //verbose
    $pytest -m engine //using mark
    $pytest -m "smoke or entertainment" //join marks
    $pytest -m "not entertainment" //all except this
    $pytest -m "smoke and body" //in this case we need both marks decorating the function
    $pytest --html="tests.html" //to generate html report



# pytest