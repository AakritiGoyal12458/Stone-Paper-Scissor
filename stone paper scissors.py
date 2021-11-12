
##
##h=input("stone paper scissor")
##c=random
##for i in range(5)
##if bhavesh==stone or akkuu==scissor or
##
##akku score 
##if(akkuu win
##   akkuu score == akku score+1)
##if(bhavesh win
##   bhavesh score == akku score+1)
##if draw either add in both or nothing add
##
##
##round(5)
##akkuu - stone , paper , scissor ,stone,paper 3point(2)
##bhaveh - scissor , stone , stone ,paper,scissor points 3 
#score need to be increatsed continously

a=input("first player name ")
b=input("second player name ")
a_s=0
b_s=0
##noOfRound=int(input("enter the number of rounds"))
for i in range(1,4):
    print("choose from-stone,paper,scissor")
    c=input( a+" choose:" )
    d=input(b +" choose:")
    if (c=="stone" and d=="scissor") or (c=="paper" and d=="stone")or(c=="scissor" and d=="paper"):
        print(a+ " win")
        a_s=a_s+1
    elif(d=="stone" and c=="scissor")or(d=="paper" and c=="stone")or(d=="scissor" and c=="paper"):
        print ( b + " win")
        b_s=b_s+1
    else:
        print ("match draw")
    
print(a+" score" , a_s)
print (b+" Score", b_s)

if (a_s>b_s):
    print(a +" win the game ")
elif(a_s<b_s):
  print( b + " win the game ")
else:
  print("Draw")
print("thank you")

    
    

