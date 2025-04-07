#>        GAME OF STORYTALEENGINE <
#--------------------------------->importing engine
import Main
import pyray as pr
SM = Main.SceneManager
UI = Main.UI
#---------------------------------> init
Main.init_game(900 , 900, "debug")
#---------------------------------> write here your script
while not pr.window_should_close():
    pr.begin_drawing()
    Main.SceneManager.update(SM)
    #> hendled buttons (rebind here)
    # > pause
    if pr.is_key_pressed(pr.KeyboardKey.KEY_TAB):
        Main.pause()
    # > debug_mod
    if pr.is_key_down(pr.KeyboardKey.KEY_F7):
        Main.UI.Show_FPS(UI)
    if pr.is_key_down(pr.KeyboardKey.KEY_F8):
        Main.UI.ToglleUI(UI)


    Main.UI.Togle_dialog_window(UI , Main.current_message , Main.current_ch_name)
    Main.UI.Togle_pause_window(UI)
    pr.clear_background(pr.BLACK)
    pr.end_drawing()

Main.exit_game()