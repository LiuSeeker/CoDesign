import json
from random import randint
from math import sqrt
from math import exp

#mostra dados do seu pokemon
def poke_stats():
    ins_poke = input("""
    /------------------------------\ 
    |    Qual pokémon deseja
    |    inspecionar?
    \------------------------------/
          > """)
    try:
        i = int(ins_poke) - 1
        if i > len(seus_poke) - 1 or i < 0:
            print_invalido()
        else:
            poke_escolhido = seus_poke[i]["nome"]
            level_poke_escolhido = ver_level(poke_escolhido)
            vida_poke_escolhido = vida(poke_escolhido,level_poke_escolhido,\
                                       iv_poke_escolhido[0])
            atk_poke_escolhido = atk(poke_escolhido,level_poke_escolhido,\
                                     iv_poke_escolhido[1])
            def_poke_escolhido = defe(poke_escolhido,level_poke_escolhido,\
                                      iv_poke_escolhido[2])
            speed_poke_escolhido = spd(poke_escolhido,level_poke_escolhido,\
                                       iv_poke_escolhido[3])
            print("""
    /------------------------------\ 
    |    {}
    |    Level: {}
    |    Vida: {}
    |    Ataque: {}
    |    Defesa: {}
    |    Velocidade: {}
    \------------------------------/
    """ .format(poke_escolhido.title(),level_poke_escolhido,\
                vida_poke_escolhido,atk_poke_escolhido,\
                def_poke_escolhido,speed_poke_escolhido))
    except ValueError:
        print_invalido()


#mostra dados do pokemon selvagem
def ins_poke_2():
    for i in range(len(allpoke)):
        if wild_poke in allpoke[i]["nome"]:
            print("""
    /------------------------------\ 
    |    {}
    |    Ataque: {}
    |    Defesa: {}
    |    Velocidade: {}
    \------------------------------/
    """ .format(wild_poke.title(),allpoke[i]["poder"],\
                allpoke[i]["defesa"],allpoke[i]["speed"]))

#rand um pokemon e calcula sua chance de aparecer
def poke_enc():
    num = randint(1, len(allpoke))
    for e in range(len(allpoke)):
        if allpoke[e]["id"] == num:
            wild_poke = allpoke[e]["nome"]
            prob = randint(1, 100)
            if prob <= allpoke[e]["chance"]:
                return wild_poke
            else:
                return False

#retorna elemento vida do dic
def vida(poke, level, iv):
    for j in range(len(allpoke)):
            if allpoke[j]["nome"] == poke:
                vida_poke = int((((allpoke[j]["vida"]+iv)*2+(sqrt(25600)/4)*\
                                  level)/100)+level+10)
                return vida_poke

#retorna elemento defesa do dic
def defe(poke, level, iv):
    for j in range(len(allpoke)):
            if allpoke[j]["nome"] == poke:
                def_poke = int((((allpoke[j]["defesa"]+iv)*2+(sqrt(25600)/4)\
                                 *level)/100)+5)
                return def_poke

#retorna elemento ataque do dic
def atk(poke, level, iv):
    for j in range(len(allpoke)):
            if allpoke[j]["nome"] == poke:
                atk_poke = int((((allpoke[j]["poder"]+iv)*2+(sqrt(25600)/4)\
                                 *level)/100)+5)
                return atk_poke

#retorna elemento velocidade do dic
def spd(poke, level, iv):
    for j in range(len(allpoke)):
        if allpoke[j]["nome"] == poke:
            spd_poke = int((((allpoke[j]["speed"]+iv)*2+(sqrt(25600)/4)*level)/\
                             100)+5)
            return spd_poke

#calcula dano do seu poke
def calc_dano_poke_escolhido():
    crit = critico(speed_poke_escolhido)
    dano_poke = int(((2*level_poke_escolhido/5+2)\
                     *atk_poke_escolhido/def_wild+2)\
                    *randint(85,100)/100*crit)
    if crit == 2:
        print("""
    /------------------------------\ 
    |    Seu {} critical hit!
    \------------------------------/""" .format(poke_escolhido))
    return dano_poke

