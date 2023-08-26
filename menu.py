import subprocess
import tkinter as tk

def start_game_multi():
    subprocess.call(["python", "TicTacToe/game.py", str("1")])
def start_game_single():
    subprocess.call(["python", "TicTacToe/game.py", str("2")])

def exibir_menu():
    def sair_do_menu():
        root.destroy()

    def start_game_m():
        root.withdraw() 
        start_game_multi()
        root.deiconify() 
    
    def start_game_s():
        root.withdraw() 
        start_game_single()
        root.deiconify() 

    root = tk.Tk()
    root.title("Menu")
    root.geometry("800x600")
    cor_rgb = "#A0A0A0"
    root.configure(bg=cor_rgb)

    botaoSair = tk.Button(root, text="Sair", fg="black", bg="red", command=sair_do_menu)
    botaoSair.pack(side='bottom')
    botaoSair.place(relx=0.5, rely=0.9, anchor='center')

    botaoMultPlayer = tk.Button(root, text="Multi Player Mode", fg="black", bg="#AECBF0", command=start_game_m)
    botaoMultPlayer.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    botaoSinglePlayer = tk.Button(root, text="Single Player Mode", fg="black", bg="#FFA54F", command=start_game_s)
    botaoSinglePlayer.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    exibir_menu()
