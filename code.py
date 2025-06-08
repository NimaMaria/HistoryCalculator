# SIMPLE CALCULATOR WITH HISTORY

def history_mode(a):
    while True:
        print('\n--- HISTORY ---')
        if len(history) == 0:
            print("No available history")
        else:
            for item in history:
                print(item)
        option=int(input("\nType 1 to to erase latest entry or 0 to go back: "))
        if option==1:
            if history:
                removed=history.pop()
                print(f"Removed: {removed}")
            else:
                print("No entry found")
        elif option==0:
            return
        else:
            print("Invalid option")

history=[]
while True:
    print("Enter your expression (eg;5+2-3) :")
    user_input=input()
    try:
        result=eval(user_input)
        if result == int(result):
            print("Result:",int(result))
        else:
            print("Result:",result)
        history.append(user_input+" ="+str(result))
    except:
        print("Invalid expression")
        continue

    while(True):
        print("Enter 1 to continue\n      0 to exit\n      2 for history mode: ")
        d = input()
        if d == '0':
            print('Calculator exited')
            exit()
        elif d == '1':
            break
        elif d == '2':
            history_mode(history)
        else:
            print('Invalid input. Try again')




