from config import TOGETHER_MODELS
from v1.prompts import defender_prompt
from together import Together

def run_defender(context, client):
    prompt = defender_prompt(context)
    response = client.chat.completions.create(
        model=TOGETHER_MODELS["defender"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
