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
        valores = [16.0, 17.0, 18.50, 25.0, 30.0, 35.0, 39.99]
        situacoes = ["baixo peso grau II", "baixo peso grau I", "peso ideal", "sobrepeso", "obesidade grau I", "obesidade grau II"]
        for valor in range(len(valores) -1):
            if valores[valor] <= imc < valores[valor+1]:
                situacao = situacoes[valor]
                break
        else:
            return "Margem de valores não aceita"

        return f"Nome: {nome} \nData de Nascimento: {data} \nPeso: {self.peso} \nAltura: {self.altura} \nSituação: {situacao} "

# nome = input("Qual o seu nome? \nR: ")
# data = input("Qual a sua data de nascimento? \nR: ")
# peso = float(input("Qual o seu peso? \nR: "))
# altura = float(input("Qual a sua altura? \nR:"))

troxa = PessoaIMC(60, 1.83)
print(troxa.resultIMC('lenner', '28/12/2003'))