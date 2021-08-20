
# Error Handling

x= 4

while True:
    try:
        x = int(input("Type the right number: "))
        if x==4:
            print("Finally. You win")
            break
    except ValueError:
        print("Wrong. Type in 4")
    