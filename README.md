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

# To deploy over IIS
```sh
First check al IISS services enabled: CGI, ASP, .Net 3.5, .Net 4.6
https://github.com/JeevanSandhu/Documentation/blob/master/Flask%20API%20on%20IIS.md
https://www.youtube.com/watch?v=Cer6HwrVgyg&ab_channel=GyanOfPython
https://github.com/mayurvkorde/Flask-Application-On-IIS/blob/main/web.config
https://medium.com/@dpralay07/deploy-a-python-flask-application-in-iis-server-and-run-on-machine-ip-address-ddb81df8edf3
https://rajesh-r6r.medium.com/deploying-a-python-flask-rest-api-on-iis-d8d9ebf886e9
https://yunkgao.wordpress.com/2021/11/17/deploy-a-python-flask-application-in-iis-server-and-run-on-machine-ip-address/
https://mtuseeq.medium.com/how-to-deploy-flask-app-on-windows-server-using-fastcgi-and-iis-73d8139d5342
```