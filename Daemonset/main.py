from flask import Flask
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
    app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)