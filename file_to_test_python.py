
import csv,sys
tweets=[]
with open('test1') as f:
	for line in f:
		tweets.append(line)
#tweets.append('@gurmeetsinghs13 Your faith, your trust is sacred to us. Together we will create a world class Delhi. http://t.co/oGgNgjHw9M')
def rem_substring(tweets,substring):
       m=0;
       for i in tweets:
              while i.find(substring)!=-1:
                     k=i.find(substring)
                     d=i.find(' ',k,len(i))
                     if d!=-1: #substring is present somwhere in the middle(not the end of the string)
                            i=i[:k]+i[d:]
                     else: #special case when the substring is present at the end, we needn't append the
                            #substring after the junk string to our result
                            i=i[:k]
                     print(i)
              tweets[m]=i #store the result in tweets "list"
              #print(i)
              m=m+1
       for i in tweets:
	       	print(i)
#rem_substring(tweets,'@')
#for i in tweets:
#	print(i)
rem_substring(tweets,'@')
