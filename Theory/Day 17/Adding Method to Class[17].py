#TODO-Theory = Adding Method to a Class

"""when function is attached to an object is called a Method"""

class User:
    def __init__(self , user_id , username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self , user):
        user.followers += 1
        self.following += 1

    def back_following(self , user):
        user.followers += 1
        self.following += 1

user_1 = User("001" , "Aryan Jaiswal")
user_2 = User("002" , "Krish Jaiswal")

user_1.follow(user_2)
user_2.back_following(user_1)

print("Followers [User_1] -->" , user_1.followers)
print("Following [User_1] -->" , user_1.following)
print("\n")
print("Followers [User_2] -->" , user_2.followers)
print("Following [User_2] -->" , user_2.following)