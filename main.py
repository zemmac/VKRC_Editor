from classes.cSrcReader import SrcReader

path = 'C:\\Users\\ats\\PycharmProjects\\VKRC_Editor\\Dummy_Files\\up21.src'

a = SrcReader(path)
a.OpenFile()

print(''.join([i.ShowInlineForm() for i in a.inlineFormList if i.ShowInlineForm()]))
