# -*- coding: utf-8 -*-
#encoding:utf-8

from zhihu import User
import visualisation as v
import heapq
import operator
def getGenders(followers):
    genders={"male":0,"female":0,"unknown":0}

    for follower in followers:
        if("male" == follower.get_gender()):
            genders["male"]=genders.get("male")+1
        elif("female" == follower.get_gender()):
            genders["female"]=genders.get("female")+1
        else:
             genders["unknown"]=genders.get("unknown")+1
    return genders

def getTop5Stars(followers):
    allFollowers={}
    for follower in followers:
        allFollowers[follower.get_user_id()]=follower.get_followers_num()

    stars = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

if __name__ == '__main__':

    user_url = "https://www.zhihu.com/people/BravoMaooo"
    user = User(user_url)
    print(user.get_work())
    '''
    user.get_user_id()
    print(user.get_followers_num())
    followers = user.get_followers()
    dics=getTop5Stars(followers)
    print(dics)
    v.plot4Top5(dics)
    '''