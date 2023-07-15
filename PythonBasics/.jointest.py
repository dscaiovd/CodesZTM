country_list = input("Insert the countries you had visit separeted by space: ")
separeted_list = country_list.split(' ')

capitalize_country = [country.capitalize() for country in separeted_list]

joined_list = ' - '.join(capitalize_country)

print('The visited countries are:', joined_list)
