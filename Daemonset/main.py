from flask import Flask
import http.client
import os



app = Flask(__name__)



@app.route('/')
def index():
    return "go away nothing to see here"

@app.route('/ping')
def ping():
    return "ping ok"



@app.route('/testnfs/<filename>')
def file(filename):
    with open("/nfsmount/"+filename, 'w') as f:
        if f.write("Writing to file "):
            return 'file write ok'.format(filename)
        else:
            return 'Failed to write to file'.format(filename)            

if __name__ == '__main__':
    try:
        WHOST = os.getenv('WHOST') # None
        WPORT = os.getenv('WPORT')
        HOSTNAME = os.getenv('HOSTNAME')
        connection = http.client.HTTPConnection(WHOST,WPORT)
        connection.request("GET", "register?hostname="+HOSTNAME)
        response = connection.getresponse()  
        data = response.read()
        print("DEBUG"+data)
    except:
        print("Could not register")
    app.run(host='0.0.0.0', port=8081)
    app.run(debug=True)

    