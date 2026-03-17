from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):

    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]

    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    elif "shorts/" in url:
        return url.split("shorts/")[1].split("?")[0]

    else:
        return None


def get_transcript(url):
    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=['en', 'hi'])

    text = " ".join([item.text for item in transcript])

    return text


# ✅ This block runs ONLY if file is executed directly
if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    transcript = get_transcript(url)

    print("\nTranscript:\n")
    print(transcript)
