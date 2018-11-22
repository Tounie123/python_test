class Settings():
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self, screen):
		"""初始化游戏的设置"""
		self.screen = screen

		#加载飞船图像并获取其外接矩形
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)