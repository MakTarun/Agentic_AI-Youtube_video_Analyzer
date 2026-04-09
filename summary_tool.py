from groq import Groq #Groq is a real installed package at this point.
from dotenv import load_dotenv
from transcript_tool import get_transcript
import os
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


DOMAIN_INSTRUCTIONS = {
    "General Knowledge": "Summarize in clear bullet points covering the main concepts.",
    "Finance": "Extract all financial metrics, numbers, percentages, and trends. Include specific figures like revenue, profit, growth rates, and market data. Format as bullet points.",
    "Sports": "Focus on match results, player performance, team strategies, and key statistics. Format as bullet points.",
    "Gaming": "Focus on gameplay mechanics, graphics, storyline, and overall experience. Format as bullet points.",
    "Tech": "Focus on technical innovations, features, use cases, and industry impact. Format as bullet points.",
    "Questions": "Extract and list every question raised or answered in the video. Format each as a numbered question ending with '?'."
}

def transcript_to_text(transcript):
    return " ".join(alls.text for alls in transcript)

def gaming_summary(transcript,domain="Gaming",mode="Summary"):
    transcript_text=transcript_to_text(transcript)
    instruction=(
        f"if len of video less than 25 min  then explain the game ,graphics,overall rating."
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=600
    )
    return response.choices[0].message.content

def tech_summary(transcript, domain="Tech", mode="Summary"):
    transcript_text = transcript_to_text(transcript)

    instruction = (
        f"You are an expert in {domain}. "
        f"{'Focus on technical innovations, features, use cases, and industry impact. Summarize in bullet points.' if mode == 'Summary' else 'Write a detailed technical explanation of the transcript.'}"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=600
    )
    return response.choices[0].message.content

def finance_summary(transcript):
    transcript_text = transcript_to_text(transcript)

    instruction = """
    You are a financial analyst.

    Extract all financial information from the transcript.

    STRICT RULES:
    - Return in bullet points
    - Clearly mention metrics like Revenue, Profit, Loss, Growth, Expenses, EBITDA, etc.
    - ALWAYS include numbers with units (%, million, billion, crore, etc.)
    
    IMPORTANT:
    After bullet points, add a section:

    Financial Data:
    Revenue: <value>
    Profit: <value>
    Growth: <value>
    Expenses: <value>

    Only include metrics that exist in the transcript.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=700
    )

    return response.choices[0].message.content
def questions_summary(transcript, domain="Questions"):
    transcript_text = transcript_to_text(transcript)

    instruction = (
        "Extract and list every question raised or answered in the transcript. "
        "Format each as a numbered question ending with '?'. "
        "If needed, translate into English."
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content
def sports_summary(transcript,domain="sports",mode="Summary"):
    transcript_text = transcript_to_text(transcript)
    instruction=(
        f"You are an expert in {domain}"
        f"Tell about venue where played and what happened if there was a rain in match"
        f"{'Summarize overall match result , high scorer and player of the match, higher wicket taker .' if mode=='Summary'else 'Write a detailed description of the following transcript.'}"
        f"{'tell magic moments of match ' if mode=='Summary' else 'describe Magic moment , who won by how much' }"
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=700
    )
    return response.choices[0].message.content


def summary(transcript, domain="General", mode="Summary"):
    transcript_text = transcript_to_text(transcript)

    instruction = (
        f"You are an expert in {domain}. "
        f"{'Summarize the following transcript in clear bullet points.' if mode == 'Summary' else 'Write a detailed description of the following transcript.'}"
        f" If the transcript is in Hindi or any other language, translate and respond in English only."
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": transcript_text}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content
if __name__ == "__main__":
    from transcript_tool import get_transcript
    url = input("Enter YouTube URL: ")
    transcript=get_transcript(url)
    print("\nSummary:\n")
    print(summary(transcript))
