import random
import time
from tkinter.constants import PROJECTING
satir = int(input("Satir sayisini giriniz : "))
sutun = int(input("Sutun sayisini gitiniz : "))
matrix = []
for i in range(satir):
  row = []
  for j in range(sutun):
    a=random.randint(0,1)
    if a==0:
        row.append("◻")
    else :
        row.append("■")
  matrix.append(row)
yeniliste=[]
atama=[]
count=0
counter=0
a="devam"
while(a!="END"):
    for i in range(satir):
        for j in range(sutun):
            if i==0 and j==0:   # i ve j 0 sol ust kose
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")

            elif i==0 and j!=sutun-1 and j!=0 :  # ust ve koseler haric
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")

            elif i==0 and j==sutun-1:       # sag ve ust kose
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            elif i!=satir-1 and j==0:       # sol yan sutun
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            elif j==sutun-1 and i!=satir-1 and i!=0:     # sag yan 
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            elif i==satir-1 and j==0 :  # sag alt kose
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            elif i==satir-1 and j==sutun-1:
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            elif i==satir-1 and j!=sutun-1 and j!=0:
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            else :
                if matrix[i-1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i-1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j+1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i+1][j-1]=="◻":
                    count+=1
                else:
                    counter+=1
                if matrix[i][j]=="◻":
                    if counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
                else:
                    if counter==2 or counter==3:
                        yeniliste.append("■")
                    else:
                        yeniliste.append("◻")
            
            count=0
            counter=0
        atama.append(yeniliste)
        yeniliste=[]
    for k in range(satir):
        for l in range(sutun):
            matrix[k][l]=atama[k][l]
    for k in range(satir):
        for l in range(sutun):
            print(matrix[k][l],end="")
        print("\n")
    for k in matrix:
        for l in k:
            print(l,end=" ")
    a=input("\nBitmesini istiyorsaniz END yaziniz :\n")
    yeniliste=[]
    atama=[]


        
