# Calculator

github repository: [Yanzzp/calculator (github.com)](https://github.com/Yanzzp/calculator)

## 1. Introduction

This is a web calculator implemented using Python's Flask framework and HTML, CSS and JS. HTML language can help me realize the appearance of this calculator, CSS can decorate this calculator, and implement the logic of the calculator through the Flask framework.

## 2. Self information

| **The Link Your Class**                    | https://bbs.csdn.net/ssynkqtd-04                          |
| :----------------------------------------- | :-------------------------------------------------------- |
| The Link of Requirement of This Assignment | https://blog.csdn.net/zpy737296/article/details/133647527 |
| The Aim of This Assignment                 | Implement a calculator                                    |
| MU STU ID and FZU STU ID                   | 21124566_832101119                                        |

## 3. PSP

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



## 4. Design and implementation process

      +-------------------+
      |   用户输入表达式 |
      +-------------------+
              |
              |
              v
      +-------------------+
      |   检查输入合法性 |
      |   (包括括号匹配) |
      +-------------------+
              |
              |
              v
      +-------------------+
      |   中缀转后缀表达式|
      |   (逆波兰表示法) |
      +-------------------+
              |
              |
              v
      +-------------------+
      |   计算后缀表达式  |
      |   (使用栈数据结构) |
      +-------------------+
              |
              |
              v
      +-------------------+
      |   显示计算结果   |
      +-------------------+
              |
              |
              v
      +-------------------+
      |   处理错误情况   |
      +-------------------+

## 5. Code block

```python
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
        return render_template('calculator2.html', result=result, expression=expression)
    except Exception as e:
        error_message = "Invalid input or calculation error: " + str(e)
        return render_template('calculator2.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
```



```html
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form method="POST" action="/calculate">
        <input type="text" name="expression" value="{{ expression }}">
        <button type="submit">Calculate</button>
        <button type="button" onclick="clearInput()">Clear</button>
        <p>{{ error_message }}</p>
        <h2>Result: {{ result }}</h2>
    </form>
    <br>
    <h3>Basic Operations:</h3>
    <p>Examples: 2+3, 5-2, 4*6, 8/4</p>
    <h3>Advanced Operations:</h3>
    <p>Examples: 2**3 (2^3), math.sin(30) (sine of 30 degrees)</p>
    <script>
        function clearInput() {
            document.querySelector('input[name="expression"]').value = '';
        }
    </script>
</body>
</html>

```

