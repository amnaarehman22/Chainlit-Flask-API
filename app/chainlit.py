import chainlit as cl
import requests

backend_url = "http://127.0.0.1:5000/query"

# Define an on_message callback
@cl.on_message
async def handle_message(message: cl.Message):
    user_query = message.content
    try:
        # Send the user query to the Flask backend
        response = requests.post(backend_url, json={"query": user_query})
        response_data = response.json()
        response_message = response_data.get('response', 'No response received')
    except Exception as e:
        response_message = f"Error occurred: {str(e)}"

    # Send the response back to the Chainlit UI
    await cl.Message(response_message).send()

if __name__ == "__main__":
    cl.run()
