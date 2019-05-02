

##################################################################
##### UNIVERSIDADE ESTACIO DE SA                             #####
##### POS-GRADUACAO EM CIENCIA DE DADOS E BIG DATA ANALYTICS #####
##### Trabalho Linguagem Python 2.7                          #####
##### Rennan Goncalves Sanches Correa                        #####
##### Linguagem Python 2.7 (NPG2064)                         #####
##### Tutor: Prof. Andre Luiz Braga                          #####
##################################################################

##################################################################
##### ANTES DE INICIAR A EXECUCAO DO ARQUIVO                 #####
##### O DIRETORIO "Trab_Rennan" DEVE ESTAR CRIADO            #####
##### EM C:\                                                 #####
##################################################################


import pickle

########################################################################################################################
# Definindo funcao para consulta de dados
def consultas():

    base = raw_input('\nDigite o nome do arquivo para consulta:\n')
    try:
        v_arquivo = open("C:/Trab_Rennan/" + base + ".dat", "rb")

    except:
        print("Erro ao abrir arquivo " + base + ".dat\n")
        raw_input("Pressione <Enter> para sair...")
        exit()
    opcao_cons = raw_input("\nSelecione o Tipo de consulta:\n"
                           "1-Listar Candidatos\n"
                           "2-Listar Votos por Candidatos\n"
                           "3-Listar Total de Votos por Cargo e Região\n"
                           "4-Listar Total de Votos por Regiao e Candidato\n"
                           "5-Sair\n")

    v_arquivo.seek(0,2)
    tamanho = v_arquivo.tell()
    v_arquivo.seek(0)

    cod_candidato = []
    nome = []
    cargo = []
    regiao = []
    num_votos = []

    while v_arquivo.tell() < tamanho:
        cod_candidato.append(pickle.load(v_arquivo))
        nome.append(pickle.load(v_arquivo))
        cargo.append(pickle.load(v_arquivo))
        regiao.append(pickle.load(v_arquivo))
        num_votos.append(pickle.load(v_arquivo))

    v_arquivo.close()

# Elaborando menu de opcoes
#################################################################
    if opcao_cons == '1':
        print '\nRelação de candidatos\n'
        texto = '|COD_CANDIDATO |'
        texto = texto + str('NOME').ljust(30,' ')
        texto = texto + str('|CARGO').ljust(22,' ')
        texto = texto + str('|REGIÃO').ljust(37,' ')
        #texto = texto + '|'
        print texto

        for i in range(len(cod_candidato)):
            if int(regiao[i]) == 1:
                estado = '01-Acre - AC'
            elif int(regiao[i]) == 2:
                estado = '02- Alagoas - AL'
            elif int(regiao[i]) == 3:
                estado = '03- Amapá - AP'
            elif int(regiao[i]) == 4:
                estado = '04- Amazonas - AM'
            elif int(regiao[i]) == 5:
                estado = '05- Bahia - BA'
            elif int(regiao[i]) == 6:
                estado = '06- Ceará - CE'
            elif int(regiao[i]) == 7:
                estado = '07- Distrito Federal - DF'
            elif int(regiao[i]) == 8:
                estado = '08- Espírito Santo - ES'
            elif int(regiao[i]) == 9:
                estado = '09- Goiás - GO'
            elif int(regiao[i]) == 10:
                estado = '10- Maranhão - MA'
            elif int(regiao[i]) == 11:
                estado = '11- Mato Grosso - MT'
            elif int(regiao[i]) == 12:
                estado = '12- Mato Grosso do Sul - MS'
            elif int(regiao[i]) == 13:
                estado = '13- Minas Gerais - MG'
            elif int(regiao[i]) == 14:
                estado = '14- Pará - PA'
            elif int(regiao[i]) == 15:
                estado = '15- Paraíba - PB'
            elif int(regiao[i]) == 16:
                estado = '16- Paraná - PR'
            elif int(regiao[i]) == 17:
                estado = '17- Pernambuco - PE'
            elif int(regiao[i]) == 18:
                estado = '18- Piauí - PI'
            elif int(regiao[i]) == 19:
                estado = '19- Roraima - RR'
            elif int(regiao[i]) == 20:
                estado = '20- Rondônia - RO'
            elif int(regiao[i]) == 21:
                estado = '21- Rio de Janeiro - RJ'
            elif int(regiao[i]) == 22:
                estado = '22- Rio Grande do Norte - RN'
            elif int(regiao[i]) == 23:
                estado = '23- Rio Grande do Sul - RS'
            elif int(regiao[i]) == 24:
                estado = '24- Santa Catarina - SC'
            elif int(regiao[i]) == 25:
                estado = '25- São Paulo - SP'
            elif int(regiao[i]) == 26:
                estado = '26- Sergipe - SE'
            elif int(regiao[i]) == 27:
                estado = '27- Tocantins - TO'

            print str(cod_candidato[i].ljust(15,' '))+'|'+ str(nome[i].ljust(30,' '))+'|'+ str(cargo[i].ljust(20,' '))+' |'+ str(estado.ljust(35,' '))

    ###---- CHAMA SUBMENU DE OPÇÕES ----###
        submenu_opt = raw_input('\nDigite uma das opções abaixo para continuar:\n'
                                '1- Voltar para consulta\n'
                                '2- Voltar para menu inicial\n'
                                '3- Sair do programa\n')

        if int(submenu_opt) == 1:
            return consultas()
        elif int(submenu_opt) == 2:
            return menu_inicial()
        else:
            exit()
    ###----------------------------------###

