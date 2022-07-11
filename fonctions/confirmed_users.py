from calendar import c


fUsers = ['naruto', 'goku', 'eren']
cUsers = []
while fUsers:
    pUsers = fUsers.pop()
    print(f"Verifying user: {pUsers.title()}")
    cUsers.append(pUsers)
print("\nThe following users have been confirmed:")
for cUser in cUsers:
    print(cUser.title())