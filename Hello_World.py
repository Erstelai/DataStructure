
print('Hello world');

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color 

blueCookie = Cookie('blue')
greenCookie = Cookie('green')
print(blueCookie.get_color())
print(greenCookie.get_color())