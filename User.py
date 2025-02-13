import pytest


# class Circle:
#     PI = 3.14159

#     @staticmethod
#     def area(radius):
#        return Circle.PI * radius**2
    
#     def __init__(self, radius):
#         self.radius = radius
#         self.foo = 'this is foo'

#     def get_diameter(self):
#         return self.radius * 2

# my_area = Circle.area(3)

# my_circle = Circle(3)
# print(type(my_circle))
# print(my_circle.get_diameter())
# print(type(Circle))

# print('my circle dict')
# print(my_circle.__dict__)
# print(Circle.__dict__)














class User:
    #posts = {}
    posts = []
    
    def __init__(self,name,email,drivers_license):
        self.Name = name
        self.Email = email
        self.Drivers_license = drivers_license
        self.User_posts = []
        #self.User_posts = {}
        
    @property
    def get_name(self):
        return self.Name
    @get_name.setter
    def set_name(self,n_name):
        self.Name = n_name

    @property
    def get_email(self):
        return self.Email
    @get_email.setter
    def set_email(self,n_email):
        self.Email = n_email

    @property
    def get_User_posts(self):
        return self.User_posts
    @get_User_posts.setter
    def set_User_posts(self,n_User_posts):
        self.User_posts = n_User_posts

    @property
    def get_Drivers_license(self):
        return self.Drivers_license
    @get_Drivers_license.setter
    def set_Drivers_license(self,n_Drivers_license):
        self.Drivers_license = n_Drivers_license

    

    def create_a_post(self):
        post_title = input("Title: ") 
        post_content = input("What is on your mind? ") 
        #self.User_posts.append(post_content)


        #self.User_posts[post_title] = post_content
        self.User_posts.append({post_title : post_content})
        self.posts.append({post_title : post_content})



    def see_my_posts(self):
        #return "" if len(self.User_posts) == 0 else (for posts in self.User_posts:print(posts))
        #return ""
        if len(self.User_posts) == 0:
            return "" 
        else: 
            # return self.User_posts
            for posts in self.User_posts: 
                print(posts)

    def delete_a_post(self):
        post_delete = input("What post do you want to delete? ")
        post_d = self.User_posts.pop(post_delete-1)
        index = self.posts.index(post_d)
        self.posts.pop(index)

        
        # # print(post_delete ,"kenny")
        # index = 0
        # for post in self.User_posts:
        #     index += 1 
        #     if index == post_delete:
        #         # print(post_delete)
        #         # print(type(post_delete))
        #     #if post == post_delete:
        #         result = post
        #         # try:
        #         #     del self.User_posts[result]
        #         # except:
        #         #     ""
        # try:
        #     del self.User_posts[result]
        #     del self.posts[result]
        # except:
        #     ""
        
        
        
        # # result = ""
        # # index = 0
        # for post in self.posts:
        #     # index += 1 
        #     if post == result:
        #     #if post == post_delete:
        #         # result = post
        #         # del self.posts[post]
        #         pass
        # try:
        #     del self.posts[result]
        # except:
        #     ""
        
        

        # for index,post in enumerate(self.User_posts):
        #     if post == post_delete:
        #         result = index
        # try:
        #     del self.User_posts[result]
        # except:
        #     ""

    def see_all_posts(self):
        return "" if len(self.posts) == 0 else print(self.posts)




# user = User("John", "john@email.com", "FDUI87")
# print(user.Name == "John")
# print(user.Email == "john@email.com")
# print(user.Drivers_license == "FDUI87")
# user.create_a_post()
# print(user.posts)
# print(user.User_posts)
# print(User.posts)



# user = User("John", "john@email.com", "FDUI87")
# user.create_a_post()
# print(user.posts)
# print(user.see_my_posts())
# print(len(user.posts))
# print(len(user.User_posts))
# user.delete_a_post()
# print(user.see_my_posts())
# print(len(user.posts))
# print(len(user.User_posts))







# user.create_a_post()
# print(user.see_my_posts())
# print(len(user.posts) == 1)
# print(len(user.User_posts) == 1)
# user.test_delete_post()
# print(user.see_my_posts())
# print(user.see_my_posts())


# input = iter(["Johns †i†le", "I Just joined OOPX"])
# input = iter([1])
# # monkeypatch.setattr("builtins.input", lambda _x: next(input))
# print(input)
# # user.delete_a_post()
# # len(user.posts) == 0
# # len(user.User_posts) == 0
# # user.see_my_posts()
# # out, err = capsys.readouterr()
# out == ""
