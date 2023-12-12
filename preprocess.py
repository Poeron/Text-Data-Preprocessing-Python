import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def clean_data(text):
    # Linkleri kaldırma
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Hashtag'leri kaldırma
    text = re.sub(r'#\w+', '', text)

    # Nümerik ifadeleri kaldırma
    text = re.sub(r'\d+', '', text)

    # Özel karakterleri ve noktalama işaretlerini kaldırma
    text = re.sub(r'[^\w\s]', '', text)

    # Küçük harfe çevirme
    text = text.lower()

    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_text = [word for word in words if word.lower() not in stop_words]

    return ' '.join(filtered_text)

def remove_duplicate_lines(lines):
    unique_lines = set(lines)
    return list(unique_lines)

def process_text_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    sentences = []
    for line in lines:
        # Satırı cümlelere ayırma
        line_sentences = sent_tokenize(line)
        sentences.extend(line_sentences)

    # Tekrar eden cümleleri silme
    unique_sentences = remove_duplicate_lines(sentences)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for sentence in unique_sentences:
            cleaned_sentence = clean_data(sentence)
            without_stopwords = remove_stopwords(cleaned_sentence)

            # Boş satırları kontrol etme ve yazma
            if without_stopwords.strip():
                file.write(without_stopwords + '\n')

if __name__ == "__main__":
    input_file_path = "input.txt"  # Değiştirilecek dosya adınızı ve yolunuzu ekleyin
    output_file_path = "output.txt"  # Değiştirilecek dosya adınızı ve yolunuzu ekleyin

    process_text_file(input_file_path, output_file_path)
