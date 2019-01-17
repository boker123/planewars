class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,xz_settings):
        """初始化统计信息"""
        self.xz_settings = xz_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化可变信息"""
        self.planes_left = self.xz_settings.ship_limit