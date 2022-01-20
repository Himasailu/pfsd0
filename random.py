import random
n=random.randbyte(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja", "Ashwin", "Rahane", "shami", "dhoni", "virat"]
mylist1={"jadeja", "Ashwin", "Rahane", "shami", "dhoni", "virat"}
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)