#################################################################
    elif opcao_cons == '2':
        print '\nRelação de votos por Candidato\n'
        texto = '|COD_CANDIDATO |'
        texto = texto + str('NOME').ljust(30, ' ')
        texto = texto + str('|CARGO').ljust(22, ' ')
        texto = texto + str('|NUM_VOTOS|')
        texto = texto + str('REGIÃO').ljust(37, ' ')

        print texto

        for i in range(len(cod_candidato)):
            if int(regiao[i]) == 1:
                estado = '01-Acre - AC'
            elif int(regiao[i]) == 2:
                estado = '02- Alagoas - AL'
            elif int(regiao[i]) == 3:
                estado = '03- Amapá - AP'
            elif int(regiao[i]) == 4:
                estado = '04- Amazonas - AM'
            elif int(regiao[i]) == 5:
                estado = '05- Bahia - BA'
            elif int(regiao[i]) == 6:
                estado = '06- Ceará - CE'
            elif int(regiao[i]) == 7:
                estado = '07- Distrito Federal - DF'
            elif int(regiao[i]) == 8:
                estado = '08- Espírito Santo - ES'
            elif int(regiao[i]) == 9:
                estado = '09- Goiás - GO'
            elif int(regiao[i]) == 10:
                estado = '10- Maranhão - MA'
            elif int(regiao[i]) == 11:
                estado = '11- Mato Grosso - MT'
            elif int(regiao[i]) == 12:
                estado = '12- Mato Grosso do Sul - MS'
            elif int(regiao[i]) == 13:
                estado = '13- Minas Gerais - MG'
            elif int(regiao[i]) == 14:
                estado = '14- Pará - PA'
            elif int(regiao[i]) == 15:
                estado = '15- Paraíba - PB'
            elif int(regiao[i]) == 16:
                estado = '16- Paraná - PR'
            elif int(regiao[i]) == 17:
                estado = '17- Pernambuco - PE'
            elif int(regiao[i]) == 18:
                estado = '18- Piauí - PI'
            elif int(regiao[i]) == 19:
                estado = '19- Roraima - RR'
            elif int(regiao[i]) == 20:
                estado = '20- Rondônia - RO'
            elif int(regiao[i]) == 21:
                estado = '21- Rio de Janeiro - RJ'
            elif int(regiao[i]) == 22:
                estado = '22- Rio Grande do Norte - RN'
            elif int(regiao[i]) == 23:
                estado = '23- Rio Grande do Sul - RS'
            elif int(regiao[i]) == 24:
                estado = '24- Santa Catarina - SC'
            elif int(regiao[i]) == 25:
                estado = '25- São Paulo - SP'
            elif int(regiao[i]) == 26:
                estado = '26- Sergipe - SE'
            elif int(regiao[i]) == 27:
                estado = '27- Tocantins - TO'

            print str(cod_candidato[i].ljust(15,' '))+'|'+ str(nome[i].ljust(30,' '))+'|'+ str(cargo[i].ljust(20,' '))+' |'+ str(num_votos[i].ljust(9,' '))+'|' + str(estado).ljust(35,' ')+'|'

    ###---- CHAMA SUBMENU DE OPÇÕES ----###
        submenu_opt = raw_input('\nDigite uma das opções abaixo para continuar:\n'
                                '1- Voltar para consulta\n'
                                '2- Voltar para menu inicial\n'
                                '3- Sair do programa\n')

        if int(submenu_opt) == 1:
            return consultas()
        elif int(submenu_opt) == 2:
            return menu_inicial()
        else:
            exit()
    ###----------------------------------###

