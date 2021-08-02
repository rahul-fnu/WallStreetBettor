from psaw import PushshiftAPI
import datetime
import operator
def wall_street_bettor():
    api = PushshiftAPI()
    start_time = int(datetime.datetime(2021, 2, 3).timestamp())
    submissions = api.search_submissions(after=start_time, 
                        subreddit='wallstreetbets',
                        filter = ['url', 'author', 'title', 'subreddit'], 
                        limit = 15000)
    stock_tracker = {}
    for submission in submissions:
        words = submission.title.split()
        cashtag = list(set(filter(lambda word: word.lower().startswith('$'), words)))

        if len(cashtag) > 0:
            for item in cashtag:
                tag = item
                if item[-1] == ',' or item[-1] == ')' or item[-1] == '?':
                    tag = item[:-1]
                if tag[1:].isalpha():
                    if tag in stock_tracker:
                        stock_tracker[tag] = stock_tracker[tag] + 1
                    else:
                        stock_tracker[tag] = 1
    stock_tracker = sorted(stock_tracker.items(), key=operator.itemgetter(1), reverse=True)
    return stock_tracker
print(wall_street_bettor())
