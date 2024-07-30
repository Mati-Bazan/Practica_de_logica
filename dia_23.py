# Patron de diseño | Singleton
# Una manera de intentar resolver un determinado problema

class Singleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
    

singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 is singleton2) # True

"""
Utiliza el patrón de diseño "singleton" para representar una clase que
    haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y email),
    recuperar los datos del usuario y borrar los datos de la sesión.
"""

class UserSession:

    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email},"
    
    def clear_user(self):
        self.id: int = None
        self.username: str = None
        self.name: str = None
        self.email: str = None

session1 = UserSession()
session1.set_user(1, "mati", "M.. B..", "mati@gmail.com")
print(session1.get_user()) # 1, mati, M.. B.., mati@gmail.com,

session2 = UserSession()
print(session2.get_user()) # 1, mati, M.. B.., mati@gmail.com,

session3 = UserSession()
session3.clear_user()
print(session3.get_user()) # None, None, None, None,

# Todos los usuarios son comunes en diferentes partes de la aplicación.
