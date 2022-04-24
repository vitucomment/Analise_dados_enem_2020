# Fonte de dados: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

import pandas as pd

# Pandas importado

dados = pd.read_csv('DADOS/MICRODADOS_ENEM_2020.csv', encoding = "ISO-8859-1", sep=';')

# Foram importados os dados passando um parametro 'encoding' para mudar a codificação da linguagem
# Foi passado também o parametro sep=';' para identificar o separador dos registros


# Após a análise das colunas úteis, com a ajuda de um visualizador de dados mais avançado
# ( foi usado o PowerQuery do PowerBI)

dados = dados.drop(columns=['Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006', 'Q007',
                            'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013', 'Q014',
                            'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021',
                            'Q022', 'Q023', 'Q024', 'Q025','TP_ENSINO','IN_TREINEIRO',
                            'CO_MUNICIPIO_ESC','NO_MUNICIPIO_ESC', 'CO_UF_ESC',
                            'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC',
                            'TP_SIT_FUNC_ESC','CO_MUNICIPIO_PROVA','CO_UF_PROVA',
                            'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC',
                            'TP_PRESENCA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH',
                            'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TX_GABARITO_CN',
                            'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT',
                            'TP_STATUS_REDACAO','NU_NOTA_COMP1', 'NU_NOTA_COMP2',
                            'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5',
                            'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC','CO_PROVA_MT'])

# Com a ajuda do PowerQuery, rapidamente é verificado as colunas que não são úteis para a ánalise
# É passada uma lista com o nome dessas colunas e atribuida a nova variável 'dados' um dataframe com apenas as colunas
# úteis.

dados.to_csv('DADOS/MICRODADOS_TRATADOS_COLUNAS.csv')
# O dataframe foi salvo com as colunas que úteis, finalizando a primeira parte do tratamento



# É possível o tratamento das linhas, retirando valores NULOS e aplicando os valores do dicionário do dataset

dados = pd.read_csv('DADOS/MICRODADOS_TRATADOS_COLUNAS.csv')

# Foi salvo na variável 'dados', nosso banco de dados com apenas as colunas úteis.

dados = dados.dropna()

# Foi usada a função 'dropna()' para remover valores nulos, foi verificado também se o valor '0' iria estar presente
# nas colunas de notas,
# como forma de verificar se o aluno zerou a redação ou área de conhecimento

dados = dados.drop(columns='Unnamed: 0')

# Uma coluna inválida foi encontrada e removida

dados = dados.reset_index()

# Foi usada a função 'reset_index()' para resetar a coluna index do dataframe

dados = dados.drop(columns='index')



# Para o tratamento das linhas que possuem números invés das informações, é fornecido
# um dataset 'Dicionário_Microdados_Enem_2020.xlsx'
# Foi observado suas respectivas informações, então foi criado um dicionário para cada coluna e com a função 'map()'
# foi passado seus recpectivos valores.

TP_FAIXA_ETARIA = {
    1:'Menor de 17 anos',
    2:'17 anos',
    3:'18 anos',
    4:'19 anos',
    5:'20 anos',
    6:'21 anos',
    7:'22 anos',
    8:'23 anos',
    9:'24 anos',
    10:'25 anos',
    11:'Entre 26 e 30 anos',
    12:'Entre 31 e 35 anos',
    13:'Entre 36 e 40 anos',
    14:'Entre 41 e 45 anos',
    15:'Entre 46 e 50 anos',
    16:'Entre 51 e 55 anos',
    17:'Entre 56 e 60 anos',
    18:'Entre 61 e 65 anos',
    19:'Entre 66 e 70 anos',
    20:'Maior de 70 anos'
}
dados.TP_FAIXA_ETARIA = dados.TP_FAIXA_ETARIA.map(TP_FAIXA_ETARIA)


