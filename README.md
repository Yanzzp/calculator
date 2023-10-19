# Calculator

## 第一次提交

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

## 第二次提交

| Key                               | Value                                                        |
| --------------------------------- | ------------------------------------------------------------ |
| The Link Your Class               | [https://bbs.csdn.net/forums/ssynkqtd-04](https://bbs.csdn.net/forums/ssynkqtd-04) |
| Link to the finished project code | [Yanzzp/calculator (github.com)](https://github.com/Yanzzp/calculator) |
| Objectives of This Assignment     | simple calculator                                            |
| MU STU ID and FZU STU ID          | 21124566_832101119                                           |

I used MySQL deployed on Tencent Cloud Server.

![image-20231019233023434](C:\Users\11057\AppData\Roaming\Typora\typora-user-images\image-20231019233023434.png)

后端简单的使用Flask框架

``` python
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://YanServer:123test@yanzzp.xyz/test2'
)
db = SQLAlchemy(app)


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(255))
    result = db.Column(db.String(255))


@app.route('/')
def calculator():
    calculations = Calculation.query.all()  # 获取所有计算记录
    return render_template('calculator2.html', result="", calculations=calculations)


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    calculations = Calculation.query.all()  # 获取所有计算记录
    try:
        result_val = eval(expression, {"__builtins__": None}, {"math": math})

        # 创建一个新的数据库记录并保存
        calculation = Calculation(expression=expression, result=str(result_val))
        db.session.add(calculation)
        db.session.commit()

        return render_template('calculator2.html', result=result_val, expression=expression, calculations=calculations)
    except Exception as e:
        error_message = "Invalid input or calculation error: " + str(e)
        return render_template('calculator2.html', error_message=error_message, calculations=calculations)



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```



#### Database calculation results displayed on the local page

![image-20231019235546356](C:\Users\11057\AppData\Roaming\Typora\typora-user-images\image-20231019235546356.png)


#### Database query results after calculation:

![image-20231019235437534](C:\Users\11057\AppData\Roaming\Typora\typora-user-images\image-20231019235437534.png)

