from classes.cVkrcPoint import VkrcPoint


class VkrcPointPTP(VkrcPoint):

    def __init__(self, pointNumber, posX, posY, posZ, posA, posB, posC, acc, robWzg, base, spsTrig,
                 E1, E2, E3, E4, E5, E6, vb, ve, configS, configT):
        super().__init__(pointNumber, posX, posY, posZ, posA, posB, posC, acc, robWzg, base, spsTrig,
                         E1, E2, E3, E4, E5, E6)
        self.vb = vb
        self.ve = ve
        self.configS = configS
        self.configT = configT
        self.motionType = 'PTP'

    def setVb(self, vb):
        try:
            if 0 < vb <= 100:
                self.vb = int(vb)
        except ValueError:
            pass

    def getVb(self):
        return self.vb

    def setVe(self, ve):
        try:
            if 0 <= ve <= 100:
                self.ve = int(ve)
        except ValueError:
            pass

    def setConfig(self, configS, configT):
        try:
            if 0 < configS < 100 and 0 < configT < 100:
                self.configS = int(configS)
                self.configT = int(configT)
        except ValueError:
            pass

    def getConfig(self):
        return self.configS, self.configT

    def getMotionType(self):
        return self.motionType

