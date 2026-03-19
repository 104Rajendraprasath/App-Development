from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = []

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({'message': 'Student added successfully!'})

@app.route('/get-students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Expose API on LAN
