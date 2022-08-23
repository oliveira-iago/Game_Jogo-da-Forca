'''
22.08.2022 - Primeira versão
Autor: Iago Leonardo Alves de Oliveira
----------------------------------------
JOGO DA FORCA
----------------------------------------
Este programa escolhe um tema aleatório, e do tema uma palavra aleatória
Pede para o usuário adivinhar a palavra chutando letra por letra
ele conta uma tentativa a cada palpite errado do usuário
'''

#OS usada para ações no sistema operacional - TIME, aguardar
import os, time
#RANDOM faz o sistema escolher ou ordenar valores de forma aleatoria
import random
#COLORAMA usada para dar cores às strings // pip install colorama
import colorama
colorama.init()
#Cores
cor_azul = '\033[1;94m'
cor_vermelho = '\033[31m'
cor_verde = '\033[1;92m'
cor_amarelo = '\033[1;93m'
cor_limpa = '\033[0;0m'

#Lista de animais
animais = ['Baleia', 'Cachorro', 'Cavalo', 'Cobra', 'Crocodilo', 'Elefante', 'Frango', 'Galinha',
        'Gambá', 'Gato', 'Golfinho', 'Leao', 'Girafa', 'Lobo', 'Macaco', 'Ovelha', 'Papagaio', 'Polvo',
        'Pombo', 'Rinoceronte', 'Tartaruga', 'Touro', 'Urso', 'Vaca', 'rato', 'camundongo', 'Avestruz',
        'Arara', 'Tubarao', 'Camaleao', 'Lagartixa']

#Lista de filmes
filmes = ['Interestelar', 'Moana', 'Star Wars', 'Guardioes da Galaxia', 'Mulher Maravilha', 
        'Doutor Estranho', 'Homem Aranha', 'Sing', 'Trolls', 'Animais Fantasticos e Onde Habitam',
        'John Wick', 'A Chegada', 'Kong A Ilha da Caveira', 'A Bela e a Fera', 'O Poderoso Chefinho', 
        'Velozes e Furiosos', 'Logan', 'Batman', 'Ate o Ultimo Homem', 'Passageiros', 'Transformers',
        'Em Ritmo de Fuga', 'Jack Reacher', 'O Vigilante do Amanha', 'Alien', 'Corra', 'Fragmentado',
        'Piratas do Caribe', 'A Mumia', 'Estrelas Alem do Tempo', 'Cinquenta Tons de cinza', 'Assassins Creed',
        'Tinha que ser ele', 'Rei Arthur', 'Power Rangers', 'Anjos da Noite Guerras de Sangue',
        'Planeta dos Macacos', 'A Grande Muralha', 'A Vida', 'A Garota no Trem', 'De volta para o futuro', 
        'La La Land', 'As Aventuras do Capitao Cueca', 'Resident Evil', 'Quatro Vidas de um Cachorro',
        'Genios do Crime', 'O Dia do Atentado', 'Baywatch SOS Malibu', 'A Torre Negra']

#Lista de gêneros
generos = ['Animal', 'Filme']

#Desenhos
desenhos = [
    '''
        +---+
        |   | 
        |
        |
        |
        |
        |''',
    f'''
        +---+
        |   |
        |   {cor_vermelho}O{cor_amarelo}
        |
        |
        |
        |''',
    f'''
        +---+
        |   | 
        |   {cor_vermelho}O{cor_amarelo}
        |   {cor_vermelho}|{cor_amarelo}
        |
        |
        |''',
    f'''
        +---+
        |   | 
        |   {cor_vermelho}O{cor_amarelo}
        |   {cor_vermelho}|\{cor_amarelo} 
        |
        |
        |''',
    f'''
        +---+
        |   | 
        |   {cor_vermelho}O{cor_amarelo}
        |  {cor_vermelho}/|\{cor_amarelo} 
        |
        |
        |''',
    f'''
        +---+
        |   | 
        |   {cor_vermelho}O{cor_amarelo}
        |  {cor_vermelho}/|\{cor_amarelo} 
        |  {cor_vermelho}/{cor_amarelo}
        |
        |''',
    f'''
        +---+
        |   |
        |   {cor_vermelho}O{cor_amarelo}
        |  {cor_vermelho}/|\{cor_amarelo} 
        |  {cor_vermelho}/ \{cor_amarelo} 
        |
        | FIM DE JOGO!''']


