from tkinter import *
import random

class Application(Frame):
	moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
	wins, total = 0, 0
	root = Tk()
	rock_img = PhotoImage(file = "./rock.gif")
	paper_img = PhotoImage(file = "./paper.gif")
	scissors_img = PhotoImage(file = "./scissors.gif")
	lizard_img = PhotoImage(file = "./lizard.gif")
	spock_img = PhotoImage(file = "./spock.gif")

	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def compare(self, player, opponent):
		win = "Victory"
		lose = "You lose scrub"
		hierarchy = "rocklizardspockscissorspaperrockscissorslizardpaperspockrock"
		string_made = player + opponent
		result = ""
		print(player, 'vs.', opponent)
		Application.total += 1
		if string_made in hierarchy:
			Application.wins += 1
			result = win
		else:
			result = lose

		self.message.destroy()
		self.score.destroy()

		self.message = Button(self,text = result)
		self.message.pack()

		self.score = Button(self, text = "Win rate: " + str(Application.wins) + '/' + str(Application.total))
		self.score.pack()

	def rock_move(self):
		player_move = self.rock["text"]
		opponent_move = Application.moves[random.randint(0,len(Application.moves)-1)]
		return self.compare(player_move, opponent_move)

	def paper_move(self):
		player_move = self.paper["text"]
		opponent_move = Application.moves[random.randint(0,len(Application.moves)-1)]
		return self.compare(player_move, opponent_move)

	def scissors_move(self):
		player_move = self.scissors["text"]
		opponent_move = Application.moves[random.randint(0,len(Application.moves)-1)]
		return self.compare(player_move, opponent_move)

	def lizard_move(self):
		player_move = self.lizard["text"]
		opponent_move = Application.moves[random.randint(0,len(Application.moves)-1)]
		return self.compare(player_move, opponent_move)

	def spock_move(self):
		player_move = self.spock["text"]
		opponent_move = Application.moves[random.randint(0,len(Application.moves)-1)]
		
		return self.compare(player_move, opponent_move)

	def createWidgets(self):
		self.message = Button(self)
		self.message.pack()

		self.score = Button(self)
		self.score.pack()

		self.QUIT = Button(self, text = "QUIT", fg = "red", command = self.quit)
		self.QUIT.pack(side = "bottom")

		self.rock = Button(self, text = 'rock', fg = 'black', command = self.rock_move)
		self.rock.pack(side = "left")
		self.rock.config(image = self.rock_img)

		self.paper = Button(self, text = 'paper', fg = 'gray', command = self.paper_move)
		self.paper.pack(side = "left")
		self.paper.config(image = self.paper_img)

		self.scissors = Button(self, text = 'scissors', fg = 'red', command = self.scissors_move)
		self.scissors.pack(side = "left")
		self.scissors.config(image = self.scissors_img)

		self.lizard = Button(self, text = 'lizard', fg = 'green', command = self.lizard_move)
		self.lizard.pack(side = "left")
		self.lizard.config(image = self.lizard_img)

		self.spock = Button(self, text = 'spock', fg = 'blue', command = self.spock_move)
		self.spock.pack(side = "left")
		self.spock.config(image = self.spock_img)

app = Application()
app.mainloop()
root.destroy()


