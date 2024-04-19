from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    global bola
    bola += 1
    return f'valor de bola: {bola}'


@app.route('/interact')
def interact():  # put application's code here
    with open("bola.txt", "r") as file:
        file.write("0")


if __name__ == '__main__':
    app.run()
    print("chegou???")
