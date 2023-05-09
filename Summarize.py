import wikipedia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# Fetching the Wikipedia page
page = wikipedia.page("Hyperspectral Imaging")

# Creating a plaintext parser
parser = PlaintextParser.from_string(page.content, Tokenizer('english'))

# Creating a summarizer with a lower similarity threshold
summarizer = LexRankSummarizer()
summarizer.similarity_threshold = 0.1

# Generating a summary for each paragraph
for paragraph in parser.document.paragraphs:
    # Generating a summary
    summary_length = 0.3  # Summary length as a fraction of the original text
    sentence_count = max(int(len(paragraph.sentences) * summary_length), 1)  # Ensure at least one sentence is included
    summary = summarizer(paragraph, sentence_count)

    # Printing the original paragraph and its summary
    print("\nORIGINAL PARAGRAPH:")
    print(paragraph)
    print("SUMMARY:")
    for sentence in summary:
        print(sentence)
