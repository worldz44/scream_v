import openai
openai.api_key = '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'

response_obj='''[
  {
    "start_time": 97.19, 
    "end_time": 127.43,
    "description": "Put here a simple description of the context in max 10 words"
    "duration":36 #Length in seconds
  },
]'''

def analyze_transcript(transcript):
    prompt = f"This is a transcript of a video. Please identify the most interesing sections from the whole, make sure that the duration is more than 2 minutes (it MUST to be more than 120 seconds), Make Sure you provide extremely accurate timestamps and respond only in this JSON format {response_obj}  \n Here is the Transcription:\n{transcript}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        n=1,
        stop=None
    )

    return response.choices[0]['message']
