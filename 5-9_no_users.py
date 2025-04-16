usernames = ['mike', 'admin', 'chris', 'abbie', 'lee']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"\nWelcome back, {username.title()}, here is the status report.")
        else:
            print(f"\nWelcome back, {username.title()}.")
else:
    print("We need to get some users!")