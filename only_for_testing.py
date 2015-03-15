
import csv,sys
tweets=[]
tweets.append('Your faith, your trust is sacred to us. Together we will create a world class Delhi. http://t.co/hdLdhl4IQm')
#for i in tweets:
#	print('line')
#	print(i)
for i in tweets:
	print(i)
#x=open('http_removed','w')
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
       print(len(tweets))
       for i in tweets:
        print(i)	
rem_substring(tweets,'http')
#for i in tweets:
#	print(i)
#rem_substring(tweets,'@')
