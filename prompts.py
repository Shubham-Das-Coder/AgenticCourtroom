def defender_prompt(context):
    return f"""You are a defense lawyer. Use the context below to defend your client:\n\n{context}"""

def critic_prompt(context):
    return f"""You are a prosecutor. Use the context below to make a strong case against the accused:\n\n{context}"""

def arbiter_prompt(defense, prosecution, context):
    return f"""
You are a judge. You have received arguments from both sides:

Defense: {defense}

Prosecution: {prosecution}

Based on the Indian Constitution and the context below, deliver a fair and constitutional verdict.

Context:
{context}
"""
