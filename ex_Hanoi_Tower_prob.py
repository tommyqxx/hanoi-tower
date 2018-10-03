
##练习
##汉诺塔的移动可以用递归函数非常简单地实现。
##请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
##移动次数是f(n).显然f(1)=1,f(2)=3,f(3)=7，且f(k+1)=2*f(k)+1。此后不难证明f(n)=2^n-1。
# -*- coding: utf-8 -*-

def fact(n):
    if n==1:
        return 1
    return fact(n-1)

def move(n,a,b,c):

    if n==1:
        print(a, '-->',c)
        #prt=(a, '-->',c)
        #arr.append(prt)
    else:
        move(n-1,a,c,b)
        move (1,a,b,c)
        move(n-1,b,a,c)
    #return arr
#print("Move: ", move(2,'A','B','C'))



def hanoi_tower(n,a,b,c,arr):
    if n==1:
        prt=(a, '-->', c)
        arr.append(prt)
    else:
        hanoi_tower(n-1,a,c,b,arr)
        hanoi_tower (1,a,b,c,arr)
        hanoi_tower(n-1,b,a,c,arr)
    return arr
    #fact(n)
#print(move(n,'A','B','C'))

'''
output = []
print("Hanoi_tower: ", hanoi_tower(2,'A','B','C',output))
'''
