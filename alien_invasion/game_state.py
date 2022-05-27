import pygame



class GameStates():
    """统计游戏信息和初始化"""
    def __init__(self):
        self.Score = 0

    def to_orgin(self, bullets, aliens, booms):
        bullets.empty()
        aliens.empty()
        booms.empty()
        self.Score = 0
        

    

        