#################################################################
    elif opcao_cons == '3':
        print '\nRelação de votos por Cargo e Região\n'
        texto = ' -- |COD_CANDIDATO|NOME                     |NUM_VOTOS|'

        agrupa_regiao = []
        agrupa_cargo = []
        regiao_votos = []
        cargo_votos = []

        i=0
        j=0
        k=0
        l=0
        m=0

        for i in range(len(cargo)):
            if cargo[i] not in agrupa_cargo:
                #print str(cargo[i]) + '| ' + str(num_votos[i])
                cargo_votos.append(int(num_votos[i]))
                agrupa_cargo.append(str(cargo[i]))

            else:
                index = agrupa_cargo.index(str(cargo[i]))
                cargo_votos[index] = int(num_votos[i])+ int(cargo_votos[index])

        for j in range(len(regiao)):
            if regiao[j] not in agrupa_regiao and cargo[j] in agrupa_cargo:
                #print str(regiao[i]) + '| ' + str(num_votos[i])
                regiao_votos.append(int(num_votos[j]))
                agrupa_regiao.append(str(regiao[j]))
            else:
                index = agrupa_regiao.index(str(regiao[j]))
                regiao_votos[index] = int(num_votos[j])+ int(regiao_votos[index])

        for k in range(len(agrupa_cargo)):
            ver_reg = []
            print '-'.ljust(60, '-')
            print '\nCARGO - '+ str(agrupa_cargo[k]).ljust(10, ' ')
            for l in range(len(agrupa_regiao)):
                for m in range(len(nome)):
                    #print imp
                    if (cargo[m] == agrupa_cargo[k]) and (regiao[m] == agrupa_regiao[l]):
                        if regiao[m] not in ver_reg:
                            if int(agrupa_regiao[l]) == 1:
                                estado = '01-Acre - AC'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 2:
                                estado = '02- Alagoas - AL'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 3:
                                estado = '03- Amapá - AP'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 4:
                                estado = '04- Amazonas - AM'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 5:
                                estado = '05- Bahia - BA'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 6:
                                estado = '06- Ceará - CE'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 7:
                                estado = '07- Distrito Federal - DF'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 8:
                                estado = '08- Espírito Santo - ES'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 9:
                                estado = '09- Goiás - GO'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 10:
                                estado = '10- Maranhão - MA'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 11:
                                estado = '11- Mato Grosso - MT'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 12:
                                estado = '12- Mato Grosso do Sul - MS'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 13:
                                estado = '13- Minas Gerais - MG'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 14:
                                estado = '14- Pará - PA'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 15:
                                estado = '15- Paraíba - PB'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 16:
                                estado = '16- Paraná - PR'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 17:
                                estado = '17- Pernambuco - PE'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 18:
                                estado = '18- Piauí - PI'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 19:
                                estado = '19- Roraima - RR'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 20:
                                estado = '20- Rondônia - RO'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 21:
                                estado = '21- Rio de Janeiro - RJ'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 22:
                                estado = '22- Rio Grande do Norte - RN'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 23:
                                estado = '23- Rio Grande do Sul - RS'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 24:
                                estado = '24- Santa Catarina - SC'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 25:
                                estado = '25- São Paulo - SP'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 26:
                                estado = '26- Sergipe - SE'
                                print '\n- REGIAO - ' + estado
                                print texto
                            elif int(agrupa_regiao[l]) == 27:
                                estado = '27- Tocantins - TO'
                                print '\n- REGIAO - ' + estado
                                print texto
                    if (cargo[m] == agrupa_cargo[k]) and (regiao[m] == agrupa_regiao[l]):
                        print ' -- |' + str(cod_candidato[m]).ljust(13,' ') +'|' + str(nome[m]).ljust(25, ' ') + '|' + str(num_votos[m]).ljust(9,' ') + '|'
                        ver_reg.append(regiao[m])

        ###---- CHAMA SUBMENU DE OPÇÕES ----###
        submenu_opt = raw_input('\nDigite uma das opções abaixo para continuar:\n'
                                '1- Voltar para consulta\n'
                                '2- Voltar para menu inicial\n'
                                '3- Sair do programa\n')

        if int(submenu_opt) == 1:
            return consultas()
        elif int(submenu_opt) == 2:
            return menu_inicial()
        else:
            exit()
    ###----------------------------------###

