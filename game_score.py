# game_score.py

name = input("Enter player name: ")
games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))

average_score = total_score / games_played

print("Player:", name)
print()
print("Games Played:", games_played)
print()
print("Total Score:", total_score)
print()
print("Average Score:", average_score)
