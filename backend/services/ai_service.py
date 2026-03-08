import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(topic: str, difficulty: str, qtype: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=800,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert educator. Always respond with valid JSON only. No markdown, no explanation."
                },
                {
                    "role": "user",
                    "content": f"""Generate 3 {difficulty} level open-ended questions about "{topic}" for a student.
Return ONLY a JSON array, no markdown, no extra text:
[
  {{"question": "Your question here?"}},
  {{"question": "Your question here?"}},
  {{"question": "Your question here?"}}
]"""
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f'[{{"question": "Error: {str(e)}"}}]'


def analyze_reasoning(topic: str, first_attempt: str, final_answer: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=800,
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict cognitive assessment AI. Always respond with valid JSON only. No markdown, no explanation. Be brutally honest in scoring — if a student clearly doesn't know something, give LOW scores."
                },
                {
                    "role": "user",
                    "content": f"""Analyze this student's thinking STRICTLY and HONESTLY.

Topic: {topic}
Student's reasoning: {first_attempt}
Student's answers: {final_answer}

Scoring rules:
- If student says "I don't know" or gives blank/wrong answers → clarity_score: 5-15, confidence_level: 5-20
- If student shows partial understanding → clarity_score: 30-55, confidence_level: 30-55  
- If student shows good understanding → clarity_score: 65-80, confidence_level: 65-80
- If student shows excellent understanding → clarity_score: 85-100, confidence_level: 85-100

Return ONLY this JSON, no markdown, no extra text:
{{
  "thinking_pattern": "one of: Analytical, Sequential, Intuitive, Systematic, Confused",
  "concept_gap": "specific gap identified in 1-2 sentences — be specific about what they don't understand",
  "confidence_level": <honest integer 0-100 based on rules above>,
  "clarity_score": <honest integer 0-100 based on rules above>,
  "feedback": "2-3 sentences of specific constructive advice based on exactly what they wrote"
}}"""
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f'{{"thinking_pattern":"Unknown","concept_gap":"Error","confidence_level":0,"clarity_score":0,"feedback":"Error: {str(e)}"}}'
