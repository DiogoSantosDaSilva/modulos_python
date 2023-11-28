# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula19_dowload.csv'

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     # next(leitor) -> Com este comando pula a primeira linha, ou seja
#     # Pula as colunas e ler os valores das colunas.

#     # print(next(leitor)) alem disso também pode iterar sobre esse valor.
#     # iterando o arquivo csv.
#     for linha in leitor:
#         print(linha)

# Abaixo uma forma de ler o arquivo em formato de dicionario.
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])
