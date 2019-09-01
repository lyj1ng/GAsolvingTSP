from tkinter import *
from genetic2 import *
import tkinter

top = tkinter.Tk()
top.title('TSP solver')


def allselect():
    for i in range(34):
        globals()['CheckVar'+str(i)].set(1)

def noneselect():
    for i in range(34):
        globals()['CheckVar'+str(i)].set(0)
        
    
def entry():
    plt.close()
    msg.insert(INSERT,'searching...\n')
    name=[]
    x=[]
    y=[]
    with open('data.txt','r') as fp:
        for line in fp.readlines():
            name.append(line.split(',')[0])
            x.append(float(line.split(',')[1]))
            y.append(float(line.split(',')[2].strip()))
    
    sflag=0
    timestoshow=1
    cities=[]
    for i in range(34):
        if globals()['CheckVar'+str(i)].get()==1:
            cities.append(i)
    #print(cities,len(cities))
    if len(cities)<=2:
        msg.insert(INSERT,'invalid cities!\n')
        return 0

    start=E1.get()
    if start=='':
        sflag=0
    elif int(start) in cities:
        msg.insert(INSERT,'start from '+name[int(start)]+'\n')
        sflag=1
    else:
        msg.insert(INSERT,'no start point setted\n')
        sflag=0

    tts=E2.get()
    if tts=='' or tts=='0':
        pass
    else:
        try:
            timestoshow=int(tts)
        except:
            pass
        
    best1,result,bests=search(cities,len(cities))
    
    
    msg.insert(INSERT,'best result:'+str(result)+'\n')
    #print(best1)#最佳路径
    #print(bests)#最佳路径集合
    print('total results:',len(bests))
    routes=0
    legend=[]
    while routes<timestoshow:
        if timestoshow>len(bests):
            timestoshow=len(bests)
        else:pass
            
        best=list(bests[-(routes+1)])
        #print(routes,best)
        #routes to show
        if sflag==1:
            turn=list(best[best.index(int(start)):]+best[:best.index(int(start))])
            msg.insert(INSERT,'route '+str(routes+1)+' :'+str(turn))
            msg.insert(INSERT,'result: '+str(10000/(evaluate(best,x,y)+40))+'\n')

            X=[x[dot] for dot in turn]
            X.append(x[turn[0]])
            Y=[y[dot] for dot in turn]
            Y.append(y[turn[0]])
            legend.append(str(10000/(evaluate(best,x,y)+40)))
            plt.plot(X,Y,'-o')
            i=0
            old=(0,0)
            for xy in zip(X, Y):
                if i!=0:
                    ta,tb=xy
                    oa,ob=old
                    tmp=((ta+oa)/2,(tb+ob)/2)
                    plt.annotate(str(i), xy=tmp, xytext=(0, 0),weight="bold", textcoords='offset points')
                old=xy
                i+=1
        else:
            msg.insert(INSERT,'route '+str(routes+1)+' :'+str(best))
            msg.insert(INSERT,'result: '+str(10000/(evaluate(best,x,y)+40))+'\n')
            X=[x[dot] for dot in best]
            X.append(x[best[0]])
            Y=[y[dot] for dot in best]
            Y.append(y[best[0]])
            legend.append(str(10000/(evaluate(best,x,y)+40)))
            plt.plot(X,Y,'-o')
            
        routes+=1
        
    i=0
    for xy in zip(x, y):
        plt.annotate(name[i], xy=xy, xytext=(-20, 10), textcoords='offset points')
        i+=1
        
    plt.legend(legend) 

    plt.show()

    
    


CheckVar0 = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()
CheckVar11 = IntVar()
CheckVar12 = IntVar()
CheckVar13 = IntVar()
CheckVar14 = IntVar()
CheckVar15 = IntVar()
CheckVar16 = IntVar()
CheckVar17 = IntVar()
CheckVar18 = IntVar()
CheckVar19 = IntVar()
CheckVar20 = IntVar()
CheckVar21 = IntVar()
CheckVar22 = IntVar()
CheckVar23 = IntVar()
CheckVar24 = IntVar()
CheckVar25 = IntVar()
CheckVar26 = IntVar()
CheckVar27 = IntVar()
CheckVar28 = IntVar()
CheckVar29 = IntVar()
CheckVar30 = IntVar()
CheckVar31 = IntVar()
CheckVar32 = IntVar()
CheckVar33 = IntVar()

