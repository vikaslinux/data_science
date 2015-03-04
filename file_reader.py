import csv,unicodedata
from unidecode import *
with open('arvindkejriwal_tweets.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print(type(spamreader))
    for value in spamreader:
        for string in value:
            if type(string) == str:
                print (string)
            else:
                print (string.decode("utf-8"))
