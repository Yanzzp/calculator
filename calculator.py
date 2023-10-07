# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def calculator():
#     result = ""
#     if request.method == 'POST':
#         num1 = float(request.form['num1'])
#         num2 = float(request.form['num2'])
#         operation = request.form['operation']
#
#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             result = num1 * num2
#         elif operation == 'divide':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 result = "除数不能为零"
#
#     return render_template('calculator.html', result=result)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator2.html', result="")

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return render_template('calculator.html', result=result, expression=expression)
    except Exception as e:
        error_message = "Invalid input or calculation error: " + str(e)
        return render_template('calculator.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
