from random import sample

print(f'''
{"="*50}
            ROCK PAPER SCISSORS
{"="*50}
''')
while True:
    answer = input("Enter ROCK/PAPER/SCISSORS --> ")
    if answer.upper() not in ["ROCK", "PAPER", "SCISSORS"]:
        print()
        print("Something went wrong. Let's try one more time.")
        continue
    break
print()
print("     Player choosed ", answer)

comp_choise = sample(["ROCK", "PAPER", "SCISSORS"], 1)[0]
print("     Computer choosed ", comp_choise)

print()

if answer == comp_choise:
    print("Draw - no winners")
elif (answer == "ROCK" and comp_choise == "SCISSORS") or (answer == "PAPER" and comp_choise == "ROCK") or (answer == "SCISSORS" and comp_choise == "PAPER"):
    print("Player wins!")
else:
    print("Computer wins!")