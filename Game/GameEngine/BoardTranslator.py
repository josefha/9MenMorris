
class BoardTranslator:
    def __init__(self):
        self.newToOld = {
              11: 0,
              41: 1,
              71: 2,
              22: 3,
              42: 4,
              62: 5,
              33: 6,
              43: 7,
              53: 8,
              14: 9,
              24: 10,
              34: 11,
              54: 12,
              64: 13,
              74: 14,
              35: 15,
              45: 16,
              55: 17,
              26: 18,
              46: 19,
              66: 20,
              17: 21,
              47: 22,
              77: 23
            }

        self.oldToNew = {
              0:11,
              1:41,
              2:71,
              3:22,
              4:42,
              5:62,
              6:33,
              7:43,
              8:53,
              9:14,
              10:24,
              11:34,
              12:54,
              13:64,
              14:74,
              15:35,
              16:45,
              17:55,
              18:26,
              19:46,
              20:66,
              21:17,
              22:47,
              23:77
        }


    # Transforms Board to old format
    def getOldBoard(self, newBoard):
        oldBoard = []

        for k,e in newBoard.items():
            if(e.owner == None):
                char = '_'
            elif(e.owner.stone_type == 'black'):
                char = 'X'
            elif(e.owner.stone_type == 'white'):
                char = 'O'

            oldBoard.append(char)

        return oldBoard

    # Transforms old postion to new
    def getNewPos(self, oldPos):
        return str(self.oldToNew[oldPos])

    # Transforms new postion to old
    def getOldPos(self, newPos):
        newPos = int(newPos)
        return self.newToOld[newPos]

    # returns current player in old format
    def getCurrentPlayerChar(self, player):
        if(player.stone_type == 'black'):
            return 'X'
        else:
            return 'O'
