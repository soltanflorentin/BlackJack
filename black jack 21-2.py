import random
import time
credit = 100
miza = 0
loop1 = 1
while True:
    while loop1 == 1:
        print("_"*20)
        pachet_carti = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14] * 4
        credit = credit + miza
        def miza_joc():
            while 1 == 1:
                miza = int(input("Bet between 1 and 10: "))
                if 0 >miza > 10:
                    print("Upss, is not between 1 and 10")
                    continue
                elif miza>credit:
                    print("Bet bigger than credit!!!")
                    continue
                return miza
        print("Credit: " + str(credit))
        miza = miza_joc()
        print("Bet: " + str(miza))
        credit = credit - miza

        def verifica_carti_cpu(x):
            while True:
                if x[0]==1 and x[1]==1 and len(x)==2:
                    x=[11,1]
                    return x
                if 1 in x:
                    if (10 in x or 12 in x or 13 in x or 14 in x) and len(x)==2:
                        for i in range(len(x)):
                            if x[i] > 11: x[i] = 10
                            if x[i]==1: x[i]=11
                        return x
                    else:
                        for i in range(len(x)):
                            if x[i] > 11:
                                x[i] = 10
                        for i in range(len(x)):
                            if x[i] ==11 and sum(x)>21:
                                x[i]=1
                                return x
                        for i in range(len(x)):
                            if x[i] == 1 and (sum(x) == 8 or sum(x) == 9 or sum(x) == 10 or sum(x) == 11):
                                x[i] = 11
                                return x
                for i in range(len(x)):
                    if x[i] > 11:
                        x[i] = 10
                return x


        def verifica_carti_pl(x):
            if x[0]==1 and x[1]==1 and len(x)==2:
                x=[11,1]
                return x
            if (1 or 11) in x:
                if (10 in x or 12 in x or 13 in x or 14 in x) and len(x)==2 :
                        print("Blackjack!!!")
                        return "blackjack"
                else:
                    for i in range(len(x)):
                        if x[i]>11: x[i]=10
                    print("Player:",x,"-",sum(x),"\n","Cpu: ", cpu_doua_carti[0], "?")
                    while True:
                        if 1 in x and sum(x)>11:
                            return x
                        intrebare_as = input("A: 1 or 11? ")
                        if intrebare_as.isalpha():
                            continue
                        if intrebare_as == str(11):
                            for i in range(len(x)):
                                    if x[i] == 1:
                                        x[i] = 11
                                        print(x)
                                        return x
                        elif intrebare_as == str(1):
                            for i in range(len(x)):
                                if x[i] == 11: x[i] = 1
                                return x
            for i in range(len(x)):
                if x[i] > 11:
                    x[i] = 10
            return x

        def doua_carti(z):
            carte_1 = random.choice(z)
            carte_2 = random.choice(z)
            return carte_2, carte_1

        # Cpu
        cpu_doua_carti = doua_carti(pachet_carti)
        cpu_doua_carti = list(cpu_doua_carti)
        carti_cpu_copy = cpu_doua_carti.copy()
        pachet_carti.remove(cpu_doua_carti[0])
        pachet_carti.remove(cpu_doua_carti[1])
        suma_cpu=sum(verifica_carti_cpu(carti_cpu_copy))
        # Player
        player_2_carti = doua_carti(pachet_carti)
        pachet_carti.remove(player_2_carti[0])
        pachet_carti.remove(player_2_carti[1])
        player_2_carti = list(player_2_carti)
        player_2_carti_copy = player_2_carti.copy()
        primele_2_carti_triate = verifica_carti_pl(player_2_carti_copy)


        if primele_2_carti_triate == "blackjack":
            miza = miza * 2.5
            print("Player: ",player_2_carti)
            break
        suma_player = sum(primele_2_carti_triate)
        print("Player: ", player_2_carti, "=", suma_player,"\n"+"Cpu: ", cpu_doua_carti[0], "?")

        def mai_da_o_carte_da(x):
            player_inca_o_carte = random.choice(pachet_carti)
            player_3_carti = list(x)
            player_3_carti.append(player_inca_o_carte)
            pachet_carti.remove(player_3_carti[2])
            carti = player_3_carti.copy()
            trei_carti_triate = verifica_carti_pl(carti)
            suma_player = sum(trei_carti_triate)
            print("Player: ", player_3_carti, "=", suma_player)

            if suma_player > 21:
                print("You lost !!!")
                return False
            return player_3_carti,suma_player

        def mai_da_o_carte_nu(x):
             carti_cpu_triate = verifica_carti_cpu(x)
             suma_cpu = sum(carti_cpu_triate)
             if suma_cpu > 21: return True
             if suma_cpu==21: return x,suma_cpu
             while suma_cpu < 17 or suma_player == suma_cpu or suma_cpu < suma_player:
                 if suma_cpu > suma_player and suma_cpu != suma_player: break
                 inca_o_carte_cpu = random.choice(pachet_carti)
                 pachet_carti.remove(inca_o_carte_cpu)
                 x.append(inca_o_carte_cpu)
                 cpu_mai_multe_carti = x.copy()
                 carti_cpu_triate = verifica_carti_cpu(cpu_mai_multe_carti)
                 suma_cpu = sum(carti_cpu_triate)
             print("Player: ", player_2_carti, "=", suma_player, "\n" + "Cpu: ",x, "=", suma_cpu)
             return x,suma_cpu

        def cine_castiga(pl, cpu):
            if pl > 21:
                return False  # pt pierdut
            elif cpu > 21:
                return True  # pt castig
            elif pl < cpu:
                return False # pt pierdut
            elif pl > cpu:
                return True  # pt castig

     # prima carte
        while True:
            player_inca_o_carte_sau_nu = input("One more card? Y/N? ")
            if player_inca_o_carte_sau_nu == "y":
                da=mai_da_o_carte_da(player_2_carti)
                if not da:
                    miza=0
                    break
                suma_player = da[1]
                player_2_carti = da[0]
                if suma_player==21:
                    pass
                else:
                    continue
            elif player_inca_o_carte_sau_nu == "n":
                nu=mai_da_o_carte_nu(cpu_doua_carti)
                if nu==True:
                    print("You win!!!")
                    miza*=2
                    break
                suma_cpu = nu[1]
                cpu_doua_carti = nu[0]
 # verificam cine castiga in def cine_castiga
            if suma_player==21 and suma_cpu==21:
                print("Draw!!!")
                break
            if cine_castiga(suma_player, suma_cpu):
                miza = miza * 2
                print("You win !!! :)")
                break
            elif not cine_castiga(suma_player, suma_cpu):
                print("You lost !!! :(")
                miza = 0
                break


