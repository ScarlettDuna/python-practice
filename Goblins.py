gamers = []
def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")
kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)
def build_daily_frequency_table():
    return {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
count_availability = build_daily_frequency_table()
# Fuction to calculate availability
def calculate_availability(gamers_list, available_frequency):
    #iterate throught each gamer
    for gamer in gamers_list:
        #iterate through each day in the gamers availability
        for day in gamer['availability']:
            #add one to that day
            available_frequency[day] += 1
    return available_frequency
print(calculate_availability(gamers, count_availability))

# Find night with biggest availability
def find_best_night(availability_table):
    best_night = 0
    for day in availability_table:
        if availability_table[day] > best_night:
            best_night = availability_table[day]
    night_week = [key for key, value in availability_table.items() if value == best_night]
    # To make sure we only get a string with one day
    game_night = night_week[0]
    return game_night

game_night = find_best_night(count_availability)
print(game_night)

#Function to see how is available on a certain day
def available_on_night(gamers_list, day):
    players_available = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            players_available.append(gamer['name'])
    return players_available

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = "{name}, the game night for {game} will be on {day}. Please make sure to attend!"

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")