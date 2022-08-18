class InlineFormPoint:

    def __init__(self, par1: int, par2: str, par3: int, par4: str, par5: str, par6: int, par7: str, par8: str,
                 par9: int, par10: str, par11: str, par12: int, par13: str, par14: int, par15: str, par16: int,
                 par17: str, par18: str, par19: int, par20: int, par21: int):

        self.par1 = int(par1)           # 1: Motion type: 1 - ptp, 2 - lin, 3 - cir, 4 - klin, 5 - kcir
        self.par2 = par2                # 2: ' vb='
        self.par3 = int(par3)           # 3: vb value
        self.par4 = par4                # 4: vb unit
        self.par5 = par5                # 5: ' ve='
        self.par6 = int(par6)           # 6: ve value
        self.par7 = par7                # 7: ve unit
        self.par8 = par8                # 8: ' acc='
        self.par9 = int(par9)           # 9: acc value
        self.par10 = par10              # 10: acc unit
        self.par11 = par11              # 11: ' RobWzg='
        self.par12 = int(par12)         # 12: RobWzg number
        self.par13 = par13              # 13: ' Base='
        self.par14 = int(par14)         # 14: Base number
        self.par15 = par15              # 15: ' SPSTrig='
        self.par16 = int(par16)         # 16: SPSTrig value
        self.par17 = par17              # 17: SPSTrig unit
        self.par18 = par18              # 18: 'P' - if there's PLC logic?
        self.par19 = int(par19)         # 19: point number (który to punkt w pliku .dat) ?
        self.par20 = int(par20)         # 20: point number (który to punkt w pliku .dat - dla kcir/cir; -1 jeśli nie dotyczy (np. PTP, LIN))) ?
        self.par21 = int(par21)         # 21: point number (liczone po kolei, ktora to instrukcja ruchu) ?

    def DefineMotionType(self):
        motionTypes = {1: 'PTP',
                       2: 'LIN',
                       3: 'CIR',
                       4: 'KLIN',
                       5: 'KCIR'}
        return motionTypes[self.par1]

    # Returns the motion instruction's inline form string (like instruction visible in normal Vkrc view)
    def InlineForm(self):
        motionType = self.DefineMotionType()

        # Example:
        # PTP VB=100% VE=0% ACC=100% RobWzg=1 Base=0 SPSTrig=5[1/100s] P
        #
        return f'{motionType}' \
               f'{self.par2}{self.par3}{self.par4}' \
               f'{self.par5}{self.par6}{self.par7}' \
               f'{self.par8}{self.par9}{self.par10}' \
               f'{self.par11}{self.par12}' \
               f'{self.par13}{self.par14}' \
               f'{self.par15}{self.par16}' \
               f'{self.par17}{self.par18}'


