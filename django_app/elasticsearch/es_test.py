from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])  # بررسی صحت آدرس

def create_tweet(tweet_data):
    response = es.index(index='tweets', body=tweet_data)
    return response