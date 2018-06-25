#Ques_1
import re
emails="zuck26@facebook.com""pages33@google.com""jeff42@amazon.com"
des_op=re.findall(r"([\w]+)@([\w]+).([com]+)",emails)                     #Using grouping syntax for grouping text
print(des_op)


#Que_2
text="Betty bought a bit of butter,But the butter was so bitter,So she bought some better butter,To make the biiter butter better."
B=re.findall(r"[Bb][\w]{1,200}",text)
print(B)


#Ques_3
sentence="A,very very;irregular_sentence"
out=re.compile("[,;_]")
out_1=out.sub(" ",sentence)                   #Replacing all the undesirable characters with space
print(out_1)


#Ques_optional
tweet='''Good advice! RT @TheNextWeb: What I
 would do differently if I was learning to code today
http://t.co/lbwej0pxOd cc:garybernhardt #rstats'''
url_reg  = r'[a-z]*[:.]+\S+'
outp=re.sub(url_reg,"",tweet)                 #substituting URl with empty string
print(outp)
