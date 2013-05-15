import sys
import json

total_terms = 0
term_counts = {}

def parse_tweets(tweet_file):
    global scores_calculated

    tweets =  map(json.loads, tweet_file.readlines());
    for tweet in tweets:
        text = ""
        if "text" in tweet: text = tweet["text"]
        increase_counts(text)

def increase_counts(tweet):
    global total_terms
    global term_counts

    for word in tweet.split(' '):
        word = word.encode('utf-8').replace("\n", "")
        if (word in term_counts) == False:
            term_counts[word] = 0.0
        term_counts[word] += 1.0
	total_terms += 1.0

def print_output():
    for word in term_counts.keys():
        print "%s %f" % (word, term_counts[word]/total_terms)

def main():
    tweet_file = open(sys.argv[1])
    parse_tweets(tweet_file)
    print_output()

if __name__ == '__main__':
    main()
