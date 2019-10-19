from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World Guillaume"

@app.route('/test')
def hello_world_t():
   return "Hello World Guillaume test"

if __name__ == '__main__':
   app.run()