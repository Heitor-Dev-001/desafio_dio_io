#Seu objetivo será associar corretamente cada aplicação ou impacto 
# da IA com sua descrição correspondente, aprofundando seu 
# entendimento sobre como essa tecnologia está moldando nosso futuro.

#Não se preocupe com a linguagem de programação, 
# pois o foco aqui é entender os conceitos. 
# Aproveite para explorar uma das linguagens suportadas pela IA.

#Entrada
#A entrada consistirá na aplicação ou impacto da IA para o qual você deve 
# retornar a descrição. Nesse contexto, os seguintes conceitos são considerados
#  válidos para este desafio de código:

#"saúde"
#"educação"
#"transporte"
#"segurança"
#Saída
#A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

#"monitoramento e prevenção de crimes"
#"veículos autônomos e otimização de rotas"
#"personalização do aprendizado e tutoria inteligente"
#"diagnóstico precoce e tratamento personalizado"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma área de aplicação e retornar sua respectiva descrição.
def descrever_aplicacao(area):
    if area == "saúde":
        return "diagnóstico precoce e tratamento personalizado"
        
    # COMPLETE AQUI: Preencha corretamente cada área de aplicação, considerando as descrições abaixo:        
    elif area == "segurança":
        return "monitoramento e prevenção de crimes"
        
    elif area == "transporte":
        return "veículos autônomos e otimização de rotas"
                            
    elif area == "educação":
        return "personalização do aprendizado e tutoria inteligente"
        
# Imprime a descrição da aplicação na área recebido na "entrada" através da função "descrever_aplicacao". 
print(descrever_aplicacao(entrada))