#calcula dano do poke selvagem
def calc_dano_wild():
    crit = critico(speed_wild)
    dano_wild = int(((2*level_wild/5+2)*atk_wild/def_poke_escolhido+2)\
                    *randint(85,100)/100*crit)
    if crit == 2:
        print("""
    /------------------------------\ 
    |    {} critical hit!
    \------------------------------/""" .format(wild_poke.title()))
    return dano_wild

#resultados da vitoria
def win():
    print("""
    /------------------------------\ 
    |    {} desmaiou!
    |    Você ganhou a batalha!
    |    {} ganhou {} exp!
    \------------------------------/
            """ .format(wild_poke.title(), poke_escolhido, calc_exp()))
    for i in range(len(allpoke)):
        if allpoke[i]["nome"] == wild_poke:
            ids = allpoke[i]["id"]
    if ids not in pokedex:
        pokedex.append(ids)
    for j in range(len(seus_poke)):
        if seus_poke[j]["nome"] == poke_escolhido:
            seus_poke[j]["exp"] += calc_exp()
            new_level = ver_level(poke_escolhido)
            if new_level != level_poke_escolhido:
                print("""
    /------------------------------\ 
    |    Seu {} subiu de nível!
    \------------------------------/
    """.format(poke_escolhido))

#resultados da derrota
def loss():
    print("""
    /------------------------------\ 
    |    Seu pokémon desmaiou!
    |    Fugindo da batalha...
    \------------------------------/
            """)

#auto explicativo
def print_dano_poke_escolhido():
    print("""
    /------------------------------\ 
    |    Seu {} deu {} de dano
    \------------------------------/
    """ .format(poke_escolhido, dano_poke_escolhido))

#auto explicativo
def print_dano_wild_poke():
    print("""
    /------------------------------\ 
    |    {} deu {} de dano
    \------------------------------/
    """ .format(wild_poke, dano_wild))

#aut explicativo
def print_invalido():
    print("""
    /------------------------------\ 
    |    Comando inválido
    \------------------------------/
            """)

#calcula exp
def calc_exp():
    for j in range(len(allpoke)):
            if allpoke[j]["nome"] == wild_poke:
                exp_base = allpoke[j]["exp_base"]
    exp = level_wild*exp_base/7
    return int(exp)

#calcula o level do poke selvagem
def calc_level_wild():
    for j in range(len(allpoke)):
        if allpoke[j]["nome"] == wild_poke:
            chance = allpoke[j]["chance"]
    level_var = int(((100-chance)/10+level_poke_escolhido/3)/2)
    if chance >= 60:
        a = randint(0, level_var)
        level_wild = level_poke_escolhido - a
    elif chance < 60 and chance >= 40:
        b = randint(-level_var, level_var)
        level_wild = level_poke_escolhido + b
        if level_wild >= 100:
            level_wild = 100
    elif chance < 40 and chance >= 20:
        d = randint(0, level_var)
        level_wild = level_poke_escolhido + 1.4*d
        if level_wild >= 100:
            level_wild = 100
    else:
        c = randint(0, level_var)
        level_wild = level_poke_escolhido + 1.8*c
        if level_wild >= 100:
            level_wild = 100
    return int(level_wild)

#auto explicativo
def fuga():
    a = randint(1,100)
    if a < 5:
        print("""
    /------------------------------\ 
    |    Não conseguiu fugir!
    \------------------------------/
            """)
        return False
    else:
        print("""
    /------------------------------\ 
    |    Fugiu com sucesso!
    \------------------------------/
            """)
        return True

