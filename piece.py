import desk
import const


def rockIsPossible(char):
    if ((char == 'k') & (const.k)):
        const.k = False
        return True
    if ((char == 'K') & (const.K)):
        const.K = False
        return True


def queenStillStand(char):
    if ((char == 'q') & (const.q)):
        const.q = False
        return True
    if ((char == 'Q') & (const.Q)):
        const.Q = False
        return True


def getPiece(cord):
    return desk.map[int(cord[1])][int(cord[0])]


def is_real(cord1, cord2):
    if (getPiece(cord1) == ' '):
        return False

    if (getPiece(cord1) == 'p'):  # Pawn rules
        if ((int(cord1[1]) == 2) & (int(cord2[1]) == 4)):
            return True
        if ((int(cord1[1]) - int(cord2[1]) != 1) | (int(cord1[1]) - int(cord2[1]) != -1)):
            if ((int(cord1[0]) - int(cord2[0]) > 2) | (int(cord1[0]) - int(cord2[0]) < 1)):
                return True
            if (getPiece(cord2) != ' '):
                return False
        else:
            if ((getPiece(cord2) == ' ') & getPiece(cord2).islower()):
                return False
            else:
                return True

    if (getPiece(cord1) == 'P'):  # Pawn rules
        if ((int(cord1[1]) == 7) & (int(cord2[1]) == 5)):
            return True
        if ((int(cord1[1]) - int(cord2[1]) != 1) | (int(cord1[1]) - int(cord2[1]) != -1)):
            if ((int(cord1[0]) - int(cord2[0]) > 2) | ((int(cord1[0]) - int(cord2[0]) < 1))):
                return True
            if (getPiece(cord2) != ' '):
                return False
        else:
            if ((getPiece(cord2) == ' ') & getPiece(cord2).isupper()):
                return False
            else:
                return True

    if (getPiece(cord1) == 'k'):  # King rules
        if getPiece(cord2) == 'q':
            if (queenStillStand('q') & rockIsPossible('k')):
                return True
            else:
                return False
        if (((((int(cord2[0]) - int(cord1[0])) == 1) | (int(cord2[0]) - int(cord1[0])) == -1) | (
                cord2[1] - cord1[1]) == 1) | (
                (int(cord2[1]) - int(cord1[1])) == -1) & (getPiece(cord2) == ' ') | (getPiece(cord2).isupper())):
            return True
        else:
            return False

    if (getPiece(cord1) == 'K'):  # King rules
        if getPiece(cord2) == 'Q':
            if (queenStillStand('Q') & rockIsPossible('K')):
                return True
            else:
                return False
        if ((((int(cord2[0]) - int(cord1[0])) == 1) | (int(cord2[0]) - int(cord1[0]) == -1) | (
                int(cord2[1]) - int(cord1[1])) == 1) | (
                int(cord2[1]) - int(cord1[1]) == -1) & (getPiece(cord2) == ' ') | (getPiece(cord2).islower())):
            return True
        else:
            return False

    if (getPiece(cord1) == 'r'):  # Rook rules
        if ((int(cord1[0]) - int(cord2[0]) == 0) & (int(cord1[1]) - int(cord2[1]) == 0) & (
                (getPiece(cord2) == ' ') | (getPiece(cord2).isupper()))):
            if (int(cord1[0]) - int(cord2[0])) == 0:
                i1 = int(cord1[1])
                i2 = int(cord2[1])

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(cord1[0] + str(i1)) != ' ':
                        return False
            if (int(cord1[1]) - int(cord2[1])) == 0:
                i1 = int(cord1[0])
                i2 = int(cord2[0])

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(str(i1) + cord1[1]) != ' ':
                        return False
            return True

    if (getPiece(cord1) == 'R'):  # Rook rules
        if ((int(cord1[0]) - int(cord2[0]) == '0') & (int(cord1[1]) - int(cord2[1]) == '0') & (
                (getPiece(cord2) == ' ') | (getPiece(cord2).islower()))):
            if (int(cord1[0]) - int(cord2[0])) == 0:
                i1 = int(cord1[1])
                i2 = int(cord2[1])

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(cord1[0] + str(i1)) != ' ':
                        return False
            if (int(cord1[1]) - int(cord2[1])) == 0:
                i1 = int(cord1[0])
                i2 = int(cord2[0])

                if (i1 - i2 > 0):
                    iglass = i2
                    i2 = i1
                    i1 = iglass

                while (i2 > i1):
                    i1 = i1 + 1
                    if getPiece(str(i1) + cord1[1]) != ' ':
                        return False
            return True

    if (getPiece(cord1) == 'b'):  # Bishop rules
        if (int(cord2[0]) - int(cord1[0]) == int(cord2[1]) - int(cord2[1]) & (
                (getPiece(cord2) == ' ') | (getPiece(cord2).islower()))):
            bish = int(cord2[0]) - int(cord1[0])
            if bish < 0:
                bish = bish * (-1)
            bish0 = 0
            while (bish0 < bish):
                bish0 = bish0 + 1
                if getPiece(str(int(cord2[0]) - bish0) + str(int(cord2[1]) - bish0)) != ' ':
                    return False
        return True

    if (getPiece(cord1) == 'B'):  # Bishop rules
        if (int(cord2[0]) - int(cord1[0]) == int(cord2[1]) - int(cord2[1]) & (
                (getPiece(cord2) == ' ') | (getPiece(cord2).islower()))):
            bish = int(cord2[0]) - int(cord1[0])
            if bish < 0:
                bish = bish * (-1)
            bish0 = '0'
            while (bish0 < bish):
                bish0 = bish0 + 1
                if getPiece(str(int(cord2[0]) - bish0) + str(int(cord2[1]) - bish0)) != ' ':
                    return False
        return True

    if (getPiece(cord1) == 'n'):  # K***ht rules
        if (((int(cord2[0]) - int(cord1[0]) <= 2) | (int(cord2[0]) - int(cord1[0]) >= -2)) & (
                (int(cord2[1]) - int(cord1[1]) <= 2) | (
                int(cord2[1]) - int(cord1[1]) == -2)) & (getPiece(cord2).isupper() | (getPiece(cord2) == ' '))):
            return True
        else:
            return False

    if (getPiece(cord1) == 'N'):  # K***ht rules
        if (((int(cord2[0]) - int(cord1[0]) <= 2) | (int(cord2[0]) - int(cord1[0]) >= -2)) & (
                (int(cord2[1]) - int(cord1[1]) <= 2) | (int(cord2[1]) - int(cord1[1]) == -2)) & (
                getPiece(cord2).isupper() | (getPiece(cord2) == ' '))):
            return True
        else:
            return False
