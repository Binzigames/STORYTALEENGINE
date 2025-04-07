#>        BASE OF STORYTALEENGINE <
#--------------------------------->libs
import sys
from colorama import *
import pyray as pr
import Base
import Base.Scenes.Scenes as Scene
from math import *


#---------------------------------> bools/data

#>debiging
Name = "[STE]"
loging = False
#>scene manager
scene_index = 0
#>bools
Ispause = False


#>ui settings
wX , wY = 900 ,900
current_message = Scene.current_message
current_ch_name = Scene.current_ch_name

show_ui = True
UI_color = pr.DARKPURPLE
#---------------------------------> functions
def init_game(wX , wY , wName):
    init(autoreset=True)
    print(Style.BRIGHT + Fore.CYAN+">STORYTALEENGINE<")
    print("-----------------")
    print(Style.BRIGHT + Fore.CYAN+">    by Porko   <")
    print("-----------------")
    print(Style.BRIGHT + Fore.CYAN+">   formating   <")
    print(Name + Style.BRIGHT + Fore.RED + "Error/ important action")
    print(Name + Style.BRIGHT + Fore.GREEN + "loging")
    print(Name + Style.BRIGHT + Fore.GREEN + "> comand")

    pr.init_window(wX,wY, wName)
    pr.set_target_fps(120)

def exit_game():
    print(Name +Style.BRIGHT + Fore.RED+ ">leaving the game<")
    pr.close_window()
    sys.exit(1)

#>pause
def pause():
    global Ispause
    print(Name + Style.BRIGHT + Fore.RED + ">pause the game<")
    Ispause = not Ispause
    if Ispause == True:
        print(Name + Style.BRIGHT + Fore.RED + ">pause the game<")
    else:
        print(Name + Style.BRIGHT + Fore.GREEN + ">unpause<")


#---------------------------------> clases
class SceneManager():
    def update(self):
        scene = Scene.debug_scene
        if loging == True:
            print(Name + Style.BRIGHT + Fore.GREEN + ">update of SceneManager<")
        global scene_index
        if scene_index == 0:
            if Scene.lvl_debug == True:
                Scene.debug_scene.run(scene)

    def change_scene(self , index):
        global scene_index ,wY , wX
        scene_index = index
        print(Name + Style.BRIGHT + Fore.GREEN + ">change scene<")

    def get_current_scene_int(self , int):
        global scene_index ,wY , wX
        int = scene_index
        print(Name + Style.BRIGHT + Fore.GREEN + f">current scene : {int}")
class UI():
    def ToglleUI(self):
        global show_ui
        show_ui = not show_ui
        print(Name + Style.BRIGHT + Fore.GREEN + f">toggle ui : {show_ui}")

    def Togle_dialog_window(self ,text , name):
        global show_ui , UI_color ,wY , wX , Ispause
        arrow_x = wX - 95 + sin(pr.get_time() * 5) * 5
        if show_ui == True and not Ispause:

            pr.draw_rectangle(50, wY - 100, wX - 100, 80, pr.BLACK)
            pr.draw_rectangle_lines_ex(pr.Rectangle(50, wY - 100, wX - 100, 80), 4, UI_color)
            pr.draw_text(text, 60, wY - 80, 20, pr.RAYWHITE)
            pr.draw_text(">",int(arrow_x) , wY - 90, 60, UI_color)



            name_box_width = 200
            name_box_height = 40
            name_x = 50
            name_y = wY - 150

            pr.draw_rectangle(name_x, name_y, name_box_width, name_box_height, pr.BLACK)
            pr.draw_rectangle_lines_ex(pr.Rectangle(name_x, name_y, name_box_width, name_box_height), 3, UI_color)
            pr.draw_text(name, name_x + 10, name_y + 10, 20, pr.RAYWHITE)

    def Show_FPS(self):
        fps_text = "fps : " + str(pr.get_fps())
        text_width = pr.measure_text(fps_text, 30) + 20
        text_height = 50
        x = wX - text_width - 20
        y = 10

        pr.draw_rectangle(x, y, text_width, text_height, pr.BLACK)
        pr.draw_rectangle_lines_ex(pr.Rectangle(x, y, text_width, text_height), 4, UI_color)
        pr.draw_text(fps_text, x + 10, y + 10, 30, pr.RAYWHITE)


    def Togle_pause_window(self):
        global show_ui, UI_color ,wY , wX , Ispause
        if show_ui == True and Ispause:
            pause_text = "<PAUSE>"
            text_width = pr.measure_text(pause_text, 30) + 20
            text_height = 50
            x = (wX - text_width) // 2
            y = (wY - text_width) // 2

            pr.draw_rectangle(x, y - 10, text_width, text_height, pr.BLACK)
            pr.draw_rectangle_lines_ex(pr.Rectangle(x, y - 10, text_width, text_height), 4, UI_color)
            pr.draw_text(pause_text, x + 10, y, 30, pr.RAYWHITE)















