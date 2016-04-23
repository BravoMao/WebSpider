# -*- coding: utf-8 -*-
#encoding:utf-8

from zhihu import User
import visualisation as v
import heapq
import operator
import json
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
        try:
            follower_number=follower.get_followers_num()
            allFollowers[follower.get_user_id()]=follower_number
        except:
            allFollowers[follower.get_user_id()]=0
        print(allFollowers)
    stars = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

def getTop5Cities(followers):
    allCities={}
    for follower in followers:
        city=follower.get_location()
        if allCities.has_key(city):
            allCities[city]+=1
        else:
            allCities[city]=1
        print allCities
    stars = dict(sorted(allCities.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

def getTop5Works(followers):
    allWork={}
    for follower in followers:
        str=follower.get_work()
        print(str)
        if allWork.has_key(str):
            allWork[str]+=1
        else:
            allWork[str]=1
        print json.dumps(allWork, encoding="UTF-8", ensure_ascii=False)
    #to delete bias
    if 'unknown' in allWork:
        del allWork['unknown']

    top5Cities = dict(sorted(allWork.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return top5Cities

def getTop5Relations(followers):
    allFollowers={}
    for follower in followers:
        allFollowers[follower.get_user_id()]=follower.get_vote_thank_relation()
        print(allFollowers)

    superFriends = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return superFriends

if __name__ == '__main__':
    #an example to get your friends' city location
    user_url = "https://www.zhihu.com/people/BravoMaooo"
    user = User(user_url)
    print(user.get_work())
    followers = user.get_followers()
    dics=getTop5Works(followers)
    print(dics)
    v.plotPie4Top5(dics)