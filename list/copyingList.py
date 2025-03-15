# When u copy a list, don't forget to use a 'slice'
my_foods = ['pizza', 'falafel', 'carot cake']
friend_foods = my_foods[:]

my_foods.append('cannonli')
friend_foods.append('ice-cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)