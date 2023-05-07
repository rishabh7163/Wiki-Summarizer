import wikipedia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

import sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# Fetching the Wikipedia page
page = wikipedia.page("Constellation")

# Creating a plaintext parser
parser = PlaintextParser.from_string(page.content, Tokenizer('english'))

# Creating a summarizer
summarizer = LuhnSummarizer()

# Calculate the number of sentences in the text
total_sentences = len(list(parser.document.sentences))

# Generating a summary
summary_length = 0.3  # Summary length as a fraction of the original text
sentence_count = max(int(total_sentences * summary_length), 1)  # Ensure at least one sentence is included
summary = summarizer(parser.document, sentences_count=sentence_count)

# Printing the summary
for sentence in summary:
    print(sentence)
