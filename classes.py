# Classe principal
class Participante:
    def __init__(self, identificacao, nome, idade, tipo): # Decidi usar a idade ao invés de email, abre portas para fazermos comparações depois
        self.__identificacao = identificacao
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def get_id(self):
        return self.__identificacao

    def apresentacao(self):
        print(f"Olá! me chamo {self.nome} e tenho {self.idade} anos!")

#----
class Campeonato(Participante):
    def __init__(self, identificacao, nome, idade, tipo, esporte):
        super().__init__(identificacao, nome, idade, tipo)

        self.esporte = esporte

    def competirEsporte(self):
        print(f"{self.nome} está competindo em: {self.esporte}")

#----
class Cosplay(Participante):
    def __init__(self, identificacao, nome, idade, tipo, personagem):
        super().__init__(identificacao, nome, idade, tipo)

        self.personagem = personagem  

    def mostrarCosplay(self):
        print(f"{self.nome} está vestido(a) de: {self.personagem}")

#----
class Palestra(Participante):
    def __init__(self, identificacao, nome, idade, tipo, palestrante):
        super().__init__(identificacao, nome, idade, tipo)

        self.palestrante = palestrante

    def competirEsporte(self):
        print(f"{self.nome} veio para assistir a palestra do(a): {self.palestrante}")

# Classe menu: Vai cuidar do cadastro e de exibir as informações gerais sobre os participantes
class Menu:
    def __init__(self):
        participantes = {}

    def cadastrarParticipante(self):
        pass        





