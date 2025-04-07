#>      SCENES OF STORYTALEENGINE <
#--------------------------------->init libs
import pyray as pr
import Base
import Base.Characters.Characters as ch
#--------------------------------->completed lvls
lvl_debug = True
#--------------------------------->ui
current_message = ""
current_ch_name = ""

#--------------------------------->your bools
#--------------------------------->debug + example
class debug_scene():
    def __init__(self , scene_name):
        self.name = scene_name


    def end(self):
        global lvl_debug
        print(f"end of lvl : debug")
        lvl_debug = False

    def run(self):
        ch = Base.Characters.Characters
        # >put here what will be on scene
        pr.draw_text("Hello,STORYTALEENGINE!", 250, 250, 20, pr.DARKBLUE)
        ch.character_example.say(ch , "hello" , current_message , current_ch_name)
        #self.end(debug_scene)
#---------------------------------> your scenes
