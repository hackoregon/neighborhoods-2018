# Main Parts of Repo

DOCKER related:

* `env.sample` - A sample env file to setup environmental variables
* bin directory - directory containing the startup and entrypoint scripts:
  * `build.sh` - This script runs a `docker-compose build` command, accepts 2 flags:
    * `-d` - Builds containers based on the `development-docker-compose.yml` file
    * `-p` - Builds containers based on the `production-docker-compose.yml` file
  * `start.sh` - This script runs a `docker-compose up` command, starting the containers and apps, accepts 2 flags:
    * `-d` - Starts containers based on the `development-docker-compose.yml` file
    * `-p` - Starts containers based on the `production-docker-compose.yml` file
  * `test.sh` - This script spins up and runs tests in test containers. and removes test container once the script is complete
  * Entrypoint scripts - These are run within the api container when `docker-compose up` is run:
    * `development-docker-entrypoint.sh` - Startup tasks for development container
    * `production-docker-entrypoint.sh` - Startup tasks for production container
    * `test-entrypoint.sh` -  Startup tasks for testing container
  * `create-api-project.sh` - Script which will remove the sample app and create a new api with specified project name. It assumes the default app created will be named `api`.
  * `remove-sample.sh` - This script removes the sample application - is called as part of the `create-api-project.sh` script.
* Backups directory - directory where you can store any database backups to restore into the local database Container; also contains the database restore script
* Docker-Compose Files -  2 files which compose containers and networking for each environment:
  * `development-docker-compose.yml` - This is a local dev environment, will spin up a local api container connecting with a local db. It will run the Django Dev Server with the DEBUG variable set to True.
  * `production-docker-compose.yml` - This is set to run a production-like environment, creating a api container running with gunicorn server, and green database pooling. It removes the local development database from the stack, connecting to a remote database for which the variables/creds are entered into the production vars in the `.env` file
* DOCKERFILEs:
  * `DOCKERFILE.db.development` - The DOCKERFILE for local database container
  * `DOCKERFILE.api.development` - The DOCKERFILE for local api container
  * `DOCKERFILE.api.production` - The DOCKERFILE for a production build of api

API Related:

* `gunicorn_config.py` - Config file for the gunicorn server

## Run this project locally

1. clone this repo
2. get a copy of the `.env` file from someone in the neighborhoods team (@hassanshamim or @AraOshin)
3. change your current working directory to this folder
2. Build the development containers using the command: `./bin/build.sh -d`. If this script won't run, you may need to confirm you have executable perms on all the scripts in the `./bin` folder: `$ chmod +x ./bin/*.sh` Feel free to read each one and assign perms individually, 'cause it is your computer :stuck_out_tongue_winking_eye: and security is a real thing.
3. Once this completes you will now want to start up the project. We will use the `start.sh` script for this, again using the `-d` flag to run locally:  `./bin/start.sh -d` The first time you run this you will see the database restores. You will also see the api container start up.

4. Open your browser and you will be able to access the Django REST framework browserable front end. The IP address you use will depend on your Docker hosting:

    * Windows 10 Pro + Docker for Windows, MacOS or Linux: API root `http://localhost:8000/api`, Swagger API schema `http://localhost:8000/schema`
    * Docker Toolbox running on Windows or Mac: API root `http://MACHINE-IP:8000/api`, Swagger API schema `http://MACHINE-IP:8000/schema`

        where `MACHINE-IP` is the IP address `docker-machine ip` returns.

5. You can stop the container using Ctrl-C to stop the process in the terminal window.

## Run the Tests

To run the tests:

1. Run `./bin/test.sh -d` - this will load the fixtures and run tests.

Currently this repo contains two type of tests:

* Unit tests which verify the expected data types are returned
* API tests, which verify correct status codes are returned when making calls to api endpoints