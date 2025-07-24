import requests
from fastapi import FastAPI


def link_scrapper(link: str):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Give me the sizes this product is outfit is available in."
            },
            {
                "role": "user",
                "content": link
            }
        ]
    }
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers).text
    return response


app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.post("/search")
async def search(link: str):
    description = link_scrapper(link)
    return description