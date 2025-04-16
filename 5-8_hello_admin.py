usernames = ['mike', 'ADmiN', 'chris', 'abbie', 'lee']

usernames_lower = [user.lower() for user in usernames]

for username in usernames_lower:
    if username == 'admin':
        print(f"Welcome back, {username.title()}, here is the status report.\n")
    else:
        print(f"Welcome back, {username.title()}.\n")
