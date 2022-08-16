# Install Backend Python Flask

```sh
cd app_backend
venv\Scripts\Activate
python get-pip.py
pip install -r requirements.txt
```

# To Run Backend

```sh
cd app_backend
set PYTHONPATH=.
set FLASK_APP=main.py
set FLASK_DEBUG=1
flask run
```