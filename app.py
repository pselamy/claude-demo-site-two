from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''<ul>
<li>Item A</li>
<li>Item B</li>
<li>Item C</li>
</ul>'''

if __name__ == '__main__':
    app.run(port=5001)