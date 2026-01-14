# number_guessing_game_project.py
# Mini Python Game: Build a Number Guessing Game!
# Goal: Practice input(), print(), loops, conditionals, random, and basic error handling

# === STARTER CODE – ONLY THIS IS GIVEN TO YOU =========================
import random
# random is a built-in module that lets us generate random numbers

print("=== Number Guessing Game – Let's build this together! ===")
print("Hint: random.randint(1, 100) gives a random integer from 1 to 100\n")

# === YOUR TURN – Follow the steps below =================================

# Step 1: Create the secret number
# - Use random.randint() to pick a number between 1 and 100
# - Store it in a variable called secret_number
# - (Don't print it – that's cheating!)



# Step 2: Welcome the player
# - Print a friendly welcome message
# - Tell them the range (1 to 100)
# - (Optional: add emojis like 🎲 or 🧠)



# Step 3: Set up a guess counter
# - Create a variable guesses = 0



# Step 4: Create the main game loop
# - Use a while True: loop (infinite until we break out)
# - Inside the loop:
#   a. Ask the player for their guess using input()
#   b. Convert the input to an integer with int()
#      → Tip: for now, assume they type a number. We'll fix crashes later.
#   c. Increase the guesses counter by 1
#   d. Compare the guess to secret_number using if / elif / else:
#      - If equal → print win message + number of guesses + break
#      - If too low → print "Too low! Try higher"
#      - If too high → print "Too high! Try lower"



# Step 5: Test what you have so far
# - Run the file often!
# - Play the game a few times
# - Fix any bugs you see (indentation, typos, logic errors)



# === Stretch Goals – Add these when the basic game works ================

# Stretch A: Handle bad input (most important one!)
# - Wrap the int(guess) in a try: / except ValueError:
# - If they type letters → print "Please enter a number!" and continue (don't count as guess)



# Stretch B: Check the range
# - After converting to int, check if 1 <= guess <= 100
# - If not → print a message and continue (don't count the guess)



# Stretch C: Allow quitting
# - Before converting to int, check if the input.lower() == 'q' or 'quit'
# - If yes → print goodbye message and break (or use return if in a function)



# Stretch D: Play again?
# - After winning (or quitting), ask "Play again? (y/n)"
# - If they say 'y' or 'yes' → restart the whole game (new secret number, reset guesses)
# - Tip: wrap most of your code in a while True: loop and break only when they say no



# Stretch E: Nice touches (if you have time)
# - Use f-strings for better messages: f"You got it in {guesses} guesses!"
# - Handle plural: "1 guess" vs "5 guesses"
# - Reveal the secret number when they win



# === Final Challenge ===================================================
# When you're done, play your game 3 times and see your best (lowest) number of guesses.
# Bonus: Add a message if they win in < 5 guesses → "Wow, you're a mind reader! 🧠"

# Good luck! Ask questions in chat if stuck.
# Most common issues: missing colon :, wrong indentation, forgetting to break

# Start coding below this line ↓↓↓
# =======================================================================