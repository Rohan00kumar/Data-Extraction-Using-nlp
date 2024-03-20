import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from textblob import TextBlob
import syllapy
import textstat

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Assuming the article text is within <p> tags, adjust this according to the website structure
        paragraphs = soup.find_all('p')
        article_text = ' '.join([paragraph.text for paragraph in paragraphs])
        return article_text
    except Exception as e:
        print(f"Error occurred while extracting text from {url}: {e}")
        return None

# Function to compute text analysis variables
def compute_text_analysis(text):
    # Tokenization
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Stopwords removal
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]

    # Positive and Negative Scores
    blob = TextBlob(text)
    positive_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity > 0)
    negative_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity < 0)

    # Polarity and Subjectivity Score
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity

    # Average Sentence Length
    avg_sentence_length = sum(len(sent.split()) for sent in sentences) / len(sentences)

    # Percentage of Complex Words
    complex_word_count = sum(1 for word in words if syllapy.count(word) > 2)
    percentage_complex_words = (complex_word_count / len(words)) * 100

    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Average Number of Words per Sentence
    avg_words_per_sentence = len(words) / len(sentences)

    # Complex Word Count
    complex_word_count = sum(1 for word in words if syllapy.count(word) > 2)

    # Word Count
    word_count = len(words)

    # Syllable per Word
    syllables_per_word = sum(syllapy.count(word) for word in words) / len(words)

    # Personal Pronouns
    personal_pronouns = sum(1 for word in words if word.lower() in ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'])

    # Average Word Length
    avg_word_length = sum(len(word) for word in words) / len(words)

    return positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, \
           percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count, \
           syllables_per_word, personal_pronouns, avg_word_length

# Load input data
input_df = pd.read_excel("Input.xlsx")

# Initialize list to store output data
output_data = []

# Iterate through URLs and perform analysis
for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    article_text = extract_text_from_url(url)
    if article_text:
        analysis_result = compute_text_analysis(article_text)
        output_data.append([url_id, *analysis_result])

# Define column names for output DataFrame
columns = [
    'URL_ID', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
    'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
    'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT',
    'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
]

# Create DataFrame for output data
output_df = pd.DataFrame(output_data, columns=columns)

# Save output to Excel
output_df.to_excel("Output.xlsx", index=False)