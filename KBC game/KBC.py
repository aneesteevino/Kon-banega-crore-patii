welcome="  Wellcome to "
KBC=" KBC "
print(welcome.center(50,"*"))
print(KBC.center(50,"*"))


print("Please press 1 if you want  to PLay !!!")
userinput=int(input("Enter here : "))
if userinput==int("1"):
    list1=['Who is founder of Pakistan ?\n1. imran khan\n2. nawaz sharif\n3. Quad e azam  '," what is capital of Pakistan ?\n1. karachi\n2. lahore\n3. islamabad  ","\n what is currency of Pakistan ?\n1. dollar\n2. rupees\n3. euro  ","\n what is national language of Pakistan ?\n1. urdu\n2. english\n3. sindhi"]
    list2=[1,3,3,2]
    rupees=[1000,2000,3000]
    print(list1[0])
    userinput=int(input("Enter  option number here : "))
    if userinput==list2[1]:
              print("congratulation you have won ",rupees[0])
    else: print("wrong answer !")
    print("Next question is : ")
    print(list1[1])
    userinput=int(input("Enter  option number here : "))
    if userinput==list2[2]:
       print(" correct answer !!! \n congratulation you have won ",rupees[1],"\n Your current winning amout is : ",int(rupees[0]+rupees[1]))
    else: print("wrong answer !")
    print("Next question is : ")
    print(list1[2])
    userinput=int(input("Enter  option number here : "))
    if userinput==list2[3]:
       print(" correct answer !!! \n congratulation you have won ",rupees[2],"\n Your current winning amout is : ",int(rupees[0]+rupees[1]+rupees[2]))

                    
    else:   
        print("Sorry you have given wrong answer")
        
