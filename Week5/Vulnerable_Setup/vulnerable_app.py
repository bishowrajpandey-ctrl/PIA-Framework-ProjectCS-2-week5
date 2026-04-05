from flask import Flask

app = Flask(__name__)

# MISCONFIGURATION: Debug mode ON
app.config['DEBUG'] = True

@app.route('/')
def home():
    return "Vulnerable Application Running"

if __name__ == '__main__':
    app.run()
