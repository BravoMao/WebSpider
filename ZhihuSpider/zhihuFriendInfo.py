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
        try:
            follower_number=follower.get_followers_num()
            allFollowers[follower.get_user_id()]=follower_number
        except:
            allFollowers[follower.get_user_id()]=0
        print(allFollowers)
    stars = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

def getTop5Cities(followers):
    allFollowers={}
    for follower in followers:
        if allFollowers.has_key(follower.get_location()):
            allFollowers[follower.get_location()]+=1
        else:
            allFollowers[follower.get_location()]=1
        print allFollowers
    stars = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

def getTop5Works(followers):
    allFollowers={}
    for follower in followers:
        print(follower.get_work())
        if allFollowers.has_key(follower.get_work()):
            allFollowers[follower.get_work()]+=1
        else:
            allFollowers[follower.get_work()]=1
        print allFollowers
    stars = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return stars

def getTop5Relations(followers):
    allFollowers={}
    for follower in followers:
        allFollowers[follower.get_user_id()]=follower.get_vote_thank_relation()
        print(allFollowers)
    superFriends = dict(sorted(allFollowers.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return superFriends

if __name__ == '__main__':
    '''
    user_url = "https://www.zhihu.com/people/BravoMaooo"
    user = User(user_url)
    print(user.get_work())
    followers = user.get_followers()
    dics=getTop5Cities(followers)
    '''
    #dics={ 'Kirio': 49508,'Ivan Yang': 5383, 'Suji Yan': 20027,'\xe5\x91\xa8\xe6\xb1\x9f\xe5\xb2\xad': 1787, '\xe7\xa9\xba\xe7\x99\xbd\xe7\x99\xbd\xe7\x99\xbd\xe7\x99\xbd': 3673}
    dics2={'unknown': 71, '\xe4\xb8\x8a\xe6\xb5\xb7': 13, '\xe5\xb7\xb4\xe9\xbb\x8e\xef\xbc\x88Paris\xef\xbc\x89': 9, '\xe5\x8c\x97\xe4\xba\xac': 8, '\xe6\xb3\x95\xe5\x9b\xbd': 5}
    print(dics2)
    v.plotPie4Top5(dics2)