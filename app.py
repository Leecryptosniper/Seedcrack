from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Code to read and display the content of one of your text files
    with open('imported_wallets.txt', 'r') as file:
        content = file.read()
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)