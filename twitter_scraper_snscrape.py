import snscrape.modules.twitter as sntwitter
import csv
import unicodedata
import datetime

# Creating list to append tweet data to
tweets_list = []
#max_tweets_number = 10000
query = "Tesla"
# users = ["coinbureau", "Bitboy_Crypto", "AltcoinDailyio", "michael_saylor", "cz_binance", "Cointelegraph", "justinsuntron",
#          "RodrigoHeralz", "Taylor_Musk", "elonmusk"]
min_faves = 1
since_date = "2021-10-01"
until_date = "2021-11-16"
filename = "{}_snscrape_{}_{}_favs{}".format(query, since_date, until_date, min_faves)
csvFile = open(filename + '.csv', 'w')
# Use csv Writer
csvWriter = csv.writer(csvFile)

# Using TwitterSearchScraper to scrape data and append tweets to list
# for user in users:
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('{} min_faves:{} lang:en since:{} until:{}'.format(query, min_faves, since_date,
                                                                                          until_date)).get_items()):
    # if i > max_tweets_number:
    #     break
    created_at = datetime.datetime.strptime(str(tweet.date), "%Y-%m-%d %H:%M:%S+%f:00").strftime('%d/%m/%Y, %H:%M:%S')
    tw = unicodedata.normalize('NFKD', tweet.content).encode('ascii', 'ignore')
    csvWriter.writerow([created_at, tw])
    print(i, created_at, tw)



