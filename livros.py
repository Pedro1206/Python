import os
from tkinter import Frame
import PySimpleGUI as sg

tema = "SystemDefault"


def caminho():
        #layout
        sg.theme(tema)

        
        layout = [
            [sg.Text('COLOCAR O CAMINHO ABAIXO | EXEMPLO: D:\\BACKUP\\LIVROS\\257 ', size=(100,1))] ,
            [sg.Input(size=(100,1), key="CAMINHO")],
            [sg.Button("Enviar", size=(20,1))],
        ]

        #janela
        janela = sg.Window("RENOMEAR LIVRO DE NOTAS").layout(layout)

        event, values = janela.read()

        caminho_livro = values["CAMINHO"]
        
        janela.Close()
        return caminho_livro

def renomear_arquivos_intercalando(pasta):
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(pasta)

    # Inicializa um contador
    contador = 1
    contador2 = 1
    contador3 = 1

    for arquivo in arquivos:
        # Verifica se o item é um arquivo (não é um diretório)
        if os.path.isfile(os.path.join(pasta, arquivo)):
            # Obtém a extensão do arquivo, se houver
            nome, extensao = os.path.splitext(arquivo)

            # Define o novo nome do arquivo
            if contador % 2 == 1:
                novo_nome = f"{contador3}"
                contador3 += 1
            elif contador % 2 == 0:
                novo_nome = f"{contador2}-{contador2}"
                contador2 += 1
                

            novo_nome += extensao

            # Renomeia o arquivo
            os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))

            # Incrementa o contador
            contador += 1

if __name__ == "__main__":
    # Substitua 'caminho_para_sua_pasta' pelo caminho da pasta que deseja renomear os arquivos
    caminho_livro = caminho()
    pasta = caminho_livro

    renomear_arquivos_intercalando(pasta)
