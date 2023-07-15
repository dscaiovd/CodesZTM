# check: if magician AND expert: "are a master magician"

# chek if magician but not export: "at least you're getting there"

# if you're not a magician: "You need magic powers"

is_magician = False
is_expert = True

if is_magician and is_expert: 
    print('You are a master magician.')
elif is_magician and not is_expert:
    print('At least you are getting there.')
elif not is_magician:
    print('You need magic powers.')

user = {
    'class' : 'Magician',
    'name' : 'Morthal',
    'Health' : 500
}

for k, v in user.items():
    print(k, v)