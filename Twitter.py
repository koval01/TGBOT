from twitter_scraper import get_tweets
from math import ceil

def twittersearch(hashtag,n,language):
    if hashtag[0] != '#':
        hashtag = '#' + hashtag
    link = ''
    number = n-1
    try:
        for tweet in get_tweets(hashtag, pages=ceil(n/2)):
            try:
                number += 1
                if number<(n-1)*10+1:
                    continue
                link = link + '\n'+('№{} Нікнейм: {}\n{}' if language == 'ukrainian' else '№{} Nickname: {}\n{}').format(number,tweet['username'], 'https://twitter.com'+ tweet['tweetUrl'])

                if number == n*10:
                    return ('Інформація за хештегом:\n{}' if language == 'ukrainian' else 'Information about the hashtag:\n{}').format(hashtag) + '\n' + link
            
            except:
                print('Виникла помилка парсингу')
    except:
        return '😢 Сформуйте хештег іншим чином' if language == 'ukrainian' else '😢 Form a hashtag differently'
    if list(get_tweets(hashtag, pages=ceil(n/2)))== []:
        return '😢 Сформуйте хештег іншим чином' if language == 'ukrainian' else '😢 Form a hashtag differently'
    
