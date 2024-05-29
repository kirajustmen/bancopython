class Conta:
    def __init__(self, usuario, saldo):
        self.usuario = usuario
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        print(f'Saldo atual: R${self.saldo:.2f}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            print(f'Saldo atual: R${self.saldo:.2f}')
        else:
            print('Saldo insuficiente.')

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, taxa):
        super().__init__(titular, saldo)
        self.taxa = taxa

    def sacar_com_taxa(self, valor):
        valor_total = valor + self.taxa
        super().saque(valor_total)
        print(f'Taxa de R${self.taxa:.2f} aplicada.')

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        self.juros = juros

    def resgate(self, valor):
        super().saque(valor)
        print(f'Resgate de R${valor:.2f} realizado.')

    def aplicar_juros(self):
        self.saldo += self.saldo * self.juros
        print(f'Juros aplicados. Saldo atual: R${self.saldo:.2f}')


def criar_conta(tipo_conta, titular, saldo_inicial):
    if tipo_conta == 'corrente':
        return ContaCorrente(titular, saldo_inicial, taxa=2.0)
    elif tipo_conta == 'poupanca':
        return ContaPoupanca(titular, saldo_inicial, juros=0.05)
    else:
        print('Tipo de conta inválido.')
        return None

def mostrar_menu():
    print("======= Menu =======")
    print("1. Criar Conta")
    print("2. Depósito")
    print("3. Saque")
    print("4. Resgate (Conta Poupança)")
    print("5. Aplicar Juros (Conta Poupança)")
    print("6. Sair")

def main():
    contas = []

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo_conta = input("Digite o tipo de conta ( 1.corrente ou 2.poupanca): ")
            titular = input("Digite o nome do titular da conta: ")
            saldo_inicial = float(input("Digite o valor do deposito inicial da conta: "))
            conta = criar_conta(tipo_conta, titular, saldo_inicial)
            if conta:
                contas.append(conta)
                print("Conta criada com sucesso!")
        elif opcao == "2":
            # Depósito
            pass
        elif opcao == "3":
            # Saque
            pass
        elif opcao == "4":
            # Resgate (Conta Poupança)
            pass
        elif opcao == "5":
            # Aplicar Juros (Conta Poupança)
            pass
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()