import random
from datetime import datetime
from tkinter import *

#banco de dados
florao = ['kpi','nodi','ot','kiri','ay','donan','ton','chris','felp','capilé','capile','victor','fernando','galdino','terto','tibico','ayrton','christian','gabriel','herick','felipe']
substantivos_mas = ['beck', 'fandangos', 'windows phone', 'iphone','android', 'animal do christian', 'bradesco']
substantivos_fem = ['mesa', 'cadeira', 'agua', 'pessoa', 'garota', 'nestle']
verbos_passado = ['bongou', 'comeu', 'fudeu', 'escreveu', 'fumou', 'brincou','bebeu', 'dagueou', 'amou', 'pensou', 'ouviu', 'chorou', 'foi', 'apertou']
verbos_futuro = ['bongara', 'comera', 'fodera', 'fumara', 'brincara','bebera','dagueara', 'amara', 'apertara']
artigo = ['o', 'aquele', 'aqueles','a','as','os','aquela', 'aquelas']
adversativa = ['mas','entretanto','todavia','no entanto','porem']
aleatorio = ['muito mais','novamente','quem lhe amava','em tudo','nada']
palavrao = ['seu merda','vai se fuder','vai pra puta que pariu','vai toma no cu','toma no cu','chupa meu saco','mama']
comeco = ['um menino chamado','um pobre coitado chamado','um menino maltrapilho chamado','o muleque mais merda de todos mais conhecido como',]
conjuntiva = ['que','cujo','o qual']

#todas as funçoes da F.L.O.R.A

def primeiro_contato():
    resposta_nome.get()
    perg_inicial = resposta_nome.lower()
    if perg_inicial in florao:
        print("MECZADA")
    else:
        print("eta menó")

def escolha_itens(perg_inicial):
    print("[FLORA] Ora, ora,",perg_inicial,"! Eu sei bastante sobre você. Meu nome é FLORA e estou ao dispor de cada um de vocês.")
    print("")
    print("O que gostaria de saber? Digite o número do item correspondente")
    item = input("1)Me conte uma historia, 2)Idade, 3)Data e Hora 4)Quem Bonga 5)R$ de Pizza/cm³ 6)Sueca de Bebida")
    if item == "1":
        historia()
    if item == "2":
        idade()
    if item == "3":
        data_hora()
    if item == "4":
        quem_bonga()
    if item == "5":
        calcula_pizza()
    if item == "6":
        jogo_bebida()


def calcula_pizza():
    #calcula pizza/cm²
    diametro1 = int(input("qual o diametro da 1ª pizza? "))
    valor1 = int(input("quanto ela custa? "))
    area1 = 3.14*(diametro1/2)**2

    diametro2 = int(input("qual o diametro da 2ª pizza? ")) 
    valor2 = int(input("quanto ela custa? "))
    area2 = 3.14*(diametro2/2)**2
    
    #diametro3 = int(input("qual o diametro da 3ª pizza? ")) 
    #valor3 = int(input("quanto ela custa? "))
    #area3 =3.14*(diametro3/2)**2

    area_total = area1 + area2
    valor_total = valor1 + valor2

    custo_beneficio = valor_total/area_total
    print("Área:",area_total, "cm²")
    print("1 cm² de pizza vale:","R$%0.2f" %custo_beneficio)


def historia():
    x = input("Gostaria de ouvir uma historia? ")
    x = x.lower()
    if x in ['s','sim','yes','y']:
        print('[YOU]',x)
        print('[FLORA] Era uma vez...')
        print(random.choice(comeco))
        print(random.choice(florao))
        print(random.choice(conjuntiva))
        print(random.choice(verbos_passado))
        print(random.choice(artigo))
        if random.choice(artigo) == 'o' or 'aquele':
            print(random.choice(substantivos_mas))
        elif random.choice(artigo) == 'aqueles' or 'os':
            print(random.choice(substantivos_mas)+'s')
        elif random.choice(artigo) == 'a' or 'aquela':
            print(random.choice(substantivos_fem))
        elif random.choice(artigo) == 'aquelas' or 'as':
            print(random.choice(substantivos_fem)+'s')
        print(random.choice(adversativa))
        print(random.choice(florao))
        print(random.choice(verbos_passado))
        print(random.choice(aleatorio))
        print('________FIM_________')


def idade():
    now = datetime.now()
    nascimento = [1995,1997,1998]
    pessoa = input('De quem deseja saber a idade? ')
    if pessoa in florao:
        if pessoa in ['victor','galdino','terto','gabriel','fernando']:
            idades = now.year - nascimento[2]
        elif pessoa in ['tibico','herick','ayrton','felipe']:
            idades = now.year - nascimento[1]
        elif pessoa == 'christian':
            idades = now.year - nascimento[0]
        print(pessoa,"tem",idades,"anos")


def data_hora():
    current_time = datetime.now()
    now = datetime.now()
    print("[FLORA] São {:%H:%M}".format(current_time))
    print("do dia",now.day,"/",now.month,"/",now.year)


