# 🎬 Agentic AI YouTube Video Analyzer

An **AI-powered YouTube Analyzer** that uses **Agentic AI + domain-specific intelligence** to extract transcripts, generate summaries, and provide structured insights — including **financial data visualization and question extraction**.

> ⚡ Convert long YouTube videos into concise summaries and meaningful analysis.

📌 Overview

With the rapid growth of video content, consuming long videos is time-consuming.

This project solves that by:

- Extracting transcripts from videos
- Applying domain-specific AI reasoning
- Generating structured summaries and insights
- Visualizing financial data
- Allowing PDF downloads

✨ Features
🎥 Core Features
- Extract transcript from YouTube videos
- AI-powered summarization
- Multi-language support (English, Hindi, German)

🧠 Agentic AI System
- Domain-based intelligent routing
- Custom prompts for different use cases
- Context-aware output generation


📊 Financial Analysis:
- Extracts metrics like:
- Revenue, Profit, Loss, Growth, ROI, EBITDA
- Converts units (K, M, B, Crore, Lakh)
- Generates:
📊 Bar charts (Matplotlib)
📁 Data tables (Pandas)
📈 Insights (Highest, Lowest, Average)

❓ Question Extraction
- Identifies important questions from videos
- Formats them into structured lists
- Useful for interviews and revision

📄 PDF Export
- Download results as PDF
- Unicode font support (NotoSans)
- Clean formatting

🧠 AI Architecture

This project uses Agentic AI with domain-specific LLM orchestration powered by Groq.

⚙️ Workflow
- Input YouTube URL
- Extract transcript
- Convert transcript → structured text
- Route to domain-specific AI agent
- Generate output (summary / insights / charts)

💻 Frontend
- Streamlit
⚙️ Backend
- Python
🤖 AI & APIs
- Groq (LLM inference)
- YouTube Transcript API
📦 Libraries
- pandas
- matplotlib
- fpdf
- dotenv

git clone https://github.com/MakTarun/Agentic_AI-Youtube_video_Analyzer.git
cd Agentic_AI-Youtube_video_Analyzer

pip install -r requirements.txt

streamlit run main.py

🚀 Usage

1.Enter a YouTube video URL

2.Select domain (Finance, Tech, etc.)

3.Choose output type:Summary or Descriptive

4.Click Analyze

5.View:Summary or Descriptive

Insights,
Charts (Finance),
Questions,
Download PDF



## ✅ Advantages
- 🧠 Implements Agentic AI for domain-specific reasoning and analysis  
- 🎯 Multi-domain support (Finance, Tech, Sports, Gaming, etc.)  
- 📊 Generates financial insights with data visualization (charts & tables)  
- ❓ Extracts key questions for learning and interview preparation  
- 📄 Supports PDF export for offline access and sharing  
- 🌍 Multi-language transcript support (EN, HI, DE)  
- 💡 Enhances productivity and knowledge extraction from video content  
- 🖥️ User-friendly interface built with Streamlit

## ⚠️ Limitations

- 🎥 Requires videos with available transcripts (captions must be enabled)  
- 🌐 Limited multilingual accuracy outside supported languages (EN, HI, DE)  
- ⏱️ Long videos may face token limits or slower processing  
- 🤖 LLM-generated outputs may occasionally miss context or produce approximations  
- 📊 Financial insights depend on explicit numerical data in transcripts  
- 🔌 Requires external API access (Groq) and internet connectivity  
- 🚫 No real-time/live video analysis support yet  
