# IMPORTAÇÕES
import pandas as pd
import os

# DEFINIÇÕES
df_model = pd.DataFrame(columns=['Periodo', 'Valor', 'Ano', 'Mes'])

# LEITURA DE ARQUIVOS
dir_admissoes = 'uploads/admissoes/'
lista_arquivos = os.listdir(dir_admissoes)

# FOR PARA PERCORRER TODOS OS ARQUIVOS DO DIRETÓRIO
for arquivo in lista_arquivos:
    if os.path.isfile(os.path.join(dir_admissoes, arquivo)):
        # nesta linha ele cria um dataframe vazio
        dataframe = pd.DataFrame()
        # nesta linha ele lê o arquivo csv e separa por ';'
        dataframe = pd.read_csv(dir_admissoes + arquivo, sep=';', skiprows=1)
        # nesta linha ele muda o eixo do dataframe e posteriormente exclui todas as linhas vazias 
        dataframe = dataframe.transpose().dropna()
        # nesta linha, o dataframe é fatiado pelo iloc, pegando todas as colunas a partir da 3ª linha e posteriormente reseta todos os indexes
        dataframe = dataframe.iloc[3:].reset_index()
        # nesta linha, ele renomeia as colunas do dataframe
        dataframe.columns = ['Periodo', 'Valor']
        # nesta linha, ele converte a coluna 'Periodo' para o tipo string
        dataframe['Periodo'] = dataframe['Periodo'].astype(str)
        # nesta linha, ele divide a coluna 'Periodo' em duas colunas 'Ano' e 'Mes'
        dataframe['Ano'] = dataframe['Periodo'].str.split('.').str[0]
        dataframe['Mes'] = dataframe['Periodo'].str.split('.').str[1]
        # nesta linha, ele concatena o dataframe com o df_model
        df_model = pd.concat([df_model, dataframe], ignore_index=True)

# corrigindo os valores nulos
df_model = df_model.fillna(0)
df_model.to_csv('export/admissoes.csv', index=False, sep=';')