C0 = Checkbutton(top, text = "北京(0)", variable = CheckVar0, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C1 = Checkbutton(top, text = "天津(1)", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C2 = Checkbutton(top, text = "上海(2)", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C3 = Checkbutton(top, text = "重庆(3)", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C4 = Checkbutton(top, text = "拉萨(4)", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C5 = Checkbutton(top, text = "乌鲁木齐(5)", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C6 = Checkbutton(top, text = "银川(6)", variable = CheckVar6, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C7 = Checkbutton(top, text = "呼和浩特(7)", variable = CheckVar7, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C8 = Checkbutton(top, text = "南宁(8)", variable = CheckVar8, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C9 = Checkbutton(top, text = "哈尔滨(9)", variable = CheckVar9, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C10 = Checkbutton(top, text = "长春(10)", variable = CheckVar10, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C11 = Checkbutton(top, text = "沈阳(11)", variable = CheckVar11, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C12 = Checkbutton(top, text = "石家庄(12)", variable = CheckVar12, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C13 = Checkbutton(top, text = "太原(13)", variable = CheckVar13, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C14 = Checkbutton(top, text = "西宁(14)", variable = CheckVar14, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C15 = Checkbutton(top, text = "济南(15)", variable = CheckVar15, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C16 = Checkbutton(top, text = "郑州(16)", variable = CheckVar16, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C17 = Checkbutton(top, text = "南京(17)", variable = CheckVar17, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C18 = Checkbutton(top, text = "合肥(18)", variable = CheckVar18, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C19 = Checkbutton(top, text = "杭州(19)", variable = CheckVar19, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C20 = Checkbutton(top, text = "福州(20)", variable = CheckVar20, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C21 = Checkbutton(top, text = "南昌(21)", variable = CheckVar21, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C22 = Checkbutton(top, text = "长沙(22)", variable = CheckVar22, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C23 = Checkbutton(top, text = "武汉(23)", variable = CheckVar23, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C24 = Checkbutton(top, text = "广州(24)", variable = CheckVar24, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C25 = Checkbutton(top, text = "台北(25)", variable = CheckVar25, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C26 = Checkbutton(top, text = "海口(26)", variable = CheckVar26, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C27 = Checkbutton(top, text = "兰州(27)", variable = CheckVar27, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C28 = Checkbutton(top, text = "西安(28)", variable = CheckVar28, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C29 = Checkbutton(top, text = "成都(29)", variable = CheckVar29, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C30 = Checkbutton(top, text = "贵阳(30)", variable = CheckVar30, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C31 = Checkbutton(top, text = "昆明(31)", variable = CheckVar31, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C32 = Checkbutton(top, text = "香港(32)", variable = CheckVar32, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C33 = Checkbutton(top, text = "澳门(33)", variable = CheckVar33, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C0.grid(row=0, column=0, sticky=W, padx=5,pady=3)
C1.grid(row=0, column=1, sticky=W, padx=5,pady=3)
C2.grid(row=0, column=2, sticky=W, padx=5,pady=3)
C3.grid(row=0, column=3, sticky=W, padx=5,pady=3)
C4.grid(row=0, column=4, sticky=W, padx=5,pady=3)
C5.grid(row=0, column=5, sticky=W, padx=5,pady=3)
C6.grid(row=1, column=0, sticky=W, padx=5,pady=3)
C7.grid(row=1, column=1, sticky=W, padx=5,pady=3)
C8.grid(row=1, column=2, sticky=W, padx=5,pady=3)
C9.grid(row=1, column=3, sticky=W, padx=5,pady=3)
C10.grid(row=1, column=4, sticky=W, padx=5,pady=3)
C11.grid(row=1, column=5, sticky=W, padx=5,pady=3)
C12.grid(row=2, column=0, sticky=W, padx=5,pady=3)
C13.grid(row=2, column=1, sticky=W, padx=5,pady=3)
C14.grid(row=2, column=2, sticky=W, padx=5,pady=3)
C15.grid(row=2, column=3, sticky=W, padx=5,pady=3)
C16.grid(row=2, column=4, sticky=W, padx=5,pady=3)
C17.grid(row=2, column=5, sticky=W, padx=5,pady=3)
C18.grid(row=3, column=0, sticky=W, padx=5,pady=3)
C19.grid(row=3, column=1, sticky=W, padx=5,pady=3)
C20.grid(row=3, column=2, sticky=W, padx=5,pady=3)
C21.grid(row=3, column=3, sticky=W, padx=5,pady=3)
C22.grid(row=3, column=4, sticky=W, padx=5,pady=3)
C23.grid(row=3, column=5, sticky=W, padx=5,pady=3)
C24.grid(row=4, column=0, sticky=W, padx=5,pady=3)
C25.grid(row=4, column=1, sticky=W, padx=5,pady=3)
C26.grid(row=4, column=2, sticky=W, padx=5,pady=3)
C27.grid(row=4, column=3, sticky=W, padx=5,pady=3)
C28.grid(row=4, column=4, sticky=W, padx=5,pady=3)
C29.grid(row=4, column=5, sticky=W, padx=5,pady=3)
C30.grid(row=5, column=0, sticky=W, padx=5,pady=3)
C31.grid(row=5, column=1, sticky=W, padx=5,pady=3)
C32.grid(row=5, column=2, sticky=W, padx=5,pady=3)
C33.grid(row=5, column=3, sticky=W, padx=5,pady=3)

L2 = Label(top, text="routes to show")
L2.grid(row=5, column=4, sticky=W, padx=5,pady=3)
E2 = Entry(top, bd =5)
E2.grid(row=5, column=5, sticky=W, padx=5,pady=3)

v=StringVar()
B = tkinter.Button(top,text='search', command = entry)
B.grid(row=6, column=3, sticky=W, padx=5,pady=5)

BF = tkinter.Button(top, text ="select_all", command = allselect)
BF.grid(row=6, column=2, sticky=W, padx=5,pady=5)

BN = tkinter.Button(top, text ="select_none", command = noneselect)
BN.grid(row=6, column=1, sticky=W, padx=5,pady=5)

L1 = Label(top, text="start from:(city code)")
L1.grid(row=6, column=4, sticky=W, padx=5,pady=5)
E1 = Entry(top, bd =5)
E1.grid(row=6, column=5, sticky=W, padx=5,pady=5)

msg=Text(top,width=150,height=10) 
msg.grid(row=7,column=0,columnspan=6)
msg.insert(INSERT,'select your cities\n')


name=[]
x=[]
y=[]
with open('data.txt','r') as fp:
    for line in fp.readlines():
        name.append(line.split(',')[0])
        x.append(float(line.split(',')[1]))
        y.append(float(line.split(',')[2].strip()))
plt.plot(x,y,'o')
i=0
for xy in zip(x, y):
    plt.annotate(name[i], xy=xy, xytext=(-20, 10), textcoords='offset points')
    i+=1
plt.show()
    



top.mainloop()
