from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App is deployed with Python Flask!'

app.run(host='0.0.0.0', port=5001,debug=True)

# port mapping is done so that this application can be accessed by outside world