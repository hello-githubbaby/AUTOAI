from .llm_client import call_llm

def interpret_video_transcript(transcript: str):
    """
    Extract meaning from a video transcript.
    """

    prompt = f"""
    You are an AI that analyzes video transcripts.
    Provide:

    - A concise summary
    - Key moments/events
    - Sentiment
    - Actionable insights

    TRANSCRIPT:
    {transcript}
    """

    return call_llm(prompt)
