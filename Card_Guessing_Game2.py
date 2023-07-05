import random
class card:
    def __init__(self,color,type,value) :
        self.color = color
        self.type = type
        self.value = value
Value = [1,2,3,4,5,6,7,8,9,10,'K','Q','J'] 
spade=[]
heart=[]
diamond=[]
club=[] 

for i in range(13):
    spade.append(card("Black", "Spade", Value[i]))
for i in range(13):
    heart.append(card("Red", "Heart",  Value[i]))
for i in range(13):
    diamond.append(card("Red", "Diamond", Value[i]))
for i in range(13):
    club.append(card("Black", "Club",  Value[i]))

cards = spade + heart + diamond + club
random.shuffle(cards)
l = random.sample(cards,21)
for i in range(21):
    print(l[i].value,l[i].type)
print("Select any card from above cards")
x=0
while(x != 3):
    p=[]
    q=[]
    r=[]
    for i in range(1,22):
        if i%3==0:
            p.append(l[i-1])
        elif i%3==1:
            q.append(l[i-1])
        elif(i%3==2):
            r.append(l[i-1])
    l = p+q+r
    for i in range(1,22):
        if(i%7==0):
            print(l[i-1].value,l[i-1].type)
        else:
            print(l[i-1].value,l[i-1].type,end=" | ")
    #SPADE HEART DIAMOND CLUB
    a = int(input("Row : "))
    if a==1:
        l = q+p+r
    elif a==2:
        l = r+q+p
    elif a==3:
        l = q+r+p
    x += 1

print(l[10].value,l[10].type)
