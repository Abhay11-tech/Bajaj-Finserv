from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.get_json()

    numbers = []
    alphabets = []

    for item in data.get("data", []):
        if item.isdigit():
            numbers.append(item)
        else:
            alphabets.append(item)

    response = {
        "status": "success",
        "user_id": "abhay_kumar_21022025",
        "college_email": "22bcs13112@cuchd.in",
        "college_roll_number": "13112",
        "array_for_numbers": numbers,
        "array_for_alphabets": alphabets,
        "is_success": True
    }
    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
