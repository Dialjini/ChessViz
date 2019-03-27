import piece
import desk

a = ''

for i in desk.map:
    print(i)

while (a != 'quit'):
    a = input()
    if (a == 'help'):
        print('Available commands:')
        print('Cord commands. For example a7-a5. (a-h, 1-8)')
        print('back : Makes a step back in current game')
        print('restart : restarts current game')

    if (a == 'restart'):
        desk.map = desk.default
        for i in desk.map:
            print(i)
