import re

def process_tweet(tweet):

    # Convert to lower case
    tweet = tweet.lower()
    # Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'url', tweet)
    tweet = re.sub('((www\.[^\s]+)|(http?://[^\s]+))', 'url', tweet)
    # Convert @username to at_user
    tweet = re.sub('@[^\s]+', 'at_user', tweet)
    # Convert #HASHTAG to hashtag
    tweet = re.sub('#[^\s]+','hashtag',tweet)
    # Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    # Remove &amp;
    tweet = re.sub(r'&amp;',' ',tweet)
    # Remove &lt;3
    tweet = re.sub(r'&lt;*(3|-)', ' ', tweet)
    # Remove punctuation
    tweet = re.sub(r'[^\w\s]','',tweet)

    return tweet


def replace_two_or_more(tweet):

    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1", tweet)



def remove_stop_words(tweet,stop_words):
    result=''
    for word in tweet.split(' '):
        if word in stop_words:
            None
        else:
            result=result+word+' '
    return result


def replace_slangs(tweet,slangs):
    result=''
    words=tweet.split(' ')
    for w in words:
        if w in slangs.keys():
            result=result+slangs[w]+' '
        else:
            result=result+w+' '
    return result


def remove_emotions(tweet,emotions):
    result = ' '
    for word in tweet.split(' '):
        if word in emotions:
            None
        else:
            result=result+word+' '
    return result


def load_slangs(slangs_txt):
    slangs={}
    with open(slangs_txt,'r') as fp:
        line=fp.readline()
        while line:
            l=line.split(r',%,')
            if len(l) == 2:
                slangs[l[0]]=l[1].strip()
            line=fp.readline()
    return slangs


def get_stop_word_list(stop_word_txt):
    stop_words = []
    stop_words.append('at_user')
    stop_words.append('url')
    stop_words.append('hashtag')
    stop_words.append('rt')
    with open(stop_word_txt, 'r') as fp:
        line = fp.readline()
        while line:
            word = line.strip()
            stop_words.extend(word)
            line = fp.readline()
    return stop_words


def load_emotions(filename):
    emotions = []
    with open(filename,'r',encoding='UTF-8') as fp:
        line = fp.readline()
        while line:
            l = line.replace("\xc2\xa0", " ")
            l = l.split()
            emotions.extend(l[:-1])
            line = fp.readline()
    return emotions