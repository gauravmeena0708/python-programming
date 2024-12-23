import re
from datetime import datetime
from collections import defaultdict
import openai
openai.api_key= 'YOUR OPEN API KEY'

SUMMARY_PROMPT = f"""Please summarize the following WhatsApp group chat based on topics that were discussed. For each topic, include its title and summary in bullet points. The bullets should include detailed information. If the topic includes recommendations about specific companies or services, please include them in the summary. Please include links that were shared."""
NEWSLETTER_PROMPT = f"""Please provide one paragraph to open a newsletter covering the following topics:"""

TIME_PER_MESSAGE = 0.015  # seconds
MAX_WORD_COUNT = 2500

# Step 1: Parse Chat Data
def parse_chat_data(chat_file):
    with open(chat_file, 'r', encoding='utf-8') as file:
        chat_lines = file.readlines()
    
    chat_data = []
    for line in chat_lines:
        # Sample line format: "01/01/21, 12:00 AM - John: Hello, everyone!"
        re1 = r'(\d{2}\/\d{2}\/\d{2}, \d{1,2}:\d{2} [apm]{2}) - ([^:]+): (.+)'
        match = re.match(r'(\d{2}\/\d{2}\/\d{2}, \d{1,2}:\d{2} [apm]{2}) - (.*?):(.*)', line)
        if match:
            timestamp, sender, message = match.groups()
            date_obj = datetime.strptime(timestamp, '%y/%m/%d, %I:%M %p')
            chat_data.append((date_obj,message))
    
    return chat_data


def whatsapp_chunk_text(messages):
    current_word_count = 0
    current_chunk = ''
    chunks = []
    for _, message in messages:
        message_word_count = len(message.split())
        if current_word_count + message_word_count > MAX_WORD_COUNT:
            chunks.append(current_chunk.strip())
            current_chunk = ''
            current_word_count = 0

        current_chunk += message
        current_word_count += message_word_count

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_messages(chunks, model):
    summary = ''
    calls_counter = 0
    for chunk in chunks:
        calls_counter += 1
        print(f"Sending prompt {calls_counter} out of {len(chunks)} to GPT! Chunk size: {len(chunk)}")
        chunk_summary = summarize_text(chunk, model)
        summary += chunk_summary + '\n\n'

    return summary

def summarize_text(text, model):
    prompt = f""""{SUMMARY_PROMPT}\n\n {text}"""
    return call_gpt(prompt, model)

def call_gpt(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    completion = openai.ChatCompletion.create(model=model, messages=messages)
    response = completion.choices[0].message.content
    print('Response:\n' + response + '\n')

    return response

chat_file = "WhatsApp_Chat.txt"  # Replace with your chat export file
chat_data = parse_chat_data(chat_file)
chunks = whatsapp_chunk_text(chat_data)
print(chunks)
model = "gpt-3.5-turbo"

summary = summarize_messages(chunks, model)

print(summary)
