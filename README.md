# Please note; this project is now no longer updated. Please do not message me or add my discord about it, I wont respond. Thanks

# Valbot Premium

[![Issues](https://img.shields.io/github/issues/MrFums/Valbot)](https://github.com/MrFums/Valbot/issues)
[![Forks](https://img.shields.io/github/forks/MrFums/Valbot)](https://github.com/MrFums/Valbot/network)
[![Stars](https://img.shields.io/github/stars/MrFums/Valbot)](https://github.com/MrFums/Valbot/stargazers)


**FAIR USE**

Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research.

Fair use is a use permitted by copyright statute that might otherwise be infringing. 

Non-profit, educational or personal use tips the balance in favor of fair use. 

## Important Notice:

Valbot is now DEPRECATED. Riot seems to have added, and are constantly improving, their AFK bot detection vectors. Valbot will not receive support or updates for the foreseeable future. Running the program is now considered unsafe and I do NOT recommend it. Some changes will also need to be made to the bot to accomodate the introdouction of the new game launcher; around line 270.


## Features

* Fully AFK XP farmer
* Discord RPC support
* Discord webhook support
* Optimized and has fail safes for events that may happen during runtime of the game
* Restarts Valorant if detects an issue with it / detects that it isn't running
* Automated restarts to prevent script from ending prematurely 
* Undetected 
* Easy navigation
* Can set XP targets and XP limits


## Requirements

Only works on 1920 x 1080 resolution. If you wish to make the bot work with a different resolution other than 1920 x 1080, you need to get your own version of the images for the bot to recognize. Read on how to do this [here](https://github.com/MrFums/Valbot/blob/master/information/change_resolution.txt).

Run the batch file as Administator to install the dependencies. 
Seems to only work on 64bit Windows 10 with Python 3.9 

For the program to function properly, please copy and paste your OWN Valorant shortcut for the program to function properly. This makes it so if Valorant encounters any issues when AFK, it can restart the game. You should not need to edit any code.

You also need a functioning brain, please have one of these; it's very important.

You should also read the [saftey precautions](https://github.com/MrFums/Valbot/blob/master/information/safetyprecautions.txt) to keep your account safe while running Valbot.

### Windows installation

You will have to have a few things installed before running Valbot. This installation guide assumes that you are on a 64bit Windows system.

First, you will need to install Python. It's recommended to use either version `3.9.0` or `3.8.6`. You must use a Python version above `3.7`. 

### Installing Python

Go to the following link and download Python:

[https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

Once you have opened the installer, make sure that you add Python to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/iefWNyw.png">

Run through the installer as normal, then download the Valbot files.


## Download

[Download here](https://github.com/MrFums/Valbot/releases/latest)

Click on the zip file that says `Valbot-X.X.X` and unzip to where you would like the bot to be stored. Be advised to not put this in an Admin only folder as the bot must write the folder it is in to manage the `config.ini` file it creates.


## Instructions

1- Install Python 3.9.0.

2- Open `PackageInstaller.bat` as admin to install pakcages using pip. Do this after every update to maintain functionality.

3- Open `Valbot.py` and read the bot console.

4- Navigate the menu and read the information.

5- Put your Valorant shortcut in the bots directory.

6- Follow the instructions that will appear on screen if you haven't already.

7- If you encounter issues please [create one](https://github.com/MrFums/ValBot/issues/new) or if you have suggestions please create a [pull request](https://github.com/MrFums/ValBot/compare)

8- (Optional) Setup a Discord webhook to get updates to your discord server for when the bot has completed a game.

## Valbot Premium

This version of the bot is a variant of Valbot that I work on in my free time. The updates or not guaranteed; think of it as my own private version. As a thank you for donating, you will be given access to this version of the bot and access to the private discord server.

Keep in mind that the premium build is not fully finished and is still being worked on. There is no promise that premium will continue to be updated as it is classed as a closed project. As it is classed as a donation, I will not accept any refund requests under any circumstances.


The minimum donation amount to gain access to *Valbot Premium* is 7USD / 6EUR / 5GBP __after fees__. Please keep in mind by donating you aren't "buying" access to Valbot Premium; it's merely a way of saying thank you for donating.

### Feature List
```
- Random mouse movements
- Humanised mouse movements
- Highly improved anti-afk system
- Most base features are rewritten
- XP Target (set how much XP you want and you will be tagged in Discord when this has been reached)
- XP Limit (set how much XP you want and then your computer will be shut down after reaching this)
- Improved restart function
- Toggle Discord Rich Presence
- Fallback image assets incase Valbot can't connect to GitHub
- Debug Discord webhook
- Better detections of current stage (kicked from game, invite screen appearing etc)
- Better front-end (includes submenus for XP options)
- Safe Cycle (run the bot for x amount of hours and pause for y amount of hours)
- Mute Valorant when in a match and unmute when in menu
- Sends a message when AFK in chat
- Force close Valbot hotkey (F5)
- Major Bugfixes
- Major optimization work
```

### Premium Changelog
```
2021-08-25

+ Added 2560 x 1440 support (should automatically detect your monitor, no input on your part needed)
+ Valbot restart has changed, unfortunately, it will leave cmd windows open which you will have to close after running the bot (this helps with finding error messages)
- Disabled auto use online assets (you can re-enable it if you wish, instead it uses the images in "/assets/" folder)


2021-07-02

+ Changed discord links and RPC


2021-06-23 (2)

+ Rich Presence fixed when in game


2021-06-23

+ Force close valbot hotkey (f5)
+ Hotkey information
+ Improved front end when entering Valbot
+ Very small bug fixes


2021-06-20

+ Added text chat to anti afk
+ Changed assets used for Valbot premium (gold logo now)
+ Minor bug fixes


2021-05-27

+ Improved rest cycle (should no longer crash if you set a long rest delay)
+ Bug fixes for latest Valorant update
+ Detects if you "false" entered a game (constant in queue checks when waiting for game)
+ Dont have to wait as long to pause the bot when anti afk is running
+ Optimized code in some places


2021-05-15

+ Added option in menu to toggle discord rich presence
+ Added option to mute valorant when in a game (when actually IN the deathmatch game)
+ Added a safe cycle (bot will play for certain amount of time and then rest)
+ Reorganised menus (xp related options now have own submenu)
+ Some print functions have been rewritten

2021-05-14

+ Fixed a bunch of bugs (should be stable now)
+ Detects invite screen errors
+ Detects when you get into a game and then get kicked
+ Now included the build name in webhook name (eg, b8 = build 8)
+ If GitHub servers are down, will fallback to the images in assets folder so bot wont crash


2021-05-10

+ Improved the read me section in the main menu
+ Added an option to turn off Rich Presence (do this in the config by changing the booleans)\
+ Added a debug discord webhook
+ XP limiter now turns off the pc after the xp limit has been reached
+ Better restart process (no need for restart.py anymore)
+ Probably more that i forgot :)


2021-05-07

+ Fixed target xp config write bug
+ Changed the format of the target xp webhook


2021-05-04

+ Improved code some more
+ Improved target xp


2021-04-30 

- First release

+ Randomised mouse movement patterns [MUCH SAFER]
+ Ability to tag you in discord webhook channel for important updates
+ improved anti-afk movement system
+ Partial rewrite
```


### Changelog
```
2021-07-02 :: Valbot-2.2.2

- Changed Discord server invite link so I can always update it if needed
- Other minor changes



2021-04-18 :: Valbot-2.2.0

Huge update again:
- Added option to limit XP, the bot will stop when reaching this XP
- Added option to target XP, the bot will notify when it has reached this XP
- Added back discord webhook support
- Added back and improved discord rich presence (to toggle, disable game activity in Discord)
- Added a new config.ini management system
- Added lifetime stat tracking for all XP earned, gamesplayed, total runtime etc
- Slightly improved anti afk feature (with more updates to come)
- Fixed a bunch of bugs when finding games
- Fixed the bot not recognising if there is a problem with the current deathmatch game
- Fixed the lag when you pause the bot
- Fixed buy menu not closing
- Improved AFK screen warning
- Improved webhook visuals
- Improved information screens
- Improved crash screens if you don't have a package installed
- Changed default colour from red to yellow (easier to see in the menu)
- Removed version checking
- Removed manual bot termination (only on my end, keep on the discord so you know when there is a problem)
- Bot should now properly run forever until stopped

Notes:

I have tried to fix the most infamous bugs and added some demanded features (back). Valbot Lite is no longer
needed as I have managed to almost fully optimise the main versions code. Other resolutions from 1920x1080
will never be supported as there are way too many resolutions to add and support. Again, if there are any 
issues or you have any suggestions, join my Discord: https://discord.gg/QFC46XKzxU

- Fums



2021-04-12 :: Valbot-2.1.0 Lite

Fixed the bot stopping running after a certain amount of time.
Also attempted to fix the launcher play screen, it should work and click play now.
! I don't have time to check if it works properly so please check for me and tell me on Discord! !

- Fums



2021-03-20 :: Valbot-2.0.0 Lite

Welcome to Valbot Lite! A much more stable version of my Valbot, all in one place.
This version of Valbot should be much more optimized than prior releases of the bot.
Valbot Lite does lack some features, however. Some of these include the Discord Presence and Discord Webhook support.
Not to worry though, I will (probably) release a normal version of the bot sometime soon with those features implemented.

This new version does come with some improvements though, not necessarily "features" that you would care about though.

Some of these include the ability for the developers to stop the use of the bot if it gets detected while in use. So if the bot gets detected while you
are AFK, I can manually stop the bot if I require to do so and you do not need to worry! 

In addition to this, I have decided to make it so all the images are hosted online, on GitHub so you no longer need to download them and I can edit
them in real-time (basically I can release updates to the bot when Valorant gets updated without you needing to do ANYTHING).


Unfortunately, I will no longer be supporting monitors / resolutions that are NOT 1920x1080. 
It is just too much work to go through all of the resolutions just to make it work for such a small amount of users. Sorry.

- Fums
```
