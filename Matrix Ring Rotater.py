# a Friend challenged me, said it was impossible to automate
# an outer ring Rotater for a 3*3


from os import system
from time import sleep

def rotate(l, n):
        return l[-n:] + l[:-n]

def printer(arr):
        for i in range(0, len(arr)):
                print()
                for j in range(0, len(arr[i])):
                        print(arr[i][j], end='   ')
        return

def rotater(Matrix,Rotations):
        linear = [None] * 8
        for i in range(0,len(Matrix)):
                for j in range(0,len(Matrix[i])):
                        if i < j:
                                linear[i+j] = Matrix[i][j]
                        elif i == j:
                                if i != 1:
                                        linear[i+j] = Matrix[i][j]                
                        elif i > j:
                                linear[8-(i+j)] = Matrix[i][j]
        linear = rotate(linear,Rotations)
        for i in range(0,len(Matrix)):
                for j in range(0,len(Matrix[i])):
                        if i < j:
                                Matrix[i][j] =  linear[i+j]
                        elif i == j:
                                if i != 1:
                                        Matrix[i][j] = linear[i+j]                 
                        elif i > j:
                                Matrix[i][j] = linear[8-(i+j)]
        
        return Matrix
                        

if __name__ == "__main__":
        while True:
                try:
                        for i in range(0,9):
                                SampleMatrix = [[1,2,3],[4,5,6],[7,8,9]]
                                printer(rotater(SampleMatrix,i))
                                print()
                                sleep(0.75)
                                system("cls")
                except KeyboardInterrupt:
                        break                
pass