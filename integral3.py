#sayisal integralin yaklasik degerinin hesaplanmasi
def f(x):
    return(x**2+2)
n=1024
a,b=1,3
integral=0
h=(b-a)/n
for i in range(1,2*n,2):
    integral+=f(a+i*h/2)*h
print(integral)
