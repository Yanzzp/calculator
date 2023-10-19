from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://YanServer:123test@1.12.68.118:3306/test2'
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
