class User: 

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Sempre se atentar que tem que chamar a Classe. Se fosse 'user_1 = ('001', 'Mateus')' iria virar uma Tupla e iria dar erro depois.
user_1 = User('001', 'Mateus') 
user_2 = User('002', 'Leticia')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)