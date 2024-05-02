#Print triangle by python

def triangle():
    print("What's kind of shape do you want to print?")
    print("1.Triangle 1")
    print("2.Triangle 2")
    question = str(input("> "))
    if question == "1":
        print("How many line do you want to print?")
        line1 = int(input("> "))
        print("#" * 15)
        for i in range(1,line1):
            print("*" * i,end="\n")
        print("#" * 15)
    elif question == "2":
        print("How many line do you want to print?")
        line2 = int(input("> "))
        print("#" * 15)
        for j in range(1,line2):
            print("*" * (line2 -j))
        print("#" * 15)  
triangle()      

