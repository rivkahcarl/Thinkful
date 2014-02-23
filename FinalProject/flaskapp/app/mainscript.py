from flask import Flask, render_template
import K12counts
import Collegecounts
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/K12statistics')
def statistics():
    result = K12counts.main()
    return render_template('K12statistics.html', result = result)

@app.route('/Collegestatistics')
def statistics2():
    result = Collegecounts.main()
    return render_template('Collegestatistics.html', result = result)

#@app.route('/basic_numbers')
#@app.route('/sample_json')


 
if __name__ == '__main__':
  app.run(debug=True)



