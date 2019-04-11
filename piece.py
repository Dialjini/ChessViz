import main
import const


def rockIsPossible(char):
    if (char == 'k' & const.k):
        const.k = False
        return True
    if (char == 'K' & const.K):
        const.K = False
        return True


def queenStillStand(char):
    if (char == 'q' & const.q):
        const.q = False
        return True
    if (char == 'Q' & const.Q):
        const.Q = False
        return True


def getPiece(cord):
    return main.a[cord[0]][cord[1]]


def is_real(cord1, cord2):
    if (getPiece(cord1) == ' '):
        return False

    if (getPiece(cord1) == 'p'):  # Pawn rules
        if (((cord1[1] - cord2[1]) != '1') | (cord1[1] - cord2[1] != '-1')):
            if (((cord1[0] - cord2[0]) > '2') | (((cord1[0] - cord2[0]) < '1'))):
                return False
            if (getPiece(cord2) != ' '):
                return False
        else:
            if (getPiece(cord2) == ' '):
                return False
            else:
                return True

    if (getPiece(cord1) == 'P'):  # Pawn rules
        if (((cord1[1] - cord2[1]) != '1') | (cord1[1] - cord2[1] != '-1')):
            if (((cord1[0] - cord2[0]) > '2') | (((cord1[0] - cord2[0]) < '1'))):
                return False
            if (getPiece(cord2) != ' '):
                return False
        else:
            if (getPiece(cord2) == ' '):
                return False
            else:
                return True

    if (getPiece(cord1) == 'k'):  # King rules
        if getPiece(cord2) == 'q':
            if (queenStillStand('q') & rockIsPossible('k')):
                return True
            else:
                return False
        if ((((cord2[0] - cord1[0]) == '1') | (cord2[0] - cord1[0] == '-1') | (cord2[1] - cord1[1]) == '1') | (
                cord2[1] - cord1[1] == '-1') & getPiece(cord2) == ' '):
            return True
        else:
            return False

    if (getPiece(cord1) == 'K'):  # King rules
        if getPiece(cord2) == 'Q':
            if (queenStillStand('Q') & rockIsPossible('K')):
                return True
            else:
                return False
        if ((((cord2[0] - cord1[0]) == '1') | (cord2[0] - cord1[0] == '-1') | (cord2[1] - cord1[1]) == '1') | (
                cord2[1] - cord1[1] == '-1') & getPiece(cord2) == ' '):
            return True
        else:
            return False

    if (getPiece(cord1) == 'r'):  # Rook rules
        if ((cord1[0] - cord2[0] == '0') & (cord1[1] - cord2[1] == '0')):
            if (cord1[0] - cord2[0]) == 0:
                i1 = cord1[1]
                i2 = cord2[1]

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(cord1[0] + i1) != ' ':
                        return False
            if (cord1[1] - cord2[1]) == 0:
                i1 = cord1[0]
                i2 = cord2[0]

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(i1 + cord1[1]) != ' ':
                        return False
            return True

    if (getPiece(cord1) == 'R'):  # Rook rules
        if ((cord1[0] - cord2[0] == '0') & (cord1[1] - cord2[1] == '0')):
            if (cord1[0] - cord2[0]) == 0:
                i1 = cord1[1]
                i2 = cord2[1]

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(cord1[0] + i1) != ' ':
                        return False
            if (cord1[1] - cord2[1]) == 0:
                i1 = cord1[0]
                i2 = cord2[0]

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(i1 + cord1[1]) != ' ':
                        return False
            return True
