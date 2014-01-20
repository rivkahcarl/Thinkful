from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/family')
def family():
  return render_template('family.html')

@app.route('/education')
def education():
  return render_template('education.html')

"""
@app.route('/user')
@app.route('/user/<name>')

def user(name=None):
  return render_template('education.html', name=name)


def addition(num, num2):
    return num + num2

@app.route('/number')
@app.route('/number/<int:num>/<int:num2>')
def number(num=0, num2=0):
  result = addition(num, num2)  
  return render_template('number.html', num=num, num2=num2, result=result)

"""

 
if __name__ == '__main__':
  app.run(debug=True)