#mostra pokedex
def ver_pokedex():
    if len(pokedex) == 0:
        print("""
    /------------------------------\ 
    |    Pokédex vazia!
    \------------------------------/
            """)
    else:
        print("""
    /------------------------------\ 
    |    Pokédex:
    |""")
        for i in range(len(pokedex)):
            ids = pokedex[i]
            for j in range(len(allpoke)):
                if allpoke[j]["id"] == ids:
                    nome = allpoke[j]["nome"]
            print("""    |    #{}: {}""" .format(ids, nome.title()))
        print("""    \------------------------------/
            """)

#pega o elemento da chave "exp" e transforma em level
def ver_level(poke):
    for j in range(len(seus_poke)):
        if seus_poke[j]["nome"] == poke:
            exp = seus_poke[j]["exp"]
    if exp >= 100 and exp < 172:
        level = 5
    if exp >= 172 and exp < 274:
        level = 6
    elif exp >= 274 and exp < 409:
        level = 7
    elif exp >= 409 and exp < 583:
        level = 8
    elif exp >= 583 and exp < 800:
        level = 9
    elif exp >= 800 and exp < 1064:
        level = 10
    elif exp >= 1064 and exp < 1382:
        level = 11
    elif exp >= 1382 and exp < 1757:
        level = 12
    elif exp >= 1757 and exp < 2195:
        level = 13
    elif exp >= 2195 and exp < 2700:
        level = 14
    elif exp >= 2700 and exp < 3276:
        level = 15
    elif exp >= 3276 and exp < 3930:
        level = 16
    elif exp >= 3930 and exp < 4665:
        level = 17
    elif exp >= 4665 and exp < 5487:
        level = 18
    elif exp >= 5487 and exp < 6400:
        level = 19
    elif exp >= 6400 and exp < 7408:
        level = 20
    elif exp >= 7408 and exp < 8518:
        level = 21
    return level

#auto explicatvo
def print_seus_poke():
    for i in range(len(seus_poke)):
        print(
"""    |    ({}) {}""".format(i+1, seus_poke[i]["nome"].title()))

#probabilidade crítico
def critico(speed):
    p = speed/2
    a = randint(0,256)
    mod = 2
    smod = 1
    if a < p:
        return mod
    else:
        return smod

#auto explicativo
def print_linha():
    print("===========================================")

#cria o iv
def rand_iv():
    total = 15
    l = []
    while len(l) <= 4:
        r = randint(0, total)
        l.append(r)
    return l
      
with open("poke.json") as arq:
    allpoke = json.load(arq)
#Ex como usar ESSE json(lista de dic): (allpoke[i]["nome"]) = "nome do poke"

###############################################
    
print("""
    /------------------------------\ 
    |    Bem vindo ao Inspérmon!
    \------------------------------/
            """)

#loop do load
loop_tipo = 1
while loop_tipo == 1:
    tipo = input("""
    /------------------------------\ 
    |    (1) Novo jogo
    |    (2) Carregar jogo
    \------------------------------/
          > """)
    
    #novo jogo
    if tipo == "1":
        pokedex = []
        with open("seupoke.json") as arq2:
            seus_poke = json.load(arq2)
        loop_tipo = 0

    #carrega jogo
    elif tipo == "2":
        with open("save.json") as arq2:
            seus_poke = json.load(arq2)
        with open("pokedex_save.json") as pokedex:
            pokedex = json.load(pokedex)
        loop_tipo = 0
        
    else:
        print_invalido()
        print_linha()
            
#loop jogo
loop_jogo = 1
iv_poke_escolhido = rand_iv()
poke_escolhido = "nd"

