cs<-"xigDFiLAOkzsrlbXempi1KDjbYlIR09TCTjjmjpkEsF702fePR"
ck<-"PqSPfWBPGNbnh7ONUDddsxZVW"
at<-"2999578561-GsLA3GN5KFIHCYM4VXFQEm7RbeseKhtIIGrsjuV"
ts<-"CYyu2QzUGK9R71bTiChUmy8rGwMrw9phCIRXZWGGPcqFj"
setup_twitter_oauth(ck,cs,at,ts)
wea_tweets = userTimeline("arvindkejrival")
wea_tweets