class VkrcPoint:

    # Init
    def __init__(self, pointNumber, posX, posY, posZ, posA, posB, posC, acc, robWzg, base, spsTrig,
                 E1, E2, E3, E4, E5, E6):

        self.pointNumber = pointNumber  # Point number in current UP/Forge
        self.posX = posX                # X cartesian coordinate
        self.posY = posY                # Y cartesian coordinate
        self.posZ = posZ                # Z cartesian coordinate
        self.posA = posA                # A rotate coordinate (Rz)
        self.posB = posB                # B rotate coordinate (Ry)
        self.posC = posC                # C rotate coordinate (Rx)
        self.acc = acc                  # Acceleration (default: 100%)
        self.robWzg = robWzg            # Robot tool number to reach this point
        self.base = base                # Robot base number in which coordinates this point is defined
        self.spsTrig = spsTrig          # SPSTrigger: 0 for via points, 5 for fine points
        self.E1 = E1                    # External axis E1 value
        self.E2 = E2                    # External axis E2 value
        self.E3 = E3                    # External axis E3 value
        self.E4 = E4                    # External axis E4 value
        self.E5 = E5                    # External axis E5 value
        self.E6 = E6                    # External axis E6 value

    # Setting pointNumber
    def setPointNumber(self, pointNumber):
        try:
            self.pointNumber = int(pointNumber)
        except ValueError:
            pass

    # Getting pointNumber
    def getPointNumber(self):
        return self.pointNumber

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

    #
    # External Axes
    #
    # E1
    # Setting E1 value
    def setE1(self, E1):
        # Check if it is float number. If not - do nothing
        try:
            self.E1 = float(E1)
        except ValueError:
            pass

    # Getting E1 value
    def getE1(self):
        return self.E1

    # E2
    # Setting E2 value
    def setE2(self, E2):
        # Check if it is float number. If not - do nothing
        try:
            self.E2 = float(E2)
        except ValueError:
            pass

    # Getting E2 value
    def getE2(self):
        return self.E2

    # E3
    # Setting E3 value
    def setE3(self, E3):
        # Check if it is float number. If not - do nothing
        try:
            self.E3 = float(E3)
        except ValueError:
            pass

    # Getting E3 value
    def getE3(self):
        return self.E3

    # E4
    # Setting E4 value
    def setE4(self, E4):
        # Check if it is float number. If not - do nothing
        try:
            self.E4 = float(E4)
        except ValueError:
            pass

    # Getting E4 value
    def getE4(self):
        return self.E4

    # E5
    # Setting E5 value
    def setE5(self, E5):
        # Check if it is float number. If not - do nothing
        try:
            self.E5 = float(E5)
        except ValueError:
            pass

    # Getting E5 value
    def getE5(self):
        return self.E5

    # E6
    # Setting E6 value
    def setE6(self, E6):
        # Check if it is float number. If not - do nothing
        try:
            self.E6 = float(E6)
        except ValueError:
            pass

    # Getting E6 value
    def getE6(self):
        return self.E6

