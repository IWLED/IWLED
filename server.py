from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_code', methods=['POST'])
def execute_code():
    data = request.get_json()
    code_to_execute = data.get('code', '')

    # تنفيذ الكود
    try:
        exec_result = exec(code_to_execute)
        response = {"success": True, "result": str(exec_result)}
    except Exception as e:
        response = {"success": False, "error": str(e)}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

