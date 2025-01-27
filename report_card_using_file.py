import os
from tabulate import tabulate

def percentage_of_3_marks(phy_mark, che_mark, bio_mark):
    percentage = (phy_mark + che_mark + bio_mark) / 3
    return round(percentage, 2)

n = int(input("Enter the number of students in your class: "))

for i in range(n):
    name = input("Enter your name: ").strip().capitalize()
    phy_mark = int(input("Enter your physics marks: "))
    che_mark = int(input("Enter your chemistry marks: "))
    bio_mark = int(input("Enter your biology marks: "))
    percentage = percentage_of_3_marks(phy_mark, che_mark, bio_mark)

    def report_card_entry(name, phy_mark, che_mark, bio_mark, percentage):
        directory = "E:\\Python\\"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, f"{name}_report_card.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Student Grade Report".center(72, "=") + "\n")
            file.write(f"{'Name':<15}{'Physics':<15}{'Chemistry':<15}{'Biology':<15}{'Percentage':<15}\n")
            file.write("=" * 72 + "\n")
            file.write(f"{name:<15}{phy_mark:<15}{che_mark:<15}{bio_mark:<15}{percentage:<15}\n")
            file.write("=" * 72 + "\n")
            

    report_card_entry(name, phy_mark, che_mark, bio_mark, percentage)
    print(f"Report card for {name} has been saved successfully.")
