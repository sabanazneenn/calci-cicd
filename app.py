from flask import Flask, request

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Bash Calculator</title>
</head>
<body>
    <h2>Simple Bash Calculator</h2>
    <form action="/calculate" method="post">
        <input type="number" name="num1" placeholder="Enter first number" required><br><br>
        <input type="number" name="num2" placeholder="Enter second number" required><br><br>
        <label for="operation">Operation:</label>
        <select name="operation" required>
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    {result}
</body>
</html>
'''

import subprocess

@app.route("/", methods=["GET"])
def index():
    return html_template.format(result="")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    operation = request.form["operation"]

    try:
        output = subprocess.check_output(["./calci.sh", num1, num2, operation])
        result = output.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        result = f"<p style='color:red;'>Error: {e.output.decode('utf-8')}</p>"

    return html_template.format(result=f"<h3>{result}</h3>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

