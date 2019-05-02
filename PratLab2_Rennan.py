
##################################################################
##### UNIVERSIDADE ESTACIO DE SA                             #####
##### POS-GRADUACAO EM CIENCIA DE DADOS E BIG DATA ANALYTICS #####
##### Trabalho Pratica de Laboratorio II                     #####
##### Rennan Goncalves Sanches Correa                        #####
##### Pratica de Laboratorio II (NPG2065)                    #####
##### Tutor: Prof. Denis Goncalves Cople                     #####
##################################################################

#Criando classe de Cliente
class Cliente:

    def __init__(self, name, tel):
        self.nome = name
        self.telefone = tel

    def getCliente(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

#Criando classe de Conta do banco
class Conta(Cliente):

    def __init__(self, num, sald):
        self.numero = num
        self.saldo = float(sald)
        self.limite = float(1000.00)
        self.val_deposito = float(0.00)
        self.saldo_final = self.saldo + self.val_deposito + self.limite
        self.transacoes = []
        self.valor = float(0.00)

    def saque(self):
        val = raw_input("\nDigite o valor de saque:")
        self.valor = float(val)

        if self.valor > (self.saldo_final):
            print "\nSaldo insifuciente!\n"
        else:
            self.transacoes.append(self.valor * (-1))
            self.saldo_final = self.saldo_final - self.valor
            print "\nSaque: " + str(self.valor)
            print "\nSaldo: " + str(self.saldo_final - self.limite)
            print "\nLimite: " + str(self.limite)
            print "\nDisponivel: " + str(self.saldo_final)


    def deposito(self):
        val = raw_input("\nDigite o valor de deposito:")
        self.valor = float(val)
        self.transacoes.append(self.valor)
        self.saldo_final = self.saldo_final + self.valor
        print "\nDeposito: " + str(self.valor)
        print "\nSaldo: " + str(self.saldo_final - self.limite)
        print "\nLimite: " + str(self.limite)
        print "\nDisponivel: " + str(self.saldo_final)

    def extrato(self):
        print "\nExtrato CC No." + str(self.numero) +":"
        if len(self.transacoes) == 0:
           print "\nDeposito: " + str(self.val_deposito)
           print "\nSaque: " + str(self.valor)
           print "\nLimite: " + str(self.limite)
           print "\nDisponivel: " + str(self.saldo_final)
        else:
           i=0
           for i in range(len(self.transacoes)):
               if self.transacoes[i] >= 0.00:
                   print "\nDeposito: " + str(self.transacoes[i])
               else:
                   print "\nSaque: " + str(self.transacoes[i])

           print "\nLimite: " + str(self.limite)
           print "\nDisponivel: " + str(self.saldo_final)

#Criando classe inicial do programa
class Principal:

    def main(self):
        print "\nAcesso ao Sistema Bancario:\n"
        cad_nome = raw_input("Digite o nome do Cliente:")
        cad_telefone = raw_input("Digite o telefone do Cliente:")
        cad_conta = raw_input("Digite sua conta bancaria:")
        cad_saldo = 5000.00
        cadastro_usu = Cliente(cad_nome,cad_telefone)
        cadastro_conta = Conta(cad_conta,cad_saldo)

        print "\nConfirme seus dados de acesso:"
        print "Nome: " + cadastro_usu.nome
        print "Telefone: " + cadastro_usu.telefone
        print "Conta bancaria: " + cadastro_conta.numero
        confirma = raw_input("\nS/N:")

        if confirma.upper() == "S":
            acesso = 1
            while acesso == 1:
                opcao_menu = raw_input("Selecione uma opcao:"
                                       "\n1- Saque"
                                       "\n2- Deposito"
                                       "\n3- Extrato"
                                       "\n4-Sair\n")
                if opcao_menu == '1':
                    cadastro_conta.saque()
                elif opcao_menu == '2':
                    cadastro_conta.deposito()
                elif opcao_menu == '3':
                    cadastro_conta.extrato()
                else:
                    acesso = 0
            exit()
        else:
            exit()


#Chamando Classe Principal para inicio de programa
inicio = Principal()
inicio.main()







