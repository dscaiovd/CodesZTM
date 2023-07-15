'''1 Create a user profile for your new game. This user profile will be 
 stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 

'''

user_profile = {
    'age' : input('Insert your age: '),
    'username' : input('What\'s your username?: '),
    'weapons' : ['Sword', 'Mace'],
    'is_active' : True,
    'clan' : 'Trahorn'
}

print(user_profile.keys())

new_weapon = user_profile['weapons'].append('Bow')
print(user_profile)

user_profile.update({'is_banned': False})
user_profile['is_banned'] = True

user2 = user_profile.copy()
user2.update({'age': input('Player 2, insert your age: '), 'username': input('Your username: ')})

username1 = user_profile.get('username')
username2 = user2.get('username')

print(f'{username1.capitalize()}, this is your character sheet: ', user_profile)
print(f'{username2.capitalize()}, this is your character sheet: ', user2)