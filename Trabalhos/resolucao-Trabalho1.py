
class Rainha:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        pass


class Tabuleiro:

    qntRainhas = 0
    rainhas = [] 

    def __init__(self,n):
        self.n = n
        self.tabuleiro =[[0 for x in range(n)] for y in range(n)]

    
    def addQueen(self,rainha):
        self.rainhas.append(rainha)
        self.tabuleiro[rainha.x][rainha.y]=1
        self.updatePositions(rainha.x,rainha.y)

    def updatePositions(self,x,y):
        # atualizando horizontal e vertical
        for i in range(self.n):
            if(i!=x):
                self.tabuleiro[i][y] = -1
            if(i!=y):
                self.tabuleiro[x][i] = -1

        #atualizando verticais
        for i in range(1,y+1):
            if(x-i >= 0 and y-i >= 0):
                self.tabuleiro[x-i][y-i] = -1
            if(x+i < self.n and y-i >= 0):
                self.tabuleiro[x+i][y-i] = -1
        for i in range(1,len(range(x,self.n))):
            if(x-i >= 0 and y+i < self.n):
                self.tabuleiro[x-i][y+i] = -1
            if(x+i < self.n and y+i < self.n):
                self.tabuleiro[x+i][y+i] = -1
        

    def showTable(self):
        for i in range(self.n):
            print(self.tabuleiro[i])

    def findValidPosition(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.tabuleiro[i][j] == 0):
                    return x,y
        return [-1,-1]

    def DFS(self):
        for i in range(self.n):
            x,y = self.findValidPosition()
            if(x == -1):
                continue

class NQueensProblem():

    def __init__(self,tab):
        self.tabuleiro = tab
        



tab = Tabuleiro(10)

tab.addQueen(Rainha(3,1))
tab.addQueen(Rainha(0,9))

tab.showTable()