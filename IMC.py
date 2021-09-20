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
        valores = {16.0: "baixo peso grau II", 17.0: "baixo peso grau I", 18.50: "peso ideal", 25.0: "sobrepeso", 30.0: "obesidade grau I", 35.0: "obesidade grau II", 39.99: None}
        for valor in range(len(valores.keys()) -1):
            if list(valores.keys())[valor] <= imc < list(valores.keys())[valor + 1]:
                situacao = valores[list(valores.keys())[valor]]
                break
        else:
            return 'Margem de valores não aceita'
        return f"Nome: {nome} \nData de Nascimento: {data} \nPeso: {self.peso} \nAltura: {self.altura} \nSituação: {situacao} "

# nome = input("Qual o seu nome? \nR: ")
# data = input("Qual a sua data de nascimento? \nR: ")
# peso = float(input("Qual o seu peso? \nR: "))
# altura = float(input("Qual a sua altura? \nR:"))

troxa = PessoaIMC(60, 1.83)
print(troxa.resultIMC('Lenner', '28/12/2003'))