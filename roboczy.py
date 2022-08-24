class klasa:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def __str__(self):
        return f'var1: {self.var1}, var2: {self.var2} '

class klasa2(klasa):
    def __init__(self, var1, var2):
        super().__init__(var1, var2)



a = klasa2(1,2)
b = klasa2(3,4)
c = klasa(5,6)

lista = [a,b,c]
lista2 = []
for i in lista:
    print(i)
    lista2.append(i.__str__())
glista = ''.join(lista2)
print(glista)

