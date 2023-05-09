## Introduction
This is a Python script that summarizes the Wikipedia page on Hyperspectral Imaging using the Sumy library. It uses the LexRank summarizer to generate summaries for each paragraph of the page.

## Requirements
This script requires the following libraries to be installed:

wikipedia
sumy

You can install these libraries using pip. For example:

pip install wikipedia
pip install sumy

## Usage
To use this script, simply run the following command in your terminal:

python <your-file-name>.py
The script will fetch the Wikipedia page and generate a summary for each paragraph.

## Parameters
The script uses the following parameters:

1. summary_length: The length of the summary as a fraction of the original text. The default value is 0.3.
2. similarity_threshold: The similarity threshold for sentence similarity. The default value is 0.1.
You can adjust these parameters by editing the script.
