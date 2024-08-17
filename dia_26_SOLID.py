# PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
# Cada clase tiene una unica responsabilidad | una sola tarea clara
# Cada clase tiene una unica razon para cambiar 
# cuando se requiere una tarea se crea una clase

# Forma incorrecta
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    # Guardar usuario en BD
    def save_to_DB(self):
        pass # Ejemplo

    # Enviar email
    def send_email(self):
        pass # Ejemplo

# MAS de una tarea en una clase | crea, guarda en BD, envia

# Forma correcta 
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserService:
    def save_to_DB(self, user):
        pass # Ejemplo
     
class EmailService:
    def send_email(self, email, message):
        pass # Ejemplo

# UNICA tarea por cada clase 


"""
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.
Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
"""
# Incorrecto
class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        self.books.append({"name": name, "id": id, "email": email})

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append({"user_id": user_id, "book_title": book_title})
                return True
            return False
        
    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                    return True
        return False
    
# correcta
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class User:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

class Loan:
    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"user_id": user.id, "book_title": book.title})
            return True
        return False

    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False
    

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self,user):
        self.books.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False
        
    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False