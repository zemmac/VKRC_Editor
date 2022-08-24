class Fold:
    # Given foldList contains all fold lines as list arguments. It corresponds each instruction in VKRC viewer
    def __init__(self, foldList: list):
        self.foldList = foldList

    def __str__(self):
        return ''.join([i for i in self.foldList])

    def ShowInlineForm(self):

        return

    def setComment(self, newComment):

        pass

    def getComment(self):

        pass

    def saveFold(self):
        a = self.foldList
        b = []

        def Recursion(somelist):
            for i in somelist:
                if type(i) is list:
                    Recursion(i)
                    continue
                b.append(i.__str__())
            return b
        Recursion(a)

        return ''.join(b)
