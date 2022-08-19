from keras.models import load_model
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.neural_network import MLPClassifier
import pickle

entrada = []

"""
Gender [0 1 2]
self_employed [0 1]
remote_work [0 1]
work_interfere [2 3 1 4 0]
family_history [0 1]
benefits [2 0 1]
care_options [1 0 2]
anonymity [2 0 1]
leave [2 0 1 3 4]
mental_health_interview [1 2 0]
phys_health_interview [0 1 2]
work_interfere [2 3 1 4 0]
"""

# colun = ['Gender','self_employed','remote_work',
#          'work_interfere','family_history', 'benefits', 'care_options', 'anonymity',
#          'leave','mental_health_interview','phys_health_interview']

def func(*args):
    arvore = pickle.load(open(r'/home/vilson/Documentos/vilson/ProjetoFInalOficial/Dados/survey_arvore_oficial.sav', 'rb'))

    previsores = arvore.predict([[gen, sem, rw, wi, fh, bf, co, ano, lea, mhi, phi]])


    if previsores == 0:
        print('\n# Paciente ok.\n')
        print("############################################################################")

        return previsores

    elif previsores == 1:
        print('\n# Paciente deve procurar auxilio psicologica.\n')
        print("############################################################################")

        return previsores


loop = int(input("# Digite para iniciar o diagnóstico:  0 - FIM | 1 - INICIAR: \n# "))
while loop != 0:
    # função para receber os parametros

    gen = input('# Seu genero consta como:\n[0]FEMININO\n[1]MASCULINO\n[2]TRANS\n')
    sem = input('# É autônomo ?\n[0]NÃO\n[1]SIM\n')
    rw = input('# Você trabalha remotamente no mínimo metade do seu tempo ?:\n[0]NÃO\n[1]SIM\n')
    wi = input('# Se você tem algum problema de saúde mental, você sente que isso interfere no seu trabalho ?:\n[0]NÃO SEI\n[1]NUNCA\n[2]FREQUENTEMENTE\n[3]RARAMENTE\n[4]AS VEZES\n')
    fh = input('# ALgun familiar seu ja foi diagnostico com alguma mal psicologico ?:\n[0]NÃO\n[1]SIM\n')
    bf = input('# Aonde você trabalha, você recebe algum beneficio para sua saúde mental ?:\n[0]NÃO SEI\n[1]NÃO\n[2]SIM\n')
    co = input('# Você tem conhecimento das opções de cuidado com a saúde mental disponíveis para você ?:\n[0]NÃO\n[1]NÃO SEI\n[2]SIM\n')
    ano = input('# Seu anonimato esta protegido se optar por tirar proveito dos recursos pára tratamento da sua saúde mental ou abuso de substancias ?:\n[0]NÃO SEI\n[1]NÃO\n[2]SIM\n')
    lea = input('# Quão fácil é para você tirar uma licença medica para tratar uma condição relacionada a sua saúde mental ?:\n[0]NÃO SEI\n[1]UM POUCO DIFICIL\n[2]UM POUCO FACIL\n[3]MUITO DIFICIL\n[4]MUITO FACIL\n')
    mhi = input('# Você falaria sobre um problema de saúde mental com um potencial contratante em uma entrevista ?:\n[0]TALVEZ\n[1]NÃO\n[2]SIM\n')
    phi = input('# Você falaria sobre um problema de saúde física com um potencial empregador em uma entrevista ?:\n[0]TALVEZ\n[1]NÃO\n[2]SIM\n')


    func(gen, sem, rw, wi, fh, bf, co, ano, lea, mhi, phi)

    loop = int(input("\n# Digite para continuar ou encerrar o diagnóstico:  0 - FIM | 1 - CONTINUAR: \n#"))
    print("############################################################################\n")