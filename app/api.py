from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    if request.is_json:
        data = request.get_json()
        user_query = data.get('query')
    else:
        user_query = request.form.get('query')

    # Process user_query as needed
    response = {'response': f'Received query: {user_query}'}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
