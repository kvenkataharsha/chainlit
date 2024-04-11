from openai import AsyncOpenAI
import chainlit as cl
import os

api_key = os.environ.get("OPENAI_API_KEY")

client = AsyncOpenAI(api_key=api_key)
cl.instrument_openai()

# setting for openai model
settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.4,
}

# on chat start it asks file from user
@cl.on_chat_start
async def start():
    await cl.Message(content="Hello!").send()

    files = None
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a text file to begin!",
            accept=["text/csv"],
            max_size_mb=100,
            timeout=180,
        ).send()

    file = files[0]

    # processing message to user
    msg = cl.Message(content=f"Processing `{file.name}`...", disable_feedback=True)
    await msg.send()

    with open(file.path, "r", encoding="utf-8") as f:
        text = f.read()

    # setting data in user session
    cl.user_session.set('data', text)

    # Complete message to user
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

# on message it takes question from user and gives answer
@cl.on_message
async def on_message(message: cl.Message):

    # retriving data from user session
    df = cl.user_session.get('data')
    print(df, message.content)

    # calling OpenAI model
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, who takes csv file as input and writes code to answer questions based on the data.",
                "role": "system"
            },
            {
                "content": df + "\n" + "Based on the above csv data, write a code for the follwing question:" + message.content,
                "role": "user"
            }
        ],
        **settings
    )
    # Response from OpenAI model
    await cl.Message(content=response.choices[0].message.content).send()
