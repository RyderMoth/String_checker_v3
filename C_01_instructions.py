# checks user enter yes (y) or (no)

def yes_no(question):
    while True:
        response = input(question).lower()

        # check the user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response =="no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


# Display instructions
def instructions():
    print('''
    
*** Instruction ***
  
  To begin, choose the number of rounds (or p
  infinite mode).
  
  Then play against the computer. You need to
  P (paper) or S (scissors).
  
  The rules are ass follows:
      Paper beats rock
      Rock beats scissors
      Scissors beats paper

Good Luck! 
    ''')

# Main routine
print()
print("💎📰✂️ Rock / Paper/ Scissors Game ✂️📰💎")
print()

#ask user if they want instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")
