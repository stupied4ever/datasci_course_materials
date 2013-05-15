import sys
import json

scores = {}
states_scores = {}

def create_scores(sent_file):
    global scores
    scores  = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

def parse_tweets(tweet_file):
    tweets =  map(json.loads, tweet_file.readlines());
    for tweet in tweets:
        if (("place" in tweet) == False) or (tweet["place"] == None) or (tweet["place"]["country_code"] != "US") or (tweet["place"]["place_type"] != "city"):
            continue
        text = ''
        if 'text' in tweet: text = tweet["text"]
        state = tweet["place"]["full_name"].replace(" ", "").split(",")[1]

        update_score(state, score(text))

def update_score(state, score):
    global states_scores
    if (state in states_scores.keys()) == False: 
        states_scores[state] = 0 
    states_scores[state] += score

def score(tweet):
    score = 0
    for word in tweet.split(" "):
        if word in scores: score += scores[word]
    return score

def print_output():
    max = -99999
    state_max = ''
    for state in states_scores.keys():
        if states_scores[state] > max:
            max = states_scores[state]
            state_max = state
    
    print state

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    create_scores(sent_file)
    parse_tweets(tweet_file)
    print_output()

if __name__ == '__main__':
    main()
