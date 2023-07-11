country_list = input("Digite os países visitados separados por espaço: ")
separeted_list = country_list.split(' ')

capitalize_country = [country.capitalize() for country in separeted_list]

joined_list = ' - '.join(capitalize_country)

print('Os países visitados são:', joined_list)