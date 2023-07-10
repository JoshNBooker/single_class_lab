class students:

    def __init__(self, student_name, student_cohort):
        self.name = student_name
        self.cohort = student_cohort

    def talk(self):
        print("Hi, I'm " + self.name + " " + "and I can talk!")

    def say_favourite_language(self,language):
        return("I love ") + language
    
class sports_team:
    
    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_new_players(self, new_player):
        new_player = new_player.lower()
        new_player = ", " + new_player
        self.players += new_player

    def has_player(self, player_check):
        if player_check in self.players:
            return True
        else:
            return False
        
    def play_game(self, result):
        if result == "win":
            points = True
        if points == True:
            self.points += 3
    

        