class Turn:
	def choice():
		choice = input("You want to have X or O?: ").lower()
		if choice == 'x':
			player1 = 'X'
			player2 = 'O'
		else:
			player1 = 'O'
			player2 = 'X'

		return player1, player2

		print("player1 is ", player1)
		print("player2 is ", player2)

	player1, player2 = choice()

	def next_player(turn):
	    if turn == 'X':
	        turn = 'O'
	    if turn == 'O':
	    	turn = 'X'
	   	return turn


	print("turn is ", turn)
	turn = next_player(turn) # was here: next_player(turn) and so below!!
	print("after next player function turn is ", turn)
	turn = next_player(turn)
	print("after next player function turn is ", turn)