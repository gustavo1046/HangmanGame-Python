import random

def list_to_string(lista): #convertendo a palavra de lista para string para realizar a impressao
    strlist = "".join(str(x) for x in lista) #funçao de conversão
    return strlist


def print_winner(word): #funçao de vencedor :)))
    print("\n\nParabéns, você ganhou!")
    print("\n", *word, sep=" ")
    print("            __      ")
    print("        '.=====.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("          .' '.        ")
    print("        '-------'       ")
    exit(1)


def print_loser(key_word): #funçao de perdedor
    print("\n\nVocê foi enforcado!")
    print(f"A palavra era {key_word}!!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   /\  ")
    print("|    XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXXX     XXXX   |      ")
    print(" |                   |      ")
    print(" _       XXXX      __/     ")
    print("   |\    XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   _             /       ")
    print("     _         _/         ")
    print("        \___/           ")
    exit(1)


def game(word, trick, score): #funçao do jogo
    erros = 0 #contador de erros para imprimir a forca
    print("                                  Jogo da Forca com Python")
    print("\n\nDica:",trick) #imprime a dica
    while erros <= 7:
        if list_to_string(score) == word: #se a string de tentativas for igual a string da palavra printa a funço de ganhador
            print_winner(score)

        print("  _______     ")
        print(" |/      |    ")

        if erros == 0:
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if erros == 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if erros == 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if erros == 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if erros == 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if erros == 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if erros == 6:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if erros == 7: #chegando aqui voce perdeu
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
            print(" |            ")
            print("_|___         ")
            print_loser(key_word=word)

        print(" |            ")
        print("_|___         ")

        # print(word)
        print(*score, sep=" ") #esse print ele imprime na tela as linhas pontilhadas de score

        letra = input("Digite a letra que deseja sugerir: ")
        while letra.isnumeric():
            letra = input("Numeros não são permitidos, digite novamente: ")
        letra = letra.lower()
        comp = list(score) #esse comp é um comparador de acertos, contabiliza os erros para alterar a forca
        for i in range(len(word)):
            if letra == word[i]:
                score[i] = letra #coloca a letra acertada na respectiva posiçao na palavra da lista score
        if comp == score: #contabiliza erros
            erros += 1
            print("Número de erros: ", erros)


def main(): #funçao principal
    palavras = [['pycharm'], ['alcides'], ['jacques'], ['numpy'], ['framework'], ['fluter'], ['computador'], ['python'],
                ['mouse'], ['html'], ['css'], ['processador'], ['php'], ['poo'], ['apache'], ['pascal'], ['false'],
                ['else'], ['linux'], ['photoshop'], ['java']] #lista de palavras cadastradas

    dica = [['IDE para utilizar linguagem python'], ['professor do curso de python do IFCE'],
            ['professor do curso de python do IFCE'], ['Biblioteca para utilizar matrizes'],
            ['promove funcionalidade genérica'],
            ['kit de desenvolvimento de interface do google'],
            ['conjunto de componentes eletricos que executa tarefas'],
            ['Linguagem de programação'], ['periférico de entrada'], ['Linguagem de marcação'],
            ['estilizador de documentos web'],
            ['componente capaz de executar tarefas logicas'], ['linguagem para back-end'], ['linguagem de estilização'],
            ['servidor web'], ['Linguagem de programaçao antiga'], ['valor booleano'],
            ['se a condição nao for satisfeita utilizamos ele'], ['software open source'], ['editor de fotos'], ['lingaugemd e programçao orientada a objeto']] #dicas das palavras cadastradas

    word = random.choice(palavras) #escolhe uma palavra aleatoria
    trick = (dica[palavras.index(word)]) #escolhe a dica na mesma posiçao de lista da palavra escolhida
    word = str(word[0]) #converte para string
    trick = str(trick[0])
    score = [] #lista de pontilhados para fins visuais
    for i in range(len(word)): #preenche o vetor score com underlines para impressao e mudança na medida dos acertos
        score.append('_ ')
    game(word, trick, score)


if __name__ == "__main__": #funçao de execução do codigo
    main()
