# Ques_1
print('''Access Token: These are things that applications use to make API requests on behalf of the user.
The access token represents the authorization of a specific application to access specific parts of the user\'s data.
Below is given a general example of access token created on Twitter:''')
Access_Token_Key_1 = "1009109163568517123-vXfU8q4NSB25cRB44r5DQ6xmW7aQ3b"  # Values taken from twitter developers page
Access_Token_Secret_2 = "M4FPhlNsG5C2bL0rrOtOWJ0nd5DyoXD6LunEhA4X8Z8Rb"
print('''Access Token Key: %s
Access Token Secret: %s''' % (Access_Token_Key_1, Access_Token_Secret_2))

# Ques_2
import socket  # in-built socket module is required for DNS lookups

web_1 = socket.gethostbyname('google.com')  # gethostbyname() funciton provide ip address lookupS
web_2 = socket.gethostbyname('facebook.com')
web_3 = socket.gethostbyname('twitter.com')
print("\ngoogle.com: ", web_1)
print("facebook.com: ", web_2)
print("twitter.com: ", web_3)

# Ques_3
from KEYS import Consumer_Key, Consumer_Secret, Access_Token_Key, Access_Token_Secret
import tweepy

oauth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
oauth.set_access_token(Access_Token_Key, Access_Token_Secret)
api = tweepy.API(oauth)

search = api.search("Antman")
for searches in search:
    print(searches)

#Ques_4
lib=("A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects.")
api_=("An API is an interface for other programs to interact with your program or library  without having direct access.")
print("\n\nLibrary: ",lib)
print("API: ",api_)

