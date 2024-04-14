import json
from openai import AsyncOpenAI
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=api_key)


async def create():
    # ... your existing create function code ...

    instructions = """You are a csv file analyzer, who takes csv file as input and writes code for generating requiered analysis asked by the user.
"""

    assistant = await client.beta.assistants.create(
        name="CSV file Analyzer",
        instructions=instructions,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview",
    )
    assistant_name = "math_tutor_and_weather_bot"
    # append key value pair to assistants.json

    def load_or_create_json(filename):
        try:
            return json.load(open(filename, "r"))
        except FileNotFoundError:
            return {}

    assistant_dict = load_or_create_json("assistants.json")
    assistant_dict[assistant_name] = assistant.id
    json.dump(assistant_dict, open("assistants.json", "w"))
    

if __name__ == "__main__":
    asyncio.run(create())
