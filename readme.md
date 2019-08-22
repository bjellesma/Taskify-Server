This is a server for the taskify app meant to handle backend API requests. These API requests will use mongodb for a database.

# Setup

## Dependencies

* Python 3.7+
* PIP (Pip Installs Packages) 19.1.1+
* Python3-venv

1. Activate the virtual environment with `source taskify-server_env.sh`
2. Once inside of the virtual environment, install packages with `pip install -r requirements`
3. Rename `.env-sample` as `.env` and enter your own values into this file

## Push to Heroku

1. `heroku login`
2. `sudo git push origin master`