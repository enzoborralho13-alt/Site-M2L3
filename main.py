import random
import string
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return (
      "<h1>Bem-vindo à Página Inicial!</h1>"
      "<p>Escolha o que você quer ver:</p>"
      '<ul>'
      '<li><a href="/random_fact">Veja um fato aleatório!</a></li>'
      '<li><a href="/secret">Ir para a página secreta (Gerador de Senhas)</a></li>'
      '</ul>'
  )


@app.route("/random_fact")
def random_fact():
  facts = [
      "O mel nunca estraga. Arqueólogos já encontraram potes de mel com mais de 3.000 anos perfeitamente comestíveis!",
      "Os polvos têm três corações e o sangue deles é azul.",
      "As bananas são naturalmente radioativas porque contêm muito potássio.",
  ]

  fact = random.choice(facts)

  return (
      "<h1>Fato Aleatório</h1>"
      f"<p>{fact}</p>"
      "<br>"
      '<a href="/">Voltar para a página inicial</a>'
  )


@app.route("/secret")
def secret_page():
  chars = string.ascii_letters + string.digits + "!@#$%"
  password = "".join(random.choice(chars) for _ in range(10))

  return (
      "<h1>🔐 Área Secreta!</h1>"
      f"<p>Sua senha super segura gerada automaticamente: <strong>{password}</strong></p>"
      "<br>"
      '<a href="/">Voltar para a página inicial</a>'
  )


if __name__ == "__main__":
  app.run(debug=True)
