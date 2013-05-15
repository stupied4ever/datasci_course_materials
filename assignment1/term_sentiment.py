import sys
import json

scores = {}
scores_calculated = {}

def create_scores(sent_file):
    global scores
    scores  = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    #print scores.items()

def parse_tweets(tweet_file):
    global scores_calculated

    tweets =  map(json.loads, tweet_file.readlines());
    for tweet in tweets:
        text = ""
        if "text" in tweet: text = tweet["text"]
        update_calculated_scores(text, score(text))

def update_calculated_scores(tweet, score):
    global scores_calculated
    for word in tweet.split(' '):
        if (word in scores_calculated) == False:
            scores_calculated[word] = 0
        scores_calculated[word] += score

def print_output():
    for word in scores_calculated.keys():
        print word, float(scores_calculated[word])

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
    print_output()

if __name__ == '__main__':
    main()
