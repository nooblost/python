
current_users = ['mike', 'admin', 'chris', 'abbie', 'Lee', 'WONG', 'AnITa']
new_users = ['MIKE', 'anita', 'lee', 'wong', 'chan']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' taken, choose a different one.")
    else:
        print(f"Welcome, new user '{new_user}'")
