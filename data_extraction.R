library("RCurl")
library("ROAuth")
library("OAuth")
library("twitteR")

requestURL <-  "https://api.twitter.com/oauth/request_token"
accessURL =    "https://api.twitter.com/oauth/access_token"
authURL =      "https://api.twitter.com/oauth/authorize"

consumerKey =   "-----------------"   #type yor own key
consumerSecret = "--------------------------"    #type your own secret

twitCred <- OAuthFactory$new(consumerKey=consumerKey,consumerSecret=consumerSecret,requestURL=requestURL,accessURL=accessURL,authURL=authURL);
twitCred$handshake(cainfo="cacert.pem")

#run the below commands after getting the authorization code

registerTwitterOAuth(twitCred)
me <- getUser("arvindkejrival",cainfo="cacert.pem")    #type whatever twitter username you want
wea_tweets = userTimeline("arvindkejrival",cainfo="cacert.pem")
