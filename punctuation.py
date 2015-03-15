def isEnglish(s):
	try:
		s.encode('ascii')
	except UnicodeEncodeError:
		return False
	else:
		return True
import csv,sys
tweets=[]
with open('language_removed') as f:
	for line in f:
		tweets.append(line)
#tweets.append('@gurmeetsinghs13 Your faith, your trust is sacred to us. Together we will create a world class Delhi. http://t.co/oGgNgjHw9M')
#for i in tweets:
#	print('line')
#	print(i)
x=open('punctuation_removed','w')
y=open('exclamation_count','w')
def rem_language(tweets,substring):
       print(len(tweets))
       for i in tweets:
        z=i.count('!')
        y.write(str(z)+'\n')
        i=i.replace('!','')
        i=i.replace(',',' ')
        i=i.replace('.',' ')
        x.write(i+'\n')        
#for i in tweets:
#	print(i)
rem_language(tweets,'a')
#rem_substring(tweets,'@')
