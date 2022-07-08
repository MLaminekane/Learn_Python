# from calendar import c


# names = ['mohamed', 'lamine', 'gunther', 'naruto', 'admin']
# names = (input("name :  "))
# if names == 'admin':
#     print(f"Hello {names}, would you like to see a status report ?")
# else:
#     print(f"Hello {names},thank you for logging in again.")


from calendar import c


current_users =  ['mohamed', 'lamine', 'gunther', 'naruto', 'lofi']
new_users =  ['messi', 'lamine', 'cr7', 'naruto', 'ozil']

for new_user in new_users:
    if new_user in current_users:
        print(f"enter a new username {new_user}")
    elif new_user not in current_users:
        print(f"the username is available {new_user}")
        copy_current_users = current_users[:]
        