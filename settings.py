import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

SCREEN_WIDTH = screensize[0]
SCREEN_HEIGHT = screensize[1]

FPS = 60
FONT_SIZE = 32
MAX_ENEMY = 5
