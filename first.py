import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome'), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Idade'), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartao?')],
            [sg.Radio('Sim', 'cartoes', key='aceitacartao'), sg.Radio('Não', 'cartoes',key='naoaceitacartao')],
            [sg.Button('Enviar', size=(10))],
        ]

        self.janela = sg.Window('Dados do usuário', layout, resizable= True)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitacartao']
            nao_aceita_cartao = self.values['naoaceitacartao']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
tela = TelaPython()
tela.Iniciar()
