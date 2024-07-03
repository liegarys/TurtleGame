import turtle
import  random


def update_position():
    # Updating position
    if (time_left > 0):

        turtle_ins.hideturtle()

        # Generate random coordinates within the screen bounds
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)

        # Move the turtle to the new coordinates
        turtle_ins.goto(x,y)

        turtle_ins.showturtle()
        # Schedule the function to be called again after 1000 ms (1 second)
        screen.ontimer(update_position, 1000)



# Function to update the countdown timer
def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_turtle.clear()
        timer_turtle.write(f"Time : {time_left}", align="center", font=("Arial", 24, "normal"))
        screen.ontimer(update_timer, 1000)
    else:
        timer_turtle.clear()
        timer_turtle.write("Time's up!", align="center", font=("Arial", 24, "normal"))



def update_score(x, y):
    if (time_left > 0):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="left", font=("Arial", 24, "normal"))


screen = turtle.Screen()
screen.bgcolor("Black")
screen.title("Catch The Turtle")


turtle_ins = turtle.Turtle()
turtle_ins.color("white")
turtle_ins.shape("turtle")

#Pen is up because we dont want turtle to sketch
turtle_ins.penup()

#timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.goto(0, 260)  # Position at the top of the screen
timer_turtle.color("red")
timer_turtle.write("Time : 10", align="center", font=("Arial", 24, "normal"))

#score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-350, 260)  # Position at the top-left of the screen
score_turtle.color("green")
score_turtle.write("Score: 0", align="left", font=("Arial", 24, "normal"))

time_left = 10
score = 0

#Updating position
update_position()

#Updationg Score if there is click
turtle_ins.onclick(update_score)

#Updating timer
update_timer()

screen.mainloop()