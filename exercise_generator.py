import random 

exercises = {
    'upper_body': {
        'push': {
            'vertical': ['Dumbbell Shoulder Press', 'Barbell Overhead Press', 'Plate Loaded Shoulder Press Machine'],
            'horizontal': ['Barbell Bench Press', 'Dumbbell Bench Press', 'Parallel Bar Dips', 'Push Ups', 'Ring Push Ups', 'Incline Dumbbell Bench', 'Incline Barbell Bench', 'Chest Press Machine'],
            'accessory': ['Dumbbell Lateral Raise', 'Dumbell Chest Fly', 'Machine Fly', 'Unilateral Cable Fly', 'Cable Tricep Pushdown', 'Barbell Skull crushers', 'Overhead Cable Tricep Extension', 'Close Grip Push Up']



        },
        'pull': {
            'vertical': ['Pull up', 'Wide Grip Pull Up', 'Chin Up', "Wide Grip Lat' Pulldown", "Supinated Lat' Pulldown"],
            'horizontal': ['Barbell Row', 'Landmine Row', 'Ring Row', 'Chest Supported Machine Row', 'Unilateral Dumbell Row', 'Cable Row'],
            'accessory': ['Straight Arm Lat Pulldown', 'Dumbell Pullover', 'Cable Facepull', "Machine Rear Delt' Fly", 'Barbell Curl', 'Incline Dumbell Curl', 'Dumbell Hammer Curl', 'Cable Rope Hammer Curl', 'Preacher Curl' ]
        }
    },
    'lower_body': {
        'push': ['High Bar Barbell Squat', 'ATG Split Squat', 'Heal Elevated Goblet Squat', 'Barbell Front Squat'],
        'pull': ['Barbell Deadlift', 'Romanian Deadlift', 'Rack Pull', 'Hyper Extensions'],
        'accessory': ['Lying Hamstring Curl', 'Tib Raises', 'Backwards Sled Pulling']
    }
}

def user_form():
    days = int(input('howmany days a week do you want to work out? '))
    goal = input('What is your goals? strength or hypertrophy? ')


    return days, goal

def sets_and_reps(goal):
    if goal.lower() == 'strength':
        return random.randint(3, 5), random.randint(3, 6)
    else:
        return random.randint(3, 4), random.randint(8, 15)
    

def generate_workout_plan(exercises, days, goal):
    
    workout_plan = {}

    for day in range(1, days +1): # Full Body Split
        if day <= 3:
            workout_plan[f"Day {day}"] = {
                'upper_push': random.choice(exercises['upper_body']['push']['vertical']),
                'upper_pull': random.choice(exercises['upper_body']['pull']['horizontal']),
                'lower_push': random.choice(exercises['lower_body']['push']),
                'push_accessory': random.choice(exercises['upper_body']['push']['accessory']),
                'pull_accessory': random.choice(exercises['upper_body']['pull']['accessory']),
                'lower_accessory': random.choice(exercises['lower_body']['accessory'])

            }
        elif days == 4 or days == 5:
            if day % 2 == 1: # 
                workout_plan[f"Day {day}"] = {
                    'upper_push': random.choice(exercises['upper_body']['push']['vertical']),
                    'upper_push': random.choice(exercises['upper_body']['push']['horizontal']),
                    'upper_pull': random.choice(exercises['upper_body']['pull']['vertical']),
                    'upper_pull': random.choice(exercises['upper_body']['pull']['horizontal']),
                    'upper_accessory': random.choice(exercises['upper_body']['accessory']),
                }
            else: # Leg day
                workout_plan[f"Day {day}"] = {
                    'lower_push': random.choice(exercises['lower_body']['push']),
                    'lower_pull': random.choice(exercises['loweer_body']['pull']),
                    'accessory_1': random.choice(exercises['lower_body']['accessory']),
                    'accessory_2': random.choice(exercises['lower_body']['accessories'])
                }

        else: # If days a week is above 5
            if day % 3 == 1: # push/pull/legs - Pull day
                workout_plan[f"day {day}"] = {
                     'upper_pull': random.choice(exercises['upper_body']['pull']['vertical']),
                     'upper_pull': random.choice(exercises['upper_body']['pull']['horizontal']),
                     'accessory_1': random.choice(exercises['upper_body']['pull']['accessory']),
                     'accessory_2': random.choice(exercises['upper_body']['pull']['accessory'])
                }
            elif day % 3 == 0: #Push day
                workout_plan[f"day {day}"] = {
                    'upper_push': random.choice(exercises['upper_boy']['push']['horizontal']),
                    'upper_push': random.choice(exercises['upper_body']['push']['vertical']),
                    'accessory_1': random.choice(exercises['upper_body']['push']['accessory']),
                    'accessory_2': random.choice(exercises['upper_body']['push']['accessory'])

                }
            else: #Leg day
                workout_plan[f"day {day}"] = {
                    'lower_push': random.choice(exercises['lower_body']['push']),
                    'lower_pull': random.choice(exercises['lower_body']['pull']),
                    'accessory_1': random.choice(exercises['lower_body']['accessory']),
                    'accessory_2': random.choice(exercises['lower_body']['accessory'])

                }

    for day, workout in workout_plan.items():
        for exercise in workout:
            sets, reps = sets_and_reps(goal)
            workout[exercise] = (workout[exercise], f"{sets} sets of {reps} reps")

    return workout_plan


days, goal = user_form()
workout_plan = generate_workout_plan(exercises, days, goal)


print("\nYour customized workout plan:")
for day, exercise in workout_plan.items():
    print(f"\n{day}:")
    for exercise, details in exercise.items():
        print(f"- {exercise.capitalize()}: {details[0]} ({details[1]})")
            

    

    