#Sorteia uma palavra de acordo com o genêro sorteado
def sortearPalavra(genero):
    #Se o genero for Filme
    if genero == 'Filme':
        #Sorteia um filme
        return str(random.choice(filmes)).upper()

    #Se o genero dor Animal
    elif genero == 'Animal':
        #Sorteia um animal
        return str(random.choice(animais)).upper()

#Função prinicipal do jogo
def jogo():
    #Letras jogadas
    letras_jogadas = []
    #Soma de erros do usuário
    erros = 0

    #Sorteia um gênero
    genero = random.choice(generos)
    #Sorteia uma palavra de acordo com o gênero sorteado
    palavra = sortearPalavra(genero).upper()

    mensagem = ''

    while True:
        #Exibe uma moldura com título
        print(cor_limpa+'\n\n\t' + '+' + ('-'*15) + '+')
        print('\t' + '|' + ' Jogo da Forca ' + '|')
        print('\t' + '+' + ('-'*15) + '+')

        #Exibe o desenho de acordo com os erros do usuário (a forca sem boneco)
        print(cor_amarelo+desenhos[erros])

        #Loop por cada digito da palavra
        mascara = ''
        for letra in palavra:
            #Se a letra já foi jogada ou é um espaço
            if letra in letras_jogadas or letra.isspace():
                #Não mascara a letra
                mascara += letra

            #Senão 
            else:
                #Mascara a letra
                mascara += '_'
        
        #Remove os espaços da palavra conta os dígitos
        digitos_palavra = len(palavra.replace(' ', ''))

        letras_jogadas_texto = str(letras_jogadas).replace("'", '').replace('[', '').replace(']', '')
        print(f'\n\t{cor_limpa}Letras já jogadas: {cor_azul}{letras_jogadas_texto}')
        print(f'\t{cor_amarelo}{genero}{cor_limpa} com {cor_amarelo}{digitos_palavra}{cor_limpa} letras')
        
        print('\n\t' + mascara)

         #Se o usuário errou 6 vezes
        if erros >= 6:
            #Exibe a mensagem de fim de jogo
            print(f'\n\t{cor_vermelho}Você perdeu!\n\t{cor_limpa}A resposta era {cor_amarelo}{palavra}')
            break

        #Se o usuário acertou a palavra
        elif mascara.replace(' ', '') == palavra.replace(' ', ''):
            #Exibe a mensagem de sucesso
            print(f'\n\t{cor_verde}Você venceu!')
            break

        print(mensagem)

        #Recebe a letra do usuário
        letra_user = str(input(f'\n\t{cor_limpa}Digite uma letra: {cor_verde}')).upper()
        mensagem = ''
        
        #Se a letra já foi jogada anteriormente
        if letra_user in letras_jogadas:
            mensagem = f'\n\t{cor_vermelho}Insira uma letra que ainda não foi jogada'
        
        #Se a letra não é texto ou tem mais de 1 dígito
        elif not(letra_user.isalpha()) or len(letra_user) > 1:
            mensagem = f'\n\t{cor_vermelho}O valor inserido não é válido!\n\t(Insira uma letra por vez)'

        #Senão
        else:
            #Adiciona a letra jogada na listagem
            letras_jogadas.append(letra_user)

            #Se a letra não corresponde à palavra
            if not(letra_user in palavra):
                #Adiciona um erro ao usuário
                erros += 1
        
        #Limpa a tela
        os.system('cls')

    #Verifica se o usuário deseja jogar novamente
    time.sleep(2)
    print(f'\n\t{cor_limpa}Deseja jogar novamente?')
    print(f'\t[{cor_azul}1{cor_limpa}] Sim, quero jogar novamente')
    print(f'\t[{cor_azul}0{cor_limpa}] Não, não quero mais jogar')
    jogar = input(f'\n\t{cor_limpa}-> {cor_verde}').replace(' ', '')

    while jogar != '1' and jogar != '0':
        print('\n\tDigite uma opção válida!')
        jogar = input(f'\n\t{cor_limpa}-> {cor_verde}').replace(' ', '')

    if int(jogar):
        #Limpa a tela
        os.system('cls')
        jogo()


#Limpa a tela
os.system('cls')
jogo()