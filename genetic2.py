from random import randint,random
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib
from copy import deepcopy
matplotlib.rcParams['font.family']='STSong'

def dist2(x1,x2,y1,y2):
    return ((x1-x2)**2)+((y1-y2)**2)
def evaluate(m,x,y):
    sums=sqrt(dist2(x[m[0]],x[m[-1]],y[m[0]],y[m[-1]]))
    size=len(m)-1
    for ii in range(size):
        sums+=sqrt(dist2(x[m[ii]],x[m[ii+1]],y[m[ii]],y[m[ii+1]]))
    score=(10000/sums)-40#increase weight of good ones
    if score<0:
        score=0.1
    return score

def search(allcities,citynum):
    name=[]
    x=[]
    y=[]
    with open('data.txt','r') as fp:
        for line in fp.readlines():
            name.append(line.split(',')[0])
            x.append(float(line.split(',')[1]))
            y.append(float(line.split(',')[2].strip()))

    #initial
    INDINUM=500     #individual number
    ITERA=citynum*20     #iter times
    crossrate=0.6   #cross rate
    mutationrate=0.1
    MUSTAGE=0.5  #when to accelerate mutation
    throttle=10  #control mutation(while throttle=0 only beneficial mutation)
    m=[]
    for i in range(INDINUM):
        init=[]
        allcity=list(allcities)
        add=allcity[int(citynum*random())]
        init.append(add)
        allcity.remove(add)
        for i in range(citynum-1):
            mindist=10000
            add=-1
            findtime=0
            for city in allcity:
                dist=dist2(x[city],x[init[-1]],y[city],y[init[-1]])
                if dist<mindist:
                    mindist=dist
                    add=city
                findtime+=1
                if findtime>(citynum//3) and random()<0.1:
                    break
            init.append(add)
            allcity.remove(add)
        m.append(init)
    ##print(m,end='\n\n')
    besteva=0
    best=[]
    historybest=list()
    gen=0

    for itera in range(ITERA):
        #evaluate
        eva=list()
        for i in range(INDINUM):
            eva.append(evaluate(m[i],x,y))
        maxeva=max(eva)
        

        if round(maxeva,6)>round(besteva,6):        
            best=deepcopy(m[eva.index(maxeva)])
            besteva=maxeva
            gen=itera
            historybest.append(best)

        if itera%(ITERA//10)==0:#输出粒度：10
            print(itera,'代：当前最佳',10000/(max(eva)+40),'历史最佳代:',gen,10000/(besteva+40))###
            #print(itera,maxeva,besteva,evaluate(best,x,y),evaluate(save,x,y))
            #pass
        
            
        preserve=[(evas/sum(eva)) for evas in eva]

        #preserve
        new=[]
        new.append(list(m[eva.index(max(eva))]))
        for i in range(INDINUM-2):
            point=random()
            for ii in range(INDINUM):
                point-=preserve[ii]
                if point<0:
                    new.append(list(m[ii]))
                    break
        new.append(best)

        m=deepcopy(new) #list()仅对第一层是深拷贝         
                    


        #process
        if itera==int(INDINUM*MUSTAGE):
            crossrate=0.3
            mutationrate=0.6
            #throttle=2

        #cross
        for i in range(INDINUM//2):
            crosspart=[]
            if random()<crossrate:
                crosslen=randint(citynum//3,citynum//2)
                crosspart.append(m[i*2][-crosslen:])
                crosspart.append(m[i*2+1][-crosslen:])

                #cross the second one
                for cp in crosspart[0][1:]:
                    m[i*2+1].remove(cp)
                ff=m[i*2+1].index(crosspart[0][0])
                crosspart[0]=crosspart[0][1:]
                crosspart[0].reverse()
                for cp in crosspart[0]:
                    m[i*2+1].insert(ff+1,cp)

                #cross the first one
                for cp in crosspart[1][1:]:
                    m[i*2].remove(cp)
                ff=m[i*2].index(crosspart[1][0])
                crosspart[1]=crosspart[1][1:]
                crosspart[1].reverse()
                for cp in crosspart[1]:
                    m[i*2].insert(ff+1,cp)
        #mutation(exchange)
        for i in range(INDINUM):    
            if random()<mutationrate:
                a=randint(0,citynum-1)
                b=randint(0,citynum-1)
            
                if a!=b:
                    tmp=list(m[i])
                    rank0=evaluate(m[i],x,y)
                    tmp[a],tmp[b]=tmp[b],tmp[a]
                    rank1=evaluate(tmp,x,y)
                    if rank1+throttle>rank0:
                        m[i][a],m[i][b]=m[i][b],m[i][a]



    #output    
    return best,(10000/(besteva+40)),historybest


