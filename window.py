from sqlite3 import Row
import arcade
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "windows xp"

class Object(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image, 0.5)
    def standing(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column

class Comp(Object):
    def __init__(self):
        super().__init__("wind.png")
        self.center_x = 100
        self.center_y = 600

class MyWindow(arcade.Window):
    def __int__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("fon.jpg")
        self.comp = Comp()
        self.touch = None


    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg = arcade.load_texture("fon.jpg")
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.comp = Comp()
        self.comp.draw()
        if self.touch != None:
            self.touch.draw()

    def on_mouse_press(self, x, y, buttom, modifiers):
        if 16 <= x <= 116:
            if 600 <= y <= 680:
                self.touch = Comp()
        if self.touch != None:
            self.touch.center_x = x
            self.touch.center_y = y
            self.touch.alpha = 150
        


window = MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()