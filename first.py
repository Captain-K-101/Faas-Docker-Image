from flask import Flask,request
import docker
app = Flask(__name__)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        client = docker.from_env()
        number1 = request.form['one']
        number2 = request.form['two']
        return(client.containers.run("docker.io/library/lol-1",command=[str(number1),str(number2)]))
    return "Hello World!"

@app.route('/sub', methods=['GET', 'POST'])
def sub():
    if request.method == 'POST':
        client = docker.from_env()
        number1 = request.form['one']
        number2 = request.form['two']
        ret=str(int(number1)-int(number2))
        return(client.containers.run("docker.io/library/sub-1",command=[str(number1),str(number2)]))
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

#