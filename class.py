from students import *

student1 = students("josh","e65")

students.talk(student1)

print(student1.say_favourite_language("python"))

team1 = sports_team("bluejays","Joe, jimmy, janey","Michael Smith")
print(team1.name)

team1.add_new_players("Jamie")
print(team1.players)

print(team1.has_player("Frankie"))

team1.play_game("win")
print(team1.points)