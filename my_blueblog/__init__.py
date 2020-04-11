from flask import Flask

app = Flask('my_bluelog')
app.config.from_pyfile('settings.py')


