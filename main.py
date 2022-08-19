from classes.cFold import Fold
from classes.cFoldComment import FoldComment
from classes.cFoldMotion import FoldMotion
from classes.cSrcReader import SrcReader

path = 'C:\\Users\\ats\\PycharmProjects\\VKRC_Editor\\Dummy_Files\\up21.src'

a = SrcReader(path)
a.OpenFile()

ttt=[]
#print(''.join([i.ShowInlineForm() for i in a.inlineFormList if i.ShowInlineForm()]))

Br: FoldMotion = a.inlineFormList[11]
print(Br.MotionType_1)
a.inlineFormList[11].setMotionType('LIN')
print(str(a.inlineFormList[11].MotionType_1))
print(Br.ShowInlineForm())
Br.setMotionType('KCIR')
print(Br.ShowInlineForm())
# ttt.append(Br.GenerateDictParserString())
# print(ttt)