
import asyncio
from model import prompt

from transformers import pipeline


async def translate(sentence,how):

    translator_pipeline = pipeline("translation_"+how,model="google-t5/t5-base",tokenizer="t5-base")

    return translator_pipeline(sentence)[0]["translation_text"]

async def entry(sentence,how):
    # Create asynchronous tasks for prompt and translate functions
    task1 = asyncio.create_task(prompt(sentence="analyze "+sentence+" for its sentiment and tell some ways to reply back within 50 words"))
    task2 = asyncio.create_task(translate(sentence,how))

    # Wait for both tasks to complete
    result1 = await task1
    result2 = await task2

    return "translated text: "+result2+"\nAnalysis:\n"+result1

