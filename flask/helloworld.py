# from flask import Flask
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/ok')
def example():
  return render_template('visualize.html', data=[], message='Hello world!')

#  return 'Ok'

@app.route('/dashboard')
def visualize():
#  print 'Dashboard'
#  flash('New entry was successfully posted')
  return 'Dashboard'
  #  return render_template('visualize.html', data=data)

if __name__ == "__main__":
  app.run()