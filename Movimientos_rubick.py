# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:21:23 2018

@author: mateo
"""

import numpy as np

class move:
    """move: define 7 metodos el primero es por default y permite pasar la 
    variable de entrada los otros 6 metodos son los movimientos, cada uno
    definido bajo un estandar de visualización del cubo para ver como se 
    organizan las matrices ver los papeles"""
    def __init__(self,cube):
        self.cube = cube 
    
    # f hace rereferencia la cara frontal, o a una fila/columna de ella, 
    #similar para las otras caras, l(left), b(back), u(up) ... 
    
    def u(self): #Movimiento de la cara superio U clockwise
        self.cube[1] = np.rot90(np.fliplr(np.flipud(self.cube[1])))
        f = self.cube[0,0,:].copy()
        l = self.cube[5,:,2].copy()
        b = self.cube[2,2,:].copy()
        r = self.cube[4,:,0].copy()
        self.cube[0,0,:] = np.flipud(r)
        self.cube[5,:,2] = f
        self.cube[2,2,:] = np.flipud(l)
        self.cube[4,:,0] = b
        print('cube is:',self.cube)
        return(self.cube)
        
    def d(self): #Movimiento de la cara inferior D counter-clockwise
        self.cube[3] = np.rot90(np.fliplr(np.flipud(self.cube[3])))
        f = self.cube[0,2,:].copy()
        l = self.cube[5,:,0].copy()
        b = self.cube[2,0,:].copy()
        r = self.cube[4,:,2].copy()
        self.cube[2,0,:] = r
        self.cube[4,:,2] = np.flipud(f)
        self.cube[0,2,:] = l
        self.cube[5,:,0] = np.flipud(b)
        print('cube is:',self.cube)
        return(self.cube)
        
    def f(self): #Movimiento de la cara frontal F clockwise
        self.cube[0] = np.rot90(np.fliplr(np.flipud(self.cube[0])))
        u = self.cube[1,2,:].copy()
        r = self.cube[4,2,:].copy()
        d = self.cube[3,0,:].copy()
        l = self.cube[5,2,:].copy()
        self.cube[1,2,:] = l
        self.cube[4,2,:] = u
        self.cube[3,0,:] = np.flipud(r)
        self.cube[5,2,:] = np.flipud(d)
        print('cube is:',self.cube)
        return(self.cube)
        
    def b(self): #Movimiento de la cara trasera B counter-clockwise
        self.cube[2] = np.rot90(np.fliplr(np.flipud(self.cube[2])))
        u = self.cube[1,0,:].copy()
        r = self.cube[4,0,:].copy()
        d = self.cube[3,2,:].copy()
        l = self.cube[5,0,:].copy()
        self.cube[3,2,:] = np.flipud(l)
        self.cube[5,0,:] = u
        self.cube[1,0,:] = r
        self.cube[4,0,:] = np.flipud(d)
        print('cube is:',self.cube)
        return(self.cube)
        
    def r(self): #Movimiento de la cara lateral derecha clockwise
        self.cube[4] = np.fliplr(np.rot90(np.fliplr(self.cube[4])))
        f = self.cube[0,:,2].copy()
        u = self.cube[1,:,2].copy()
        b = self.cube[2,:,2].copy()
        d = self.cube[3,:,2].copy()
        self.cube[0,:,2] = d
        self.cube[1,:,2] = f
        self.cube[2,:,2] = u
        self.cube[3,:,2] = b
        print('cube is:',self.cube)
        return(self.cube)
        
    def l(self): #Movimiento de la cara lateral izquierda counter-clockwise
        self.cube[5] = np.fliplr(np.rot90(np.fliplr(self.cube[5])))
        f = self.cube[0,:,0].copy()
        u = self.cube[1,:,0].copy()
        b = self.cube[2,:,0].copy()
        d = self.cube[3,:,0].copy()
        self.cube[0,:,0] = u
        self.cube[1,:,0] = b
        self.cube[2,:,0] = d
        self.cube[3,:,0] = f
        print('cube is:',self.cube)
        return(self.cube)
        
        
        
p = move(np.array([[[1,1,1],[1,1,1],[1,1,1]],[[2,2,2],[2,2,2],[2,2,2]],[[3,3,3]
            ,[3,3,3],[3,3,3]],[[4,4,4],[4,4,4],[4,4,4]],[[5,5,5],[5,5,5],
              [5,5,5]],[[6,6,6],[6,6,6],[6,6,6]]],int))
p.l()
        
#p = move(a)
#cube = p.u()
#a = cube 






