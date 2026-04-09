from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(url):
    parsed_url=urlparse(url)
    
    if parsed_url.netloc == "youtu.be":
        return parsed_url.path.lstrip("/")
    
    # Handles: youtube.com/watch?v=VIDEO_ID (with optional extra params)
    query_params = parse_qs(parsed_url.query)
    if "v" in query_params:
        return query_params["v"][0]
    if query_params.path.startswith("/shorts/"):
        return query_params.path.split("/shorts/")[1]
    raise ValueError(f"Could not extract video ID from URL: {url}")
def get_transcript(url):
    video_id = extract_video_id(url)
    transcript=YouTubeTranscriptApi().fetch(video_id,languages=['en','hi','de'])
    return transcript
# ✅ This block runs ONLY if file is executed directly
if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    transcript = get_transcript(url)
    print("\nTranscript:\n")
    print(transcript)
