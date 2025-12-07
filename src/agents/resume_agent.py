from .llm_client import call_llm

def review_resume(resume_text: str):
    """
    Provide actionable improvements for a resume.
    """

    prompt = f"""
    You are a professional tech recruiter and resume reviewer.
    Review this resume and provide:

    - 5 improvement suggestions
    - A rewritten optimized summary
    - Skill gaps to fill

    RESUME:
    {resume_text}
    """

    return call_llm(prompt)
