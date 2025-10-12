from ursina import *
from ursina.prefabs.firstpersoncontroller import FirstPersonCortroller
def start_game():
  app = Ursina()
  player = FirstPersonController()
  ground = Entity(
  model = "plane",
  collider = "box",
  texture = color.green,
  scale = (100 , 100 , 100)
  )
  def input(key):
      direction = (hit_pos - camera.world_position).normalized()
      hit_pos = mouse.world_point +  direction * 2
      if key == "left mouse down":
        cube = Entity(
          model = "box",
          collider = "box",
          scale = (2,2,2),
          postition = hit_pos
        )
  app.input = input

  Sky()
  app.run
    
  
