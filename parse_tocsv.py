import xml.etree.ElementTree as ET
import pandas as pd


def parse(file):
    # Carregue o arquivo XML
    tree = ET.parse(file)
    root = tree.getroot()

    # Crie listas para armazenar os dados
    cod_estacao = []
    data = []
    hora = []
    vazao = []
    nivel = []
    chuva = []

    # Itere sobre os elementos do XML e extraia os dados
    for dados in root.findall('.//DadosHidrometereologicos'):
        cod_estacao.append(dados.find('CodEstacao').text)
        data_hora = dados.find('DataHora').text.strip()
        data.append(data_hora.split()[0])
        hora.append(data_hora.split()[1])
        vazao.append(dados.find('Vazao').text)
        nivel.append(dados.find('Nivel').text)
        chuva.append(dados.find('Chuva').text)

    # Crie um DataFrame pandas com os dados extraídos
    df = pd.DataFrame({
        'Data': data,
        'Hora': hora,
        'Vazao': vazao,
        'Nivel': nivel,
        'Chuva': chuva
    })

    df.to_csv(f"{file[:-4]}.csv")

# Imprima o DataFrame resultante
if __name__ == "__main__":
    files = ["files/57562000.xml"]


    for file in files:
        parse(file)
        print(f"'{file}' is done!")