while loop_jogo == 1:
    pokedex.sort()
    print_linha()
    comando = input("""
    /------------------------------\ 
    |    O que deseja fazer?
    |
    |    (1) Passear
    |    (2) Ver pokédex
    |    (3) Inspecionar seus pokémons
    |    (4) Salvar jogo
    |    (5) Dormir
    \------------------------------/
          > """)

    #escolha do pokemon
    if comando == "1":
        passeio = 1
        print_linha()
        print("""
    /------------------------------\ 
    |    Com qual pokémon?""")
        print_seus_poke()
        print(
"""    \------------------------------/""")
        poke_escolhido = input("""
          > """)
        try:
            poke_escolhido = int(poke_escolhido)
            
            if poke_escolhido >= 1 and poke_escolhido <= len(seus_poke):
                poke_escolhido = seus_poke[poke_escolhido-1]["nome"]

                #loop passeio
                while passeio == 1:

                    #loop encontro batalha
                    loop_enc_batalha = 1
                    while loop_enc_batalha == 1:

                        #status do seu pokemon
                        level_poke_escolhido = ver_level(poke_escolhido)
                        vida_poke_escolhido = vida(poke_escolhido,\
                                                   level_poke_escolhido,\
                                                   iv_poke_escolhido[0])
                        atk_poke_escolhido = atk(poke_escolhido,\
                                                 level_poke_escolhido,\
                                                 iv_poke_escolhido[1])
                        def_poke_escolhido = defe(poke_escolhido,\
                                                  level_poke_escolhido,\
                                                  iv_poke_escolhido[2])
                        speed_poke_escolhido = spd(poke_escolhido,\
                                                   level_poke_escolhido,\
                                                   iv_poke_escolhido[3])

                        #chance de aparecimento
                        wild_poke = poke_enc()
                        if wild_poke == False:
                            break
                        else:

                            #status pokemon selvagem
                            iv_wild_poke = rand_iv()
                            level_wild = calc_level_wild()
                            vida_wild = vida(wild_poke, level_wild,\
                                             iv_wild_poke[0])
                            atk_wild = atk(wild_poke, level_wild,\
                                           iv_wild_poke[1])
                            def_wild = defe(wild_poke, level_wild,\
                                            iv_wild_poke[2])
                            speed_wild = spd(wild_poke, level_wild,\
                                             iv_wild_poke[3])

                            #loop da pergunta da batalha
                            loop_perg_batalha = 1
                            while loop_perg_batalha == 1:
                                print_linha()
                                perg_batalha = input("""
    /------------------------------\ 
    |    Encontrou {} nv. {}!
    |    Deseja Batalhar?
    |
    |    (1) Sim
    |    (2) Não
    |    (3) Parar passeio
    \------------------------------/
          > """ .format(wild_poke, level_wild))

                                #batalha
                                if perg_batalha == "1":
                                    loop_enc_batalha = 0
                                    loop_perg_batalha = 0
                                    while vida_wild or vida_poke_escolhido > 0:
                                        print_linha()
                                        print("""
    /------------------------------\ 
    |    Vida seu {}: {}
    |    Vida {}: {}
    \------------------------------/
            """ .format(poke_escolhido, vida_poke_escolhido, \
                        wild_poke, vida_wild))

                                        #ataque
                                        batalha = input("""
    /------------------------------\ 
    |    (1) Atacar
    |    (2) Fugir
    |    (3) Inspecionar pokémon
    \------------------------------/
          > """)
                                        if batalha == "1":

                                            #se seu poke é mais rapido
                                            if speed_poke_escolhido >=\
                                                   speed_wild:
                                                dano_poke_escolhido =\
                                                    calc_dano_poke_escolhido()
                                                print_linha()
                                                print_dano_poke_escolhido()
                                                vida_wild = vida_wild -\
                                                            dano_poke_escolhido
                                                if vida_wild <= 0:
                                                    print_linha()
                                                    win()
                                                    break
                                                dano_wild = calc_dano_wild()
                                                print_dano_wild_poke()
                                                vida_poke_escolhido =\
                                                    vida_poke_escolhido - \
                                                    dano_wild
                                                if vida_poke_escolhido <= 0:
                                                    print_linha()
                                                    loss()
                                                    passeio = 0
                                                    break

                                            #se poke selvagem é mais rapido
                                            else:
                                                dano_wild = calc_dano_wild()
                                                print_linha()
                                                print_dano_wild_poke()
                                                vida_poke_escolhido =\
                                                    vida_poke_escolhido - \
                                                    dano_wild
                                                if vida_poke_escolhido <= 0:
                                                    print_linha()
                                                    loss()
                                                    passeio = 0
                                                    break
                                                dano_poke_escolhido =\
                                                    calc_dano_poke_escolhido()
                                                print_dano_poke_escolhido()
                                                vida_wild = vida_wild -\
                                                            dano_poke_escolhido
                                                if vida_wild <= 0:
                                                    print_linha()
                                                    win()
                                                    loop_enc_batalha = 0
                                                    break

                                        #fuga durante a batalha
                                        elif batalha == "2":
                                            if fuga() == True:
                                                break
                                            else:
                                                dano_wild = calc_dano_wild()
                                                print_linha()
                                                print_dano_wild_poke()
                                                vida_poke_escolhido =\
                                                    vida_poke_escolhido\
                                                    - dano_wild
                                                if vida_poke_escolhido <= 0:
                                                    loss()
                                                    passeio = 0
                                                    break
                                                
                                        #inspeciona poke selvagem
                                        elif batalha == "3":
                                            print_linha()
                                            ins_poke_2()
                                        else:
                                            print_invalido()

                                #fuga antes da batalha
                                elif perg_batalha == "2":
                                    loop_enc_batalha = 0
                                    loop_perg_batalha = 0

                                #para passeio
                                elif perg_batalha == "3":
                                    loop_enc_batalha = 0
                                    loop_perg_batalha = 0
                                    passeio = 0
                                else:
                                    loop_enc_batalha = 0
                                    print_invalido()
            else:
                print_invalido()
        except ValueError:
            print_invalido()
            
    #mostra pokedex
    elif comando == "2":
        ver_pokedex()

    #mostra seus pokemons
    elif comando == "3":
        print_linha()
        print("""
    /------------------------------\ 
    |    Seus pokémons:""")
        print_seus_poke()
        print(
"""    \------------------------------/""")
        poke_stats()

    #save
    elif comando == "4":
        print_linha()
        ctz = input("""
    /------------------------------\ 
    |    O novo save apagará o
    |    save anterior.
    |    Deseja realmente salvar?
    |
    |    (1) Sim
    |    (2) Não
    \------------------------------/
          > """)
        if ctz == "1":
            if poke_escolhido == "nd":
                print("""
    /------------------------------\ 
    |    Nada para salvar!
    \------------------------------/""")

            #cria uma lsta de dicionarios para salvar
            else:
                list_save = [{}]
                for j in range(len(seus_poke)):
                    list_save[j]["nome"] = seus_poke[j]["nome"]
                    list_save[j]["exp"] = seus_poke[j]["exp"]
                    list_save[j]["id"] = seus_poke[j]["id"]
                    list_save[j]["vida"] = seus_poke[j]["vida"]
                    list_save[j]["poder"] = seus_poke[j]["poder"]
                    list_save[j]["defesa"] = seus_poke[j]["defesa"]
                    list_save[j]["chance"] = seus_poke[j]["chance"]
                    list_save[j]["speed"] = seus_poke[j]["speed"]
                with open("save.json", "w") as save1:
                    json.dump(list_save, save1)
                #salva a pokedex
                with open("pokedex_save.json", "w") as save2:
                    json.dump(pokedex, save2)
                print("""
    /------------------------------\ 
    |    Jogo salvo com sucesso!
    \------------------------------/""")
        elif ctz == "2":
            False
        else:
            print_invalido()
        
    #sai do programa
    elif comando == "5":
        print_linha()
        print("Dormindo... Até a próxima!")
        loop_jogo = 0
    else:
        print_invalido()
