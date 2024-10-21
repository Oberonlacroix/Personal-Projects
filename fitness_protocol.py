from exercise_generator import generate_workout_plan, user_form
from exercise_generator import exercises
from food_data import data
import random

""" A programme to generate a fitness protocol """


class Trainer:
    """
    A class to represent a personal trainer.

    Attributes:
        name (str): The name of the trainer.
        fee (int): The fee charged by the trainer per session.
    """

    def __init__(self, name, fee):
        """
        Initializes a Trainer instance.

        Parameters:
            name (str): The name of the trainer.
            fee (int): The fee charged per session.
        """
        self.name = name
        self.fee = fee

    def book_sessions(self, days_num):
        """
        Books workout sessions for a client based on the number of days.

        Parameters:
            days_num (int): The number of days for which sessions are booked.
            client (Client): The client who is booking the sessions.

        Returns:
            list: A list of days for the scheduled workouts.
        """
        # Converting number of days to int
        days_num = int(days_num)
        workout_days = []
        days_of_the_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        # Scheduling workout days based on the number of days provided

        if days_num == 2:  # If 2 days a week to workout: Monday and Thursday selected
            workout_days.extend([days_of_the_week[0], days_of_the_week[3]])
        elif (
            days_num == 3
        ):  # If 3 days a week to workout: Monday, Wednesday and Friday selected
            workout_days.extend(
                [days_of_the_week[0], days_of_the_week[2], days_of_the_week[3]]
            )
        elif (
            days_num == 4
        ):  # If 4 days a week to workout: Monday, Tuesday, Thursday and Friday selected
            workout_days.extend(
                [
                    days_of_the_week[0],
                    days_of_the_week[1],
                    days_of_the_week[3],
                    days_of_the_week[4],
                ]
            )
        elif days_num == 5:  # If 5 days a week to workout: Monday - Friday selected
            workout_days.extend(
                [
                    days_of_the_week[0],
                    days_of_the_week[1],
                    days_of_the_week[2],
                    days_of_the_week[4],
                    days_of_the_week[5],
                ]
            )
        elif days_num == 6:  # If 6 days a week to workout: Monday - Saturday Selected
            workout_days.extend([days_of_the_week[:-1]])
        elif days_num == 7:  # If 7 days a week to workout: All week selected
            workout_days.extend([days_of_the_week])
        else:
            print("Theres only 7 days in the week!")

        return workout_days

    def calculate_cost(self, session_num, fee):
        """
        Calculates the total cost for the booked sessions.

        Parameters:
            session_num (int): The number of sessions booked.
            fee (int): The fee charged per session.

        Returns:
            The total cost of the sessions.
        """
        # Calculating total coast of sessions per week
        total = int(session_num * fee)
        return total

    def plan_workout(self):
        """
        Plans a workout for the trainer.

        Returns:
            dict: A generated workout plan.
        """
        # Instantiating a Workout object and generating the workout plan
        self.workout_instance = Workout()
        workout_data = self.workout_instance.generate()
        return workout_data


class Client:
    """
    A class to represent a client.

    """

    def __init__(self, name, age_yrs, height_cm, weight_kg, sex, weight_goal):
        self.name = name
        self.age = age_yrs
        self.height = height_cm
        self.weight = weight_kg
        self.sex = sex
        self.weight_goal = weight_goal


class Workout:
    """
    A class to represent a workout plan.
    """

    def __init__(self):
        """
        Initializes a Workout instance and collects user input for workout days and goals.

        """
        self.days, self.goal = user_form()
        self.workout_plan = None

    def generate(self):
        """
        Generates a workout plan based on the user's input.

        Returns:
          dict: The generated workout plan.
        """
        # Generates a workout plan based on user input from an imported function
        self.workout_plan = generate_workout_plan(exercises, self.days, self.goal)
        return self.workout_plan


