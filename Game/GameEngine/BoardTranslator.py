import ../GamePlatform/GameBoard

class BoardTransalator:
    def __init__(self):
        self.newToOld = {
              11: 0,
              14: 1,
              17: 2,
              22: 3,
              24: 4,
              26: 5,
              33: 6,
              34: 7,
              35: 8,
              41: 9,
              42: 10,
              43: 11,
              45: 12,
              46: 13,
              47: 14,
              53: 15,
              54: 16,
              55: 17,
              62: 18,
              64: 19,
              66: 20,
              71: 21,
              74: 22,
              77: 23
            }

        self.oldToNew = {
              0:11,
              1:14,
              2:17,
              3:22,
              4:24,
              5:26,
              6:33,
              7:34,
              8:35,
              9:41,
              10:42,
              11:43,
              12:45,
              13:46,
              14:47,
              15:53,
              16:54,
              17:55,
              18:62,
              19:64,
              20:66,
              21:71,
              22:74,
              23:77
        }

#TODO
def oldBoard(oldBoard):

    return []

def getXyPos(oldPos):
    return self.oldToNew[oldPos]

def getOldPos(newPos):
    return self.newToOld[newPos]
