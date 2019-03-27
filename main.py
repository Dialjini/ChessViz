import desk
import piece

a = ''


def getCord1(a):
    return True


# TODO make getCord... methods

def getCord2(a):
    return True


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
    if (len(a) == 5):
        if (a[2] == '-'):
            cord1 = getCord1(a)
            cord2 = getCord2(a)
            if (desk.is_real(cord1=cord1, cord2=cord2)):
                desk.history.append({'step': a, 'stash': piece.getPiece(cord=cord2)})
            print('debug')
