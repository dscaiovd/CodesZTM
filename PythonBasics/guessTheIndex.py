def list_range():
    while True:
        try:
            start, end = map(int, input('Insert the range of the list separating by a comma: ').split(', '))
            break
        except ValueError:
            print('Invalid input. Certify to insert two integers separeted by a comma')
    for i, char in enumerate(range(start, end +1)):
            if char == 50:
                print(f'The index of 50 is {i}')
                return

    print('The character 50 has not been found in the list. Try again.\n')

list_range()