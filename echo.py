from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('form.html')

@app.route('/welcomePage', methods=['POST'])
def welcome():
	return render_template('input.html')


if __name__ == "__main__":
	app.debug = True
	app.run()