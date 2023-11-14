import socket

class Person():
    def __init__(self,id, username, password):
        self.id = id;
        self.username = username;
        self.password = password;
    def __str__(self):
        return "User name: " + self.username + '\n' + "Passsword: " + self.password + '\n' + "ID: " + self.id;
