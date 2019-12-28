# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define html="gg"

python:
    import urllib.request
    response = urllib.request.urlopen('http://python.org/')
    html = response.read()


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
image spaceWow=im.Scale("space wow.png",characterScaleX,characterScaleY)
define nil = Character("Nil")
image nilIdle  = im.Scale("nil.png", characterScaleX, characterScaleY, bilinear=True)

# The game starts here.

label start:

    # This begins the game
    #space "[html]"
    #play music mainm
    play music poolparty
    scene bgs:
        linear 5.0 zoom 1.1
        linear 5.0 zoom 1.0
        repeat
    with dissolve
    show spaceSmile at right
    with dissolve
    space "Hello~!!! My name is Space"
    hide spaceSmile
    show spaceShy at right
    with dissolve
    space "This is my first visual novel project :)"
    space "I have added this background music named \"Pool Party Upbeat\" is one of my favorite songs"
    space "Do you like this song?"
    $ musiclist = False;
    menu:
        "Yes":
            hide spaceShy
            show spaceLaugh at right
            with dissolve
            space "I'm glad you like it"
        "No":
            hide spaceShy
            show spaceWow at right
            with dissolve
            space "Oh Okay"
            $ musiclist = True

    if musiclist:
        hide spaceLaugh
        hide spaceWow
        show spaceSmile at right
        with dissolve
        space "There are some songs which you can play:"

        label songmenu:
        menu:

            "Main Menu Lyrical Version":
                hide spaceSmile
                scene Vocal:
                    linear 5.0 zoom 1.1
                    linear 5.0 zoom 1.0
                    repeat
                with dissolve
                play music vocal
                #pause
                pause
            #    jump songmenu

            "Energetic Upbeat Pop":
                hide spaceSmile
                with dissolve
                play music mainm

            "Weekend Chill":
                hide spaceSmile
                with dissolve
                play music weekendchill

            "Cool Electronic Chill Energy":
                hide spaceSmile
                with dissolve
                play music energy

            "Time's Battle Theme":
                hide spaceSmile
                scene Time
                with dissolve
                play music time
                #pause
                pause
                #jump songmenu


            "Space's Battle Theme":
                hide spaceSmile
                scene Space
                with dissolve
                play music spacem
                #pause
                pause
                #jump songmenu

            "Nil's Battle Theme":
                hide spaceSmile
                scene Nil
                with dissolve
                play music nil
                #pause
                pause
            #    jump songmenu

            #"Quit":
            #    jump quit

        #label quit:
        #    pause 0.1
        show spaceLaugh at right with dissolve
        space "You can go back by pressing back button if you want to change the song"

    scene bgs:
        linear 5.0 zoom 1.1
        linear 5.0 zoom 1.0
        repeat
    hide spaceLaugh
    show spaceSmile: #at right:
        xpos 600
        ypos 50
        linear 1.3 xpos 900
    with dissolve
    show time at left
    with dissolve
    space "OK, this is Time"
    space "She can make the universe move. Forwards, backwards... She can jump to any moment she has already experienced"
    space "In other words, she can travel time"
    space "She can delete her own memories and replace them with new ones"
    space "Time is the Main Character in \"Her Tears Were My Light\""
    hide time
    show nilIdle at left
    with dissolve
    space "This is Nil, She can create time loops, she can delete the memories of Time"
    hide spaceSmile
    show spaceWorry:
        xpos 1000
        ypos 50
    with dissolve
    space "Nil can erase the entire Universe"
    space "She can stop Time from rewinding but resetting the entire universe"
    show spaceLaugh:
            xpos 1000
            ypos 50
    with dissolve
    space "Time can survive even after Nil erased the entire Universe and can also go back before the Universe was erased"

    # This ends the game.

    return
