import customtkinter as ctk


# # Janela
# app = ctk.CTk()
#
# app.title("Teste de janela")
# app.geometry("700x600")
#
# titulo = ctk.CTkLabel(
#     app,
#     text="Monitoramento de energia"
# )
#
# titulo.pack(pady=20)
#
#
# # Botão de Iniciar
# def iniciar():
#     print("Sistema iniciado!")
#
# botao = ctk.CTkButton(
#     app,
#     text="Iniciar",
#     command=iniciar
# )
# botao.pack(pady=10)
#
#
#
# # Caixa de Entrada
# def mostrar_nome():
#     nome = entrada.get()
#     print(nome)
#
# entrada = ctk.CTkEntry(
#     app,
#     placeholder_text="Digite seu nome"
# )
#
# entrada.pack(pady=10)
#
# botao = ctk.CTkButton(
#     app,
#     text="Enviar",
#     command=mostrar_nome
# )
#
# botao.pack(pady=10)
#
#
# # Frames
# frame = ctk.CTkFrame(app)
#
# frame.pack(
#     padx=20,
#     pady=20,
#     fill="both",
#     expand=True
# )
#
# titulo = ctk.CTkLabel(
#     frame,
#     text="ChargeGrid Intelligence"
# )
#
# titulo.pack(pady=20)
#
# app.mainloop()

import customtkinter as ctk


def iniciar():
    resultado.configure(text="Sistema iniciado!")


# Configurações
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Janela
app = ctk.CTk()

app.title("ChargeGrid Intelligence")
app.geometry("600x400")


# Título
titulo = ctk.CTkLabel(
    app,
    text="ChargeGrid Intelligence",
    font=("Arial", 24)
)

titulo.pack(pady=30)


# Campo
entrada = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Nome da estação"
)

entrada.pack(pady=10)


# Botão
botao = ctk.CTkButton(
    app,
    text="Iniciar sistema",
    command=iniciar
)

botao.pack(pady=10)


# Resultado
resultado = ctk.CTkLabel(
    app,
    text=""
)

resultado.pack(pady=20)


# Iniciar aplicação
app.mainloop()