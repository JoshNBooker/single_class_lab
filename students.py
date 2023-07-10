class students:

    def __init__(self, student_name, student_cohort, favourite_language):
        self.name = student_name
        self.cohort = student_cohort
        self.language = favourite_language

    def talk(self):
        print("Hi, I'm " + self.name + " " + "and I can talk!")

    def say_favourite_language(self):
        return("I love ") + self.language
    
class sports_team:
    
    def __init__(self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_new_players(self):
        self.name += 

        