import re
import hashlib




def hashing(password):
    key = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return key


class Account:
    
    
    def __init__(self, username: str, password: str, phone_number: str, email: str) -> None:
        self.username = Account._check_user(username)
        self.password = Account._check_password(password)
        self.phone_number = Account._check_phone_number(phone_number)
        self.email = Account._check_email(email)
        
    
    @staticmethod    
    def _check_user(username):
        if re.match(r"[a-zA-Z]+_[a-z A-Z]+", username):
            return username
        else:
            raise Exception("invalid username")
        
    
    @staticmethod
    def _check_password(password):
        if re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]+){8,}$", password):
            return hashing(password)
        else:
            raise Exception("invalid password")
    

    @staticmethod
    def _check_phone_number(phone_number):
        if re.match(r"^([+]98|0)9\d{9}$", phone_number):
            return "0"+phone_number[3:] if phone_number.startswith("+") else phone_number
        else:
            raise Exception("invalid phone number")
    
        
    @staticmethod
    def _check_email(email):
        if re.match(r"^[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]{2,5}$", email):
            return email
        else:
            raise Exception("invalid email")    


class Site:
    
    
    def __init__(self, url) -> None:
        self.url = url
        self.register_users = []
        self.active_users = []


    def register(self, user: Account):
        if user in self.register_users:
            raise Exception("user already registered")
        else:
            self.register_users.append(user)
            return("register successful")
    
    
    def login(self, users: Account, username: str = None, password: str = None, email: str = None):
        if users in self.active_users:
            raise Exception("user already logged in")
        else:
            for user in self.register_users:
                if username == None:
                    if user.email == email and user.password == hashing(password):
                        self.active_users.append(user)
                        return("login successful")
                elif email == None:
                    if user.username == username and user.password == hashing(password):
                        self.active_users.append(user)
                        return("login successful")
                elif user.username == username and user.email == email and user.password == hashing(password):
                        self.active_users.append(user)
                        return("login successful")    
                else:
                    raise Exception("invalid login")
                
                  
    def logout(self, user: Account):
        if user in self.active_users:
            self.active_users.remove(user)
            return("logout successful")
        else:
            return("user is not logged in")