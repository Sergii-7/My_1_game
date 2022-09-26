class Stats():
    '''відслідує статистику'''

    def __init__(self):
        '''ініциалізує статистику'''
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        '''статитика, яка змінюється під час гри'''
        self.guns_left = 2
        self.score = 0

