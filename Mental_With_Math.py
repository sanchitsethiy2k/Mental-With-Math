import csv
import os
import time
import sys
import random
from tabulate import tabulate

class Test:
    def __init__(self, name, level, timemode):
        self.name = name
        self.level = level
        self.timemode = timemode

    @classmethod
    def get_test_type(cls, name):
        print("")
        print("Kindly choose the NUMBER corresponding to the LEVEL you want to attempt.")
        print("")
        print("""1. Level 1: Beginner
2. Level 2: Intermediate
3. Level 3: Advanced""")

        while True:
            try:
                print("")
                level = int(input("Level (1, 2, 3): "))
                if not level in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("")
                print("Invalid Level Inputted (Did you input the NUMBER corresponding to the Level you want to attempt)")
                continue

        print("")
        print(f"Level {level} selected")

        print("")
        print("Kindly choose the NUMBER corresponding to the Timemode you want.")
        print("")
        print("""1. 1 min
2. 3 mins
3. 5 mins""")

        while True:
            try:
                print("")
                timemode = int(input("Timemode (1, 2, 3): "))
                if not timemode in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("")
                print("Invalid Timemode Inputted (Did you input the NUMBER corresponding to the Timemode you want)")
                continue
        times = [1, 3, 5]
        print("")
        print(f"{times[timemode - 1]} min Timemode Chosen")
        return cls(name, level, times[timemode-1])

    def test_and_csv(self):
        n = 0
        m = 0
        add_ques = 0
        add_inc = 0
        sub_ques = 0
        sub_inc = 0
        mul_ques = 0
        mul_inc = 0
        div_ques = 0
        div_inc = 0
        perc_ques = 0
        perc_inc = 0

        wrong_ans = []
        time_list = []
        print("")
        print("INSTRUCTION: Answer Upto 2 Decimal Points If Applicable")
        print("")
        start_time = time.perf_counter()
        

        while time.perf_counter() - start_time < self.timemode * 60:

            if self.level == 1:
                w = [40, 30, 20, 10, 0]
                a = random.randint(1, 10)
                b = random.randint(1, 10)

            elif self.level == 2:
                w = [20, 20, 30, 20, 10]
                a = random.randint(11, 99)
                b = random.randint(11, 99)
                c = random.randint(1, 99)
                d = random.randint(1, 99)

            elif self.level == 3:
                w = [10, 10, 30, 30, 20]
                a = random.randint(100, 999)
                b = random.randint(100, 999)
                c = random.randint(1, 99)
                d = random.randint(100, 999)
            

            op = random.choices(["+", "-", "x", "/", "%"], weights = w)[0]
            if op != "%":

                try:
                    start_ques = time.perf_counter()
                    user_ans = float(input(f"Q{m + 1} {a} {op} {b} = "))
                    end_ques = time.perf_counter()
                except ValueError:
                    continue

                if op == "+":
                    if user_ans != a + b:
                        n += 1
                        add_inc += 1
                        wrong_ans.append(f"Q{m+1} {user_ans} ==> X, {a + b} ==> ✓")
                    m += 1
                    add_ques += 1
                elif op == "-":
                    if user_ans != a - b:
                        n += 1
                        sub_inc += 1
                        wrong_ans.append(f"Q{m+1} {user_ans} ==> X, {a - b} ==> ✓")
                    m += 1
                    sub_ques += 1
                elif op == "x":
                    if user_ans != a * b:
                        n += 1
                        mul_inc += 1
                        wrong_ans.append(f"Q{m+1} {user_ans} ==> X, {a * b} ==> ✓")
                    m += 1
                    mul_ques += 1
                elif op == "/":
                    if user_ans != round(a/b, 2):
                        n += 1
                        div_inc += 1
                        wrong_ans.append(f"Q{m+1} {user_ans} ==> X, {round(a / b, 2)} ==> ✓")
                    m += 1
                    div_ques += 1

            elif op == "%":

                try:
                    start_ques = time.perf_counter()
                    user_ans = float(input(f"Q{m+1} {c}{op} of {d} = "))
                    end_ques = time.perf_counter()
                except ValueError:
                    continue

                if user_ans != round((c/100) * d, 2):
                    n += 1
                    perc_inc += 1
                    wrong_ans.append(f"Q{m+1}, {user_ans} ==> X, {round((c/100) * d, 2)} ==> ✓")
                m += 1
                perc_ques += 1

            time_list.append(end_ques - start_ques)
        time_sum = 0
        for t in time_list:
            time_sum += t
        time_avg = str(round(time_sum / len(time_list), 2)) if len(time_list) != 0 else "N/A"
        accuracy = str(round(100 - ((n/m) * 100), 2)) + "%" if m != 0 else "N/A"
        add_acc = str(round(100 - (add_inc/add_ques) * 100, 2)) + "%" if add_ques != 0 else "N/A"
        sub_acc = str(round(100 - (sub_inc/sub_ques) * 100, 2)) + "%" if sub_ques != 0 else "N/A"
        mul_acc = str(round(100 - (mul_inc/mul_ques) * 100, 2)) + "%" if mul_ques != 0 else "N/A"
        div_acc = str(round(100 - (div_inc/div_ques) * 100, 2)) + "%" if div_ques != 0 else "N/A"
        perc_acc = str(round(100 - (perc_inc/perc_ques) * 100, 2)) + "%" if perc_ques != 0 else "N/A"


        print("")
        print("*****************************************")
        print("RESULTS")
        print("")
        print(f"Score: {((m - n) * 4) - n}")
        print(f"Total Question Attempted: {m}")
        print(f"No. Correct Ans: {m-n}")
        print(f"No. Incorrect Ans: {n}")
        print(f"Total Accuracy: {accuracy}")
        print(f"Avg Time Taken Per Ques: {time_avg} secs")
        print("*****************************************")

        while True:
            try:
                print("")
                add_stats = input("Do you wish to see deeper insights into your performance and the ques you got WRONG? (Y/N): ").upper().strip()
                if add_stats not in ["Y", "N", "YES", "NO"]:
                    raise ValueError
                break
            except ValueError:
                print("")
                print("Invalid Input. Kindly ans with 'Y' or 'N'")
                continue

        if add_stats == "Y" or add_stats == "YES":
            print("")
            print("**********************************************")
            print("")
            for ques in wrong_ans:
                print(ques)
                print("")
            print("**********************************************")
            print("")
            print(f"Accuracy on ADDITION Questions: {add_acc}")
            print(f"Accuracy on SUBTRACTION Questions: {sub_acc}")
            print(f"Accuracy on MULTIPLICATION Questions: {mul_acc}")
            print(f"Accuracy on DIVISION Questions: {div_acc}")
            print(f"Accuracy on PERCENTAGE COMPUTATION Questions: {perc_acc}")

        with open(f"{self.name}.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames = ["Lvl", "TM", "Score", "Total Qs Attempt", "Correct Ans", "Incorrect Ans", "Net Accuracy", "Avg Time/Q", "Accuracy '+' Qs", "Accuracy '-' Qs", "Accuracy 'x' Qs", "Accuracy '/' Qs", "Accuracy '%' Qs"])
            #here, i want the username to be appended to the username list iff they have completed atleast one game and i have done this only when file.tell == 0 because otherwise u would get duplicate entries in Username.csv
            if file.tell() == 0:
                with open("Username.csv", "a") as file_:
                    writer_ = csv.DictWriter(file_, fieldnames= ["Name"])
                    if file_.tell() == 0:
                        writer_.writeheader()
                    writer_.writerow({"Name": self.name})
                writer.writeheader()
            writer.writerow({"Lvl": self.level, "TM": self.timemode, "Score": ((m - n) * 4) - n, "Total Qs Attempt": m, "Correct Ans": m-n, "Incorrect Ans": n, "Net Accuracy": accuracy, "Avg Time/Q": time_avg, "Accuracy '+' Qs": add_acc, "Accuracy '-' Qs": sub_acc, "Accuracy 'x' Qs": mul_acc, "Accuracy '/' Qs": div_acc, "Accuracy '%' Qs": perc_acc})


        


class User:
    def __init__(self, name_list, leaderboard_1, leaderboard_2, leaderboard_3):
        self.name_list = name_list
        self.leaderboard_1 = leaderboard_1
        self.leaderboard_2 = leaderboard_2
        self.leaderboard_3 = leaderboard_3

    @classmethod
    def get_lists(cls):
        name_list = []
        leaderboard_1 = []
        leaderboard_2 = []
        leaderboard_3 = []

        with open("Username.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_list.append(row)

        for name in name_list:
            score_1 = []
            score_2 = []
            score_3 = []
            with open(f"{name['Name']}.csv") as file_:
                reader_ = csv.DictReader(file_)
                for line in reader_:
                    if line["Lvl"] == "1":
                        score_1.append({"Name": name["Name"], "Level": line["Lvl"], "Timemode": line["TM"], "Score": int(line["Score"])})
                    elif line["Lvl"] == "2":
                        score_2.append({"Name": name["Name"], "Level": line["Lvl"], "Timemode": line["TM"], "Score": int(line["Score"])})
                    elif line["Lvl"] == "3":
                        score_3.append({"Name": name["Name"], "Level": line["Lvl"], "Timemode": line["TM"], "Score": int(line["Score"])})

            if len(score_1) > 0:
                score_1 = sorted(score_1, key = lambda line: line["Score"], reverse = True)
                leaderboard_1.append(score_1[0])

            if len(score_2) > 0:
                score_2 = sorted(score_2, key = lambda line: line["Score"], reverse = True)
                leaderboard_2.append(score_2[0])

            if len(score_3) > 0:
                score_3 = sorted(score_3, key = lambda line: line["Score"], reverse = True)
                leaderboard_3.append(score_3[0])

        leaderboard_1 = sorted(leaderboard_1, key = lambda line: line["Score"], reverse = True)
        leaderboard_2 = sorted(leaderboard_2, key = lambda line: line["Score"], reverse = True)
        leaderboard_3 = sorted(leaderboard_3, key = lambda line: line["Score"], reverse = True)

        for i in range(len(leaderboard_1)):
            row = leaderboard_1[i]
            leaderboard_1[i] = {"Position": i + 1, "Name": row["Name"], "Level": row["Level"], "Timemode": row["Timemode"], "Score": row["Score"]}
        for i in range(len(leaderboard_2)):
            row = leaderboard_2[i]
            leaderboard_2[i] = {"Position": i + 1, "Name": row["Name"], "Level": row["Level"], "Timemode": row["Timemode"], "Score": row["Score"]}

        for i in range(len(leaderboard_3)):
            row = leaderboard_3[i]
            leaderboard_3[i] = {"Position": i + 1, "Name": row["Name"], "Level": row["Level"], "Timemode": row["Timemode"], "Score": row["Score"]}


        return cls(name_list, leaderboard_1, leaderboard_2, leaderboard_3)

    def leaderboard(self):
        if len(self.leaderboard_1) > 0 or len(self.leaderboard_2) > 0 or len(self.leaderboard_3) > 0:

            if len(self.leaderboard_1) > 0:
                print("")
                print("LEADERBOARD FOR LEVEL 1: BEGINNER")
                print(tabulate(self.leaderboard_1, headers="keys", tablefmt="heavy_grid"))
            else:
                print("")
                print("NOTICE: NO LEADERBOARD DATA FOUND FOR LEVEL 1")
            
            if len(self.leaderboard_2) > 0:
                    print("")
                    print("LEADERBOARD FOR LEVEL 2: INTERMEDIATE")
                    print(tabulate(self.leaderboard_2, headers="keys", tablefmt="heavy_grid"))
            else:
                print("")
                print("NOTICE: NO LEADERBOARD DATA FOUND FOR LEVEL 2")

            if len(self.leaderboard_3) > 0:
                print("")
                print("LEADERBOARD FOR LEVEL 3: ADVANCED")
                print(tabulate(self.leaderboard_3, headers="keys", tablefmt="heavy_grid"))
            else:
                print("")
                print("NOTICE: NO LEADERBOARD DATA FOUND FOR LEVEL 3")

        else:
            print("NOTICE: NO LEADERBOARD DATA FOUND")



def main():
    print("")
    print("Welcome To Mental With Math, make math a lil less infuriating while improving mental calculations....")
    while True:
        try:
            print("")
            name = input("Enter Username: ").title()
            if not name or name.isnumeric():
                raise ValueError
            break
        except ValueError:
            print("")
            print("Invalid Name")
            continue


    

    while True:
        print("")
        print("Kindly choose the NUMBER corresponding to the feature you want to use.")
        print("")
        print("""1. Play
2. Detailed Performance Stat History For Nerds
3. Leaderboard For Cool Top Achievers
4. Exit""")
        while True:
            try:
                print("")
                option = int(input("Option: "))
                if not option in [1, 2, 3, 4]:
                    raise ValueError
                break
            except ValueError:
                print("")
                print("Invalid Option (Did you choose the NUMBER corresponding to the option?)")
        if option == 1:
            test = Test.get_test_type(name)
            test.test_and_csv()

        elif option == 2:
            user_stats = []
            file_exists = os.path.exists(f"{name}.csv")

            if file_exists:
                with open(f"{name}.csv") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        user_stats.append(row)
                print("")
                print(tabulate(reversed(user_stats), headers = "keys", tablefmt = "simple"))
                print("")
                print("NOTE: TM => Time Mode in mins.")

            else:
                print("")
                print("No gameplay history found")


        elif option == 3:
            user = User.get_lists()
            user.leaderboard()

                          
                          
            
        elif option == 4:
            print("")
            print("Hope to see you soon. Stay Sharp.")
            sys.exit("")

if __name__ == "__main__":
    main()
