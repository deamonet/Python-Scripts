from matplotlib import pyplot as plt
import numpy
import random as r


def initial():
    global inimark,daymark
    inimark=r.random()*100+100
    daymark=r.random()*0.8+0.1


def marks():
    x=list(range(1000))
    y=list(range(1000))
    y[0]=inimark
    day=[r.randint(1,1000),r.randint(1,1000),r.randint(1,1000)]
    for i in range(1000-1):
        if i in day:
            y[i+1]=y[i]+5
        else:
            y[i+1]=y[i]+daymark+r.random()*0.2-0.1-y[i]*0.001*(r.random()+1)
            

def main():
    plt.title("考研")
    plt.xlabel("days")
    plt.ylabel("marks")
    for j in range(100):
        initial()
        marks()
    plt.show()


main()