TP_ESTADO_CIVIL = {
    0:'Não informado',
    1:'Solteiro(a)',
    2:'Casado(a)/Mora com companheiro(a)',
    3:'Divorciado(a)/Desquitado(a)/Separado(a)',
    4:'Viúvo(a)'
}
dados.TP_ESTADO_CIVIL = dados.TP_ESTADO_CIVIL.map(TP_ESTADO_CIVIL)


TP_COR_RACA = {
    0:'Não declarado',
    1:'Branca',
    2:'Preta',
    3:'Parda',
    4:'Amarela',
    5:'Indígena'
}
dados.TP_COR_RACA = dados.TP_COR_RACA.map(TP_COR_RACA)


TP_NACIONALIDADE = {
    0:'Não informado',
    1:'Brasileiro(a)',
    2:'Brasileiro(a) Naturalizado(a)',
    3:'Estrangeiro(a)',
    4:'Brasileiro(a) Nato(a), nascido(a) no exterior'
}
dados.TP_NACIONALIDADE = dados.TP_NACIONALIDADE.map(TP_NACIONALIDADE)


TP_ST_CONCLUSAO = {
    1:'Já concluí o Ensino Médio',
    2:'Estou cursando e concluirei o Ensino Médio em 2020',
    3:'Estou cursando e concluirei o Ensino Médio após 2020',
    4:'Não concluí e não estou cursando o Ensino Médio'
}
dados.TP_ST_CONCLUSAO = dados.TP_ST_CONCLUSAO.map(TP_ST_CONCLUSAO)


TP_ANO_CONCLUIU = {
    0:'Não informado',
    1:'2019',
    2:'2018',
    3:'2017',
    4:'2016',
    5:'2015',
    6:'2014',
    7:'2013',
    8:'2012',
    9:'2011',
    10:'2010',
    11:'2009',
    12:'2008',
    13:'2007',
    14:'Antes de 2007'
}
dados.TP_ANO_CONCLUIU = dados.TP_ANO_CONCLUIU.map(TP_ANO_CONCLUIU)


TP_ESCOLA = {
    1:'Não Respondeu',
    2:'Pública',
    3:'Privada',
    4:'Exterior'
}
dados.TP_ESCOLA = dados.TP_ESCOLA.map(TP_ESCOLA)


TP_LINGUA = {
    0:'Inglês',
    1:'Espanhol'
}
dados.TP_LINGUA = dados.TP_LINGUA.map(TP_LINGUA)


# Para finalizar o processo de tratamento das linhas, o dataframe é salvo em um novo dataset
dados.to_csv('DADOS/MICRODADOS_TRATADOS_COLUNAS_LINHAS.csv')


#_____________________________________FINALIZADO PRIMEIRA PARTE DO TRATAMENTO_____________________________________



# Pandas importado


dados = pd.read_csv('DADOS/MICRODADOS_TRATADOS_COLUNAS_LINHAS.csv')
# O banco de dados tratado na primeira parte do projeto é lido e salvo na variavel dados


dados = dados.rename(columns={
    'NU_INSCRICAO':'Nº de incrição',
    'NU_ANO':'Ano',
    'TP_FAIXA_ETARIA':'Faixa etaria',
    'TP_SEXO':'Sexo',
    'TP_ESTADO_CIVIL':'Estado civil',
    'TP_COR_RACA':'Raça',
    'TP_NACIONALIDADE':'Nacionalidade',
    'TP_ST_CONCLUSAO':'Situação E.M.',
    'TP_ANO_CONCLUIU':'Ano de conclusão E.M.',
    'TP_ESCOLA':'Tipo de escola',
    'NO_MUNICIPIO_PROVA':'Municipio',
    'SG_UF_PROVA':'Estado',
    'NU_NOTA_CN':'Nota ciências naturais',
    'NU_NOTA_CH':'Nota ciências humanas',
    'NU_NOTA_LC':'Nota linguagens',
    'NU_NOTA_MT':'Nota matemática',
    'TP_LINGUA':'Lingua estrangeira',
    'NU_NOTA_REDACAO':'Nota redação'
})
# A mudança do nome das colunas poderia ter sido feita na primeira parte do tratamento
# A função rename(columns={}) foi usada para passar um dicionário com o nome das colunas


