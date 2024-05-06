#Module required

import tweepy
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# list to store tweets fro processing
tweets=[]
tweets_1=[]
tweets_data=[]

# keyword from user
key_word=input("Enter a Keyword :" )

# Import the stopwords
my_file = open("stopwords.txt", "r")
data = my_file.read()
stopwords_list = data.split("\n")

#bearer token for authentication
bearer_token=input("Enter your bearer token: ")

# Twitter authentication
client = tweepy.Client(bearer_token)

# Creating the query
response = client.search_recent_tweets(query = f'{key_word} lang:en', max_results = 100)

# passing the query to paginator which will look for 10k tweets
# At a time it can lookup at most 100 tweets

for tweet in tweepy.Paginator(client.search_recent_tweets,query = f'{key_word} lang:en', max_results = 100).flatten(limit=10000):
    tweets_1.append(tweet.data['text'])

# tweets text preprocessing
# Removing the RT(retweet) string from the tweets text
for x in tweets_1:
    x=str(x)[3:]
    tweets_data.append(str(x))



# Removing hyperlink, punctuations and stopwords
for x in tweets_data:
    z=re.sub(r"http\S+", "", x)
    res = re.sub(r'[^\w\s]', '', z)
    word_tokens = word_tokenize(res)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stopwords_list]
    for y in filtered_sentence:
        tweets.append(y)

# joining them into string to generate wordcloud
text=" ".join(tweets)

#generating wordcloud
word_cloud = WordCloud(width=2000, height=1000,collocations = False, background_color = 'white').generate(text)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")

#saving the file as png image
plt.savefig('twitter.png', dpi=300)
plt.show()

