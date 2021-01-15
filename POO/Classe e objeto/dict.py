class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    pedro = Pessoa(nome="Pedro")
    henrique = Pessoa(pedro, nome="Henrique")


    henrique.sobrenome = "Pedro"
    print(henrique.__dict__)
    print(pedro.__dict__)            #printa um dicionario com os atributos da instancia (atributos de dados apenas)
