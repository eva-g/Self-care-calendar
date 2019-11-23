
#---------------------- BOARD STARTER ----------------------#

import turtle
turtle.tracer(0, 0)
turtle.speed(0)
	
# number of rows and columns.
ROWS = 25
COLS = 8

# the dimensions of the board being drawn.
BOARD_WIDTH = 600
BOARD_HEIGHT = 600

# the dimensions of the window being displayed.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

def make_board_list(rows, cols):
	'''
	Purpose: 
		creates a lists of lists where 
		each item represents a row of a board.

	Inputs: Number of rows, and number of columns.
	Outputs: A list of lists.
	'''
	board=[]
	for i in range(1,rows+1):
		row=[]
		for i in range(1,cols+1):
			row.append(0)
		board.append(row)
	return board

# Make a ROWSxCOLS list of lists.
BOARD_DATA = make_board_list(ROWS, COLS)
# Draw the interface.
"""BoardGUI.draw_board(BOARD_WIDTH, BOARD_HEIGHT, ROWS, COLS, 
	WINDOW_WIDTH, WINDOW_HEIGHT)"""
BOARD_DATA[0][1] = "Sunday"
BOARD_DATA[0][2] = "Monday"
BOARD_DATA[0][3] = "Tuesday"
BOARD_DATA[0][4] = "Wednesday"
BOARD_DATA[0][5] = "Thursday"
BOARD_DATA[0][6] = "Friday"
BOARD_DATA[0][7] = "Saturday"

BOARD_DATA[0][0] = "Time"
time = 0
for i in range(1,25):
	time = time + 1
	BOARD_DATA[i][0] = time 


########BOARD GUI###########

# has a lot of inputs, just use a new line!

def setup():
	'''
	Purpose:
		Configure turtle before drawing.
		Tracer affects the rate that turtle refreshes the screen.
		Setting it to 0 turns it off so we don't compute any
		unnecessary animations.

		####### VERY IMPORTANT NOTE #########
		YOU WILL NEED TO CALL turtle.update() whenever you finish drawing something.

		We also set our turtle's speed to 0 which is the fastest animation.'''

def draw_board(board_width, board_height, rows, cols, 
	window_width, window_height):
	'''
	Purpose: Draws the board.
	Inputs: Board dimensions, row and columns, and window size.
	Outputs: Nothing.
	'''
	pass

def draw_board_border(board_width, board_height):
	'''
	Purpose: Draw the border around the board.
	Inputs: the board's width and height.
	Outputs: Nothing.
	'''
	turtle.penup()
	turtle.goto(-(board_width/2), -(board_height/2))
	turtle.pendown()
	for i in range(0,4):
		turtle.forward(board_width)
		turtle.left(90)

def draw_vertical_lines(board_height, board_width, cols):
	'''
	Purpose: Helper for drawing the vertical lines of the board.
	Inputs: the board's height and the amount of columns it has.
	Outputs: Nothing.
	'''
	turtle.penup()
	turtle.goto(-(board_width/2), (board_height/2))
	for i in range(1,cols+1):
		x=turtle.xcor()
		y=turtle.ycor()
		turtle.setheading(270)
		turtle.pendown()
		turtle.forward(board_height)
		turtle.penup()
		turtle.setx(x+board_width/cols)
		turtle.sety(y)

def draw_horizontal_lines(board_width, board_height, rows):
	'''
	Purpose: Helper for drawing the horizontal lines of the board.
	Inputs: the board's width and the number of rows we have.
	Outputs: Nothing.
	'''
	turtle.goto(-(board_width/2), (board_height/2))
	for i in range(1,rows+1):
		turtle.penup()
		x=turtle.xcor()
		y=turtle.ycor()
		turtle.setheading(0)
		turtle.pendown()
		turtle.forward(board_width)
		turtle.penup()
		turtle.setx(x)
		turtle.sety(y-board_height/rows)

