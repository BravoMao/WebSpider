# -*- coding: utf-8 -*-
#encoding:utf-8
from matplotlib import pyplot as plt


def plotPie4Gender(dics):
    plt.figure(figsize=(6,9))
    labels = getLables(dics)
    sizes = getSizes(dics)
    colors = ['red','yellowgreen','lightskyblue']
    explode = (0.05,0,0)
    patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                    labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                    startangle = 90,pctdistance = 0.6)
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    plt.axis('equal')
    plt.legend()
    plt.show()
def getSizes(dicts):
    sizes=[]
    for key in dics:
        sizes.append(dics[key])
    return sizes

def getLables(dics):
    lables=[]
    for key in dics:
        lables.append(key)
    return lables

if __name__ == '__main__':
    dics={"male":3,"female":3,"unknown":3}
    plotPie4Gender(dics)

