import js as p5

print('click on a Sprite to make it disappear..')

print('while loop example:')
i = 0  # variable to use in a while loop
# loop while the condition is True:
while (i < 5):  
  print('i = ' + str(i))
  i += 1  # increment variable
print('finished with i = ' + str(i))

print('while loop with a break statement:')
i = 0 
while (i < 5):  
  print('i = ' + str(i))
  if(i == 3):
    break  # end the loop early
  i += 1  
print('finished with i = ' + str(i))


# generic Sprite object:
class Sprite:  
  
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def draw(self):
    p5.ellipse(self.x, self.y, 50, 50) 

sprite_list = []
# add 4 sprites to sprite_list with append:
for i in range(4):
  sprite = Sprite(x = 50 + i*65, y = 150)
  sprite_list.append(sprite)

def setup():
  p5.createCanvas(300, 300)  

def draw():
  p5.background(255)   
  p5.fill(0)     
  p5.noStroke()  
  # traverse sprite_list with a while loop:
  i = 0
  while(i < len(sprite_list)):
    sprite = sprite_list[i]
    # calculate distance from cursor to sprite:
    d = p5.dist(p5.mouseX, p5.mouseY, sprite.x, sprite.y)
    # cursor is inside sprite:
    if(d < 25): 
      p5.fill(255, 0, 0)  # fill with red
      # remove sprite if it is clicked:
      if (p5.mouseIsPressed == True): 
        print('remove sprite..', i)
        sprite_list.pop(i)
    else:
      p5.fill(0)  # fill with black
      
    sprite.draw()
    p5.text('sprite ' + str(i), sprite.x - 20, sprite.y - 30)
    # don't forget to increment loop variable:
    i += 1 

def keyPressed(event):
  pass

def keyReleased(event):
  pass

def mousePressed(event):
  pass

def mouseReleased(event):
  pass