class MealPlan:
    """
    A class to represent a meal plan.

    Methods:
        calorie_calculator: Calculates daily calorie needs based on BMR.
        meal_plan_generator: Generates a meal plan based on calorie needs.
    """

    def calorie_calculator(self, age, height, weight, sex, weight_goal):
        """
        Calculates calorie requirements for client based on attributes and goal

        parameters:
          age(int): age in yrs
          height(int): Height in cm
          weight(int): Weight in kg
          sec(str): Biological sex of client

        returns:
          Appropiate calories for the client

        """

        # BMR calculation based on gender
        if sex == "male":
            BMR = int(10 * weight + 6.25 * height - 5 * age + 5)
        else:
            BMR = int(10 * weight + 6.25 * height - 5 * age - 161)

        # Calorie needs based on goal (weight loss/ weight gain or maintain)
        maintenance_calories = BMR * 1.55
        weight_loss_calories = maintenance_calories - 400
        weight_gain_calories = maintenance_calories + 400

        # Returning calories based on the client's goal
        if weight_goal.lower() == "weight loss":
            return weight_loss_calories
        elif weight_goal.lower() == "weight gain":
            return weight_gain_calories
        elif weight_goal.lower() == "maintain":
            return maintenance_calories

    def meal_plan_generator(self, calories):
        """
        Generates a meal plan based on daily caloric needs.

        Parameters:
           calories (float): The daily caloric intake for the meal plan.

        Returns:
           list: A list of meals for the meal plan.
        """

        food_data = data  # Imported food data
        meal_calories = calories // 3  # Dividing daily calories into 3 equal meals

        # Sorting food into lists by category from imported data
        protein_sources = [food for food in food_data if food["Category"] == "Protein"]
        carb_sources = [
            food for food in food_data if food["Category"] == "Carbohydrate"
        ]
        fat_sources = [food for food in food_data if food["Category"] == "Fat"]
        vegetable_sources = [
            food for food in food_data if food["Category"] == "Vegetable"
        ]

        meal_plan = []

        # Looping to generate 3 meals per day
        for meal_num in range(3):

            meal = {"Meal": f"Meal {meal_num + 1}"}
            # Randomly selection food from each category
            protein = random.choice(protein_sources)
            carb = random.choice(carb_sources)
            fat = random.choice(fat_sources)
            vegetable = random.choice(vegetable_sources)

            # Defining serving sizes, based on general guidelines/recommendations
            serving_sizes = {
                "Protein": 150,
                "Carbohydrate": 200,
                "Fat": 30,
                "Vegetable": 100,
            }
            # Calculating total meal calories
            total_meal_calories = (
                (protein["Calories (kcal)"] * serving_sizes["Protein"] / 100)
                + (carb["Calories (kcal)"] * serving_sizes["Carbohydrate"] / 100)
                + (fat["Calories (kcal)"] * serving_sizes["Fat"] / 100)
                + (vegetable["Calories (kcal)"] * serving_sizes["Vegetable"] / 100)
            )

            # Adjusting serving sizes to match the desired meal caloric intake
            portion_factor = meal_calories / total_meal_calories

            # Adding each food group with adjusted servings to the meal
            meal["Protein"] = {
                "Food": protein["Food"],
                "Serving (g)": serving_sizes["Protein"] * portion_factor,
                "Calories (kcal)": protein["Calories (kcal)"]
                * serving_sizes["Protein"]
                / 100
                * portion_factor,
            }

            meal["Carbohydrate"] = {
                "Food": carb["Food"],
                "serving (g)": serving_sizes["Carbohydrate"] * portion_factor,
                "Calories (kcal)": carb["Calories (kcal)"]
                * serving_sizes["Carbohydrate"]
                / 100
                * portion_factor,
            }

            meal["Fat"] = {
                "Food": fat["Food"],
                "serving (g)": serving_sizes["Fat"] * portion_factor,
                "Calories (kcal)": fat["Calories (kcal)"]
                * serving_sizes["Fat"]
                / 100
                * portion_factor,
            }

            meal["Vegetables"] = {
                "Food": vegetable["Food"],
                "serving (g)": serving_sizes["Vegetable"] * portion_factor,
                "Calories (kcal)": vegetable["Calories (kcal)"]
                * serving_sizes["Vegetable"]
                / 100
                * portion_factor,
            }

            meal["Total Calories"] = (
                meal["Protein"]["Calories (kcal)"]
                + meal["Carbohydrate"]["Calories (kcal)"]
                + meal["Fat"]["Calories (kcal)"]
                + meal["Vegetables"]["Calories (kcal)"]
            )

            meal_plan.append(meal)

        return meal_plan


John = Trainer("John Merchant", 50)
Bob = Client("Bob Righteous", 35, 189, 85, "male", "weight loss")
bobs_meal_plan = MealPlan()

the_workout = John.plan_workout()

bobs_schedule = John.book_sessions(John.workout_instance.days)

bobs_cost = John.calculate_cost(3, John.fee)

bobs_calories = bobs_meal_plan.calorie_calculator(
    Bob.age, Bob.height, Bob.weight, Bob.sex, Bob.weight_goal
)

bobs_meals = bobs_meal_plan.meal_plan_generator(bobs_calories)


print("\nWorkout Plan: ")
for day, exercises in the_workout.items():
    print(f"{day}:")
    for exercise, details in exercises.items():
        print(f" -{exercise.capitalize()}: {details[0]} ({details[1]})")


print("\nWorkout Schedule: ")
print("Days scheduled for workouts:")
for day in bobs_schedule:
    print(day)

print(f"Total cost per week of training: £{bobs_cost}")

print("\nMeal Plan: ")
for meal in bobs_meals:
    print(f"\n{meal['Meal']}:")
    print(
        f"  Protein: {meal['Protein']['Food']} serving: ({round(meal['Protein']['Serving (g)'])}g, ({round(meal['Protein']['Calories (kcal)'])} kcal)"
    )
    print(
        f"  Carbohydrate: {meal['Carbohydrate']['Food']} serving: ({round(meal['Carbohydrate']['serving (g)'])}g, {round(meal['Carbohydrate']['Calories (kcal)'])} kcal)"
    )
    print(
        f"  Fat: {meal['Fat']['Food']} serving: ({round(meal['Fat']['serving (g)'])}g, {round(meal['Fat']['Calories (kcal)'])} kcal)"
    )
    print(
        f"  Vegetables: {meal['Vegetables']['Food']} serving: ({round(meal['Vegetables']['serving (g)'])}g, {round(meal['Vegetables']['Calories (kcal)'])} kcal)"
    )
    print(f"  Total Calories: {round(meal['Total Calories'])} kcal")
