import openai

openai.api_key =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 
with open("data/logline.txt", "r", encoding="utf-8") as f:
    logline = f.read()

with open("data/characters.txt", "r", encoding="utf-8") as f:
    characters = f.read()

prompt = f"""
Analyze this film project:

Logline:
{logline}

Characters:
{characters}

1. Genre
2. Target audience
3. Commercial potential
4. Strengths
5. Weaknesses
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response['choices'][0]['message']['content'])
