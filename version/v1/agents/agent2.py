from version.v1.config import TOGETHER_MODELS
from version.v1.prompts import critic_prompt
from together import Together

def run_prosecutor(context, client):
    prompt = critic_prompt(context)
    response = client.chat.completions.create(
        model=TOGETHER_MODELS["prosecutor"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
