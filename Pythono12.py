def ankitaFunction(i):
    return 'Ankita'+'_'+str(i)


def rajanFunction(i):
    return 'Rajan'+'_'+str(i)


for i in range(1,101):
    if(i%2==0) :
        result =ankitaFunction(i)
        print(result)
    else:
        result = rajanFunction(i)
        print(result)




def jyotsnafunction(i) :
    return 'jyotsna'+'_'+str(i)

def rajkumarfunction(i) :
    return 'rajkumar'+'_'+str(i)

for i in range(1,30) :
    if (i%4==0) :
        result=jyotsnafunction(i)
        print(result)
    else:
        result=rajkumarfunction(i)
        print(result)






def rajafunction(i) :
    return 'raja'+'-'+str(i)


def anjalifunction(i) :
    return'ajanli'+'_'+str(i)

for i in range(20,100) :
    if (i%5==0) :
        result=rajafunction(i)
        print(result)
    else:
        result=anjalifunction(i)
        print(result)





def anuragfunction(i) :
    return 'anurag'+'%'+str(i)

def mittufunction(i) :
    return 'mittu'+'%'+str(i)

for i in range(30,300) :
    if (i%10==0) :
        result=anuragfunction(i)
        print(result)
    else:
        result=mittufunction(i)
        print(result)




def pihufunction(i) :
    return 'pihu'+'@'+str(i)

def satwikafunction(i) :
    return 'satwika'+'@'+str(i)


for i in range(2,400) :
    if(i%4==0) :
        result=pihufunction(i)
        print(result)
    else :
        result=satwikafunction(i)
        print(result)
