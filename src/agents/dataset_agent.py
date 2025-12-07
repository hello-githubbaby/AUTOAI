from .llm_client import call_llm

def generate_dataset(topic: str, n: int = 10):
    """
    Generate synthetic datasets using LLM.
    """

    prompt = f"""
    Generate a synthetic dataset with {n} rows about:
    {topic}

    Return the dataset as JSON array.
    """

    return call_llm(prompt)
