from tkinter import *
import random

GAME_WIDTH = 450
GAME_HEIGHT = 450
GAME_SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.bodysize = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snakie")
            self.squares.append(square)

    pass


class Food:

    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "left":
        x -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "up":
        y -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
    window.after(GAME_SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
            
    elif new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction




def check_collisions():
    pass


def game_over():
    pass


window = Tk()
window.title = "Snake game"
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('Arial', 40))
label.pack()
canvas = Canvas(window, background=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
# centering the game window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
y = int((screen_height / 2) - (window_height / 2))
x = int((screen_width / 2) - (window_width / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
# keys configuration
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
next_turn(snake, food)


window.mainloop()
