counta=0
counte=0
counti=0
counto=0
countu=0
a="Guvi Geeks Network Private Limited"
for i in a:
    if i=="a":
        counta=counta+1
    elif i=="e":
        counte=counte+1
    elif i=="i":
        counti=counti+1
    elif i=="o":
        counto=counto+1
    elif i=="u":
        countu=countu+1
vowelcount=counta+counte+counti+counto+countu
print("Total Number of Vowels ",vowelcount)
print ("Vowel A ", counta)
print ("Vowel E ", counte)
print ("Vowel I ", counti)
print ("Vowel O ", counto)
print ("Vowel U ", countu)