# calculator



``` python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "除数不能为零"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

```



``` html
<!DOCTYPE html>
<html>
<head>
    <title>calculator</title>
</head>
<body>
    <h1>calculator</h1>
    <form method="POST">
        <input type="text" name="num1" placeholder="input the first number" required>
        <select name="operation">
            <option value="add">Addition</option>
            <option value="subtract">subtraction</option>
            <option value="multiply">multiplication</option>
            <option value="divide">division</option>
        </select>
        <input type="text" name="num2" placeholder="input the second number" required>
        <input type="submit" value="calculate">
    </form>
    <p>result: {{ result }}</p>
</body>
</html>

```



| **Personal Software Process Stages**    | Estimated Time (minutes) | Actual Time (minutes) |
| :-------------------------------------- | :----------------------- | :-------------------- |
| Planning                                | 10                       | 8                     |
| • Estimate                              | 2                        | 8                     |
| Development                             | 10                       | 4                     |
| • Analysis                              | 2                        | 4                     |
| • Design Spec                           | 2                        | 8                     |
| • Design Review                         | 2                        | 6                     |
| • Coding Standard                       | 2                        | 5                     |
| • Design                                | 2                        | 7                     |
| • Coding                                | 2                        | 8                     |
| • Code Review                           | 2                        | 6                     |
| • Test                                  | 2                        | 9                     |
| Reporting                               | 10                       | 20                    |
| • Test Report                           | 2                        | 10                    |
| • Size Measurement                      | 2                        | 4                     |
| • Postmortem & Process Improvement Plan | 2                        | 6                     |
| **Sum**                                 | 30                       | 6                     |