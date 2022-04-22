

import sys
from checkifint import check
s = set() 

s.add(1)
s.add(3)
s.add(2)

print(f"Set has {len(s)} elemets")
print(s)

def restart ():
    print(f"The script started")


    print("Number to add: ")   

    v = check()

  

    while v > 0:
        s.add(len(s)+1)
        print(f"Added {v}")
        v -= 1 


    print(f"The set {s} \n has {len(s)} elemets")

    print("Number to remove: ")   

    v = check()

    while v > 0:
     s.remove(len(s))
     v -= 1 

    print(f"The set {s} \n has {len(s)} elemets")
    m = input("Restart? ")
    if  m == "Y" or m == "y":
     restart()
    else: 
        print("Goodbye")
        sys.exit(1)
   

    

restart()

    





