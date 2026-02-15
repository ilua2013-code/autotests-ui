from abc import ABC, abstractmethod


class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def displays_name(self):
        return f"Имя:{self.name}"
    
    def displays_age(self):
        return f"Возраст:{self.age}"
    

class NewUser(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__stats = 10
    
    @property
    def stats(self):
        return self.__stats

    def displays_name(self):
        return f"Новое имя:{self.name}"
    
new_user = NewUser("ivan", 15)
new_user.stats = "25"

class User(ABC):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):  
        pass
    
    def displays_name(self):
        return f"Имя:{self.name}"
    
    def displays_age(self):
        return f"Возраст:{self.age}"