from classes.cFold import Fold


class FoldMotion(Fold):

    motionTypes = {1: 'PTP',
                   2: 'LIN',
                   3: 'CIR',
                   4: 'KLIN',
                   5: 'KCIR'}
    speedUnits = {1: '%',
                  2: '[mm/s]',
                  3: '[mm/s]',
                  4: '[mm/s]',
                  5: '[mm/s]'}
    approxLabels = {1: ' VE=',
                    2: ' VE=',
                    3: ' VE=',
                    4: ' Genau=',
                    5: ' Genau='}
    approxUnits = {1: '%',
                   2: '%',
                   3: '%',
                   4: '[mm]',
                   5: '[mm]'}

    def __init__(self, foldList):
        super().__init__(foldList)

        self.dictParser = self.getDictParser()

        self.MotionType_1 = self.dictParser[1]
        self.SpeedLabel_2 = self.dictParser[2]
        self.SpeedValue_3 = self.dictParser[3]
        self.SpeedUnit_4 = self.dictParser[4]
        self.ApproxLabel_5 = self.dictParser[5]
        self.ApproxValue_6 = self.dictParser[6]
        self.ApproxUnit_7 = self.dictParser[7]
        self.AccLabel_8 = self.dictParser[8]
        self.AccValue_9 = self.dictParser[9]
        self.AccUnit_10 = self.dictParser[10]
        self.ToolLabel_11 = self.dictParser[11]
        self.ToolValue_12 = self.dictParser[12]
        self.BaseLabel_13 = self.dictParser[13]
        self.BaseValue_14 = self.dictParser[14]
        self.SPSTrigLabel_15 = self.dictParser[15]
        self.SPSTrigValue_16 = self.dictParser[16]
        self.SPSTrigUnit_17 = self.dictParser[17]
        self.LogicLabel_18 = self.dictParser[18]
        self.PointNrP1_19 = self.dictParser[19]
        self.PointNrP2_20 = self.dictParser[20]
        self.PointNrView_21 = self.dictParser[21]

    # ;FOLD KLIN VB=7[mm/s] Genau=0[mm] ACC=100% RobWzg=1 Base=2 SPSTrig=5[1/100s] P ;%{P}%MKUKATPVW,%CMOVE8,%VKLIN,
    #    %P 1:4, 2: VB=, 3:7, 4:[mm/s], 5: Genau=, 6:0, 7:[mm], 8: ACC=, 9:100, 10:%, 11: RobWzg=, 12:1,
    #    13: Base=, 14:2, 15: SPSTrig=, 16:5, 17:[1/100s], 18: P, 19:18, 20:-1, 21:16

    def getDictParser(self):
        dictParser = {}

        data = self.foldList[0].split('%P ')

        for name, val in [item.split(':') for item in data[1].split(",")]:
            dictParser[int(name)] = val

        return dictParser

    # def setDictParser(self):
    #
    #     self.dictParser[1] = self.MotionType_1
    #     self.dictParser[2] = self.SpeedLabel_2
    #     self.dictParser[3] = self.SpeedValue_3
    #     self.dictParser[4] = self.SpeedUnit_4
    #     self.dictParser[5] = self.ApproxLabel_5
    #     self.dictParser[6] = self.ApproxValue_6
    #     self.dictParser[7] = self.ApproxUnit_7
    #     self.dictParser[8] = self.AccLabel_8
    #     self.dictParser[9] = self.AccValue_9
    #     self.dictParser[10] = self.AccUnit_10
    #     self.dictParser[11] = self.ToolLabel_11
    #     self.dictParser[12] = self.ToolValue_12
    #     self.dictParser[13] = self.BaseLabel_13
    #     self.dictParser[14] = self.BaseValue_14
    #     self.dictParser[15] = self.SPSTrigLabel_15
    #     self.dictParser[16] = self.SPSTrigValue_16
    #     self.dictParser[17] = self.SPSTrigUnit_17
    #     self.dictParser[18] = self.LogicLabel_18
    #     self.dictParser[19] = self.PointNrP1_19
    #     self.dictParser[20] = self.PointNrP2_20
    #     self.dictParser[21] = self.PointNrView_21

    def GenerateDictParserString(self):
        a = ' ' + ' '.join([f'{item}:{self.dictParser[item]},' for item in self.dictParser])[:-1]
        return a

    def getMotionType(self):

        return self.motionTypes[int(self.MotionType_1)]

    def setMotionType(self, newMotionType: str):

        self.MotionType_1 = [key for key, value in self.motionTypes.items() if value == newMotionType][0]
        self.SpeedUnit_4 = [value for key, value in self.speedUnits.items() if key == self.MotionType_1][0]
        self.ApproxLabel_5 = [value for key, value in self.approxLabels.items() if key == self.MotionType_1][0]
        self.ApproxUnit_7 = [value for key, value in self.approxUnits.items() if key == self.MotionType_1][0]

        self.ShowInlineForm()
        print(self.foldList[0])

    def UpdateFoldList(self):

        pass

    def ShowInlineForm(self):

        # Visible inline form:
        # ;FOLD KLIN VB=7[mm/s] Genau=0[mm] ACC=100% RobWzg=1 Base=2 SPSTrig=5[1/100s] P;
        #       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # Define Buffers for all sections
        speedBuffer = self.SpeedLabel_2 + \
                      self.SpeedValue_3 + \
                      self.SpeedUnit_4
        approxBuffer = self.ApproxLabel_5 + \
                       self.ApproxValue_6 + \
                       self.ApproxUnit_7
        accBuffer = self.AccLabel_8 + \
                    self.AccValue_9 + \
                    self.AccUnit_10
        toolBuffer = self.ToolLabel_11 + \
                     self.ToolValue_12
        baseBuffer = self.BaseLabel_13 + \
                     self.BaseValue_14
        spstrigBuffer = self.SPSTrigLabel_15 + \
                        self.SPSTrigValue_16 + \
                        self.SPSTrigUnit_17
        logicBuffer = self.LogicLabel_18

        # Combine buffers into one
        buffer = self.getMotionType() + \
                 speedBuffer + \
                 approxBuffer + \
                 accBuffer + \
                 toolBuffer + \
                 baseBuffer + \
                 spstrigBuffer + \
                 logicBuffer + '\n'

        return buffer

