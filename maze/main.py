import turtle
import math
import random
import os.path


# Initialise list
levels = ['']
walls = []
treasures = []
monsters = []

screen = turtle.Screen()

screen.bgcolor('black')
screen.title('MAZE GAME')
screen.setup(800, 800)

Turtle = turtle.Turtle
gif_imgs = ['wall.gif', 'kratos_right.gif', 'kratos_left.gif', 'gold.gif', 'monster_right.gif', 'monster_left.gif', 'game_over.gif', 'trophy.gif']

dir = os.path.dirname(__file__)
img_list = []
# Image files direcotry
img_path = './img/'
for gif in gif_imgs:
  # Join the directory with each image file
  src = os.path.join(dir, img_path) + gif
  turtle.register_shape(src)
  img_list.append(src)

class Instruction(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.color('blue')
    self.penup()
    self.speed(0)
    self.setposition(-288, 280)
    self.hideturtle()

class Score(Turtle):
   def __init__(self):
    Turtle.__init__(self)
    # self.shape(img_list[0])
    self.color('white')
    self.penup()
    self.speed(0)
    self.setposition(300, 320)
    self.hideturtle()


# Pen class as subclass of Turtle
class Pen(Turtle):
  # create constructor
  def __init__(self):
    Turtle.__init__(self)
    self.shape(img_list[0])
    self.color('white')
    self.penup()
    self.speed(0)

# Create a warrior class as subclass of the Turtle
class Warrior(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.shape(img_list[1])
    self.color('cyan')
    self.penup()
    self.speed(0)
    self.wealth = 0
  
      
  def move(self, x, y):
    if (x, y) not in walls:
      self.goto(x, y)

  def move_up(self):
    coord_x = warrior.xcor()
    coord_y = warrior.ycor() + 24
    self.move(coord_x, coord_y)
    

  def move_down(self):
     coord_x = warrior.xcor()
     coord_y = warrior.ycor() - 24
     self.move(coord_x, coord_y)

  def move_left(self):
     coord_x = warrior.xcor() - 24
     coord_y = warrior.ycor()
     self.shape(img_list[2])
     self.move(coord_x, coord_y)
     

  def move_right(self):
     coord_x = warrior.xcor() + 24
     coord_y = warrior.ycor() 
     self.shape(img_list[1])
     self.move(coord_x, coord_y)
  
  def is_collide(self, the_treasure):
    # using distance between two point formula d(p,q) = sqrt((x2-x1)^2 + (y2-y1)^2)
    x = self.xcor() - the_treasure.xcor()
    y = self.ycor() - the_treasure.ycor()
    distance = math.sqrt((x ** 2) + (y ** 2))
    if distance <= 5:
      return True
    else:
      return False


# Create treasure class
class Treasure(Turtle):
  def __init__(self, x, y):
    Turtle.__init__(self)
    self.shape(img_list[3])
    self.penup()
    self.speed(0)
    self.goto(x, y)
    self.wealth = 100
    

  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()
  
# Create Enemy class
class Monster(Turtle):
  def __init__(self, x, y):
    Turtle.__init__(self)
    self.shape(img_list[4])
    self.penup()
    self.speed(0)
    self.wealth = 5
    self.goto(x, y)
    self.direction = random.choice(["Up", "Down", "Right", "Left"])

  # Calculate the distance between the warrior and monster
  def is_nearby(self, the_warrior):
    x = self.xcor() - the_warrior.xcor()
    y = self.ycor() - the_warrior.ycor()
    distance = math.sqrt((x ** 2) + (y ** 2))
    return distance

  def motion(self):
    
    if self.direction == "Right":
      point_x = 24
      point_y = 0
      self.shape(img_list[4])
    elif self.direction == "Left":
      point_x = -24
      point_y = 0
      self.shape(img_list[5])
    elif self.direction == "Up":
      point_x = 0
      point_y = 24
    elif self.direction == "Down":
      point_x = 0
      point_y = -24
    else:
      point_x = 0
      point_y = 0
    
    coord_x = self.xcor() + point_x
    coord_y = self.ycor() + point_y

    if(coord_x, coord_y) not in walls:
      self.goto(coord_x, coord_y)
    else:
      self.direction = random.choice(["Up", "Down", "Right", "Left"])
    
    # Set random motion time to keep monsters moving
    turtle.ontimer(self.motion, t=random.randint(300, 600))

    # Make the monster aware of the warrior proximity
    if self.is_nearby(warrior) <= 60:
      if warrior.xcor() > self.xcor():
        self.direction = "Right"
      elif warrior.xcor() < self.xcor():
        self.direction = "Left"
      elif warrior.ycor() > self.ycor():
        self.direction = "Up"
      elif warrior.ycor() < self.ycor():
        self.direction = "Down"
  def destroy(self):
    self.goto(-3000, -3000)
    self.hideturtle()
    


# Instantiate Instruction, Score, Pen, and Warrior class
instruction = Instruction()
score = Score()
pen = Pen()
warrior = Warrior()

level = [
  'KKKKKKKKKK KKKKKKKKKKKKKK',
  'KW KKKKKKK    M     KKKKK',
  'K  KKKKKKK  KKKKKK  KKKKK',
  '        KK  KKKKKK  KKKKK',
  'K  G    KK  KKK        KK',
  'KKKKKK  KK  KKK          ',
  'KKKKKK  KK  KKKKKK  KKKKK',
  'KKKKKK  KK    KKKK   KkkK',
  'K  KKK     M  KKKKkk   KK',
  'K  KKK   KKKKKKKKKKKKKGKK',
  'K          KKKKKKKKKKKKKK',
  'K    M            KKKKKKK',
  'KKKKKKKKKK    M  KKKKK  K',
  'KKKKKKKKKKKKK    KKKKK  K',
  'KKK  KKKKKKKK           K',
  'KKK                    GK',
  'KKKM       KKKKKKKKKKKKKK',
  'KKKKKKKKK  KKKKKKKKKKKKKK',
  'KKKKKKKKK               K',
  'KK  KKKKK G           M K',
  'KK  KKKKKKKKKKKKKK  KKKKK',
  'KK   YKKKKKKKKKKKK  KKKKK',
  'KK          KKKK       GK',
  'KKKK     M             MK',
  'KKKKKKK KKKKKK KKKKKKKKKK',
  'KKKKKKG KKKKKKKKKKKKKKKKK',
]

# Append level to levels
levels.append(level)

# Setup level
def setup_maze_level(levl_lst):
  for i in range(len(levl_lst)):
    for j in range(len(levl_lst[i])):
      char = levl_lst[i][j]

      # Specify the cordinates that the Pen will be positioned
      coord_x = -288 + (j * 24)
      coord_y = 288 - (i * 24)
      

      # Pen should go to the specified coordinates if the character is K
      if char == 'K':
        pen.goto(coord_x, coord_y)
        pen.stamp()
        walls.append((coord_x, coord_y))
      
      # Pen should go to the P(warrior) coordinate if the character is P
      if char == 'W':
        warrior.goto(coord_x, coord_y)
        # warrior.stamp()
      if char == 'G':
        treasures.append(Treasure(coord_x, coord_y))
      
      if char == 'M':
        monsters.append(Monster(coord_x, coord_y))

# Call the setup_maze_level function
setup_maze_level(levels[1])

instruction_str = """
To play the game, use the keyboar arrow keys.\nYou can collect treasure and avoid contacting the monsters.\nYou win the game when you get certain score.\nYou loose when your score runs below certain value.\nYou can draw a monster out of the maze into the darkness of unknown.
"""
instruction.write(instruction_str, False, align='left', font=('Serif', 16, 'normal'))
score.write('Score: 0', False, align='left', font=('Serif', 16, 'normal'))

# Keep track of the score
def keep_score():
  score.undo()
  scorestring = f'score: {warrior.wealth}'
  score.write(scorestring, False, align='left', font=('Serif', 16, 'normal'))
  print(f'You collected {warrior.wealth} gold!')

# Keep track of the game state
def set_state(img_index):
   warrior.goto(3000, 3000)  
   warrior.hideturtle()
   screen.clear()
   screen.bgcolor('black')
   screen.bgpic(img_list[img_index])
   for monster in monsters:
     monster.goto(-3000, -3000)
     monster.hideturtle()

def warrior_state():
  if warrior.wealth <= -100:
    set_state(6)
  elif warrior.wealth >= 200:
    set_state(7)
  elif warrior.wealth != 200 and len(treasures) == 0:
    set_state(6)


# Enable turtle to use keyboard arrow key - Keyboard Binding
turtle.listen()
turtle.onkey(warrior.move_up, 'Up')
turtle.onkey(warrior.move_down, 'Down')
turtle.onkey(warrior.move_left, 'Left')
turtle.onkey(warrior.move_right, 'Right')

# Turn screen updates off
screen.tracer(0)

# Set the time for monsters to start moving
for monster in monsters:
  turtle.ontimer(monster.motion, t=300)
  
# The main Game Loop
while True:
  for treasure in treasures:
    if warrior.is_collide(treasure): 
      warrior.wealth += treasure.wealth
      treasure.destroy()
      treasures.remove(treasure)
      keep_score()
      warrior_state()
      
  for monster in monsters:
    if warrior.is_collide(monster):
      warrior.wealth -= monster.wealth
      keep_score()
      warrior_state()

    #Destroy a monster that goes beyond the maze wall 
    if monster.xcor() < -312 or monster.xcor() > 312 or monster.ycor() < -312 or monster.ycor() > 312:
      monster.destroy()
  # Enable screen update
  screen.update()

  
  
