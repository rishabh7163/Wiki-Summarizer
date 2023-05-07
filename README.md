## Introduction
This code is used to generate a summary of a Wikipedia page using the Luhn algorithm. It uses the Sumy library to create a plaintext parser, tokenizers, and a summarizer. The output is a summary of the Wikipedia page based on a specified fraction of the original text.


## Dependencies
- Python 3.6 or higher
- Sumy library
- Wikipedia library


## Usage
1. Install the required dependencies
2. Replace "Enter_the_Wiki_Topic_Here" with the title of the Wikipedia page you want to summarize.
3. Adjust the summary length by changing the value of `summary_length`. It should be a fraction between 0 and 1, indicating the proportion of the original text to be included in the summary.
4. Run the code. The summary will be printed in the console.


## Output
The code generates a summary of the Wikipedia page based on the specified fraction of the original text. The output is a list of sentences that represent the main points of the article.


## Limitations
The Luhn algorithm is a simple summarization technique that may not always produce the best results. The output may not be as accurate or comprehensive as a summary created by a human. Additionally, the code may not work for all Wikipedia pages, particularly those with non-English content.
