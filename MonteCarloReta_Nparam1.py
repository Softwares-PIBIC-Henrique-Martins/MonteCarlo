# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:04:38 2021

@author: Samaung
"""

import numpy as np
import matplotlib.pyplot as plt

def Ajuste(f,xs,ys,p0,n,raio):
    ListaIndexEnsaios=[]
    sigma=np.std(ys)
    n_dados=len(xs)
    
    Termo1=[(f(xs[j],*p0)-ys[j])**2/sigma**2 for j in range(n_dados)]
    Qui0=np.sum(Termo1)
    ListaQuis=[Qui0]
    
    Transposta=[2*raio[i]*np.random.random_sample(n)-raio[i] for i in range(len(p0))]
    Ensaios=list(map(lambda *i: [j for j in i], *Transposta))
    index_ensaios=0
    
    for delta in Ensaios:
        Termo=[(f(xs[j],*[p0[i]+delta[i] for i in range(len(p0))])-ys[j])**2/sigma**2 for j in range(n_dados)] #Termo é cada termo da soma que compõe o quiquadrado
        Qui1=np.sum(Termo)
        if Qui1 < Qui0:
            Qui0=Qui1
            ListaQuis.append(Qui0)
            ListaIndexEnsaios.append(index_ensaios)
        index_ensaios+=1

    if len(ListaIndexEnsaios)>0:
        i=ListaIndexEnsaios[-1]
        estimativa=[p0[k]+Ensaios[i][k] for k in range(len(p0))]
        valores_de_delta=[Ensaios[k] for k in ListaIndexEnsaios]
    else:
        estimativa=p0
        valores_de_delta=[Ensaios[k] for k in ListaIndexEnsaios]
        
    return estimativa, valores_de_delta, ListaQuis

def func(x, a, b):
    return (a/b)*x

xs=np.arange(0,400,1)
ys=np.arange(0,400,1)+np.random.normal(0, 10, 400)

estimativa, deltas, Quis =Ajuste(func, xs, ys, [1.5,0.5], 1000, [1,1])
plt.figure(1)
print('Interações: ',deltas)
print("a =",estimativa[0])
print("b =",estimativa[1])
plt.plot(xs, ys, 'o')
plt.plot(xs, func(xs,*estimativa), '-')
#plt.title('Kef=%.0f'%estimativa)
plt.show()

plt.figure(2)
deltas_transp=list(map(lambda *i: [j for j in i], *deltas))
plt.plot(deltas_transp[0], deltas_transp[1],'o')
plt.show()