from pyfiglet import Figlet
import sys
import csv
from fuzzywuzzy import process
from fpdf import FPDF
from datetime import datetime
import json
import os


def main():
    f = Figlet(font="smslant")
    print(f.renderText("Welcome to your Nutrition App"))
    food_diary, day = load_food_diary()
    get_choice(food_diary, day)


def get_choice(food_diary, day):
    time = datetime.now().strftime("%Y-%m-%d")
    food_diary, day = load_food_diary()

    data_base = get_data_base()

    while True:
        try:
            choice = (
                input(
                    "Do you want to add a food on the diary or create a report? <Diary/Report/Exit>: "
                )
                .strip()
                .lower()
            )
            match choice:
                case "diary":
                    f = Figlet(font="smslant")
                    print(f.renderText(f"Food Diary - Day: {day}"))
                    while True:
                        food_name, food_quantity = get_food()

                        if food_name == "exit":
                            next_day = input("Would you like to move on to the next day?<Y/n>").lower().strip()
                            if next_day == "y":
                                day += 1
                            elif next_day == "n":
                                pass
                            else:
                                continue
                            save_food_diary(food_diary,day)
                            break

                        get_food_info(
                            food_name, food_quantity, data_base, food_diary, day
                        )

                case "report":
                    show_report(food_diary, time)
                    sys.exit()

                case "exit":
                    sys.exit("You exited program")

        except ValueError:
            print("Error")
            continue


def get_data_base():
    data_base = {}

    with open("/workspaces/93020764/cs50p_problems/final_project/project/data/nutrition.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_base[row["name"].lower().strip()] = {
                "calories": float(row["calories"]),
                "serving_size": (float(row["serving_size"].replace(" g", ""))),
                "protein": (
                    float(row["protein"].replace(" g", ""))
                    if "protein" in row
                    else 0
                ),
                "carbs": (
                    float(row["carbohydrate"].replace(" g", ""))
                    if "carbohydrate" in row
                    else 0
                ),
                "fats": (
                    float(row["total_fat"].replace("g", ""))
                    if "total_fat" in row
                    else 0
                ),
            }

    return data_base


def get_food():
    data_base = get_data_base()
    while True:
        food = (
            input(f"Enter Food <Name> or type <Exit> to finish for the day: ")
            .lower()
            .strip()
        )
        match food:
            case "exit":
                return "exit", None

            case _:

                all_foods = list(data_base.keys())
                matches = process.extract(food, all_foods, limit=5)

                food_matches = []
                for match, score in matches:
                    if score >= 80:
                        food_matches.append((match, score))

                if not food_matches:
                    print("No matching foods found")
                    continue

                print("Matching Foods: ")

                for rank, (match, score) in enumerate(food_matches, start=1):
                    print(f"{rank}. {match}")

                try:
                    food_choice = int(
                        input(
                            "Choose the number of the closest match or enter 0 to put a different food: "
                        )
                    )

                    if food_choice == 0:
                        continue

                    if 0 < food_choice <= len(food_matches):
                        food_name = food_matches[food_choice - 1][0]
                        food_quantity = float(
                            input(f"Enter quantity for {food_name} in grams: ")
                        )

                        if food_quantity <= 0:
                            print("Invalid input")
                            continue

                        return food_name, food_quantity

                    else:
                        print("Invalid input")
                        continue

                except ValueError:
                    print("Invalid input")
                    continue


def get_food_info(food_name, food_quantity, data_base, food_diary, day):
    food_info = data_base[food_name]
    real_quantity = food_quantity / food_info["serving_size"]
    diary = {
        "food": food_name,
        "quantity": food_quantity,
        "calories": round(food_info["calories"] * real_quantity),
        "protein": round(food_info["protein"] * real_quantity),
        "carbs": round(food_info["carbs"] * real_quantity),
        "fats": round(food_info["fats"] * real_quantity),
    }
    if str(day) not in food_diary:
        food_diary[str(day)] = []
    food_diary[str(day)].append(diary)


def save_food_diary(food_diary, day):
    data = {"diary": food_diary, "day": day}
    with open("food_diary.json", "w") as file:
        json.dump(data, file)


def load_food_diary():
    if os.path.exists("food_diary.json"):
        with open("food_diary.json", "r") as file:
            data = json.load(file)
            return data["diary"], data.get("day", 1)
    return {}, 1


def show_report(food_diary, time):
    if os.path.exists("food_diary.pdf"):
        os.remove("food_diary.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_font("helvetica", style="B", size=20)

    pdf.cell(0, 10, "Food Diary", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(8)

    for day, foods in food_diary.items():
        pdf.set_font("helvetica", style="B", size=15)
        pdf.cell(0, 10, f"Day:{day}")
        pdf.ln(6)
        pdf.cell(0, 10, f"{time}")
        pdf.ln(5)

        total_calories = 0
        total_proteins = 0
        total_carbs = 0
        total_fats = 0

        for food in foods:
            pdf.set_font("helvetica", size=13)
            pdf.cell(0, 10, text=f"**Food:** {food['food']}", markdown=True)
            pdf.ln(5)
            pdf.cell(
                0, 10, text=f"**Quantity:** {food['quantity']:.1f} grams", markdown=True
            )
            pdf.ln(5)
            pdf.cell(
                0, 10, text=f"**Calories:** {food['calories']:.1f} kcal", markdown=True
            )
            pdf.ln(5)
            pdf.cell(
                0,
                10,
                text=f"**Protein:** {food['protein']:.1f} g, **Carbs:** {food['carbs']:.1f} g, **Fats:** {food['fats']:.1f} g",
                markdown=True,
            )
            pdf.ln(10)

            total_calories += food["calories"]
            total_proteins += food["protein"]
            total_carbs += food["carbs"]
            total_fats += food["fats"]

        pdf.cell(0, 10, text=f"**Total Calories:** {total_calories:.1f}", markdown=True)
        pdf.ln(5)
        pdf.cell(
            0,
            10,
            text=f"**Total Macros: Protein:** {total_proteins:.1f} g, **Carbs:** {total_carbs:.1f} g, **Fats:** {total_fats:.1f} g",
            markdown=True,
        )
        pdf.ln(15)
    pdf.output("food_diary.pdf")
    print("PDF Created: food_diary.pdf")


if __name__ == "__main__":
    main()