def jogo_bebida():
    lista_cartas = ['K','J','D',10,9,8,7,6,5,4,3,2,'A']
    carta_sorteada = random.choice(lista_cartas)
    print("A carta sorteada foi:",carta_sorteada)
    if carta_sorteada == 'K':
        return "O próprio jogador deve beber uma dose, seja ele homem ou mulher."
    elif carta_sorteada == 'J':
        return "Todos os jogadores homens devem beber uma dose."
    elif carta_sorteada == 'D':
        return "Todas as jogadoras devem beber uma dose."
    elif carta_sorteada == 10:
        return "PALAVRA PROIBIDA: \n O jogador que pegar essa carta deve definir uma palava que ninguém poderá pronunciar. O primeiro que o fizer, deve beber uma dose e a regra termina até o próximo 10 ser retirado e assim definida outra palavra. Dica: não falar verbos, substantivos, por exemplo, também é válido na carta 10."
    elif carta_sorteada == 9:
        return "DEDINHO: \n O jogador que pegar essa carta, poderá a qualquer momento da RODADA, posicionar o dedo indicador discretamente sobre algum lugar em que possa ser visto por todos, sem falar nada, e os outros jogadores devem perceber no decorrer do tempo e fazer o mesmo. O último jogador a posicionar o dedo na mesa, bebe uma dose."
    elif carta_sorteada == 8:
        return "CRIE UMA REGRA: \n Invente algo que todos ou alguns tenham que fazer por uma rodada, o criador da regra tem o direito de excluir-se dela."
    elif carta_sorteada == 7:
        return "PIN: \n Inicia-se uma sequencia de números, onde o número 7, números terminados em 7 e números múltiplos de 7, devem ser substituídos pela palavra PIN ou outra definida pelo jogador da vez. Quem falar o número ao invés de PIN, bebe uma dose. \n \n Obs: Se houverem 7 jogadores, muda-se o número e seus múltiplos para 8."
    elif carta_sorteada == 6:
        return "BANHEIRO: \n Parabéns! Pode ir ao banheiro. \n \n Obs: Essa carta só tem efeito durante uma rodada, mas você pode negociá-la com algum outro jogador. Após isso, se não houve negociação, deve-se descartá-la. Ex. Tipos de negociação: tomar X doses, pagar prenda, etc."
    elif carta_sorteada == 5:
        return "C S COMPOSTO: \n A partir de agora o jogador da vez deve escolher uma palavra inicial que não deve começar nem com C, nem com S e nem ser uma palavra composta. Logo em seguida os outros jogadores devem falar palavras que tenham relação com a dita anteriormente sem que ela comece com C nem S nem ser uma palavra composta. O primeiro a errar, bebe uma dose."
    elif carta_sorteada == 4:
        return "EU NUNCA: \n O jogador que tirou a carta, deve falar alguma coisa que nunca tenha feito. Todos os outros que algum dia já tenham feito, devem beber"
    elif carta_sorteada == 3:
        return "Mande 3 jogadores beberem uma dose cada."
    elif carta_sorteada == 2:
        return "Mande dois jogadores beberem uma dose cada."
    elif carta_sorteada == 'A':
        return "Mande um jogador beber uma dose."


def quem_bonga():
    lista_vazia = []
    print("Quem deve bongar primeiro? escreva o nome de cada participante e dps dê enter")
    omnitrix = input("1. ")
    lista_vazia.append(omnitrix)
    omnitrix = input("2. ")
    lista_vazia.append(omnitrix)
    omnitrix = input("3. ")
    lista_vazia.append(omnitrix)
    omnitrix = input("4. ")
    lista_vazia.append(omnitrix)
    random.shuffle(lista_vazia)
    print("A ordem de quem bonga primeiro é: \n 1º",lista_vazia[0],"\n 2º",lista_vazia[1],"\n 3º",lista_vazia[2],"\n 4º",lista_vazia[3])


def reboot(reiniciar):
    reiniciar = input("Reiniciar o programa? ")
    if reiniciar in ["nao","n"]:
        return '[FLORA] Okay... Desligando o sistema...'

#estetica
janela = Tk()
janela.title("Flora")
janela["bg"] = "blue"
background_image=tk.PhotoImage("eye.png")
background_label = tk.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Largura x Altura + Esquerda + Topo
janela.geometry("400x600+550+80")
h1_algo = Label(janela, text="Olá viajante!", font="calibri")
h1_algo.place(x=140,y=20,width=120, heigh=30)
h1 = Label(janela, text="Identifique-se para que eu me identifique:", width=40, heigh=3, font="calibri")
h1.place(x=60, y=50)

#itens janela1
identificacao = Label(janela, text="Seu nome:")
identificacao.place(x=80,y=150)
resposta_nome = Entry(janela)
resposta_nome.place(x=150,y=150)
butao_id = Button(janela, text="OK", command=primeiro_contato())
butao_id.place(x=280,y=145)
butao_sair = Button(janela, text='SAIR ⤬',command=quit, font="calibri") 
butao_sair.place(x=30,y=550)
janela.wm_iconbitmap('eye.ico')
"""

#roda a Flora no tkinter
janela.mainloop()


