class InlineFormComment:
    def __init__(self, par1: str, par2: str):
        self.par1 = par1
        self.par2 = par2

    def InlineForm(self):

        return f'-- {self.par2} --'
