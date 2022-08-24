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
print(Br.ShowInlineForm())
a.inlineFormList[11].setMotionType('LIN')
print(Br.ShowInlineForm())

a.SaveFile()

# ttt.append(Br.GenerateDictParserString())
# print(ttt)