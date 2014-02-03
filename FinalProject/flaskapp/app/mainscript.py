from flask import Flask, render_template
import K12counts
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/statistics')
def statistics():
    result = K12counts.main()
    return render_template('statistics.html', result = result)

#@app.route('/basic_numbers')
#@app.route('/sample_json')



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



