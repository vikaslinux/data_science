
import csv,sys
file=sys.argv[1] #The second command line argument is the csv file to be read 
tweets=[] #store tweets in a list
with open(file, newline='\n',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"') #use the csv package
    for value in spamreader:
           tweets.append(value[2]) #store the seocnd column
       
#the following function removes text after RT until semicolon
def rem_rt(tweets):
       m=0;
       #iterate over all the tweets in the list
       for i in tweets:
              if i[0]=='R' and i[1]=='T': #if RT exists
                     k=i.find(':') #find the first occurence of :
                     if k!=-1:
                            tweets[m]=i[k+1:] # remove all the char before the : and also the :
                            #print the string
              m=m+1


#the following function removes any occurence of a substring that starts with the parameter substring in the following function from a given substring.
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
              tweets[m]=i #store the result in tweets "list"
              print(i)
       m=m+1
def rem_http(tweets): #function to remove links
       rem_substring(tweets,'http')
#finally call the above method here
rem_rt(tweets)
rem_http(tweets)
