import time
n=input("请输入时间")
a=0
while a>=0:
    if a==n:
        a=0
        break
    else:
        time.sleep(1)
        a=a+1
        print(a)
        
    
