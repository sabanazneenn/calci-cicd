from flask import Flask, request, render_template_string
import subprocess
import os
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: #f4f7f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .container {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            width: 350px;
        }}

        h2 {{
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }}

        input, select, button {{
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }}

        button {{
            background: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        button:hover {{
            background: #0056b3;
        }}

        .result {{
            margin-top: 15px;
            padding: 10px;
            background: #e9f7ef;
            border-left: 5px solid #28a745;
            color: #155724;
            font-weight: bold;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Bash Calculator</h2>
        <form method="post">
            <input type="text" name="num1" placeholder="Enter first number" required>
            <select name="operation">
                <option value="+">Addition (+)</option>
                <option value="-">Subtraction (-)</option>
                <option value="*">Multiplication (*)</option>
                <option value="/">Division (/)</option>
            </select>
            <input type="text" name="num2" placeholder="Enter second number" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calc():
    result = None
    if request.method == 'POST':
        try:
            num1 = request.form['num1']
            num2 = request.form['num2']
            operation = request.form['operation']
            script_path = os.path.join(os.path.dirname(__file__), 'calci.sh')

            output = subprocess.check_output(['bash', script_path, num1, num2, operation])
            result = output.decode('utf-8').strip()
        except Exception as e:
            print("ERROR:", traceback.format_exc())
            result = f"Error: {str(e)}"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

