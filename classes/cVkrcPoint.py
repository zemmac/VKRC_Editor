class VkrcPoint:

    # Init
    def __init__(self, posX, posY, posZ, posA, posB, posC, acc, robWzg, base, spsTrig):

        self.posX = posX        # X cartesian coordinate
        self.posY = posY        # Y cartesian coordinate
        self.posZ = posZ        # Z cartesian coordinate
        self.posA = posA        # A rotate coordinate (Rz)
        self.posB = posB        # B rotate coordinate (Ry)
        self.posC = posC        # C rotate coordinate (Rx)
        self.acc = acc          # Acceleration (default: 100%)
        self.robWzg = robWzg    # Robot tool number to reach this point
        self.base = base        # Robot base number in which coordinates this point is defined
        self.spsTrig = spsTrig  # SPSTrigger: 0 for via points, 5 for fine points

    # X
    # Setting point's X coordinate
    def setPosX(self, posX):
        # Check if it is float number. If not - do nothing
        try:
            self.posX = float(posX)
        except ValueError:
            pass

    # Getting point's X coordinate
    def getPosX(self):
        return self.posX

    # Y
    # Setting point's Y coordinate
    def setPosY(self, posY):
        # Check if it is float number. If not - do nothing
        try:
            self.posY = float(posY)
        except ValueError:
            pass

    # Getting point's Y coordinate
    def getPosY(self):
        return self.posY

    # Z
    # Setting point's Z coordinate
    def setPosZ(self, posZ):
        # Check if it is float number. If not - do nothing
        try:
            self.posZ = float(posZ)
        except ValueError:
            pass

    # Getting point's Z coordinate
    def getPosZ(self):
        return self.posZ

    # A
    # Setting point's A rotated coordinate
    def setPosA(self, posA):
        # Check if it is float number. If not - do nothing
        try:
            self.posA = float(posA)
        except ValueError:
            pass

    # Getting point's A rotated coordinate
    def getPosA(self):
        return self.posA

    # B
    # Setting point's B rotated coordinate
    def setPosB(self, posB):
        # Check if it is float number. If not - do nothing
        try:
            self.posB = float(posB)
        except ValueError:
            pass

    # Getting point's B rotated coordinate
    def getPosB(self):
        return self.posB

    # C
    # Setting point's C rotated coordinate
    def setPosC(self, posC):
        # Check if it is float number. If not - do nothing
        try:
            self.posC = float(posC)
        except ValueError:
            pass

    # Getting point's C rotated coordinate
    def getPosC(self):
        return self.posC

    # ACC
    # Setting point's acceleration value
    def setAcc(self, acc):
        # Check if it is int number. If not - do nothing
        try:
            self.acc = int(acc)
        except ValueError:
            pass

    # Getting point's acceleration value
    def getAcc(self):
        return self.acc

    # RobWzg
    # Setting point's tool number to reach this point
    def setRobWzg(self, robWzg):
        # Check if it is int number. If not - do nothing
        try:
            self.robWzg = int(robWzg)
        except ValueError:
            pass

    # Getting point's tool number to reach this point
    def getRobWzg(self):
        return self.robWzg

# Osobne klasy dla ruchu PTP i LIN - będą dziedziczyć po klasie VkrcPoint (otrzymają dodatkowe pola)

