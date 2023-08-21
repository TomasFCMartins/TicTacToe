import tkinter as tk
from tkinter import PhotoImage

gameArray=[0, 0, 0, 0, 0, 0, 0, 0, 0]
number = 0
imagens = []
def play(event):
    x = event.x
    y = event.y
    spotx = -1
    spoty = -1
    spot = 0
    global number
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
        print("Choose an empty spot to play")
    if verifyWinner():
        if number%2 == 0:
            winner = "O"
            color = "blue"
        else:
            winner = "X"
            color="red"
        button = tk.Button(window, text="Winner is " + winner + "!", command=close, width=10, height=5, bg=color)
        button.pack(pady=280)
        
    if number == 9:
        button = tk.Button(window, text="Press to restart!", command=close, height=10,)
        button.pack(pady=280)

def close():
    window.destroy()
# 0 1 2
# 3 4 5
# 6 7 8

def verifyWinner():      
    if ((gameArray[0] == gameArray[1] == gameArray[2] and gameArray[0] != 0) or (gameArray[3] == gameArray[4] == gameArray[5] and gameArray[3] != 0) or 
    (gameArray[6] == gameArray[7] == gameArray[8] and gameArray[6] != 0) or (gameArray[0] == gameArray[3] == gameArray[6] and gameArray[0] != 0) or 
    (gameArray[1] == gameArray[4] == gameArray[7] and gameArray[1] != 0) or (gameArray[2] == gameArray[5] == gameArray[8] and gameArray[2] != 0) or 
    (gameArray[0] == gameArray[4] == gameArray[8] and gameArray[0] != 0) or (gameArray[2] == gameArray[4] == gameArray[6] and gameArray[2] != 0)):
        return True
    return False
                                                            
def placeImg(spotx, spoty, num):
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

window = tk.Tk()
window.title("Board")
width = 900
height = 600
size = f"{width}x{height}"
window.geometry(size)
whiteBG = tk.Frame(window, bg="white")
whiteBG.place(relwidth=1, relheight=1)

canvas = tk.Canvas(whiteBG, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<Button-1>", play)

lines()

window.mainloop()