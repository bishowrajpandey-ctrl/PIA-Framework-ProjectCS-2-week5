from flask import Flask

app = Flask(__name__)

# FIXED: Debug mode OFF
app.config['DEBUG'] = False

@app.route('/')
def home():
    return "Secure Application Running"

if __name__ == '__main__':
    app.run()
