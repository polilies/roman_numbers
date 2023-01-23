# Import Flask modules
from flask import Flask, redirect, url_for, render_template, request


def int_to_roman(num):
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    ans = (thousands + hundreds +
           tens + ones)
  
    return ans
    
# Create an object named app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = int(request.form['number'].title())
        print(f"number is : {number}")
        if 0 < number < 3999:
            
            roman_number = int_to_roman(number)
            return redirect(url_for('roman', number_decimal=number, number_roman= roman_number))
        else:
            return render_template('index.html', not_valid = True)
    else:
        return render_template('index.html', not_valid = False, developer_name="Alican KAYIKCI")


#
@app.route('/roman/<number_decimal>/<number_roman>', methods=['GET'])
def roman(number_decimal, number_roman):
    return render_template('result.html', number_decimal=number_decimal, number_roman=number_roman, developer_name="Alican KAYIKCI")
 

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)