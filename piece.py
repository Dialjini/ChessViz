import main


def getPiece(cord):
    return main.a[cord[0]][cord[1]]


def is_real(piece, cord1, cord2):
    if (getPiece(cord1) == ' '):
        return False

    if (getPiece(cord1) == 'p'):
        if (((cord1[2] - cord2[2]) != '1') | (cord1[2] - cord2[2] != '-1')):
            if (((cord1[1] - cord2[1]) > '2') | (((cord1[1] - cord2) < '1'))):
                return False
            if (getPiece(cord2) != ' '):  # Pawn rules
                return False
        else:
            if (getPiece(cord2) == ' '):
                return False
            else:
                return True
