# -*- coding: utf-8 -*-
#encoding:utf-8
from matplotlib import pyplot as plt
import numpy as np

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


def plot4Top5(xlabel,ylabel,title,dics):
   n_groups = 5
   means_women = getSizes(dics)
   print(means_women)
   fig, ax = plt.subplots()
   index = np.arange(n_groups)
   bar_width = 0.35

   opacity = 0.4
   rects2 = plt.bar(index + bar_width/2, means_women, bar_width,alpha=opacity,color='r',label='User')

   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.title(title)
   plt.xticks(index + bar_width, getLables(dics))
   plt.ylim(0,50000)
   plt.legend()
   plt.tight_layout()
   plt.show()

def getSizes(dics):
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
    s={"male":3,"female":3,"unknown":3}
    s2={"A":3700,"B":11100,"C":49139,"D":2000,"E":3540}
    #plotPie4Gender(s)
    plot4Top5('top 5 stars','number of followers','Result of Your top 5 stars',s2)

