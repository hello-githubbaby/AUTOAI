"""
This is a minimal LLM abstraction layer.
- Works offline via placeholder response
- When OPENAI_API_KEY is present → uses real OpenAI API
"""

import os

def call_llm(prompt: str, max_tokens=400):
    api_key = os.getenv("OPENAI_API_KEY")

    # real LLM mode
    if api_key:
        try:
            import openai
            openai.api_key = api_key

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )

            return response["choices"][0]["message"]["content"]

        except Exception as e:
            return f"[LLM error: {e}]"

    # Offline fallback
    return f"[PLACEHOLDER RESPONSE]\nPrompt:\n{prompt[:800]}"