def draw_grid(board_width, board_height, rows, cols):
	'''
	Purpose: Draws the grid of the board
	Inputs: the board's width, height, and the number of rows and columns we have.
	Outputs: Nothing.
	'''
	draw_board_border(board_width,board_height)
	draw_vertical_lines(board_height,board_width,cols)
	draw_horizontal_lines(board_width,board_height,rows)

draw_grid(600,600,25,8)

def set_row_col_to_val(row,col,val):
	BOARD_DATA[row][col] = val

def go_to_row_col_in_display(row,col):
	turtle.penup()
	turtle.setx((-300 + 75*col)+5)
	turtle.sety(300-(24*(row))-20)

def create_text_at_row_col(text, row, col):
	set_row_col_to_val(row, col, text)
	go_to_row_col_in_display(row, col)
	turtle.write(text, font = ("Arial",12,"normal"))


########program###########
	
print("Welcome to Your Self Care Calendar! Here are some commands:")
print("To display calendar, type 'display_calendar()'") 
print("To make an event, type 'make_event()'") 
print("To delete an event, type 'delete_event()'")
print("There are three self-care events you are required to have in your calendar: exercise (at least 5 days a week), meditate (at least 7 days a week), and treat yo self (at least 1 day a week).")
print("To make a self care event, type 'make_selfcare_event('name of the self care event, SPELLED RIGHT!')'.")


print("How many hours of scheduled events can you handle in one day?")
hour_limit = int(input())


def make_event():
	print("State the name of event.")
	name = input()
	print("What day is your event on? Sun = 1, Mon = 2...")
	date = int(input())
	print("When does the event start (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	start_time = int(input())
	print("When does the event end (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	end_time = int(input())
	#board[(start_time,date)]=name
	for hour in range(start_time, end_time):
		BOARD_DATA[hour][date] = name 
	display_calendar()



def column(day):
	lst=[]
	for i in range(0,12):
		lst.append(BOARD_DATA[i][day])
	return lst

def daily_schedule_too_busy(limit,day):
	lst=[event for event in column(day) if event!=0]
	return len(lst)>limit

def delete_event():
	print("What day is the event you would like to delete on?")
	date =int(input())
	print("When does the event start (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	start_time = int(input())
	print("When does the event end (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	end_time = int(input())
	for hour in range(start_time, end_time):
		BOARD_DATA[hour][date] = 0
	display_calendar()

def sched_limit():
	for i in range(1,7):
		if daily_schedule_too_busy(hour_limit,i) == True:
			print("Your schedule is too busy on day " + str(i)+ ". Please delete so you only have " +str(hour_limit)+ " hours scheduled.")
	

def make_selfcare_event(activity):
	print("What day do you want to " + activity + " ? Sun = 1, Mon = 2...")
	date = int(input())
	print("When does the event start (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	start_time = int(input())
	print("When does the event end (In military time. Do not append :00. Example: 1:00 pm = 13)?")
	end_time = int(input())
	#board[(start_time,date)]=name
	for hour in range(start_time, end_time):
		BOARD_DATA[hour][date] = activity 
	display_calendar()

def activity_in_day(activity,day):
	return activity in column(day)

def selfcare_check(reqfreq,activity):
	lst = [i for i in range(0,7) if activity_in_day(activity,i) == True]
	if len(lst) < reqfreq:
		print("You still need to plan " +str(activity) + " on " + str(reqfreq-len(lst))+ " days.")
		#selfcare_check(reqfreq,activity)
			
def BOARD_DATA_to_display():
	for row in range(0,25):
		for col in range(0,8):
			if BOARD_DATA[row][col] != 0:
				create_text_at_row_col(BOARD_DATA[row][col],row,col)

def display_calendar():
	turtle.reset()
	draw_grid(600,600,25,8)
	print(BOARD_DATA)
	BOARD_DATA_to_display()
	sched_limit()
	selfcare_check(5, "exercise")
	selfcare_check(7, "meditate")
	selfcare_check(1, "treat yo self")
	
	print("What do you want to do?)Choose to type:")
	print("make_event()")
	print("delete_event()")
	print("make_selfcare_event(name of the self care event SPELLED RIGHT in quotation marks!)")


