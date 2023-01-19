from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

@app.route('/generate_password', methods=["GET"])
def generate_password():
    length = request.args.get("length", 8)
    complexity = request.args.get("complexity", "alpha_numeric")

    if complexity == "alpha_numeric":
        chars = string.ascii_letters + string.digits
    elif complexity == "alpha":
        chars = string.ascii_letters
    elif complexity == "numeric":
        chars = string.digits

    password = ''.join(random.choices(chars, k=length))
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
