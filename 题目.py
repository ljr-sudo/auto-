import random

z=float(input("请选题（1~7）："))
a = random.randint(10,90)
b = random.randint(10,20)
c = random.randint(1,10)
if z==1:
    for i in range(2,b+1):

        print("小明有", a, "个苹果，小红的苹果数是小明的",c,"/", i, "小红有几个苹果？")
        y=float(input("如需答案请敲1"))
        if y==1:
            if i >= 1:
                print("答案")
                print(a,'*',c,'/',i,"=")
                print(a*c/i)
            else:
                print('ZeroDivisionError: division by zero')
if z==2:
    for i in range(2,b+1):

        print("小军有",a, "个苹果，小亮的苹果数是比小军多",c,"/", i, "小亮有几个苹果？")
        y=float(input("如需答案请敲1"))
        if y==1:
            if i >= 1:
                print("答案")
                print(a,'*(1+(',c,'/',i,'))')
                print(a*(1+(c/i)))
            else:
                print('ZeroDivisionError: division by zero')
if z==3:
    for i in range(2,b+1):

        print("小明吃包子，他吃若干个包子后体积增加了",c,"/",i,"，上完厕所后将吃的包子全部排空，体积减小了几分之几？")
        y=float(input("如需答案请敲1"))
        if y==1:
            if i >= 1:
                print("答案")
                x=c+i
                print(c,'/',x)
            else:
                print('ZeroDivisionError: division by zero')
if z==4:
    for i in range(2,b+100):

        print("按1:",a,"的比配置了一瓶",i,"mL的稀释液，其中浓缩液和水的体积分别是多少？")
        y=float(input("如需答案请敲1"))
        if y==1:
            if i >= 1:
                print("答案")
                l = i/a
                print("每份是：",i,"/",a,"=",l,"(mL)")
                print("浓缩液有：",l,"x1=",l,"(mL)")
                j = l*a
                print("水有：",l,"X",a,"=",j,"(mL)")
                print("PS:由于程序BUG,分数表示为小数")
            else:
                print('ZeroDivisionError: division by zero')
if z==5:
    for i in range(2,b+10):

        print('有一个圆，半径为',c+b,',面积是多少?')
        y=float(input("如需答案请敲1"))
        if y == 1:
            if i >= 1:
                x=c+b
                print('答案')
                print('C=2πr')
                print(' =2xπx',x)
                print(' =',2*3.14*x)
            else:
                print('ZeroDivisionError: division by zero')
if z==6:
    for i in range(2,b+10):

        print('有一个圆，直径为',c+b,',面积是多少?')
        y=float(input("如需答案请敲1"))
        if y == 1:
            if i >= 1:
                print('答案')
                print('C=πd')
                x = c + b
                print(' =πx',x)
                print(' =',3.14*x)
            else:
                print('ZeroDivisionError: division by zero')
if z==7:
    for i in range(2,b+10):

        print('有一个圆，半径为',c+b,'面积是多少')
        y=float(input("如需答案请敲1"))
        if y == 1:
            if i >= 1:
                print('答案')
                print('S=πr2')
                x = c + b
                print(' =πx',x,'x',x)
                print(' =πx',x*x)
                print(' =',3.14*x*x)
            else:
                print('ZeroDivisionError: division by zero')
if z>=8:
    print("[一] [口] [X]")
    print(ValueError)
    print("You do a what gui?")
print('over.')