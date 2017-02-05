ans = []

message = ["Hello", "Bye", "Greetings"]

while True:
    n = input("Enter your message : ")
    ans.append(n)
    #print(ans)
    if n in message:
        if n is message[0]:
            print(message[0])
    for m, n in zip(message, ans):
        print("Bot : ",m)
    for user_ans in ans:
        print("User : ",user_ans)