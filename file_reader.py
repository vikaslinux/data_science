
import csv,sys
file=sys.argv[1]
tweets=[]
with open(file, newline='\n',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    print(type(spamreader))
    for value in spamreader:
           tweets.append(value[2])
           print(value[2])

