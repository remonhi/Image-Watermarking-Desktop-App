## Day 85 - Image Watermarking Desktop App

## Requirements

Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark logo/text.
Normally, you would have to use an image editing software like Photoshop to add the watermark, but your program is going to do it automatically. Use case: e.g you want to start posting your photos to Instagram but you want to add your website to all the photos, you can now use your software to add your website/logo automatically to any image.

A similar online service is: https://watermarkly.com/

You might need..

    https://pypi.org/project/Pillow/

    https://docs.python.org/3/library/tkinter.html

    ...and some Googling.

## My Notes

1/6/26

Okay, I just took this day to start getting organized. Having not used Tkinter in a while I decided to go back to Day 20 to look at teh projects there. I decided to refresh on my code for the 'Snake Game.' Also, it is using OOP that is great. So for today, I just copied all the code over and laid out plans for tomorrow.

With an small window of time, I decided to do a little preparation...


    Initialized the virtual environment → python -m venv venv
        Activated the virtual environemtn → source venv/bin/activate
        Copied over Git Ignore → cp ../'Day 84'/.gitignore .
        Initlaized a new repo →
            git init
            git add .
            git commit -m "initial commit"
        Noted old Git Ignore still there → cat .gitignore
        Set branch name → git branch -M main
        Created new repo at Gig Hub → https://github.com/remonhi/Tic-Tac-Toe
        Connected to net repo → git remote add origin git@github.com:remonhi/Tic-Tac-Toe.git
        Pushed → git push -u origin main




1/7/26

1. Get 150.py working again, but rename to snake.py (and use my CONVENTIONAL FORMATING)
2. Review the service https://watermarkly.com/
3. Study https://pypi.org/project/Pillow/, https://docs.python.org/3/library/tkinter.html and little Googling.
4. Initalize the project development space.
5. Layout plans for building this out.

This one really got me thinking. First, I was not going to post to my portfolio website. Second, should I use an array or a dictionary. 3rd, how to make it displa and how to select the location. Anyway, to get started I just copied over one of my previous text based programs.

1/3/26

I started the day with...

    1.  Cleaning up the files (not needed) ✅

    2.  Updating main.py to the most basic needs (and installing modules as nededed) ✅

    3.  Get overview for project ✅

        Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

        This is a simple demonstration of how the game works:
        https://www.google.com/search?q=tic+tac+toe

        You can choose how you want your game to look. The simplest is to create a game board using "|" and "\_" symbols. But the design is up to you.

        If you have more time, you can challenge yourself to build an AI player to play the game with you.

    4.  Setup Git and Git Hub (to save for later) ✅

        Removed old virtual environment → rm -rf venv
        Removed the old git tracking → rm -rf .git
        Initialized the virtual environment → python -m venv venv
        Activated the virtual environemtn → source venv/bin/activate
        Initlaized a new repo →
        git init
        git add .
        git commit -m "initial commit"
        Noted old Git Ignore still there → cat .gitignore
        Set branch name → git branch -M main
        Created new repo at Gig Hub → https://github.com/remonhi/Tic-Tac-Toe
        Connected to net repo → git remote add origin git@github.com:remonhi/Tic-Tac-Toe.git
        Pushed → git push -u origin main

    5.  Last, laid out my approach... ✅

        1. Ask if want to play.
        2. Setup coin flip (using my weather station).
        3. Create the game board.
        4. Outline all the possible "wins"
        5. Address how to select location.
        6. Figure out how to "stategize" next move of computer.
        7. Determeine when game is won or stalemate
        8. Ask to play a new game.

Alright, got started. I completed the following...

    - Ask if want to play. ✅
    - Setup coin flip (using location of ISS just for the fun of using an API). ✅
    - Create the game board. ✅
    - Address how to select location.✅

I had enough for today, so cleaned up it up and did a little plannign for next day.

1/5/26

Well, I missed a couple of days. Unfortuately and forutnatley, I have other things going on in my life besides codidng. Anyway, I had about an hour to "play" today.l

    1. Prevent "duplicates" for selecting a cell already picked.✅
        a. First, telling USER something is already picked.✔️
        b. Tell COMPUTER to try again. ✔️

    2. Check for wins (right after play) ✅
        a. Tried a lot of weird stuff and go it working, but it was ugly. ✔️
        b. Check with Copilot and got something slightly cleaner. ✔️
        c. Actually, returning True or False played very well into my logic strutucture that addressed stalemale. ✔️

    3. Come up with strategy logic. ❌

    4. Ask to play a new game. ✅
        a. Okay, this really changed my logic...had to set some flags. ✔️
        b. Need to review "NEW" game flag. ✔️
        c. Address duplciate of "resetting" the board array. ✔️
        d. Assign whoever goes first the X. ✔️

    5. Regineer the coin flip ✅
        a. Move into a function
        b. The function shoudl all selecting Head or Tails and returnign Heads or Tails

1/?/26 - THE END

    1. Clean up (and test) the code. ✅
        a. Had the wife test, and found issue with checking win. ✔️
        b. Cleaned up debugging. ✔️
        c. Skimmed once more.✔️
        d. Ran a few more times until a stalemate. ✔️
            i. Found a problem...seems to flip with playhing again.
            ii. Had to change the 'game' flag

    2. Push to Git Hub

    3. Post assignment.

        a. Layout top line approach
        b. Note lesson learned
        c. Share code via Git Hub
