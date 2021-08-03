from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('The eye-tracking is started!')
  os.system("python3 main.py")

if __name__ == '__main__':
  app.run(debug=True)
