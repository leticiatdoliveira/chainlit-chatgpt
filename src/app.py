import chainlit as cl
import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@cl.on_message
async def main(message: cl.Message):

    # Set LLM model to use in data processing
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "you are a helpful assistant"},
            {"role": "user", "content": message.content},
        ],
        temperature=1,
        max_tokens=20,
    )

    # Send a response back to the user
    await cl.Message(
        content=str(response)
    ).send()
