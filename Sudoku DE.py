import random




mylist=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solved_soduko=[[8, 2, 7, 1,5, 4 ,3, 9, 6],
              [9, 6, 5, 3, 2, 7, 1, 4, 8],
              [3, 4, 1, 6, 8, 9, 7, 5, 2],
              [5, 9, 3, 4, 6, 8, 2, 7, 1],
              [4, 7, 2, 5, 1, 3, 6, 8, 9],
              [6, 1, 8, 9, 7, 2, 4, 3, 5],
              [7, 8, 6, 2, 3, 5, 9, 1, 4],
              [1, 5, 4, 7, 9, 6, 8, 2, 3],
              [2, 3, 9, 8, 4, 1, 5, 6, 7]]

##get larget index of the population
def max_index(sorted_population):
    max = 0
    index=0
    for i in range (100):
        x=gridsvalid(sorted_population[i])
        if x>max:
            max=x
            index=i
    return index
##selec first parent
def select_v1(i):
    x=random.randint(0,99)
    if x==i:
        select_v1(i)
    if x == None:
        select_v1(i)
    else:
        return x
##selec 2end parent

def select_v2(i,v1):
    y=random.randint(0,99)
    if y==i:
        select_v2(i,v1)
    if y==v1:
        select_v2(i,v1)
    if y==None:
        select_v2(i,v1)
    else:
        return y

##selec 3rd parent

def select_v3(i,v1,v2):
    z=random.randint(0,99)
    if z==i:
        select_v3(i, v1, v2)
    if z==v1:
        select_v3(i, v1, v2)
    if z==v2:
        select_v3(i, v1, v2)
    if z==None:
        select_v3(i, v1, v2)
    else:
        return z

##selec target parent
def select_target():
    x=random.randint(0,99)
    return x
#check if a cell unique in row
def rowisvalid(grid,i,e):
    rowok=0
    for c in range(9):
        if e!=grid[i][c] :
            rowok=rowok+1

    return rowok==8

#check if a cell unique in column
def colisvalid(grid,j,e):
    colok=0
    for c in range(9):
        if e!=grid[c][j] :
            colok=colok+1

    return colok==8

#check if a cell unique in sector
def sectisvalid(grid,i,j,e):
    secok=0
    sectopx,sectopy=3*(i//3),3*(j//3)
    for x in range(sectopx,sectopx+3):
        for y in range(sectopy,sectopy+3):
            if e != grid[x][y]:
                secok=secok+1
    return secok==8

## return the fittness of the entire soduko
def gridsvalid(grid):
    count=0
    for i in range (9):
        for j in range (9):
            row=rowisvalid(grid,i,grid[i][j])
            col=colisvalid(grid,j,grid[i][j])
            sect=sectisvalid(grid,i,j,grid[i][j])
            if row and col and sect:
                count=count+1

    return count

##return the fittness of your entire population one by one
def population_fit(population):
    dictionary_fit={}
    for i in range (100):
        fit=gridsvalid(population[i])
        dictionary_fit[i] = fit
    return dictionary_fit

##put the fixed number of your sudoku
def put_fixed(sorted_population):
    for i in range(100):
        sorted_population[0][0] = 5
        sorted_population[0][1] = 3
        sorted_population[0][4] = 7
        sorted_population[1][0] = 6
        sorted_population[1][3] = 1
        sorted_population[1][4] = 9
        sorted_population[1][5] = 5
        sorted_population[2][1] = 9
        sorted_population[2][2] = 8
        sorted_population[2][7] = 6
        sorted_population[3][0] = 8
        sorted_population[3][4] = 6
        sorted_population[3][8] = 3
        sorted_population[4][0] = 4
        sorted_population[4][3] = 8
        sorted_population[4][5] = 3
        sorted_population[4][8] = 1
        sorted_population[5][0] = 7
        sorted_population[5][4] = 2
        sorted_population[5][8] = 6
        sorted_population[6][1] = 6
        sorted_population[6][6] = 2
        sorted_population[6][7] = 8
        sorted_population[7][3] = 4
        sorted_population[7][4] = 1
        sorted_population[7][5] = 9
        sorted_population[7][8] = 5
        sorted_population[8][4] = 8
        sorted_population[8][7] = 7
        sorted_population[8][8] = 9

## initialize the popualtion empty firstly
population=[]

##this loop put at the firt 100 parent in the firt generation (the fixed numbers and 0 s
for i in range(100):
    population.append(mylist)


##this loop iterat on very cell have 0 value and put random value
for i in range(100):
        for r in range(9):
           for c in range (9):
               if(population[i][r][c]==0):
                    population[i][r][c]=random.randint(1,9)


#initiate the trial parent/ vector
trial=[[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

#initiate the mutant vectoor
mutant=[[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

##initiate the crossover rate ith value from 0 to 1
cr=0.8

max=max_index(population)
i=0
count=0
while population[max]!=81:

    if(count==100):
        print("the fittness of the fittest solution in this generation is:  ",gridsvalid(population[max]))
        print("the solution is","\n")

        for r in range(9):
            for c in range(9):
                print(population[1][r][c]," ",end = '')
            print("\n")





        quit()
    i=select_target()
    a=select_v1(i)
    b=select_v2(i,a)
    c=select_v3(i,a,b)

    target=population[i]
    v1=population[a]
    v2=population[b]
    v3=population[c]
    for r in range (9):
        for c in range (9):
            mutant[r][c] = v1[r][c] - (v2[r][c] + v3[r][c])
            if (mutant[r][c] > 9):
                mutant[r][c] = random.randint(0,9)
                if(mutant[r][c]<0):
                    mutant[r][c]=random.randint(0,9)
        #making crossover between mutant vector and target vector
    for r in range(9):
        for c in range (9):
            n = random.uniform(0.0, 1.0)
            if n>cr:
                trial[r][c]=target[r][c]
            else:
                trial[r][c]=mutant[r][c]
    ##look at tep number 6 ya
    # calculate the fit of target and trail vector to choose which on will be in the next population

    trial[0][0] = 5
    trial[0][1] = 3
    trial[0][4] = 7
    trial[1][0] = 6
    trial[1][3] = 1
    trial[1][4] = 9
    trial[1][5] = 5
    trial[2][1] = 9
    trial[2][2] = 8
    trial[2][7] = 6
    trial[3][0] = 8
    trial[3][4] = 6
    trial[3][8] = 3
    trial[4][0] = 4
    trial[4][3] = 8
    trial[4][5] = 3
    trial[4][8] = 1
    trial[5][0] = 7
    trial[5][4] = 2
    trial[5][8] = 6
    trial[6][1] = 6
    trial[6][6] = 2
    trial[6][7] = 8
    trial[7][3] = 4
    trial[7][4] = 1
    trial[7][5] = 9
    trial[7][8] = 5
    trial[8][4] = 8
    trial[8][7] = 7
    trial[8][8] = 9

    target_fit = gridsvalid(target)
    trial_fit = gridsvalid(trial)
    if (target_fit > trial_fit):
        population[i] = target
    else:
        population[i] = trial
    for x in range (100):
        put_fixed(population[x])
    max=max_index(population)
    count=count+1
