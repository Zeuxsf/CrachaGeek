# Classe principal
class Participante:
    def __init__(self, identificacao, nome, idade, tipo): # Decidi usar a idade ao invés de email, abre portas para fazermos comparações depois
        self.__identificacao = identificacao
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def getId(self):
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

    def assistirPalestra(self):
        print(f"{self.nome} veio para assistir a palestra do(a): {self.palestrante}")

#--------------------------------------------------------------------------------------

# Classe menu: Vai cuidar do cadastro e de exibir as informações gerais sobre os participantes
class Menu:
    def __init__(self):
        self.participantes = {}
        self.id = 0
        self.quantidade = 0
        
        self._rodarMenu()

    def _cadastrarParticipante(self):
        self.id += 1
        P = f"P{self.id}" # Vai servir para criar uma variável com nome dinâmico, já que eu não quero ter que criar um json para salvar os dados
        
        nome = str(input("Nome do Participante: "))
        idade = int(input("Idade do Participante: "))
        
        while True:
            print("""
                  1 - Campeonato
                  2 - Cosplay
                  3 - Palestra
                  (Qualquer Tecla) - Outro
                  """)
            tipo = str(input("Para oque veio: "))
            
            if tipo == "1":
                esporte = str(input("Em qual esporte vai competir: "))
                campeao = Campeonato(self.id, nome, idade, "Campeonato", esporte)
                self.participantes[P] = campeao
                
            elif tipo == "2":
                personagem = str(input("Está fazendo cosplay de qual personagem: "))
                cosplayer = Cosplay(self.id, nome, idade, "Cosplay", personagem)
                self.participantes[P] = cosplayer
                
            elif tipo == "3":
                palestrante = str(input("Veio assistir a palestra do(a): "))
                aluno = Palestra(self.id, nome, idade, "Palestra", palestrante)
                self.participantes[P] = aluno
                
            else:
                comum = Participante(self.id, nome, idade, "Outro")
                self.participantes[P] = comum
            
            self.quantidade += 1
            break    
                
    
    def _quantidadeTotal(self):
        print(f"O evento tem {self.quantidade} participantes cadastrados até o momento!")
    
    def _mostrarParticipantes(self):
        if self.participantes == {}:
            print("Sem participantes cadastrados.")
        else:    
            while True:
                print("""
                    1 - Campeonato
                    2 - Cosplay
                    3 - Palestra
                    4 - Outro
                    (Qualquer Tecla) - Todos
                    """)
                mostrar = str(input("Mostrar: "))
                
                if mostrar == "1":
                    for p in self.participantes.values():
                        if p.tipo == "Campeonato":
                            print(f"{p.getId()} - {p.nome} \ {p.idade} anos \ Esporte: {p.esporte}")
                    
                elif mostrar == "2":
                    for p in self.participantes.values():
                        if p.tipo == "Cosplay":
                            print(f"{p.getId()} - {p.nome} \ {p.idade} anos \ Personagem: {p.personagem}")
                    
                elif mostrar == "3":
                    for p in self.participantes.values():
                        if p.tipo == "Palestra":
                            print(f"{p.getId()} - {p.nome} \ {p.idade} anos \ Palestrante: {p.palestrante}")
                            
                elif mostrar == "4":
                    for p in self.participantes.values():
                        if p.tipo == "Outro":
                            print(f"{p.getId()} - {p.nome} \ {p.idade} anos \ Explorando o Evento")                            
                    
                else:
                    for p in self.participantes.values():
                        print(f"{p.getId()} - {p.nome} \ {p.idade} anos \ {p.tipo}") 

                    print("Dict: ",self.participantes) # Só pra mostrar como a variável dinâmica funcionou muito bem     
                break          
    
    def _rodarMenu(self): # É a função principal do nosso Menu, vai fazer a mágica acontecer
        while True:
            print("""
                1 - Cadastrar Participante
                2 - Quantidade de Participantes Cadastrados
                3 - Mostrar Participantes
                (Qualquer Tecla) - Sair
                """)
            opcao = str(input("Opção: "))
            
            if opcao == "1":
                self._cadastrarParticipante()
                continue
            if opcao == "2":
                self._quantidadeTotal()
                continue
            if opcao == "3":
                self._mostrarParticipantes()
                continue
            else:
                break        
