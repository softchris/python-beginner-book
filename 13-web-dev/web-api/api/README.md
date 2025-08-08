# Run backend

## Install

Set up virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

Install libraries

```sh
pip install flask flask-cors
```

## Run

```sh
python server.py
```

## Enable port

For this to work in GitHub Codespaces, the port needs to be enabled.

Make a note of the URL as you need to set `BASE_URL` in `frontend/` project.

