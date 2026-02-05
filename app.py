from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['num1'])
    b = float(request.form['num2'])
    op = request.form['operation']

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = "Error (Division by zero)" if b == 0 else a / b

    return render_template('index.html', result=result, num1=a, num2=b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
