import numpy as np
import sys
 
def getMaxPieces(pieces, ligne, col):
    m,n=pieces.shape
 
    if ((ligne < 0) or (ligne == m) or (col == n)): return 0
    else:
        droite = getMaxPieces(pieces,ligne,col+1)
        droiteGauche=getMaxPieces(pieces,ligne-1,col+1)
        droiteDroite=getMaxPieces(pieces,ligne+1,col+1)
        return pieces[ligne][col]+max(droite,droiteGauche,droiteDroite)
 
 
def collectpieces(pieces):
    m,n=pieces.shape
    maxi=0
    pos=0
    for i in range(m):
        val=getMaxPieces(pieces,i,0)
        if val > maxi :
            maxi=val 
            pos=i
     
    return (maxi,pos)
 