#################################################################
    elif opcao_cons == '4':
        print '\nRelação de votos por Região\n'
        texto = ' -- |COD_CANDIDATO|NOME                     |CARGO                    |NUM_VOTOS|'

        agrupa_regiao = []
        regiao_votos = []

        j=0
        k=0
        l=0
        m=0

        for j in range(len(regiao)):
            if regiao[j] not in agrupa_regiao:
                regiao_votos.append(int(num_votos[j]))
                agrupa_regiao.append(str(regiao[j]))
            else:
                index = agrupa_regiao.index(str(regiao[j]))
                regiao_votos[index] = int(num_votos[j])+ int(regiao_votos[index])

        for l in range(len(agrupa_regiao)):
            ver_reg = []
            for m in range(len(nome)):
                if (regiao[m] == agrupa_regiao[l]):
                    if regiao[m] not in ver_reg:
                        if int(agrupa_regiao[l]) == 1:
                            estado = '01-Acre - AC'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 2:
                            estado = '02- Alagoas - AL'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 3:
                            estado = '03- Amapá - AP'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 4:
                            estado = '04- Amazonas - AM'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 5:
                            estado = '05- Bahia - BA'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 6:
                            estado = '06- Ceará - CE'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 7:
                            estado = '07- Distrito Federal - DF'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 8:
                            estado = '08- Espírito Santo - ES'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 9:
                            estado = '09- Goiás - GO'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 10:
                            estado = '10- Maranhão - MA'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 11:
                            estado = '11- Mato Grosso - MT'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 12:
                            estado = '12- Mato Grosso do Sul - MS'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 13:
                            estado = '13- Minas Gerais - MG'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 14:
                            estado = '14- Pará - PA'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 15:
                            estado = '15- Paraíba - PB'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 16:
                            estado = '16- Paraná - PR'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 17:
                            estado = '17- Pernambuco - PE'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 18:
                            estado = '18- Piauí - PI'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 19:
                            estado = '19- Roraima - RR'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 20:
                            estado = '20- Rondônia - RO'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 21:
                            estado = '21- Rio de Janeiro - RJ'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 22:
                            estado = '22- Rio Grande do Norte - RN'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 23:
                            estado = '23- Rio Grande do Sul - RS'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 24:
                            estado = '24- Santa Catarina - SC'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 25:
                            estado = '25- São Paulo - SP'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 26:
                            estado = '26- Sergipe - SE'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                        elif int(agrupa_regiao[l]) == 27:
                            estado = '27- Tocantins - TO'
                            print '-'.ljust(80, '-')
                            print '\n- REGIAO - ' + estado + ' - TOTAL DE VOTOS - ' + str(regiao_votos[l])
                            print texto
                if (regiao[m] == agrupa_regiao[l]):
                    print ' -- |' + str(cod_candidato[m]).ljust(13,' ') +'|' + str(nome[m]).ljust(25, ' ') + '|' + str(cargo[m]).ljust(25,' ') + '|' + str(num_votos[m]).ljust(9,' ') + '|'
                    ver_reg.append(regiao[m])

        ###---- CHAMA SUBMENU DE OPÇÕES ----###
        submenu_opt = raw_input('\nDigite uma das opções abaixo para continuar:\n'
                                '1- Voltar para consulta\n'
                                '2- Voltar para menu inicial\n'
                                '3- Sair do programa\n')

        if int(submenu_opt) == 1:
            return consultas()
        elif int(submenu_opt) == 2:
            return menu_inicial()
        else:
            exit()
    ###----------------------------------###

