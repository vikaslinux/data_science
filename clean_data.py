#the following function is used to detect the nonEnglish characters
def isEnglish(s):
 try:
  s.encode('ascii')
 except UnicodeEncodeError:
  return False
 else:
  return True
import csv,sys
tweets=[]
#filename is the name of the file we want to clean.Please note, that this file contains only one column, i.e. only tweets
filename="test1"
with open(filename) as f:
	for line in f:
		tweets.append(line)
#tweets.append('@gurmeetsinghs13 Your faith, your trust is sacred to us. Together we will create a world class Delhi. http://t.co/oGgNgjHw9M')
#for i in tweets:
#	print('line')
#	print(i)
#x=open('at_the_rate_removed','w')
#The following function removes the part of the string that contains the substring eg. if
#substring = 'http' , then http://www.google.com is removed, that means, remove until a space is found
def rem_substring(tweets,substring):
       m=0;
       print(len(tweets))
       for i in tweets:
              while i.find(substring)!=-1:
                     k=i.find(substring)
                     d=i.find(' ',k,len(i))
                     if d!=-1: #substring is present somwhere in the middle(not the end of the string)
                            i=i[:k]+i[d:]
                     else: #special case when the substring is present at the end, we needn't append the
                            #substring after the junk string to our result
                            i=i[:k]
                     
              tweets[m]=i #store the result in tweets "list"
              #print(i)
              m=m+1
       return tweets
def removeNonEnglish(tweets):
    result=[]
    for i in tweets:
        if isEnglish(i):
            result.append(i)
    return result
def rem_language(tweets):
 print(len(tweets))
 m=0
 for i in tweets:
  i=i.replace('!','')
  i=i.replace(',',' ')
  i=i.replace('.',' ')
  tweets[m]=i
  m=m+1
 return tweets
#for i in tweets:
#	print(i)

#the following function call removes @something from each of the tweet
tweets=rem_substring(tweets,'@')
#the following function call removes http://something from each of the tweet
tweets=rem_substring(tweets,'http')
tweets=rem_substring(tweets,'#')
tweets=removeNonEnglish(tweets)
tweets=rem_language(tweets)
for i in tweets:
	print(i)
