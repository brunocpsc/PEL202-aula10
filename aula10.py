# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import random as rd
col,lin = 3,2
n,gama= 0.1, 0.9 #n --> n, taxa de aprendizado / gama -> taxa de desconto
matriz_recomp= [[-1 for j in range(col*lin)]for i in range (lin*col)]
q_matrix=[[0 for j in range(col*lin)]for i in range (lin*col)] #matriz Q começa zerada
ind_rd=[]
ind_rdn=[]
s,i,j,mx = 0,0,0,0
episodes=1000

#atribuindo recompensas
matriz_recomp[3][5]=100
matriz_recomp[4][5]=100
matriz_recomp[5][5]=0
matriz_recomp[0][1]=0
matriz_recomp[0][2]=0
matriz_recomp[1][0]=0
matriz_recomp[1][3]=0
matriz_recomp[2][0]=0
matriz_recomp[2][3]=0
matriz_recomp[2][4]=0
matriz_recomp[3][1]=0
matriz_recomp[3][2]=0
matriz_recomp[4][2]=0

print('Matriz de Recompensa\n', np.array(matriz_recomp))
print('Matriz Q inicial\n',np.array(q_matrix))


def format_row(row):
    return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'

def format_board(board):
    return '\n'.join(format_row(row) for row in board)

while (episodes>0):#while para contagem de episódios
    s=np.random.randint(0,(col*lin-1)) #estado inicial arbitrário
    while (s != 5): #while para saída somente no estado final (s5)
        for i in range (lin*col): #for para decisão das ações
            if reward_matrix[s][i]>=0:
                ind_rd.append(i)
        a=rd.choice(ind_rd) #decisão arbitrária de qual ação tomar, dentre as possíveis
        for i in range (lin*col): #for para decisão das ações futuras
            if reward_matrix[a][i]>=0:
                ind_rdn.append(i)
        for i in range (len(ind_rdn)):
            if q_matrix[a][ind_rdn[i]]>=mx:#cálculo de Q máximo
                mx=q_matrix[a][ind_rdn[i]]
        q_matrix[s][a]=(1-n)*q_matrix[s][a]+n*(reward_matrix[s][a]+gama*mx) #cálculo de Q
        mx=0
        s=a
        ind_rd=[]
        ind_rdn=[]
    episodes=episodes-1
print('Matriz Q após 1000 episódios\n',np.array(q_matrix))

print('Obtenção do V:')

for i in range(len(q_matrix)):
        print('S',i,round(max(q_matrix[i]),0))

#print(format_board([['s0','s1','s2'],['s3','s4','s5']]))