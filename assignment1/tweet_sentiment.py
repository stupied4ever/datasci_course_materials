import sys
import json

scores = {}

def create_scores(sent_file):
    global scores
    scores  = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    #print scores.items()

def parse_tweets(tweet_file):
    tweets =  map(json.loads, tweet_file.readlines());
    for tweet in tweets:
        text = ""
        if "text" in tweet: text = tweet["text"]
        print score(text)
    
def score(tweet):
    score = 0
    for word in tweet.split(" "):
        if word in scores: score += scores[word]
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    create_scores(sent_file)
    parse_tweets(tweet_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
