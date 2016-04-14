# -*- coding: utf-8 -*-
#encoding:utf-8

from zhihu import User
import visualisation as v
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
    stars={}
    for follower in followers:
        if(len(stars)<5):
            stars[follower.get_user_id()]=follower.get_followers_num()
        else:
            keys=stars.keys()
            for key in keys:
                if stars[key]<follower.get_followers_num():
                    stars.pop(key,None)
                    stars[follower.get_user_id()]=follower.get_followers_num()

        print stars

if __name__ == '__main__':

    user_url = "https://www.zhihu.com/people/BravoMaooo"
    user = User(user_url)
    user.get_followers_num()
    followers = user.get_followers()
    dics=getTop5Stars(followers)
    v.plotPie4Gender(dics)
