alien_0 = { 
    'couleur': 'red',
    'points': '10'
}
# print(alien_0)
alien_0['x_positions'] = 0
alien_0['y_positions'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

# alien = {}
# alien['color'] = 'black'
# alien['taille'] = '1m80'
# print(alien)
# alien['color'] = 'red'
# print(f"nouvelle couleur {alien['color']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_positions'] = alien_0['x_positions'] + x_increment
print(f"position: {alien_0['x_positions']}")