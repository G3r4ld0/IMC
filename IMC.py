class PessoaIMC:
    def __init__(self, peso, altura):
        self._peso = peso
        self._altura = altura

    @property
    def peso(self):
        return self._peso
    
    @property
    def altura(self):
        return self._altura
    
    def calculaIMC(self):
        return self.peso/(self.altura**2)

    def resultIMC(self, nome, data):
        imc = self.calculaIMC()
        print(imc)
        if 16.0 <= imc <= 16.99:
            situacao = "baixo peso grau II"
        elif 17.0 <= imc <= 18.49:
            situacao = "baixo peso grau I"
        elif 18.50 <= imc <= 24.99:
            situacao = "peso ideal"
        elif 25.0 <= imc <= 29.99:
            situacao = "sobrepeso"
        elif 30.0 <= imc <= 34.99:
            situacao = "obesidade grau I"
        elif 35.0 <= imc <= 39.99:
            situacao = "obesidade grau II"
        else:
            return "margem de valores apresentados não aceita"

        return f"Nome: {nome} \nData de Nascimento: {data} \nPeso: {self.peso} \nAltura: {self.altura} \nSituação: {situacao} "

nome = input("Qual o seu nome? \nR: ")
data = input("Qual a sua data de nascimento? \nR: ")
peso = float(input("Qual o seu peso? \nR: "))
altura = float(input("Qual a sua altura? \nR:"))

troxa = PessoaIMC(peso, altura)
print(troxa.resultIMC(nome, data))