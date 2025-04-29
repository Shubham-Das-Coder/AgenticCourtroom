from version.v2.config import TOGETHER_MODELS
from version.v2.prompts import arbiter_prompt
from together import Together

def run_judge(defense, prosecution, context, client):
    prompt = arbiter_prompt(defense, prosecution, context)
    response = client.chat.completions.create(
        model=TOGETHER_MODELS["judge"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
