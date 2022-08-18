from classes.cFold import Fold


class FoldComment(Fold):

    def __init__(self, foldList):
        super().__init__(foldList)

        self.Comment = self.getComment()

    def ShowInlineForm(self):
        return f'-- {self.getComment()} -- \n'

    def getComment(self):

        a = self.foldList[0].replace(';FOLD -- ', '')
        a = a[3:a.index(';')-4]
        # Second is just to check if both are the same
        b = self.foldList[0]
        b = b[b.index(',%P 1:Comment:')+18:-1]

        if a == b:
            return a
        else:
            return '!!!Error in Inline Form!!!'

    def setComment(self, newComment):

        self.foldList[0] = self.foldList[0].replace(f'-- {self.Comment} --', f'-- {newComment} --')
        self.foldList[0] = self.foldList[0].replace(f':, 2:{self.Comment}', f':, 2:{newComment}')
        self.foldList[2] = self.foldList[2].replace(f'M_COMMENT("{self.Comment}', f'M_COMMENT("{newComment}')

        return self.foldList



