from flask import Flask, request, jsonify, send_from_directory
from langchain_community.llms import Ollama

app = Flask(__name__)

# Initialize LLaMA model
try:
    cached_llm = Ollama(model="llama3:latest")
except Exception as e:
    print(f"Error loading LLaMA model: {str(e)}")
    cached_llm = None

# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Endpoint for querying LLM
@app.route('/query', methods=['POST'])
def query():
    if cached_llm is None:
        return jsonify({'response': 'Error: LLaMA model not loaded'}), 500

    if request.is_json:
        user_query = request.json.get('query')
    else:
        user_query = request.form.get('query')

    if not user_query:
        return jsonify({'response': 'Error: No query provided'}), 400

    try:
        # Generate response using LLaMA model
        response = cached_llm.invoke(user_query)
    except Exception as e:
        return jsonify({'response': f"Error generating response: {str(e)}"}), 500

    return jsonify({'response': response}), 200

if __name__ == "__main__":
    app.run(debug=True)
