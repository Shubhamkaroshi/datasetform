from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def addNews():
    return render_template('datasetForm.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)