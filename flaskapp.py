from flask import Flask, json, request



app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/rich',methods=['POST'])
def getdata():
    if request.headers['Content-Type'] == 'application/json':
        print(json.dumps(request.json))
    return 'Successful'


if __name__ == "__main__":
    app.run(debug = True)