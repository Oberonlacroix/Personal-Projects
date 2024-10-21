import random

""" A programme to generate a workout plan """

# Dict storing potential exercises
exercises = {
    "upper_body": {
        "push": {
            "vertical": [
                "Dumbbell Shoulder Press",
                "Barbell Overhead Press",
                "Plate Loaded Shoulder Press Machine",
            ],
            "horizontal": [
                "Barbell Bench Press",
                "Dumbbell Bench Press",
                "Parallel Bar Dips",
                "Push Ups",
                "Ring Push Ups",
                "Incline Dumbbell Bench",
                "Incline Barbell Bench",
                "Chest Press Machine",
            ],
            "accessory": [
                "Dumbbell Lateral Raise",
                "Dumbell Chest Fly",
                "Machine Fly",
                "Unilateral Cable Fly",
                "Cable Tricep Pushdown",
                "Barbell Skull crushers",
                "Overhead Cable Tricep Extension",
                "Close Grip Push Up",
            ],
        },
        "pull": {
            "vertical": [
                "Pull up",
                "Wide Grip Pull Up",
                "Chin Up",
                "Wide Grip Lat' Pulldown",
                "Supinated Lat' Pulldown",
            ],
            "horizontal": [
                "Barbell Row",
                "Landmine Row",
                "Ring Row",
                "Chest Supported Machine Row",
                "Unilateral Dumbell Row",
                "Cable Row",
            ],
            "accessory": [
                "Straight Arm Lat Pulldown",
                "Dumbell Pullover",
                "Cable Facepull",
                "Machine Rear Delt' Fly",
                "Barbell Curl",
                "Incline Dumbell Curl",
                "Dumbell Hammer Curl",
                "Cable Rope Hammer Curl",
                "Preacher Curl",
            ],
        },
    },
    "lower_body": {
        "push": [
            "High Bar Barbell Squat",
            "ATG Split Squat",
            "Heal Elevated Goblet Squat",
            "Barbell Front Squat",
        ],
        "pull": [
            "Barbell Deadlift",
            "Romanian Deadlift",
            "Rack Pull",
            "Hyper Extensions",
        ],
        "accessory": ["Lying Hamstring Curl", "Tib Raises", "Backwards Sled Pulling"],
    },
}


def user_form():
    """
    takes user input.

    returns days to work out each week and goal (strength/hypertrophy)

    """
    days = int(input("howmany days a week does the client want to work out? "))
    goal = input("What is his/her goal? strength or hypertrophy? ")

    return days, goal


def sets_and_reps(goal):
    """
    Takes goal from and applies appropriate sets and reps accoridngly

    parameters:
        goal(str): client goal (strength/hypertrophy)


    """

    # Choosing appropriate set and rep range for goal
    if goal.lower() == "strength":
        return random.randint(3, 5), random.randint(3, 6)
    elif goal.lower() == "hypertrophy":
        return random.randint(3, 4), random.randint(8, 15)
    else:
        print(f" {goal} is not one of the options")


def generate_workout_plan(exercises, days, goal):
    """
    Creates workout plan

    parameters:
        exercises(dict): potential exercises for selection
        days(int): Number of days to work out each week
        goal(str): Weight training goal (strength/hypertrophy)

        returns:
            Workout plan

        Additional info: Workout structure changes depending on amount of days stated



    """

    workout_plan = {}

    # Iterating over number of days a week and creating a workout for each day
    for day in range(1, days + 1):

        # If the workout plan is 1-3 days, create a full-body workout (push/pull/legs)
        if day <= 3:
            workout_plan[f"Day {day}"] = {
                "upper_push": random.choice(
                    exercises["upper_body"]["push"]["vertical"]
                ),
                "upper_pull": random.choice(
                    exercises["upper_body"]["pull"]["horizontal"]
                ),
                "lower_push": random.choice(exercises["lower_body"]["push"]),
                "push_accessory": random.choice(
                    exercises["upper_body"]["push"]["accessory"]
                ),
                "pull_accessory": random.choice(
                    exercises["upper_body"]["pull"]["accessory"]
                ),
                "lower_accessory": random.choice(exercises["lower_body"]["accessory"]),
            }
        # For 4-5 days a week, alternate between upper body and lower body focused workout
        elif days == 4 or days == 5:
            if day % 2 == 1:  # Odd days for upper body push/pull
                workout_plan[f"Day {day}"] = {
                    "upper_push": random.choice(
                        exercises["upper_body"]["push"]["vertical"]
                    ),
                    "upper_push": random.choice(
                        exercises["upper_body"]["push"]["horizontal"]
                    ),
                    "upper_pull": random.choice(
                        exercises["upper_body"]["pull"]["vertical"]
                    ),
                    "upper_pull": random.choice(
                        exercises["upper_body"]["pull"]["horizontal"]
                    ),
                    "upper_accessory": random.choice(
                        exercises["upper_body"]["push"]["accessory"]
                    ),
                    "upper_accessory": random.choice(
                        exercises["upper_body"]["pull"]["accessory"]
                    ),
                }
            else:  # Even days for lower body
                workout_plan[f"Day {day}"] = {
                    "lower_push": random.choice(exercises["lower_body"]["push"]),
                    "lower_pull": random.choice(exercises["lower_body"]["pull"]),
                    "accessory_1": random.choice(exercises["lower_body"]["accessory"]),
                    "accessory_2": random.choice(exercises["lower_body"]["accessory"]),
                }

        else:  # If days a week is above 5, alternate between push/pull/leg days
            if day % 3 == 1:  # Pull day
                workout_plan[f"day {day}"] = {
                    "upper_pull": random.choice(
                        exercises["upper_body"]["pull"]["vertical"]
                    ),
                    "upper_pull": random.choice(
                        exercises["upper_body"]["pull"]["horizontal"]
                    ),
                    "accessory_1": random.choice(
                        exercises["upper_body"]["pull"]["accessory"]
                    ),
                    "accessory_2": random.choice(
                        exercises["upper_body"]["pull"]["accessory"]
                    ),
                }
            elif day % 3 == 0:  # Push day
                workout_plan[f"day {day}"] = {
                    "upper_push": random.choice(
                        exercises["upper_body"]["push"]["horizontal"]
                    ),
                    "upper_push": random.choice(
                        exercises["upper_body"]["push"]["vertical"]
                    ),
                    "accessory_1": random.choice(
                        exercises["upper_body"]["push"]["accessory"]
                    ),
                    "accessory_2": random.choice(
                        exercises["upper_body"]["push"]["accessory"]
                    ),
                }
            else:  # Leg day
                workout_plan[f"day {day}"] = {
                    "lower_push": random.choice(exercises["lower_body"]["push"]),
                    "lower_pull": random.choice(exercises["lower_body"]["pull"]),
                    "accessory_1": random.choice(exercises["lower_body"]["accessory"]),
                    "accessory_2": random.choice(exercises["lower_body"]["accessory"]),
                }
    # For each day and workout, assign sets and reps based on user's goal
    for day, workout in workout_plan.items():
        for exercise in workout:
            if exercise != "Backwards Sled Pulling":
                sets, reps = sets_and_reps(goal)
                workout[exercise] = (workout[exercise], f"{sets} sets of {reps} reps")
            else:  # For Sled Pulling, reps is not vald - change to distance covered
                sets, reps = sets_and_reps(goal)
                workout[exercise] = (
                    workout[exercise],
                    f"{sets} sets of 20 metres covered",
                )

    return workout_plan
