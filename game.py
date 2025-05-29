import json
# import main as game

def load_highscores():
    # try to find the file - if it doesn't exist - create an empty highscores
    try:
        inf = open('highscore.txt', 'r')
        highscores = json.load(inf)
    except Exception as e:
        highscores = {}
    return  highscores


# for name in highscores:
#     print(name, highscores[name])

# name = "()"
# score = 11

# highscores[name] = score  # adds the name and score to my highscores

# for name in highscores:
#     print(name, highscores[name])

def save_highscores(highscores):
    # save the highscores to a file
    outf = open('highscore.txt', 'w')
    json.dump(highscores, outf, indent=4)
    # outf.write(json.dumps(highscores))


def add_score_to_highscore(name, score):
    # add a new score to the highscores
    print(name, score)
    highscores = load_highscores()
    print(f"HS before update: {highscores}")
    if name not in highscores or score > highscores[name]:
        highscores[name] = score
        print(highscores)
        save_highscores(highscores)
# highscores = load_highscores()

def display_highscores():
    # Display existing highscores
    print("Current Highscores:")
    for name, score in highscores.items():
        print(f"{name}: {score}")



# # Ask user for new highscore entry
# name = input("Enter your name: ")
# #check if game is won or lost
# if game.game_outcome == 1:
#     get_current_level = game.world.level
#     add_to_hscore = save_highscores(get_current_level)

# # Add/update score
# highscores[name] = score

# # Save and confirm
# save_highscores(highscores)
# print("Highscore updated!")

# # Show updated list
# print("\nUpdated Highscores:")
# for name, score in highscores.items():
#     print(f"{name}: {score}")
