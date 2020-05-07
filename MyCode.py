#Ex:1
for i in range(4):
    for j in range(4):
        print("# ",end=" ")
    print()

#Ex:2
for i in range(4):
    for j in range(i+1):
        print("# ",end=" ")
    print()

#Ex:3
for i in range(4):
    for j in range(4-i):
        print("# ",end=" ")
    print()

#Ex:4
for i in range(1,5):
      for j in range(i,5):
            print(j,end="  ")
      print()


#Ex:5
string1 = 'APQR'
string2 = 'ABCD'
for i in range(len(string1)):
    string1 = string1.replace(string1[i], string2[i])
    print(string1)

    
#Ex:6
a="ABCD"
b="PQR"
for i in range (4):
    print(a[:i+1]+ b[i:])



#Ex:7
string = '1234'
for i in range(len(string)):
    print(string[i:])



