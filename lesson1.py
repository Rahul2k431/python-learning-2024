print("Hi! Whats your name")
name=input()
print("Hi",name,"its nice to meet you")

print("How old are you")
age=int(input())
print("I see, you are",age,"years old")

print("Where do you live")
place=input()
print("I see, you live in",place)

print("Tell me your 4 favourite places in",place)
pl1=input()
pl2=input()
pl3=input()
pl4=input()

places= [pl1,pl2,pl3,pl4]
print("I see your favourite places in",place,"are:")
for place in places:
    print(place)
