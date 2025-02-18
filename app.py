from flask import Flask, jsonify, request
from math import sqrt, isqrt
import requests

app = Flask(__name__)

def is_prime(n):
    n = abs(n)  # Handle negative numbers
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    n = abs(n)  # Handle negative numbers
    if n <= 1:
        return False
    sum_factors = sum(i for i in range(1, n) if n % i == 0)
    return sum_factors == n

def is_armstrong(n):
    n = abs(n)  # Handle negative numbers
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

def get_properties(n):
    n = abs(n)  # Handle negative numbers
    properties = []
    
    # Numeric sign property
    properties.append("negative" if n < 0 else "positive")
    
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    if is_armstrong(n):
        properties.append("armstrong")
    
    if is_prime(n):
        properties.append("prime")
        
    return properties

def get_fun_fact(n):
    original_n = n
    n = abs(n)
    
    if is_armstrong(n):
        num_str = str(n)
        power = len(num_str)
        fact = f"{original_n} is an Armstrong number because "
        parts = [f"{digit}^{power}" for digit in num_str]
        fact += " + ".join(parts) + f" = {n}"
        return fact
    
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        return response.text
    except:
        return f"{original_n} is an interesting number!"

def get_digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def process_number(input_number):
    try:
        number = int(input_number)
        
        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": get_properties(number),
            "digit_sum": get_digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }, 200
    
    except ValueError:
        return {
            "number": input_number,
            "error": True,
            "message": "Please provide a valid number"
        }, 400

@app.route('/number/<input_number>')
def number_properties(input_number):
    response, status_code = process_number(input_number)
    return jsonify(response), status_code

@app.route('/api/classify-number')
def classify_number():
    number = request.args.get('number')
    if number is None:
        return jsonify({
            "error": True,
            "message": "Query parameter 'number' is required"
        }), 400
    
    response, status_code = process_number(number)
    return jsonify(response), status_code

@app.errorhandler(Exception)
def handle_error(error):
    return jsonify({
        "error": True,
        "message": "An unexpected error occurred"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)