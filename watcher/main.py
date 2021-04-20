from flask import Flask
import http.client

app = Flask(__name__)

@app.route('/')
def index():
    return "go away nothing to see here"

@app.route('/ping')
def ping():
    return "ping ok"

@app.route('/checkall')
def checkminions():
    DSHOST = os.getenv('DSHOST') # None
    DSPORT = os.getenv('DSPORT')
    connection = http.client.HTTPConnection(DSHOST,DSPORT)
    connection.request("GET", "/testnfs/ll")
    response = connection.getresponse()  
    data = response.read()

    print(data)
    return data    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
    app.run(debug=True)


