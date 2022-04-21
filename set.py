from re import T


s = set() 

s.add(1)
s.add(3)
s.add(2)


print(s)

def restart ():
    print(f"The set has {len(s)} elemets")

    v = int(input("Number"))

    while v > 0:
        s.add(len(s)+1)
        v -= 1 

    

    print(f"The set {s} \n has {len(s)} elemets")

    v = int(input("Number to remove "))

    while v > 0:
     s.remove(len(s))
    v -= 1 



    print(f"The set {s} \n has {len(s)} elemets")

    

if input("Again? ") == "Yes":
    restart ()


