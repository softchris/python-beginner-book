# Run sample

## Routes

- `/`, default route, renders index.html
- `/products-template`, renders a template with data
- `/products`, renders JSON but allows you to filter via query params page and pageSize
- `/data`, just JSON
- `/data/<name>`, shows router param, good for loading specific products
- `/query?name`, takes a query parameter name


## Install

Set up virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

Install libraries

```sh
pip install flask
```

## Run

```sh
python server.py
```
