import subprocess
import tkinter as tk

def start_game():
    subprocess.call(["python", "TicTacToe/game.py", str("1")])

def exibir_menu():
    def sair_do_menu():
        root.destroy()

    def start_game_dec():
        root.withdraw()  # Oculta a janela principal antes de iniciar o jogo
        start_game()
        root.deiconify()  # Reexibe a janela principal após o jogo terminar

    root = tk.Tk()
    root.title("Menu")
    root.geometry("800x600")
    cor_rgb = "#A0A0A0"  # Código RGB equivalente a (192, 192, 192)
    root.configure(bg=cor_rgb)

    botaoSair = tk.Button(root, text="Sair", fg="black", bg="red", command=sair_do_menu)
    botaoSair.pack(side='bottom')
    botaoSair.place(relx=0.5, rely=0.9, anchor='center')

    botaoSinglePlayer = tk.Button(root, text="Single Player Mode", fg="black", bg="gray", command=start_game_dec)
    botaoSinglePlayer.pack()
    
    root.mainloop()

if __name__ == "__main__":
    exibir_menu()
