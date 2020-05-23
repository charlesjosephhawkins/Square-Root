#INTEGER SQUARE ROOT
#COPYRIGHT(2020) CHARLES JOSEPH HAWKINS
def SQRT(N):
        T,M,L=0,N,N
        while M%2==0:M,T=M//4,T+1
        if M==1:print('OUTPUT: SQRT[',N,'] =',2**T)
        if T>0:N=M
        X,Y,Z=((N-1)//2)%9,((N+1)//2)%9,((((N+1)//2)+1)//6)%9
        if all([X==3,Y==4]):A1,A2=5,13
        if all([X==6,Y==7]):A1,A2=11,7
        if all([X==0,Y==1]):A1,A2=17,19
        if all([X==4,Y==5,Z==1]):A1,A2=15,3
        if all([X==4,Y==5,Z==7]):A1,A2=9,0
        while A1<N or A2<N:
                if any([A1**2==N,A2**2==N]):break    
                A1,A2=A1+18,A2+18
        if all([A1**2==N,T==0]):print('OUTPUT: SQRT[',N,'] =',A1)
        if all([A2**2==N,T==0]):print('OUTPUT: SQRT[',N,'] =',A2)
        if all([A1**2==N,T>=1]):print('OUTPUT: SQRT[',L,'] =',A1*(2**T))
        if all([A2**2==N,T>=1]):print('OUTPUT: SQRT[',L,'] =',A2*(2**T))

print('INPUT:')    
x = input()
SQRT(int(x))
 


