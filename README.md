# The Battleships game

# About
This is a game of battleships, a well known game aimed for kids growing up, usually the game will be played against an opponent opposite you, however this differs as it'll be a game agaisnt a computer making random guesses.

# How to play
The game will ask you for your name and will randomly generate 4 ships for you and the computer on a 5x5 board that will be shown as "X". The game will then request you to guess a collum and a row (co-ordinates), after this it will infrom you wether it is a hit or a miss or an already guessed location and the computer will then take its own fully random gueess. Once 10 turns each have been taken by the player and the computer the winner will be dertimed by who has the most hits.

# Features
![image of battle ships home](//images/battleships-features.png)

- Allows for personalisation by adding your name.
- Automatically keeps count of turns taken.
- User has full control as you need to enter through each turn.
- Allows any valid shot to be made.
- The game is played against a computer who guesses at random.

# Data Model

I decided to use a board class as the main model of the project. The game creates two scenarios the hold for the computer and the user.

the board class holds the board size, number of ships, position of the ships, the guesses against the board and details of the board type.

the class also provides ease for the user in the print commands that present the board at each turn.

# Testing

- The interger entered is expected to be between 1 and 5 and when testing i tried the following:
  - Entering intergers not expected (e.g. 1, 6) which resulted in an error message stating the numbers to use to guess.
  - Entering letters resulted in an error message stating the numbers to use to guess.
  - Entering enter resulted in an error message stating the numbers to use to guess.
- I checked the maximum amount of moves is 10.
- I checked that there is always 4 randomly generated boats.

# Bugs

- After breifly testing throughout i realised that 0, 0 might be confusing as the top right co-ordinate so changed it to 1, 1.
- I had issues with displaying the correct board to the user which has been rectified to make it easier for the user to play.
- Originally i didnt plan for a maximum of 10 turns, but upon testing i realised the game taakes a very long times and seeing the board might make it confusing for the user.

# Remaining bugs

- There are no remaining bugs.

# Validator testing

- Fully passed the [https://pep8ci.herokuapp.com/] with no errors only 'issues' with spaces/ white space .

# Deplopyment

- This project was deployed through Heroku.

The steps taken were as followed:
- Added two buildpacks; heroku/python and heroku/nodejs.
- Created a Config Var called 'PORT' with the value of 8000.
- Link the heroku app to the repository .
- Deploy.

# Credits

= Code institute for the deployment terminal.
- The tutors at Code Institute for the information and coaching.