from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'


########## main ###########
if __name__ == '__main__':
	app.run()

