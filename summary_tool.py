from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_transcript(transcript):
    """
    Generates a detailed summary including financial impact.
    """
    prompt = f"""
You are an AI assistant.

Analyze the following YouTube transcript and generate:

1. A short summary (3-4 sentences)
2. Key points in bullet form
3. Main topics discussed
4. Learning insights (what someone can learn from the video)
5. Financial impact (if applicable, explain any financial implications, market effects, or business consequences)

Transcript:
{transcript}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )

        summary = response.choices[0].message.content
        return summary

    except Exception as e:
        return f"Error generating summary: {str(e)}"
