# Twitter-Keyword-Word-Cloud-Generator
This Python program retrieves 10,000 tweets from Twitter based on a keyword input, removes redundant words/phrases, and generates a word cloud visualizing the most frequent words. It uses Tweepy, NLTK, Matplotlib, and WordCloud libraries for accessing the API, text processing, and visualization.

#Overview
This Python program enables users to extract at least 10,000 tweets from Twitter based on a keyword input, and generates a word cloud visualization depicting the most frequent words used in the extracted tweets. The program utilizes Tweepy for Twitter API access, NLTK for text processing, and Matplotlib along with WordCloud for visualization.

#Installation
Clone the repository: git clone https://github.com/your_username/twitter-keyword-word-cloud.git
Install the required libraries: pip install tweepy matplotlib wordcloud nltk

#Usage
Obtain Twitter API credentials from Twitter Developer Platform.
Fill in the credentials in the config.py file.
Run the main.py script and input a keyword when prompted.
The program will retrieve tweets, process them, and generate a word cloud image.

#Libraries Used
Tweepy: For accessing the Twitter API
NLTK: For text tokenization and stop word removal
Matplotlib: For generating plots and visualizations
WordCloud: For generating the word cloud image
