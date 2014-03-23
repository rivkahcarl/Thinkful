from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
        return render_template('home.html')
 
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/results', methods=['POST'])
def calculate_rate(base, percentage):
    return base * percentage

def calculate_tip(meal_base, tip_rate):
     """
    Calculates dollar amounts for tip using base meal cost
    """
    meal_base = 
    tip_value = calculate_rate(meal_base, tip_rate)
    return(tip_value)
    

def results():
  return render_template('results.html')

