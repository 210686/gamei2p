counter=0
correct = 0
i = 0
answer = ["true","false","false","true","true","false","false","false","false","true","true","true","true","false","true","false"]
while counter<15:
    f=open("testfile.txt","r")
    lines=f.readlines()
    print (lines[i*4+3]+lines[i*4]+lines[i*4+1]+lines[i*4+2]+lines[i*4+3])
    f.close()
    ans = input("").lower()
    while ans != "true" and ans != "false":
        print("Invalid")
        ans = input("").lower()
    if ans == answer[i]:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect")
    i += 1
    counter +=1
print("Your got",correct,"correct, which is",str(round(correct/15,2)*100)+"%.")
