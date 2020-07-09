import PySimpleGUI as gui
import mysql.connector

conn =  mysql.connector.connect(host = 'localhost', database = 'ex10', user ='root', password = '')

def gravar(nome, email, endereco):
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nome, email, endereco) VALUES ("
    query+= " '" + str(nome) + "' , '" + str(email) + "' , '" + str(endereco) + "')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

class Usuario:
    def __init__(self, nome,email, endereco):
        self.__nome = self.setNome(nome)
        self.__email = self.setEmail(email)
        self.__endereco = self.setEndereco(endereco)

    def setNome(self, nome):
        return nome

    def setEmail(self, email):
        return email
    
    def setEndereco(self, endereco):
        try:
            endereco = int(endereco)
            return endereco
        except:
            return None
    
    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email

    def getEndereco(self):
        return self.__endereco
    


class Tela:
    def __init__(self):
        layout = [
            [gui.Text('Nome'), gui.Input()],
            [gui.Text('email'), gui.Input()],
            [gui.Text('Endereço'), gui.Input()],
            [gui.Button("Enviar")]
            ]
        self.tela = gui.Window("Usuário").layout(layout)

    def show(self):
        self.button, self.values = self.tela.Read()
        if self.button in (None, 'Enviar'): 
            usuario = Usuario(self.values[0], self.values[1], self.values[2])
            gravar(usuario.getNome(), usuario.getEmail(), usuario.getEndereco())

tela = Tela()
tela.show()