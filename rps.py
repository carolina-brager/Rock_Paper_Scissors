
from Tkinter import *
from PIL import ImageTk, Image #for the r,p,s images
from random import randint

winMsg = None # Stores the message printed at the end of a round

def play(i):
	options = ["Rock", "Paper", "Scissors"] #The three options of the game
	computer = options[randint(0,2)] #choose one of the three indeces of the options array
	player = options[i] #Player is based in the player choice
	quote = None #quote will be the message printed
	if(player == computer): #if the player and computer choose the same sign
		quote = "You played %s and so did the Computer. It's a tie =|" % (player)
	elif(player == "Rock"): 
		if(computer == "Scissors"): #Player chooses Rock, computer Chooses Scissors - player wins
			quote = "You played %s, the Computer played %s. You Win =D" % (player, computer)
		elif(computer == "Paper"): #Player chooses Rock, computer Chooses Paper- player looses
			quote = "You played %s, the Computer played %s. You Loose =(" % (player, computer)
	elif(player == "Paper"):
		if(computer == "Rock"): #Player chooses Paper, computer Chooses Rock - player wins
			quote = "You played %s, the Computer played %s. You Win =D" % (player, computer)
		elif(computer == "Scissors"): #Player chooses Paper, computer Chooses Scissors - player looses
			quote = "You played %s, the Computer played %s. You Loose =(" % (player, computer)
	elif(player == "Scissors"):
		if(computer == "Paper"): #Player chooses Scissors, computer Chooses Paper - player wins
			quote = "You played %s, the Computer played %s. You Win =D" % (player, computer)
		elif(computer == "Rock"): #Player chooses Scissors, computer Chooses Rock - player looses
			quote = "You played %s, the Computer played %s. You Loose =(" % (player, computer)
	else: #Just in case, but shouldn't ever happen
		quote = "Well something went wrong... Sorry about that"

	winMsg.config(text = quote) #change the winMsg to correct quote

app = Tk() #The window
app.title("Rock Paper Scissors")
app.resizable(0,0)
app.minsize(width = 430, height = 50) #minimum widht and height of the window

frame1 = Frame(app) #for the title
frame2 = Frame(app) #for the buttons
frame3 = Frame(app, bg = 'snow2') #for the message

# Images for Rock, Paper, and Scissors acquired from:
# http://developer.ibm.com/dwblog/wp-content/uploads/sites/73/2016/02/dwblog-rockpaperscissors-450x225.png

img1 = ImageTk.PhotoImage(Image.open("Rock.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Paper.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Scissors.jpg"))
#Button with rock image, rock is index 0 in options array
ROCK = Button(master = frame2, image = img1, command = lambda: play(0)) 
#Button with paper image, rock is index 1 in options array
PAPER = Button(master = frame2, image = img2, command = lambda: play(1))
#Button with scissors image, rock is index 2 in options array
SCISSORS = Button(master = frame2, image = img3, command = lambda: play(2))

title = Label(frame1, text = "Rock Paper Scissors", font ="-size 30" )

winMsg = Message(frame3, text = "", bg = 'snow2', width = 500)

frame1.pack(side = TOP, fill = X)
title.pack( padx = 10)

frame2.pack(padx = 10) 
ROCK.pack(side = LEFT, padx = 15)
PAPER.pack(side = LEFT,padx = 15)
SCISSORS.pack(side = LEFT,padx = 15)

frame3.pack(side = BOTTOM, fill = BOTH)
winMsg.pack()

app.mainloop()