class VkrcPoint:

    def __init__(self, posX, posY, posZ, posA, posB, posC, acc, robWzg, base, spsTrig):

        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.posA = posA
        self.posB = posB
        self.posC = posC
        self.acc = acc
        self.robWzg = robWzg
        self.base = base
        self.spsTrig = spsTrig

# Osobne klasy dla ruchu PTP i LIN - będą dziedziczyć po klasie VkrcPoint (otrzymają dodatkowe pola)

