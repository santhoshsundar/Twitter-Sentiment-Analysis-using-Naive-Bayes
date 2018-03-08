import csv
from Source import DataCleaning
from Source import DataPreprocessing
import random


def len_dataset(positive_tweets, negative_tweets):
    return len(positive_tweets),len(negative_tweets), (len(positive_tweets) + len(negative_tweets))


def class_probability(positive_tweets_len, negative_tweets_len, total_tweets_len):
    return round((positive_tweets_len/total_tweets_len),3),round((negative_tweets_len/total_tweets_len),3)


def split_dataset(dataset):
    train_size = int(len(dataset) * .80)
    train_set = []
    dataset_copy = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(dataset_copy))
        train_set.append(dataset_copy.pop(index))

    return [train_set, dataset_copy]


def get_feature_extractor():
    input_tweets_positive = csv.reader(open('../Data/processed/positive_processed.csv', 'r',encoding='UTF-8'), delimiter=',')
    input_tweets_negative = csv.reader(open('../Data/processed/negative_processed.csv', 'r',encoding='UTF-8'), delimiter=',')
    tweets_positive = []
    tweets_negative = []
    tweets_positive_sentiment = []
    tweets_negative_sentiment = []

    for row_tweet in input_tweets_positive:
        sentiment = row_tweet[0]
        tweet = row_tweet[1]
        tweets_positive_sentiment.append((tweet, sentiment))
        tweets_positive.append(tweet)

    for row_tweet in input_tweets_negative:
        sentiment = row_tweet[0]
        tweet = row_tweet[1]
        tweets_negative_sentiment.append((tweet, sentiment))
        tweets_negative.append(tweet)

    return tweets_positive_sentiment,tweets_negative_sentiment,tweets_positive,tweets_negative


def get_words_in_tweets(tweets_positive, tweets_negative):
    all_words_positive = []
    all_words_negative = []
    all_words = []

    for text in tweets_positive:
        for word in text.split(' '):
            if word not in all_words_positive:
                all_words_positive.append(word)
                all_words.append(word)

    for text in tweets_negative:
        for word in text.split(' '):
            if word not in all_words_negative:
                all_words_negative.append(word)
                all_words.append(word)

    return all_words_positive,all_words_negative, all_words


def get_feature_words(word_list_positive,word_list_negative,word_list ):
    freq_dict_positive = {}
    freq_dict_negative = {}

    for word in word_list_positive:
        for key in freq_dict_positive.keys():
            if word in key:
                freq_dict_positive[word] = freq_dict_positive[word] + 1
                print("+")
            else:
                freq_dict_positive[word] = 1

    for word in word_list_negative:
        if word in freq_dict_negative.keys():
            freq_dict_negative[word] = freq_dict_negative[word] + 1
        else:
            freq_dict_negative[word] = 1

    for word in word_list:
        if word not in freq_dict_positive.keys():
            freq_dict_positive[word] = 1
        if word not in freq_dict_negative.keys():
            freq_dict_negative[word] = 1

    return freq_dict_positive, freq_dict_negative


def feature_word_probability(freq_dict_positive, freq_dict_negative,positive_words_len, negative_words_len):
    freq_dict_positive_len = len(freq_dict_positive)
    freq_dict_negative_len = len(freq_dict_negative)
    for key in freq_dict_positive.keys():
        freq_dict_positive[key] = freq_dict_positive[key]/(positive_words_len + freq_dict_positive_len)

    for key in freq_dict_negative.keys():
        freq_dict_negative[key] = freq_dict_negative[key]/(negative_words_len+ freq_dict_negative_len)

    return freq_dict_positive, freq_dict_negative


def predict(tweet,freq_dict_positive_probability, freq_dict_negative_probability,\
                        positive_class_probability, negative_class_probability ):
    positive_probability = 1
    negative_probability = 1
    word_list = tweet.split(' ')

    for word in word_list:
        positive_probability = positive_probability * freq_dict_positive_probability[word]
        negative_probability = negative_probability * freq_dict_negative_probability[word]

    positive_probability = positive_probability * positive_class_probability
    negative_probability = negative_probability * negative_class_probability

    if positive_probability > negative_probability:
        print(" Tweet is Positive")
    else:
        print(" Tweet is Negative")


def accuracy(total_test_tweets,freq_dict_positive_probability, freq_dict_negative_probability,\
                        positive_class_probability, negative_class_probability):

    negative_probability=1
    positive_probability=1
    accuracy = 0

    number_tweets = len(total_test_tweets)

    for tweets in total_test_tweets:

        word_list = tweets[0].split(' ')

        for word in word_list:
            positive_probability = positive_probability * freq_dict_positive_probability[word]
            negative_probability = negative_probability * freq_dict_negative_probability[word]

        positive_probability = positive_probability * positive_class_probability
        negative_probability = negative_probability * negative_class_probability

        if positive_probability > negative_probability:
            label = 'Positive'
        else:
            label = 'Negative'

        if label == tweets[1]:
            accuracy += 1
            print(accuracy)

        negative_probability = 1
        positive_probability = 1

    accuracy_percentage = accuracy/number_tweets

    print(" Accuracy of classifier is {} of {}".format(accuracy,number_tweets))
    print('\n')
    print(" Accuracy percentage of classifier is {}".format(accuracy_percentage))

if __name__ == "__main__":

    # Dataset Preprocessed
    stop_words = DataPreprocessing.get_stop_word_list('../Resources/stop_words.txt')
    emotions = DataPreprocessing.load_emotions('../Resources/emotions.txt')
    slangs = DataPreprocessing.load_slangs('../Resources/internet_slangs.txt')

    DataCleaning.positive_tweet_process(stop_words, emotions, slangs)
    DataCleaning.negative_tweet_process(stop_words, emotions, slangs)

    # Get positive and negative tweets
    tweets_positive_sentiment , tweets_negative_sentiment, tweets_positive,tweets_negative = get_feature_extractor()

    # split datasets into training and test
    training_tweets_positive_sentiment, test_tweets_positive_sentiment = split_dataset(tweets_positive_sentiment)
    training_tweets_negative_sentiment, test_tweets_negative_sentiment = split_dataset(tweets_negative_sentiment)
    total_test_tweets = test_tweets_positive_sentiment + test_tweets_negative_sentiment

    # Number of positive, negative and total tweets
    positive_tweets_len, negative_tweets_len, total_tweets_len = len_dataset(tweets_positive,tweets_negative)

    # positive and negative prior class probabilities
    positive_class_probability, negative_class_probability = \
                                class_probability(positive_tweets_len, negative_tweets_len, total_tweets_len)

    # get all words in positive, negative and combined dataset
    all_words_positive, all_words_negative, all_words = \
                               get_words_in_tweets(tweets_positive,tweets_negative)

    # get number of words in positive, negative and combined dataset
    positive_words_len, negative_words_len, total_words_len = len_dataset(all_words_positive,all_words_negative)

    # get number of occurrence of each word in each class
    freq_dict_positive, freq_dict_negative = get_feature_words(all_words_positive, all_words_negative,all_words)

    # get probability occurrence of each words in each class
    freq_dict_positive_probability, freq_dict_negative_probability = \
              feature_word_probability(freq_dict_positive, freq_dict_negative,positive_words_len, negative_words_len )

    # predict the tweet
    for tweet in total_test_tweets:
        predict(tweet[0],freq_dict_positive_probability, freq_dict_negative_probability, \
                positive_class_probability, negative_class_probability)

    # accuracy of classifier
    accuracy(total_test_tweets,freq_dict_positive_probability, freq_dict_negative_probability,\
             positive_class_probability, negative_class_probability)