class VkrcPoint:

    def __init__(self, moveType, vb, ve, acc, robWzg, base, spsTrig):

        self.moveType = 'PTP'
        self.vb = 100
        self.ve = 0
        self.acc = 100
        self.robWzg = 0
        self.base = 0
        self.spsTrig = 0

    def __iter__(self):
        self.startIteration = self.moveType
        return self

    def __next__(self):
        pass
