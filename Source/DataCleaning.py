import csv
from Source import DataPreprocessing

NOT_AVAILABLE = 'not available'

def negative_tweet_process(stop_words, emotions, slangs):
    sentiment = 'Negative'

    with open('../Data/processed/negative_processed.csv', 'w',encoding='UTF-8') as fw:
        write_line = csv.writer(fw, delimiter=',')
        with open('../Data/sem/negative.tsv', 'r') as fr:
            read_lines = csv.reader(fr, delimiter='\t')

            for line in read_lines:
                tweet_text = line[-1]
                tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                if tweet_preprocess.strip() == NOT_AVAILABLE:
                    continue
                tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                write_line.writerow([sentiment, tweet_remove_stopword.strip()])

        with open('../Data/sts/negative.csv', 'r',encoding='latin-1') as fr:
            read_lines = csv.reader(fr, delimiter=',')

            for line in read_lines:
                tweet_text = line[5]
                tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                write_line.writerow([sentiment, tweet_remove_stopword.strip()])

        with open('../Data/assorted_data.csv', 'r') as fr:
            read_lines = csv.reader(fr, delimiter=',')

            for line in read_lines:
                if line[0] =='0':
                    tweet_text = line[5]
                    tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                    tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                    tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                    tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                    tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                    write_line.writerow([sentiment, tweet_remove_stopword.strip()])

def positive_tweet_process(stop_words, emotions, slangs):
    sentiment = 'Positive'

    with open('../Data/processed/positive_processed.csv', 'w',encoding='UTF-8') as fw:
        write_line = csv.writer(fw, delimiter=',')
        with open('../Data/sem/positive.tsv', 'r') as fr:
            read_lines = csv.reader(fr, delimiter='\t')

            for line in read_lines:
                tweet_text = line[-1]
                tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                if tweet_preprocess.strip() == NOT_AVAILABLE:
                    continue
                tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                write_line.writerow([sentiment, tweet_remove_stopword.strip()])


        with open('../Data/sts/positive.csv', 'r',encoding='latin-1') as fr:
            read_lines = csv.reader(fr, delimiter=',')

            for line in read_lines:
                tweet_text = line[5]
                tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                write_line.writerow([sentiment, tweet_remove_stopword.strip()])

        with open('../Data/assorted_data.csv', 'r') as fr:
            read_lines = csv.reader(fr, delimiter=',')

            for line in read_lines:
                if line[0] =='4':
                    tweet_text = line[5]
                    tweet_remove_emotion = DataPreprocessing.remove_emotions(tweet_text, emotions)
                    tweet_preprocess = DataPreprocessing.process_tweet(tweet_remove_emotion)
                    tweet_replace_repeats = DataPreprocessing.replace_two_or_more(tweet_preprocess)
                    tweet_replace_slang = DataPreprocessing.replace_slangs(tweet_replace_repeats, slangs)
                    tweet_remove_stopword = DataPreprocessing.remove_stop_words(tweet_replace_slang, stop_words)

                    write_line.writerow([sentiment, tweet_remove_stopword.strip()])