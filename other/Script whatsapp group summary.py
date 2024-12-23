#List of Authors
#Author Wordclouds
#authorwise number of msg, media, emoji, links, words per msg
#top domains shared
#unique words, total_words, most_frequent words
#emojirank, fav emouji of each author
#most_busy, most silent, time_day heatmap
#message_per_month, messages_per_person, per_year, per_weekday, per_week, per_monthday, length_msg_per_person
#Activity graph using the cumulative sum of message count
#Mind the time, time_vs_length
#immediate_reply_buddies, birthday_popularity, activity_vs_hour


import re
from datetime import datetime
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import heapq
nltk.download('punkt')
nltk.download('stopwords')
MAX_WORD_COUNT = 2500
custom_stopwords = {"Bhai", "<Media omitted>", "Media omitted", "Media","omitted", "bro", 'would', 'ye', 'ke', 
                    'ko', 'doge', 'aap'}
stop_words = set(stopwords.words('english')).union(custom_stopwords)

#step 0: filter messages based on date
def filter_messages_by_dates(messages, start_day, end_day):
    start_date = datetime.strptime(start_day, '%m/%d/%Y')
    
    end_date = datetime.strptime(end_day, '%m/%d/%Y')
    print(start_date, end_date)
    filtered_data = [(date, text) for date, text in messages if start_date <= date <= end_date]

    return filtered_data

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
            date_obj = datetime.strptime(timestamp, '%d/%m/%y, %I:%M %p')
            chat_data.append((date_obj,message))
    
    return chat_data

# Step 2: Chunk the text
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

# Step 3: Get the summary of each chunk
def get_summary(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    word_freq = FreqDist(filtered_words)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq.keys():
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = TreebankWordDetokenizer().detokenize(summary_sentences)
    return summary



chat_file = "WhatsApp_Chat2.txt"  # Replace with your chat export file
chat_data = parse_chat_data(chat_file)
start_date = "9/17/2023"
end_date =   "10/04/2023"
filtered_data = filter_messages_by_dates(chat_data,start_date,end_date)
#print(chat_data)
chunks = whatsapp_chunk_text(filtered_data)
for chunk in chunks:
    text = get_summary(chunk)
    text1 = re.sub(r'<Media omitted>', '', text)
    # Print the text without media omitted placeholders
    print(text1,'\n')



#text_without_media = re.sub(r'<Media omitted>', '', text)
text = " ".join(get_summary(review) for review in chunks) 
text1 = re.sub(r'Media Omitted', '', text)
text2 = re.sub(r'https', '', text1)

wordcloud = WordCloud(stopwords=stop_words, background_color='black', colormap='rainbow').generate(text2) 
#Display the generated image 
plt.figure( figsize=(16,9)) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")
plt.show(); 
