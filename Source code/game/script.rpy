# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bgs  = im.Scale("bgs.png", 1920, 1080, bilinear=True)
image Space  = im.Scale("spacemusic.jpg", 1920, 1080, bilinear=True)
image Time  = im.Scale("bgstime.jpg", 1920, 1080, bilinear=True)
image Nil  = im.Scale("bgsnil.jpg", 1920, 1080, bilinear=True)
image Vocal  = im.Scale("vocal.jpg", 1920, 1080, bilinear=True)

#Character
define characterScaleX = 1250
define characterScaleY = 1050
#space
define space = Character("Space")
image spaceSmile=im.Scale("space smile.png",characterScaleX,characterScaleY)
image spaceShy=im.Scale("space shy.png",characterScaleX,characterScaleY)
image spaceWorry=im.Scale("space worry.png",characterScaleX,characterScaleY)
image spaceLaugh=im.Scale("space laugh.png",characterScaleX,characterScaleY)

# The game starts here.

label start:

    # This begins the game
    play music mainm
    scene bgs
    with dissolve
    show spaceSmile at right
    space "Hello~!!! My name is Space"
    hide spaceSmile
    show spaceShy at right
    with dissolve
    space "This is my first visual novel project :)"
    space "Do you like this song?"

    menu:
        "Yes":
            hide spaceShy
            show spaceLaugh at right
            with dissolve
            space "I'm glad you like it"
        "No":
            hide spaceShy
            show spaceWorry at right
            with dissolve
            space "Oh Okay"

    hide spaceLaugh
    hide spaceWorry
    show spaceSmile at right
    with dissolve
    space "There are some musics you can play:"

    label songmenu:
    menu:
        "Time's Battle Theme":
            hide spaceSmile
            scene Time
            with dissolve
            play music time
            pause
            jump songmenu

        "Space's Battle Theme":
            hide spaceSmile
            scene Space
            with dissolve
            play music spacem
            pause
            jump songmenu

        "Nil's Battle Theme":
            hide spaceSmile
            scene Nil
            with dissolve
            play music nil
            pause
            jump songmenu

        "Main Menu Lyrical Version":
            hide spaceSmile
            scene Vocal
            with dissolve
            play music vocal
            pause
            jump songmenu

        "Quit":
            jump quit

    label quit:
        pause 0.1

    # This ends the game.

    return
