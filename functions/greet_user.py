def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['m', 'l', 'k']
greet_users(usernames)
