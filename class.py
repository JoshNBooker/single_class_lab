from students import *

student1 = students("josh","e65","python")

students.talk(student1)

student1.say_favourite_language()
print(student1.say_favourite_language())

team1 = sports_team("bluejays","Joe, jimmy, janey","Michael Smith")
print(team1.name)

team1.add_new_players("Jamie")
print(team1.players)

print(team1.has_player("Frankie"))

team1.play_game("win")
print(team1.points)

team2 = sports_team("")