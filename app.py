from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        a = float(request.form.get("num1"))
        b = float(request.form.get("num2"))
        operation = request.form.get("operation")

        if operation == "add":
            result = a + b
        elif operation == "sub":
            result = a - b
        elif operation == "mul":
            result = a * b
        elif operation == "div":
            if b == 0:
                result = "Error: Division by zero"
            else:
                result = a / b
        else:
            result = "Invalid operation"

    except Exception as e:
        result = "Invalid input"

    return render_template(
        "index.html",
        result=result,
        num1=a,
        num2=b
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
