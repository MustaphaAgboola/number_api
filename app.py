from flask import Flask, jsonify
from math import sqrt, isqrt
import requests

app = Flask(__name__)

def get_factors(n):
    factors = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def get_fun_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        return response.text
    except:
        return f"{number} is an interesting number!"

@app.route('/api/<int:number>')
def number_properties(number):
    properties = {
        "number": number,
        "is_even": number % 2 == 0,
        "is_prime": is_prime(number),
        "factors": get_factors(number),
        "square": number ** 2,
        "square_root": round(sqrt(number), 2),
        "fun_fact": get_fun_fact(number)
    }
    
    # Additional properties
    properties["is_perfect_square"] = isqrt(number) ** 2 == number
    properties["sum_of_digits"] = sum(int(d) for d in str(number))
    properties["is_palindrome"] = str(number) == str(number)[::-1]
    
    return jsonify(properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)