dados.to_csv('DADOS/MICRODADOS_TRATADOS_COLUNAS_LINHAS.csv')
# Salvamos rapidamente o banco de dados com as colunas alteradas


def media_notas(area, dataset):
    media = round(dataset[area].mean(),2)
    return media
# Uma função que retorna o valor da média dos resultados, passando os parametros da 'area de conhecimento' e 'banco de dados'


media_ciencias_naturais = media_notas('Nota ciências naturais', dados)
media_ciencias_humanas = media_notas('Nota ciências humanas', dados)
media_linguagens = media_notas('Nota linguagens', dados)
media_matematica = media_notas('Nota matemática', dados)
media_redacao = media_notas('Nota redação', dados)
# Salvando o valor da média de cada área usando a função criada para o calculo


# Feita a instalação do pacote 'sqlalchemy' que possibilita a criação de um banco de dados sql
# Usando funções de 'select' de banco de dados SQL, é possivel fazer consultas de maneira prática e ágil


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
# Criamos um banco de dados usando uma engine, passamos como parametro o SQLITE (poderia ser usado MySQL, por exemplo)
# O banco de dados é salvo na memoria local


dados.to_sql('dados', engine)
# Transformamos o banco de dados salvo na variavel 'dados' em um banco de dados do tipo 'sql'


# A seguir são feitas algumas consultas usando a linguagem SQL, ao todo foram feitas 3 consultas filtrando por 'tipo de escola'
# 'select * from dados' = CONSULTA TODOS OS DADOS DO DATASET 'DADOS', 'where "Tipo de escola"'= FILTRA PELO TIPO DE ESCOLA
# As tres consultas são salvas em dataframes separados, essa estratégia ajuda na criação de um dashboard que será feito porteriormente

consulta = 'select * from dados where "Tipo de escola" = "Pública"'
database_escolas_publicas = pd.read_sql(consulta, engine)
database_escolas_publicas.to_csv('DADOS/database_escolas_publicas.csv')

consulta = 'select * from dados where "Tipo de escola" = "Privada"'
database_escolas_privadas = pd.read_sql(consulta, engine)
database_escolas_privadas.to_csv('DADOS/database_escolas_privadas.csv')

consulta = 'select * from dados where "Tipo de escola" = "Não Respondeu"'
database_escolas_nao_informada = pd.read_sql(consulta, engine)
database_escolas_nao_informada.to_csv('DADOS/database_escolas_nao_informada.csv')


medias_gerais = [
    ['Média_geral_ciencias_naturais', media_ciencias_naturais],
    ['Média_geral_ciencias_humanas', media_ciencias_humanas],
    ['Média_geral_linguagens', media_linguagens],
    ['Média_geral_matematica', media_matematica],
    ['Média_geral_redacao', media_redacao]
]
medias_gerais = pd.DataFrame(medias_gerais, columns=['Area_Conhecimento', 'Valor Média'])
# Criamos uma lista de valores que recebem as médias calculadas usando a função 'medias_notas'
# Salvamos numa variável a transformação dessa lista em um dataframe

medias_gerais.to_csv('DADOS/database_medias_gerais.csv')
# Por fim, o dataframe 'medias_gerais' é salvo em um dataset para auxiliar na criação do dashboard


dados['Média de notas individual'] = ((dados['Nota ciências naturais']+
                                     dados['Nota ciências humanas']+
                                     dados['Nota linguagens']+
                                     dados['Nota matemática']+
                                     dados['Nota redação'])/5).round(2)
# Por ultimo, criamos uma coluna e passamos a média das 5 notas individualmente


dados.to_csv('DADOS/MICRODADOS_COMPLETO.csv')
# Os dados são salvos num novo dataset
