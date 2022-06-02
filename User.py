class User:
    # dicto log user posts
    post_dict = {}
    #added a post count to keep track of user post numbers and initialized each users
    # dict when they are added to the class
    def __init__(self, name, age, phone_number, email_address):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email_address = email_address
        self.post_count = 0
        User.post_dict[self.name] = {}

    def post_get(self, post_num):
        print(f"{self.name} said \"{User.post_dict[self.name][post_num]}\"")
    
    def post(self, post):
        if self.post_count == 0:
            User.post_dict[self.name][0] = post
            self.post_count += 1
        else:
            User.post_dict[self.name][self.post_count] = post
            self.post_count += 1

    def post_del(self, post_num):
        del User.post_dict[self.name][post_num]

bob = User('Bob', 42, '(123)-222-4444', 'bob@mail.com')
cindy = User('Cindy', 55, '(123)-222-4444', 'cindy@mail.com')
tim = User('Tim', 32, '(123)-222-4444', 'tim@mail.com')
chuck = User('Chuck', 59, '(123)-222-4444', 'chuck@mail.com')


tim.post("I love this ability in the new app")
bob.post("YIPEE kiyay MF")
tim.post("this really is the stuff")
tim.post_del(0)
print(User.post_dict)
tim.post_get(1)
bob.post_get(0)

# del test_dict['Mani']