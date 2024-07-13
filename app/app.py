from flask import Flask, request
from langchain_community.llms import Ollama
import chainlit as cl

app = Flask(__name__)

# Initialize LLaMA model
try:
    cached_llm = Ollama(model="llama3:latest")
except Exception as e:
    print(f"Error loading LLaMA model: {str(e)}")
    cached_llm = None

# Handle incoming messages using Chainlit
@cl.on_message
async def main(message: cl.Message):
    if cached_llm is None:
        await cl.Message("Error: LLaMA model not loaded").send()
        return

    try:
        # Generate response using LLaMA model
        response = cached_llm.invoke(message.content)
    except Exception as e:
        await cl.Message(f"Error generating response: {str(e)}").send()
        return

    # Send the response back
    await cl.Message(response).send()
