


a=1
for i in range(1,10):
    a=a*i
    print(a,"{}factorial".format(i))
    
    
    


def fibo_series(num):
    a=0
    b=1
    d=[0,1]
    if num==0:
        return("no number")
    elif 0 <num<=1:
        return( 0 )
    else:
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            d.append(c)
    return(d)
        
        
        

fibo_series(2)
       
        
