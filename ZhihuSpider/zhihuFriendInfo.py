from zhihu import User

if __name__ == '__main__':
    user_url = "https://www.zhihu.com/people/BravoMaooo"
    user = User(user_url)
    followers = user.get_followers()
    for follower in followers:
        print(follower.get_user_id())