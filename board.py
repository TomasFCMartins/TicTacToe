import tkinter as tk
from tkinter import PhotoImage

gameArray=[0, 0, 0, 0, 0, 0, 0, 0, 0]
number = 0
imagens = []
screen_width = 0
screen_height = 0
winner_found = False
def play(event):
    x = event.x
    y = event.y
    spotx = -1
    spoty = -1
    spot = 0
    global number, winner_found
    if x < width/3:
        if y < height/3:
            spotx = 0
            spoty = 0
            spot = 0
        elif y > height/3 and y < height*2/3:
            spotx = 0
            spoty = 1
            spot = 1
        elif y > height*2/3 and y < height:
            spotx = 0
            spoty = 2
            spot = 2
    elif x > width/3 and x < width*2/3:
        if y < height/3:
            spotx = 1
            spoty = 0
            spot = 3
        elif y > height/3 and y < height*2/3:
            spotx = 1
            spoty = 1
            spot = 4
        elif y > height*2/3 and y < height:
            spotx = 1
            spoty = 2
            spot = 5
    elif x > width*2/3 and x < width:
        if y < height/3:
            spotx = 2
            spoty = 0
            spot = 6
        elif y > height/3 and y < height*2/3:
            spotx = 2
            spoty = 1
            spot = 7
        elif y > height*2/3 and y < height:
            spotx = 2
            spoty = 2
            spot = 8
    
    if gameArray[spot] == 0:
        if number % 2 == 0:
            gameArray[spot] = 1
            placeImg(spotx, spoty, 1)
        else:
            gameArray[spot] = 2
            placeImg(spotx, spoty, 2)
        number = number+1
    
    else:
        print("Choose an empty spot to play.")
    if verifyWinner() and winner_found == False:
        if number%2 == 0:
            winner = "The winner is O!"
            color = "blue"
        else:
            winner = "The winner is X!"
            color="red"
        game_over_window(winner, color)
        winner_found = True
        
    if number == 9 and winner_found == False:
        game_over_window("There was no winner!", "gray")

def close():
    window.destroy()

def verifyWinner():      
    if ((gameArray[0] == gameArray[1] == gameArray[2] and gameArray[0] != 0) or (gameArray[3] == gameArray[4] == gameArray[5] and gameArray[3] != 0) or 
    (gameArray[6] == gameArray[7] == gameArray[8] and gameArray[6] != 0) or (gameArray[0] == gameArray[3] == gameArray[6] and gameArray[0] != 0) or 
    (gameArray[1] == gameArray[4] == gameArray[7] and gameArray[1] != 0) or (gameArray[2] == gameArray[5] == gameArray[8] and gameArray[2] != 0) or 
    (gameArray[0] == gameArray[4] == gameArray[8] and gameArray[0] != 0) or (gameArray[2] == gameArray[4] == gameArray[6] and gameArray[2] != 0)):
        return True
    return False
                                                            
def placeImg(spotx, spoty, num):
    global winner_found
    if winner_found == False:
        if num == 1:
            imagem = PhotoImage(file="TicTacToe/img/x.png")
        else:
            imagem = PhotoImage(file="TicTacToe/img/o.png")
        largura_imagem = imagem.width()
        altura_imagem = imagem.height()

        x = (width/3 + spotx*width*2/3 - largura_imagem) // 2
        y = (height/3 + spoty*height*2/3 - altura_imagem) // 2
        canvas.create_image(x, y, anchor=tk.NW, image=imagem)
        canvas.image = imagem  
        imagens.append(imagem)

def lines():
    x1 = width/3
    x2 = width*2/3
    y1 = height/3
    y2 = height*2/3
    line_width = 3
    canvas.create_line(x1, 0, x1, height, fill="black", width=line_width)
    canvas.create_line(x2, 0, x2, height, fill="black", width=line_width)
    canvas.create_line(0, y1, width, y1, fill="black", width=line_width)
    canvas.create_line(0, y2, width, y2, fill="black", width=line_width)

def game_over_window(winner, color):
    global gameOver
    gameOver = tk.Toplevel(window)
    widthGO = 200
    heightGO = 100
    x = (screen_width - widthGO) // 2
    y = (screen_height - heightGO) // 2
    size = f"{widthGO}x{heightGO}+{x}+{y}"
    gameOver.geometry(size)
    gameOver.overrideredirect(True)
    button = tk.Button(gameOver, text=winner + "\n" + "Press to restart!", command=restart_game, height=10, bg=color)
    button.pack(fill="both", expand=True)

def restart_game():
    global number, gameArray, imagens, winner_found
    winner_found = False
    number = 0
    gameArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for imagem in imagens:
        imagem.blank()
    imagens = []
    canvas.delete("all")
    lines()
    if gameOver.winfo_exists(): 
        gameOver.destroy()

window = tk.Tk()
window.title("Board")
width = 900
height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
size = f"{width}x{height}+{x}+{y}"
window.geometry(size)
whiteBG = tk.Frame(window, bg="white")
whiteBG.place(relwidth=1, relheight=1)

canvas = tk.Canvas(whiteBG, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<Button-1>", play)

lines()

window.mainloop()