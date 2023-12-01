import flet as ft
import mysql.connector
import os


clientesAgendados = []
datasAgendadas = []
domingos = (3, 10, 17, 24)



def main(pagina: ft.Page):
    pagina.title = "Barbearia RockeFelix"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    def returnPage(e):
        dataCliente.value = dataCliente.value
        horarioCliente.value = horarioCliente.value
        senhainput.value = ''
        pagina.clean()
        pagina.add(
            ft.Row([ft.Text("AGENDE SEU CORTE NO MÊS DE DEZEMBRO !")],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([nomeCliente], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([dataCliente], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([horarioCliente], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER),
            #ft.Row([botao_cadastros], alignment=ft.MainAxisAlignment.CENTER),
        )
        pagina.update()


    def btn_click(e):  # função de verificação do botao "agendar"

        if not nomeCliente.value:
            nomeCliente.error_text = "Por favor, digite seu nome!"
            pagina.update()
        else:
            nome = nomeCliente.value
            if nome in clientesAgendados:

                text_resposta = ft.Text(f"{nome} ja foi cadastrado!")
                pagina.clean()
                pagina.add(
                    ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                pagina.add(
                    ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))
                pagina.update()

            else:

                if not dataCliente.value:
                    dataCliente.error_text = "Por favor, escolha um dia!"
                    pagina.update()
                else:
                    dataCliente.value = int(dataCliente.value)
                    if dataCliente.value <= 0 or dataCliente.value > 31 or dataCliente.value == 25:

                        text_resposta = ft.Text(
                            f"Dia {dataCliente.value} não é uma data disponivel")
                        pagina.clean()
                        pagina.add(
                            ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                        pagina.add(
                            ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))
                        pagina.update()

                    elif dataCliente.value in domingos:
                        text_resposta = ft.Text(
                            f"Não abrimos aos domingos!")
                        pagina.clean()
                        pagina.add(
                            ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                        pagina.add(
                            ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))
                        pagina.update()
                    else:

                        if not horarioCliente.value:
                            horarioCliente.error_text = "Por favor, digite um horario!"
                            pagina.update()

                        else:
                            horarioCliente.value = int(horarioCliente.value)
                            if horarioCliente.value > 19 or horarioCliente.value < 9 or horarioCliente.value == 12:
                                text_resposta = ft.Text(
                                    f"Esse horario não está disponivel")
                                pagina.clean()
                                pagina.add(
                                    ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                                pagina.add(
                                    ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))
                                pagina.update()

                            else:

                                adicionarDatas = dataCliente.value, horarioCliente.value
                                if adicionarDatas in datasAgendadas:
                                    text_resposta = ft.Text(
                                        f"{horarioCliente.value}hrs está ocupado, escolha um horario vago!")
                                    pagina.clean()
                                    pagina.add(
                                        ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                                    pagina.add(
                                        ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))
                                    pagina.update()

                                else:

                                    text_resposta = ft.Text(
                                        f"Olá, {nome}. Você foi agendado para o dia {dataCliente.value} as {horarioCliente.value}:00 hrs!")
                                    pagina.clean()
                                    pagina.add(
                                        ft.Row([text_resposta], alignment=ft.MainAxisAlignment.CENTER))
                                    pagina.add(
                                        ft.Row([botao_return], alignment=ft.MainAxisAlignment.CENTER))

                                    clientesAgendados.append(nome)
                                    datasAgendadas.append(adicionarDatas)
                                    pagina.update()
                                    

    # criar os itens que queremos na pagina
    nomeCliente = ft.TextField(label="Seu Nome")
    dataCliente = ft.TextField(label="Dia (Ex: 12)")
    horarioCliente = ft.TextField(label="Horário (Ex: 13)")
    senhainput = ft.TextField(label="Password", password=True)
    botao = ft.ElevatedButton("Agendar", on_click=btn_click)
    botao_return = ft.ElevatedButton("voltar", on_click=returnPage)
    #botao_entrar = ft.ElevatedButton("entrar", on_click=entrar)
    #botao_cadastros = ft.ElevatedButton("Sou o Barbeiro", on_click=cadastros)
    # adicionar os itens na pagina

    pagina.add(
        ft.Row([ft.Text("AGENDE SEU CORTE NO MÊS DE DEZEMBRO !")],
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nomeCliente], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([dataCliente], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([horarioCliente], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER),
        #ft.Row([botao_cadastros], alignment=ft.MainAxisAlignment.CENTER),
    )
    pagina.update()





ft.app(target=main, view=ft.FLET_APP_WEB)