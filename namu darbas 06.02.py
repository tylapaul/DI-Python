groceries = []
shop = input("Įvesk tau žinomą parde, kai užknis įvesk 'done': ") 
while shop != "done" :
    shop = input("Įvesk tau žinomą parde, kai užknis įvesk 'done': ") 
    groceries.append(shop)
print ("Man žinomos pardės: ", groceries)
skaiciai = []
num = 0 
val = 0 
skaicius = 0
for i in range(1, 6):
    num = num + 1
    skaicius = input(f"Įvesk {num} skaičių: ")
    skaicius = int(skaicius)
    skaiciai.append(skaicius)
#avg = sum(skaiciai) / len(skaiciai)
total = 0
for val in skaiciai:
    total += val
avg = total / len(skaiciai)
print(avg)