#################################################################
    elif opcao_cons == 5:
        exit()

########################################################################################################################

# Definindo funcao para cadastrar dados no arquivo binario
def cadastrar_dados():
    nom_arq = raw_input("Digite o nome do arquivo:\n")
    try:
        arquivo = open("C:/Trab_Rennan/"+nom_arq+".dat","ab")

    except:
        print("Erro ao abrir arquivo "+nom_arq+".dat\n")
        raw_input("Pressione <Enter> para sair...")
        exit()

    controle=1

    while (controle >0):
        cod_candidato = raw_input("\nDigite o código do candidato:")
        nome = raw_input("\nDigite o nome do candidato:")
        print '\nSelecione o cargo do candidato:\n1-Governador\n2-Prefeito\n3-Deputado Estadual\n4-Vereador'
        cargo = raw_input("\nCargo:")
        print 'Código de Região:\n'
        print '01- Acre – AC		      10- Maranhão – MA				19- Roraima – RR\n02- Alagoas – AL		  11- Mato Grosso – MT			20- Rondônia – RO\n03- Amapá – AP		      12- Mato Grosso do Sul – MS	21- Rio de Janeiro – RJ\n04- Amazonas – AM	      13- Minas Gerais – MG			22- Rio Grande do Norte – RN\n05- Bahia – BA		      14- Pará – PA				    23- Rio Grande do Sul – RS\n06- Ceará – CE		      15- Paraíba – PB				24- Santa Catarina – SC\n07- Distrito Federal – DF 16- Paraná – PR			    25- São Paulo – SP\n08- Espírito Santo – ES	  17- Pernambuco – PE	        26- Sergipe – SE\n09- Goiás – GO			  18- Piauí – PI				27- Tocantins – TO\n'
        regiao = raw_input("\nDigite o código da região do candidato:")
        num_votos = raw_input("\nDigite a quantidade de votos do candidato:")

        if str(cargo) == '1':
            cod_cargo = 'Governador'
        elif str(cargo) == '2':
            cod_cargo = 'Prefeito'
        elif str(cargo) == '3':
            cod_cargo = 'Deputado Estadual'
        elif str(cargo) == '4':
            cod_cargo = 'Vereador'

        dados = [cod_candidato,nome,cod_cargo,regiao,num_votos]
        #print(dados)
        conf_dados =raw_input("Confirma dados? (S/N)\n")

        if conf_dados.upper() == "S":
            pickle.dump(cod_candidato,arquivo)
            pickle.dump(nome.upper(),arquivo)
            pickle.dump(cod_cargo.upper(),arquivo)
            pickle.dump(regiao,arquivo)
            pickle.dump(num_votos,arquivo)
            print "Dados gravados com sucesso!\n"
            conf_dados = raw_input("Cadastrar novos dados? (S/N)\n")
            if conf_dados.upper() == "S":
                controle = 1
            else:
                arquivo.close()
                controle = controle - 1
        else:
            conf_dados = raw_input("Cadastrar novos dados? (S/N)\n")
            if conf_dados.upper() == "S":
                controle = 1
            else:
                arquivo.close()
                controle = controle - 1

    return menu_inicial()
########################################################################################################

# Criando Menu Inicial de Opcoes
def menu_inicial():
    menu_principal = raw_input("\nSelecione uma das opções abaixo:\n"
                                  "1- Cadastrar dados de candidatos\n"
                                  "2- Consultar dados de candidatos\n"
                                  "3- Sair do programa\n")

    if int(menu_principal) == 1:
        return cadastrar_dados()
    elif int(menu_principal) == 2:
        return consultas()
    else:
        exit()

########################################################################################################

####------ INICIANDO PROGRAMA -------####
menu_inicial()





