'''
Password retry system (max 3 attempts)
If password is correct show login successful
else ask for password 3 times.
Once attemps exceed show account locked.
'''
p1 = "abc123"
for i in range(3):
    p2 = input("Enter your password: ")
    if p2 == p1:
        print("Login successful")
        break
    else:
        print("Incorrect password")
else:
    print("Account locked.")