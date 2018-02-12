# Backend
Backend for our ECSE 428 application

# Development Setup
We're using python 3+ with django v2. 
Ensure that the python and pip versions you use are configured 
for python 3+.

### Configure VirtualEnv
VirtualEnv ensures that you will have an isolated environment for this project

To create a new virtualenv
```
pip install virtualenv
virtualenv env
```

To activate the virtual env from a bash command line use
```
source env/bin/activate
```

### Install the Project Dependencies

Ensure you're in the virtual environment for the project, then run
```
pip install -r requirements.txt
```

### Installing New Packages

If you require a new package during development, ensure that you add a line for it in requirements.txt.
The easiest way to do this is to use the `--save` flag with pip.
```
pip install --save [package]
```

# Testing

Go into the timemachine folder

```
cd timemachine/
python manage.py test
```

# Style Checking & Linting

```
./test.sh
```
