#the necessary variables for the code
counter=0
correct = 0
i = 0

#the answers
answer = ["true","false","false","true","true","false","false","false","false","true","true","true","true","false","true","false"]

#the body of the code
while counter<15:
    f=open("testfile.txt","r")#open the file
    lines=f.readlines()
    print (lines[i*4+3]+lines[i*4]+lines[i*4+1]+lines[i*4+2]+lines[i*4+3])#printing out the lines on the text file
    f.close()#close the file
    ans = input("").lower()#inputting user's answer
    while ans != "true" and ans != "false":
        print("Invalid")
        ans = input("").lower()
    if ans == answer[i]:#correct
        print("Correct!")
        correct += 1
    else:#wrong
        print("Incorrect")
    i += 1
    counter +=1
print("Your got",correct,"correct, which is",str(round(correct/15,2)*100)+"%.")
#point showed in npercentage form
