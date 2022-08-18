from classes.cFold import Fold
from classes.cFoldAnfang import FoldAnfang
from classes.cFoldComment import FoldComment
from classes.cFoldMotion import FoldMotion


def DefineFoldType(foldList: list):
    #
    # 0 - Error - no proper Fold
    # 1 - not used
    # 2 - '--' - Comment
    # 3 - Move instruction Fold
    # 4 - Empty line Fold
    # 5 - Anfang Fold (for Folge Anfang there is empty line in Viewer)
    #
    if ';FOLD -- ' in foldList[0]:
        return 2
    elif ';FOLD PTP ' in foldList[0] \
            or ';FOLD LIN ' in foldList[0] \
            or ';FOLD CIR ' in foldList[0] \
            or ';FOLD KLIN' in foldList[0] \
            or ';FOLD KCIR' in foldList[0]:
        return 3
    elif '; FOLD ;%{H}' in foldList[0]:
        return 4
    elif '; FOLD ;%{H} %MKUKATPVW' in foldList[0] or \
            '; FOLD' in foldList[0] and 'Anfang' in foldList[0]:
        return 5
    else:
        return 0


class SrcReader:

    # Reading the .src file and split it into useful folds:
    # - whole motion instructions with plc logic (between ;FOLD ;ENDFOLD instructions)
    # - UP Anfang instructions
    # - File header
    # - SPS_Trig section (bottom of each .src file)
    # Read and pass motion folds into InlineFormPoint class to create instructions

    def __init__(self, filePath):
        self.filePath = filePath
        self.inlineFormList = []

    def OpenFile(self):
        # Open file
        try:
            srcFile = open(self.filePath)
        except OSError as error:
            return
        # Read lines into list
        srcLines = srcFile.readlines()
        #
        # Separate useful Folds in list
        #
        # Main SRC Function definition name. No idea how to get it in better way and put into file.
        # For now, it must be enough...
        defName = []
        # Stack for Folds. Motion folds has plc logic folds inside.
        # We want to have all PLC logic of a current motion instruction within one motion fold.
        foldsStack = []
        # Stack for DEFs in SRC File. There could be DEF UP or DEF SPS_TRIG.
        # Only useful for Def UP. Pass DEF SPS_TRIG as it is
        defStack = []
        # List for SRC Header instructions. Some parameters are stored here before 'Anfang' section
        # Could be useful for later conception.
        header = []
        # List for SRC Anfang instructions
        anfang = []
        # List of Inline Forms with whole folds inside. Each index is full Inline Form instruction
        inlineFormList = []
        # Buffer list. Stored lines between fold-endfold before assign it to specific list
        bufferList = []
        #
        # Help flags for control if part of the code has already been stored in list
        srcAnfang = False
        endOfPoints = False
        endOfHeader = False
        #
        # Main fun here
        for i in srcLines:
            if not endOfPoints:             # Separate folds for motion instructions, comments, header and anfang
                if 'def ' in i.lower():     # First DEF instruction in file. Useful to separate Anfang
                    defStack.append(i)      # Add line to stack (doesn't matter what to add)
                    defName.append(i)       # First DEF instruction defines the main function (file name).
                    endOfHeader = True      # First DEF instructions defines end of header section
                # END instruction tells that this is end of DEF main function. Need exactly 'END' no more
                if 'end' in i.lower() and len(i.replace('\n', '')) == 3:    # There is '\n' after 'END' so remove it
                    defStack.pop()                      # Remove DEF stack
                    if len(foldsStack) > 0:             # There is FOLD ;%{H} before END so need to remove stack
                        foldsStack.pop()                #
                    inlineFormList.append(bufferList)   # Add to inline form list current buffer
                    bufferList = []                     # Erase buffer
                    endOfPoints = True                  # This is end of motion instruction folds
                    bufferList.append(i)                # These instructions add 'END' to the list
                    inlineFormList.append(bufferList)   # --
                    bufferList = []                     # Erase buffer
                # Add folds to stack to separate motion instructions
                if ' fold' in i.lower() or ';fold ' in i.lower():
                    foldsStack.append(i)

                if len(foldsStack) > 0:
                    bufferList.append(i)
                # When reach ENDFOLD, remove last input in stack
                if 'endfold' in i.lower() and len(foldsStack) > 0:
                    foldsStack.pop()
                    # When after remove last input in stack, stack is empty, assign whole buffer to the list
                    if len(foldsStack) == 0:
                        inlineFormList.append(bufferList)
                        bufferList = []
                        del bufferList[:]

                # Separate file's Header
                if not endOfHeader:
                    header.append(i)

                # Separate file's 'Anfang'
                if len(defStack) == 1 and not srcAnfang:
                    anfang.append(i)
            # When reach End of Points flag, just add every line to buffer. No need to bother this
            else:
                bufferList.append(i)

        # After all iterations add buffer to inline form list
        inlineFormList.append(bufferList)
        bufferList = []
        bufferList.clear()

        # Add Header at [0] and DefName at [1] to the inlineFormList
        inlineFormList.insert(0, defName)
        inlineFormList.insert(0, header)


        # We need to declare Motion folds, Comment folds and Anfang fold.
        # After that, replace list with a class object of each fold
        # So for example: list that contains Motion Fold is now object of class FoldMotion
        # The list is now in class object: inlineFormList[X] -> FoldMotion(X)


        for i in range(len(inlineFormList)):
            a = DefineFoldType(inlineFormList[i])
            if a == 2:
                inlineFormList[i] = FoldComment(inlineFormList[i])
            elif a == 3:
                inlineFormList[i] = FoldMotion(inlineFormList[i])
            elif a == 4:
                inlineFormList[i] = Fold(inlineFormList[i])
            elif a == 5:
                inlineFormList[i] = FoldAnfang(inlineFormList[i])
            else:
                inlineFormList[i] = Fold(inlineFormList[i])



        # After above code, there is a list inlineFormList where all instruction for each Inline Form are stored
        # One list index of inlineFormList is complete code stored as list - each line has its own index
        # inLineFormList[0] - file header. Some useful elements like: comment
        # inLineFormList[1] - definition of the main function name
        # inlineFormList[2] - Anfang
        # inlineFormList[-3] - ;FOLD ;%{H}
        # inLineFormList[-2] - END
        # inLineFormList[-1] - DEF SPS_TRIG
        # From [2] element we need to just join every element for future file creation
        # From [-3] and [-2] just pass to the future file
        # From [-1] element we need to join every elementy for future file creation
        # Rest elements are visible in VKRC and are needed for edit/take args etc. (we will pass them to class creation)
        #

        self.inlineFormList = inlineFormList

        return self.inlineFormList

    def FileName(self):
        fileName = self.inlineFormList[1][0].replace('\n', '').replace('DEF ', '').replace('()', '')
        return fileName

    def SaveFile(self):
        fileName = self.FileName()
        checkFile = open(f'Output_Files/{fileName}.src', 'w')
        checkFile.write(''.join(sum(self.inlineFormList, [])))



