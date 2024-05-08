'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def dequeue_i(self , i):
   if self.num == 0:
       rase Exception("Queue empty")
    item=self.Q[i]
    del self.Q[i]
    index=[(self.num+self.first)%self.max_size]
    self.Q.insert(0,index)
    self.num-=1
    return item