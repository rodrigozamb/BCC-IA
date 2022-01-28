

inFile = open("in.txt",'r')
outFile = ""
solutionsCount = 0


#Função que checa se uma determinada rainha entra em conflito com outra rainha do tabuleiro
def checkValidPosition(tabuleiro, r, c):
 
    # conflito de rainhas na mesma coluna
    for i in range(r):
        if tabuleiro[i][c] == 'X':
            return False
 
    # conflito de rainhas na diagonal primaria
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 'X':
            return False
        i -= 1
        j -= 1
 
    # conflito de rainhas na diagonal secundaria
    (i, j) = (r, c)
    while i >= 0 and j < len(tabuleiro):
        if tabuleiro[i][j] == 'X':
            return False
        i -= 1
        j += 1
 
    return True
 
 
def showSolution(tabuleiro):
    for r in tabuleiro:
        # print(str(r).replace(',', '').replace('\'', ''))
        outFile.write(str(r).replace(',', '').replace('\'', '')+'\n')
    # print()
    outFile.write('\n')
 
 
def nRainhas(tabuleiro, r):
    global solutionsCount

    # caso base, onde uma solução foi encontrada
    if (r == len(tabuleiro)):
        showSolution(tabuleiro)
        solutionsCount+=1
        return
 
    # adicionar uma rainha e dar sequencia na recursão
    for i in range(len(tabuleiro)):
 
        # testa validade de uma determinada posição passivel de ser colocada uma rainha
        if checkValidPosition(tabuleiro, r, i):
            
            tabuleiro[r][i] = 'X'
 
            # adiciona uma rainha e segue a recusão
            nRainhas(tabuleiro, r + 1)
 
            # remove a rainha da posição, deixando-a inválida para as próximas iterações 
            tabuleiro[r][i] = '-'
 

def main():
    global solutionsCount
    global inFile
    global outFile
    for i in inFile:
        n = int(i)
        solutionsCount = 0

        tabuleiro = [['-' for x in range(n)] for y in range(n)]
 
        outFileStr = "./outs/"+str(n)+'-out.txt'
        outFile = open(outFileStr,'w')
        
        nRainhas(tabuleiro, 0)
        
        outFile.write('\nSolutions = '+str(solutionsCount)+'\n')
        
        
    
    outFile.close()
    inFile.close()


main()