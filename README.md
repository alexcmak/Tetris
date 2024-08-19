# Tetris

This is a Tetris clone written in python based on an excellent tutorial by Nick Koumaris from [Programming with Nick](https://github.com/educ8s/Python-Tetris-Game-Pygame).

## pygame
You will need to have *pygame* on your computer. [Follow this guide.](https://www.pygame.org/wiki/GettingStarted)


### Mac
python is tricky on the iMac, this [link](https://hackernoon.com/fixing-the-externally-managed-environment-error-when-using-pip-a-quick-guide) helped me.

pygame will not be installed as easily as you would like. To successfully do so you will need an "venv", activate it then you can use pip3.

After you have all my source code, use the Terminal and cd to the folder; you will need to do the following:

```
python3 -m venv alex_env
source ./alex_env/bin/activate
python3 -m pip install pygame
python3 TetrisGame.py
```
You don't need to install pygame everytime, you just must run the activate command first.


## Features added so far: 
Nick's version is pretty great but I added a few things:
- More sensible OOP division, the subclasses of Block should have its own attributes such as color and width
- P for pause game
- Pause when game over, N for new game
- Make tiles stone color when game over
- Space bar to drop

## Screenshots


![screenshot](https://github.com/alexcmak/tetris/blob/main/screenshot1.png)

![screenshot](https://github.com/alexcmak/tetris/blob/main/screenshot2.png)
