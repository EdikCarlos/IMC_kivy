from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0/255, 105/255, 92/255, 1)

class Container(BoxLayout):
    def calcular_imc(self, peso, altura):
        imc = peso / (altura ** 2)
        return imc

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidade grau 1 (leve)"
        elif imc < 40:
            return "Obesidade grau 2 (moderada)"
        else:
            return "Obesidade grau 3 (grave)"
    def calc(self):
        altura = float(self.ids.altura.text)
        peso = int(self.ids.peso.text)
        imc = self.calcular_imc(peso, altura)
        classificacao = self.classificar_imc(imc)
        resultado = f"Seu IMC é {imc:.2f} e sua classificação está como {classificacao}"

        self.ids.resultado.text = resultado

class Imc(App):
    def build(self):
        return Container()

Imc().run()