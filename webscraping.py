from bs4 import BeautifulSoup  # Importando a biblioteca BeautifulSoup.

import requests  # Importando a biblioteca BeautifulSoup

# Objeto site recebe o conteúdo da requisição http do site em questão.
site = requests.get("https://www.climatempo.com.br").content

# Objeto soup baixa do site o html através da requisição html.parser.
soup = BeautifulSoup(site, 'html.parser')

# Exibe o html tranformado em string pelo prettify.
print(soup.prettify())

# Procura no html a estrutura ("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
vento = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

# RESOLVER - Imprime temperarura
print('\n', vento.string)

# Imprime título
print('\n', soup.title.string)

# Imprime primeiro link encontrado
print('\n', soup.a)

# Imprime a primeira tag p encontrada
print('\n', soup.p.string)

# Procura na estrutra html relação com a palavra "admin"
print('\n', soup.find('admin'))
