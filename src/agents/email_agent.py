from .llm_client import call_llm

def summarize_email(email_text: str):
    """
    Summarize an email into 3 key bullet points.
    """

    prompt = f"""
    Summarize this email into exactly 3 bullet points.

    EMAIL:
    {email_text}
    """

    return call_llm(prompt)
