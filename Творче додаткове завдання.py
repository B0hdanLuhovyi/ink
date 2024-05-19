import random

class Student:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class User:
    """Користувач сайту"""
    
    def __init__(self, name, comments=0, likes=0 , publication=""):
        self.name = name
        self.comments = comments
        self.likes = likes
        self.publication = publication 
    
    def talk(self):
        print("Моє ім'я:", self.name)
    
    def add_publication(self,publication):
        self.publication = publication
        
    
    def add_comments(self, num_comments):
        self.comments += num_comments
    
    def add_likes(self, num_likes):
        self.likes += num_likes
    
    def activity_level(self):
        return self.comments + self.likes
    
    def __str__(self):
        ans = 'Користувач сайту' + self.name + '\n'
        ans += 'Коментарі користувача: ' + str(self.comments) + '\n'
        ans += 'Остання публікація користувача: ' + self.publication + '\n'
        ans += 'Лайки користувача: ' + str(self.likes)
        return ans

class TV:

    def __init__(self,chanel=1,volume=50):
        self.chanel = chanel
        self.volume = volume
    
    def vol_reg(self,num):
        self.volume = num
    
    def chanel_reg(self,num):
        self.chanel= num
    
    def __str__(self):
        ans = 'Об\'єкт класа User\n'
        ans += 'Номер канала : ' + str(self.chanel) + '\n'
        ans += 'Гучність : ' + str(self.volume) + '\n'
        return ans

def main():
    users = [
        User("Іван", random.randint(1, 10), random.randint(1, 10)),
        User("Марія", random.randint(1, 10), random.randint(1, 10)),
        User("Петро", random.randint(1, 10), random.randint(1, 10))
    ]
    
    while True:
        print("\nМеню:")
        print("1. Публікувати коментарі")
        print("2. Додати лайки")
        print("3. Дізнатися рівень активності користувачів")
        print("4. Вийти")
        
        choice = input("Оберіть дію: ")
        
        if choice == '1':
            num_comments = int(input("Введіть кількість коментарів для публікації: "))
            for user in users:
                user.add_comments(num_comments)
            print("Коментарі успішно опубліковано!")
        elif choice == '2':
            num_likes = int(input("Введіть кількість лайків для додавання: "))
            for user in users:
                user.add_likes(num_likes)
            print("Лайки успішно додано!")
        elif choice == '3':
            print("\nРівень активності користувачів:")
            for user in users:
                print(user.name + ": " + str(user.activity_level()))
        elif choice == '4':
            print("До зустрічі:)")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

def site():
    list_users=[User(input("name:"),random.randint(1, 10), random.randint(1, 10),input("publication:")) for i in range(int(input("Количество юзеров:")))]
    comand = input("t = talk , c = add_comemnts , l = add_likes , p = add_publication , 0 = exit : ")
    while comand != "0":
        if comand == "t":
            for i in list_users:
        
                i.talk()
        elif comand == "c":
            for i in list_users:
                
                i.add_comments(int(input("кількість коментарів:")))
        elif comand == "l":    
            for i in list_users:
                
                i.add_likes(int(input("кількість лайків:"))) 
        elif comand == "0":
            break 
        elif comand == "p":
            for i in list_users:
                
                i.add_publication(input("публікація:"))
        else:
            print("команда введена з помилкою")
        comand = input("t = talk , c = add_comemnts , l = add_likes , 0 = exit : ")
  
def study_prog():
    list_sudents=[Student(input("name:"),input("gender:")) for i in range(int(input()))]
    for i in list_sudents:
        print(i.name,i.gender)




