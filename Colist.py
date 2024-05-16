'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

import numpy
while True:
    print('commands:')
    print('1-input')
    print('2-sum')
    print('3-multiply')
    print('4-print')
    print('5-exit')
    comm=int(input('enter number:'))
    if comm==1:
       numco=int(input('enter number of coefficient:'))
       colist1=[]
       for i in range(numco):
           coefficient=int(input('enter coefficient:'))
           colist1.append(coefficient)
       p=numpy.poly1d(colist)
       colist2=[]
       for i in range(numco):
           coefficient1=int(input('enter new coefficient:'))
           colist2.append(coefficient1)
       p1=numpy.poly1d(colist2)
    if comm==2:
        sump=[x+y for x,y in zip(colist1,colist2)]
        psum=numpy.poly1d(sump)
        print('sum two functions:',psum)
    if comm==3:
        pmul=numpy.polymul(p,p1)
        print('multiply two functions:',pmul)
    if comm==4:
        print(p,p1)
    if comm==5:
        break
