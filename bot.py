try:
    from colorama import Fore, Style
    from colorama import init
    import os

    init()

    os.system('mode con: cols=54 lines=12')
    title = "title Valbot"
    os.system(title)

    print(Fore.YELLOW + """
           ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
           ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
           ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
            ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
            ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
             ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝""")

    print(Style.RESET_ALL)
    print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "                      Fums#0888")
    print(Style.RESET_ALL)
    print(Style.RESET_ALL)


except Exception as e:
    print(e), print("Try to reinstall packages"), input(), quit()

try:
    import gc
    import pathlib
    import requests
    import webbrowser
    import math
    import keyboard
    import psutil
    import pyautogui
    import pygetwindow as gw
    import os
    import sys
    import time
    import urllib.request
    import datetime
    import random
    import platform

    import configloader as cfg

    from pypresence import Presence
    from PIL import Image
    from pathlib import Path
    from random import randint, uniform
    from time import sleep
    from colorama import Fore, Style
    from colorama import init
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from configparser import ConfigParser
    from pycaw.pycaw import AudioUtilities
except Exception as e:
    print(e), print("Package(s) needs downloading"), print("Run PackageInstaller.bat"), input(), quit()

init()  # loads the colorama init function (why is this needed for this function?)

# ------------------------------------------------------------------------------

pyautogui.FAILSAFE = False


class bot:
    def __init__(self):

        self.cheaterdetected_png = "assets/cheated_detected.png"
        self.continueterminated_png = "assets/continue_terminated.png"
        self.deathmatch_png = "assets/deathmatch.png"
        self.ingame_png = "assets/ingame.png"
        self.inqueue_png = "assets/inqueue.png"
        self.inqueue2_png = "assets/inqueue_2.png"
        self.ondeathmatch_png = "assets/ondeathmatch.png"
        self.play_png = "assets/play.png"
        self.playagain_png = "assets/playagain.png"
        self.start_png = "assets/start.png"
        self.afkwarning = "assets/afkwarning.png"
        self.invitescreen = "assets/invitescreenerror.png"
        self.invitescreen_updated = "assets/invitescreenerror_updated.png"

        screenWidth, screenHeight = pyautogui.size()

        if screenWidth == 2560 and screenHeight == 1440:
            print(Style.RESET_ALL)
            print(f"{Fore.GREEN} [√] DETECTED 2560 X 1440 RESOLUTION")
            print(f"{Fore.GREEN} [√] LOADING CORRECT ASSETS")

            self.deathmatch_png = "assets/deathmatch1440.png"
            self.ingame_png = "assets/ingame1440.png"
            self.inqueue_png = "assets/inqueue_21440.png"
            self.inqueue2_png = "assets/inqueue_21440.png"
            self.ondeathmatch_png = "assets/ondeathmatch1440.png"
            self.play_png = "assets/play1440.png"
            self.playagain_png = "assets/playagain1440.png"
            self.start_png = "assets/start1440.png"

        # for 2560 x 1440, you must multiply each coordinate by 1.22 to convert 1920 x 1080 coordinates to 2560 x 1440.
        # this is because a 1440p monitor has 77~% more pixels than a 1080p monitor and 1.77 represents 177% in scale.

        if screenWidth == 2560 and screenHeight == 1440:
            self.scaleFloat = 1.23
        else:
            self.scaleFloat = 1.00


        self.xpamount = 0  # how much xp the bot has earned during runtime
        self.restarted = 0  # how many times the bot has restarted during runtime
        self.gamesplayed = 0  # num of games played during runtime
        self.restarttime = time.time() + 3600  # 1 hour after starting bot

        self.messagelist = ['glhf', ':)', '???', 'im on 3fps', 'lol', 'bruh']
        self.messagelistBAK = []
        self.foundwebhook = False  # if no webhook has been setup it wont attempt to send to one

        config = ConfigParser(allow_no_value=True)
        config.read('config.ini')




        if os.path.exists('config.ini'):

            if "https://discord.com/api/webhooks/" not in cfg.webhook:
                self.foundwebhook = False
            else:
                self.foundwebhook = True

            self.userid = '<@' + cfg.discordID + '>'  # sets the user id tag for discord <@int>


        else:
            print (f"{Fore.RED} [!] Valbot will not run without a config file")
            print (f"{Fore.RED} [!] Either it was not created or cannot be accessed")
            time.sleep(10)
            quit()

        self.versionfix = "Valbot Premium"  # add four spaces if version number is vx.x and remove spaces if vx.x.x
        self.versionnumber = self.versionfix.replace("Valbot ", "")  # add two spaces if version number is vx.x and remove spaces if vx.x.x
        self.versionnumber = self.versionnumber.replace("  ", "")  # add two spaces if version number is vx.x and remove spaces if vx.x.x
        self.version = "Valbot " + self.versionnumber  # variable str to change valbot version name in outputs
        self.premiumnumber = "b16"

        self.PROCNAME = "VALORANT-Win64-Shipping.exe"  # valorant exe process name
        self.discordbutton = [{"label": "View on GitHub", "url": "https://github.com/MrFums/Valbot"}]

        self.computer_name = platform.node()  # gets the pc name for webhook embed footer
        self.start_time = time.time()


        if cfg.rpcEnabled is True:
            try:  # if cant connect to discord (if it isnt open for example), bot doesnt crash
                self.RPC = Presence(client_id="856181408715767859")  # discord rpc client id

                try:
                    self.RPC.close()
                except Exception:
                    pass
                self.RPC.connect()  # connects to rpc
            except Exception as e:
                print(f"{Style.BRIGHT + Fore.RED} [!] {e, Style.RESET_ALL}")


        try:
            config = ConfigParser(allow_no_value=True)  # grabs the values for the previous runtime of the bot if needed

            config.read('config.ini')

            self.restarted = cfg.restarted
            self.timestarted = cfg.timestarted
            self.gamesplayed = cfg.gamesplayed
            self.xpamount = cfg.xpamount
            self.xptarget = cfg.xptarget

        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

    def restartbot(self):  # restarts the bot after 1 hour

        if cfg.debugWebhook:
            debugmessage = "Restarting bot"
            self.debugwebhookpush(debugmessage)
        self.titlescreen()
        print(Fore.RED + " [!] BOT IS RESTARTING")
        print(Style.RESET_ALL)

        try:
            self.RPC.close()  # closes the rpc if it is active
        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        gc.collect()  # garbage collection

        os.startfile('restart.bat')
        time.sleep(.5)
        quit()

    def debugwebhookpush(self, debugmessage):
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=cfg.webhook,
                    username="Valbot")
                embed = DiscordEmbed(color=0x000000, title="Debug Webhook",
                                     description=debugmessage)
                authorname = self.version + " " + self.premiumnumber
                embed.set_author(
                    name=authorname,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                )
                textforfooter = self.computer_name

                embed.set_footer(text=textforfooter,
                                 icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A DEBUG WEBHOOK BUT IT IS NOT SETUP")
        return

    def mutevalorant(self):
        try:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == self.PROCNAME:
                    if cfg.muteInGame:
                        volume.SetMute(1, None)
                    else:
                        volume.SetMute(0, None)
        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
        return

    def unmutevalorant(self):
        try:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session.SimpleAudioVolume
                if session.Process and session.Process.name() == self.PROCNAME:
                    if cfg.muteInGame:
                        volume.SetMute(0, None)
                    else:
                        volume.SetMute(1, None)
        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
        return

    def resttimecheck(self):
        safecycle = False
        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')
                safecycle = config.getboolean('rest_cycle', 'safe_cycle')
                play_time_secs = config.getfloat('rest_cycle', 'play_time_secs')
                rest_time_secs = config.getfloat('rest_cycle', 'rest_time_secs')
                try:
                    config.set('rest_cycle', 'rest_start', 'False')
                    with open('config.ini', 'w+') as configfile:
                        config.write(configfile)
                except Exception as e:
                    print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
            except Exception as e:
                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        else:
            return
        if safecycle is True:

            if time.time() > play_time_secs:
                # reached play time, now resting
                self.forceclose()
                activeactivity = "Resting"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbotpremium",
                                    large_text=self.version, details=activeactivity, buttons=self.discordbutton)

                except Exception:
                    pass

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=cfg.webhook,
                            username="Valbot")
                        embed = DiscordEmbed(color=0xFF0000, title="Safe Cycle",
                                             description="Valbot has reached the set amount of playtime.\nThe bot will now rest.")
                        authorname = self.version + " " + self.premiumnumber
                        embed.set_author(
                            name=authorname,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                        )
                        textforfooter = self.computer_name

                        embed.set_footer(text=textforfooter,
                                         icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                while time.time() < rest_time_secs:
                    self.forceclose()
                    if time.time() > self.restarttime:

                        # now we need to restart bot to stop recurrsion error, will resume back at rest.
                        if os.path.exists('config.ini'):
                            try:
                                config = ConfigParser(allow_no_value=True)
                                config.read('config.ini')
                                config.set('rest_cycle', 'rest_start', 'True')
                                with open('config.ini', 'w+') as configfile:
                                    config.write(configfile)

                                self.restartbot()
                            except Exception as e:
                                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
                    pass

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=cfg.webhook,
                            username="Valbot")
                        embed = DiscordEmbed(color=0xFF0000, title="Safe Cycle",
                                             description="Valbot has reached the set amount of resttime.\nThe bot will now resume.")
                        authorname = self.version + " " + self.premiumnumber
                        embed.set_author(
                            name=authorname,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                        )
                        textforfooter = self.computer_name

                        embed.set_footer(text=textforfooter,
                                         icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                try:
                    playtime = config.getint('rest_cycle', 'play_time')
                    resttime = config.getint('rest_cycle', 'rest_time')

                    playtime *= 3600
                    resttime *= 3600

                    resttime += playtime + time.time()

                    playtime += time.time()

                    config.set('rest_cycle', 'play_time_secs', str(playtime))
                    config.set('rest_cycle', 'rest_time_secs', str(resttime))
                    config.set('rest_cycle', 'rest_start', 'False')

                    with open('config.ini', 'w+') as configfile:
                        config.write(configfile)
                except Exception as e:
                    print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
                self.restartbot()

            else:
                return
        return

    def titlescreen(self):

        if cfg.debugWebhook:
            debugmessage = "Showing title screen"
            self.debugwebhookpush(debugmessage)
        print(Style.RESET_ALL)
        os.system('mode con: cols=54 lines=18')  # makes the window a certain size
        title = "title " + self.versionfix  # window title
        os.system(title)

        print(Fore.YELLOW + """
           ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
           ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
           ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
            ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
            ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
             ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝""")

        print(Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "           " + self.versionfix + "       Fums#0888")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        return

    def valorantrunningcheck(self):
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                return True
        print(Style.RESET_ALL)
        print(Fore.RED + " [!] COULD NOT FIND VALORANT PROCESS")
        return False

    def valorantrunning(self):  # checks if valorant process is running. if it isnt trys to start it
        found = False

        if cfg.debugWebhook:
            debugmessage = "Checking if Valorant is running"
            self.debugwebhookpush(debugmessage)
        print(Fore.YELLOW, "[-] CHECKING IF VALORANT IS RUNNING")
        print(Style.RESET_ALL)
        time.sleep(2)

        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                found = True
                break

        if cfg.debugWebhook:
            debugmessage = "Valorant running", str(found)
            self.debugwebhookpush(debugmessage)

        if not found:
            print(Fore.RED, "[!] VALORANT IS NOT RUNNING")
            print(Style.RESET_ALL)
            self.startvalorant()
        else:
            print(Fore.GREEN, "[√] VALORANT IS RUNNING")
            time.sleep(25)
            # clicks the play button when you are in launcher to fix some peoples launchers
            screenWidth, screenHeight = pyautogui.size()
            pyautogui.click(screenWidth / 2, screenHeight / 2)
            time.sleep(1)
            self.playbutton()

    def startvalorant(self):
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=cfg.webhook,
                    username="Valbot")
                embed = DiscordEmbed(color=0xFF0000, title="Restarting Valorant",
                                     description="Possible error with Valorant.\nValorant will now be relaunched.\nBot will resume as normal.")
                authorname = self.version + " " + self.premiumnumber
                embed.set_author(
                    name=authorname,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                )
                textforfooter = self.computer_name

                embed.set_footer(text=textforfooter,
                                 icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")
        for proc in psutil.process_iter():  # goes through all running processes and trys to find valorant and ends the task
            try:
                if proc.name().lower() == self.PROCNAME.lower():
                    proc.kill()
                    print(Fore.YELLOW, "[-] KILLING THE VALORANT PROCESS")
                    time.sleep(10)
            except:
                print(Fore.RED, "[!] COULD NOT KILL THE VALORANT PROCESS")

        print(Style.RESET_ALL + Fore.YELLOW, "[-] STARTING VALORANT")
        print(Style.RESET_ALL)
        root = str(pathlib.Path(__file__).parent.absolute())
        fullpath = root + "\Valorant.lnk"
        vallnk = Path(fullpath)
        if vallnk.is_file():
            # file exists
            time.sleep(1)
            os.startfile("Valorant.lnk")

        else:
            print(Style.RESET_ALL, Fore.RED + "[!] COULD NOT FIND A VALORANT SHORTCUT")
            print(Style.RESET_ALL)
        time.sleep(15)
        self.restarted += 1
        # clicks the play button when you are in launcher to fix some peoples launchers
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.click(screenWidth / 2, screenHeight / 2)
        time.sleep(15)
        self.valorantrunning()

    def invitescreenerror(self):
        invite = pyautogui.locateOnScreen(self.invitescreen, grayscale=True)
        invite2 = pyautogui.locateOnScreen(self.invitescreen, confidence=0.6, grayscale=True)

        invite_updated = pyautogui.locateOnScreen(self.invitescreen_updated, grayscale=True)
        invite_updated2 = pyautogui.locateOnScreen(self.invitescreen_updated, confidence=0.6, grayscale=True)

        if invite is not None or invite2 is not None or invite_updated is not None or invite_updated2 is not None:
            if cfg.debugWebhook:
                debugmessage = "Invite screen error found"
                self.debugwebhookpush(debugmessage)

            if invite is not None:
                time.sleep(1)
                x, y = pyautogui.center(invite)
                x = randint(x - 20, x + 20)
                y = randint(x - 5, x + 5)
                pyautogui.moveTo(x, y, (randint(1, 3) / 4), pyautogui.easeOutQuad)
                time.sleep(randint(1, 3) / 15)
                pyautogui.click(x, y)
                time.sleep(3)

            if invite2 is not None:
                time.sleep(1)
                x, y = pyautogui.center(invite2)
                x = randint(x - 20, x + 20)
                y = randint(x - 5, x + 5)
                pyautogui.moveTo(x, y, (randint(1, 3) / 4), pyautogui.easeOutQuad)
                time.sleep(randint(1, 3) / 15)
                pyautogui.click(x, y)
                time.sleep(3)

            if invite_updated is not None:
                time.sleep(1)
                x, y = pyautogui.center(invite_updated)
                x = randint(x - 20, x + 20)
                y = randint(x - 5, x + 5)
                pyautogui.moveTo(x, y, (randint(1, 3) / 4), pyautogui.easeOutQuad)
                time.sleep(randint(1, 3) / 15)
                pyautogui.click(x, y)
                time.sleep(3)

            if invite_updated2 is not None:
                time.sleep(1)
                x, y = pyautogui.center(invite_updated2)
                x = randint(x - 20, x + 20)
                y = randint(x - 5, x + 5)
                pyautogui.moveTo(x, y, (randint(1, 3) / 4), pyautogui.easeOutQuad)
                time.sleep(randint(1, 3) / 15)
                pyautogui.click(x, y)
                time.sleep(3)
        return

    def playbutton(self):

        self.messagelistBAK = self.messagelist

        activeactivity = "At Menu"

        earned = "{:,}".format(self.xpamount)

        if cfg.debugWebhook:
            debugmessage = "Searching for play button"
            self.debugwebhookpush(debugmessage)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbotpremium",
                            large_text=self.version, details=activeactivity, buttons=self.discordbutton)

        except Exception:
            pass

        self.fullscreenval()
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR PLAY BUTTON")
        time.sleep(.5)

        now = time.time()

        future = now + 720
        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            self.forceclose()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            play = pyautogui.locateOnScreen(self.play_png, grayscale=True)
            play2 = pyautogui.locateOnScreen(self.play_png, confidence=0.6, grayscale=True)

            afkwarning = pyautogui.locateOnScreen(self.afkwarning, grayscale=True)
            afkwarning2 = pyautogui.locateOnScreen(self.afkwarning, confidence=0.6, grayscale=True)

            self.invitescreenerror()

            if afkwarning is not None or afkwarning2 is not None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] WARNED FOR AFK")

                if afkwarning is not None:
                    time.sleep(1)
                    x, y = pyautogui.center(afkwarning)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 5), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    time.sleep(3)

                if afkwarning2 is not None:
                    time.sleep(1)
                    x, y = pyautogui.center(afkwarning2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 5), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    time.sleep(3)

            if play is not None or play2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED PLAY BUTTON")

                if play is not None:
                    time.sleep(.5)
                    x, y = pyautogui.center(play)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    time.sleep(.5)
                    self.playbuttonclicked()

                if play2 is not None:
                    time.sleep(.5)
                    x, y = pyautogui.center(play2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    time.sleep(.5)
                    self.playbuttonclicked()

    def deathmatchbutton(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW, "[-] SEARCHING FOR DEATHMATCH BUTTON")
        now = time.time()

        future = now + 45

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            deathmatch = pyautogui.locateOnScreen(self.deathmatch_png, grayscale=True)
            deathmatch2 = pyautogui.locateOnScreen(self.deathmatch_png, confidence=0.6, grayscale=True)

            afkwarning = pyautogui.locateOnScreen(self.afkwarning, grayscale=True)
            afkwarning2 = pyautogui.locateOnScreen(self.afkwarning, confidence=0.6, grayscale=True)
            self.invitescreenerror()

            if afkwarning is not None or afkwarning2 is not None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] WARNED FOR AFK")

                if afkwarning is not None:
                    time.sleep(1)
                    x, y = pyautogui.center(afkwarning)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 2), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 2) / 20)
                    pyautogui.click(x, y)
                    time.sleep(3)

                if afkwarning2 is not None:
                    time.sleep(1)
                    x, y = pyautogui.center(afkwarning2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 2), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 2) / 20)
                    pyautogui.click(x, y)
                    time.sleep(3)

            if deathmatch is not None or deathmatch2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED DEATHMATCH BUTTON")

                if deathmatch is not None:
                    x, y = pyautogui.center(deathmatch)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 2) / 20)
                    pyautogui.click(x, y)
                    self.deathmatchbuttonclicked()

                if deathmatch2 is not None:
                    x, y = pyautogui.center(deathmatch2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 2) / 20)
                    pyautogui.click(x, y)
                    self.deathmatchbuttonclicked()

    def deathmatchbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] DETECTING IF DEATHMATCH IS DETECTED")
        time.sleep(1)
        now = time.time()

        future = now + 120

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            ondeathmatch = pyautogui.locateOnScreen(self.ondeathmatch_png, grayscale=True)
            ondeathmatch2 = pyautogui.locateOnScreen(self.ondeathmatch_png, grayscale=True, confidence=0.5)
            self.invitescreenerror()

            if ondeathmatch is not None or ondeathmatch2 is not None:

                if ondeathmatch is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT DEATHMATCH IS SELECTED")
                    time.sleep(.5)
                    self.searchforgame()

                if ondeathmatch2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT DEATHMATCH IS SELECTED")
                    time.sleep(.5)
                    self.searchforgame()

            if ondeathmatch is None or ondeathmatch2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT DEATHMATCH IS NOT SELECTED")
                time.sleep(.5)
                self.deathmatchbutton()

    def playbuttonclicked(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] CHECKING IF PLAY BUTTON IS SELECTED")
        now = time.time()

        future = now + 120

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            onplay = pyautogui.locateOnScreen(self.start_png, grayscale=True)
            onplay2 = pyautogui.locateOnScreen(self.start_png, grayscale=True, confidence=0.5)
            self.invitescreenerror()

            if onplay is not None or onplay2 is not None:

                if onplay is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT PLAY BUTTON IS SELECTED")
                    time.sleep(.2)
                    self.deathmatchbutton()

                if onplay2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED THAT PLAY BUTTON IS SELECTED")
                    time.sleep(.2)
                    self.deathmatchbutton()

            if onplay is None or onplay2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED THAT PLAY BUTTON IS NOT SELECTED")
                time.sleep(.4)
                self.playbutton()

    def fullscreenval(self):

        try:
            window = gw.getWindowsWithTitle('Valorant')[0]
            if not window.isMaximized:
                window.maximize()
        except IndexError:
            self.startvalorant()
        return

    def firststart(self):

        self.titlescreen()
        foundval = False
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                foundval = True
        if not foundval:
            self.startvalorant()

        self.fullscreenval()

        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        for i in range(7, -1, -1):
            print(Fore.RED, Style.BRIGHT + "[!] BOT WILL BEGIN IN", i, "SECONDS                  ", end='\r')
            self.forceclose()
            sleep(1)
        print(Style.RESET_ALL)
        self.playbutton()

    def searchforgame(self):

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR START BUTTON")

        now = time.time()

        future = now + 240

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            start = pyautogui.locateOnScreen(self.start_png, grayscale=True)
            start2 = pyautogui.locateOnScreen(self.start_png, confidence=0.6, grayscale=True)

            if start is not None or start2 is not None:
                if cfg.debugWebhook:
                    debugmessage = "Detected start button"
                    self.debugwebhookpush(debugmessage)
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED START BUTTON")

                if start is not None:
                    time.sleep(.5)
                    x, y = pyautogui.center(start)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    self.inqueue()

                if start2 is not None:
                    time.sleep(.5)
                    x, y = pyautogui.center(start2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    self.inqueue()

    def playagain(self):

        again = pyautogui.locateOnScreen(self.playagain_png, grayscale=True)
        again2 = pyautogui.locateOnScreen(self.playagain_png, confidence=0.6, grayscale=True)
        self.invitescreenerror()
        playbuttoncheck = time.time() + 20

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR PLAY AGAIN BUTTON")

        while time.time() < playbuttoncheck:

            if again is not None or again2 is not None:

                if cfg.debugWebhook:
                    debugmessage = "Detected play again button"
                    self.debugwebhookpush(debugmessage)

                if again is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED PLAY AGAIN BUTTON")
                    time.sleep(.5)
                    x, y = pyautogui.center(again)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    self.inqueue()

                if again2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED PLAY AGAIN BUTTON")
                    time.sleep(.5)
                    x, y = pyautogui.center(again2)
                    x = randint(x - 40, x + 40)
                    y = randint(y - 10, y + 10)
                    pyautogui.moveTo(x, y, (randint(1, 3) / 3), pyautogui.easeOutQuad)
                    time.sleep(randint(1, 3) / 15)
                    pyautogui.click(x, y)
                    self.inqueue()

        print(Style.RESET_ALL)
        print(Fore.RED + " [!] COULD NOT FIND PLAY AGAIN BUTTON")
        self.playbutton()

    def inqueue(self):

        if cfg.debugWebhook:
            debugmessage = "Checking if in queue"
            self.debugwebhookpush(debugmessage)
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] CHECKING IF IN QUEUE")
        now = time.time()

        future = now + 240
        self.fullscreenval()

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break
            self.invitescreenerror()

            q = pyautogui.locateOnScreen(self.inqueue_png, grayscale=True)
            q2 = pyautogui.locateOnScreen(self.inqueue_png, grayscale=True, confidence=0.6)
            q_aftergame = pyautogui.locateOnScreen(self.inqueue2_png, grayscale=True)
            q_aftergame2 = pyautogui.locateOnScreen(self.inqueue2_png, grayscale=True, confidence=0.6)

            if q is not None or q2 is not None or q_aftergame is not None or q_aftergame2 is not None:

                self.inqueueCounter = time.time() + 900  # if not in game after 15 mins, restart valorant as there may be an error.
                # Change this if your servers are bad (in seconds) (900 = 15m)

                if q is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    self.waitingforgame()

                if q2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    self.waitingforgame()

                if q_aftergame is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    self.waitingforgame()

                if q_aftergame2 is not None:
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] DETECTED IN QUEUE")
                    self.waitingforgame()

            if q is None or q2 is None or q_aftergame is None or q_aftergame2 is None:
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] DETECTED NOT IN QUEUE")
                time.sleep(1)

                self.playbutton()

    def inqueuesearching(self):
        # to check if youre still in the queue
        queuecheck = pyautogui.locateOnScreen(self.inqueue_png)
        queuecheck2 = pyautogui.locateOnScreen(self.inqueue_png, confidence=0.5)

        queuecheck_2 = pyautogui.locateOnScreen(self.inqueue2_png)
        queuecheck_22 = pyautogui.locateOnScreen(self.inqueue2_png, confidence=0.5)

        if queuecheck is not None or queuecheck2 is not None or queuecheck_2 is not None or queuecheck_22 is not None:
            return True
        else:
            if self.valorantrunningcheck() is True:
                return False
            else:

                self.startvalorant()

    def waitingforgame(self):

        if cfg.debugWebhook:
            debugmessage = "In a queue"
            self.debugwebhookpush(debugmessage)
        activeactivity = "In Queue"

        earned = "{:,}".format(self.xpamount)

        try:

            self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbotpremium",
                            large_text=self.version, details=activeactivity, buttons=self.discordbutton)


        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] WAITING FOR A GAME")

        now = time.time()

        checkingame = False

        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > self.inqueueCounter:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break
            if self.inqueuesearching() is False:
                checkingame = True

            ingame = pyautogui.locateOnScreen(self.ingame_png)
            ingame2 = pyautogui.locateOnScreen(self.ingame_png, confidence=0.5)

            if ingame is not None or ingame2 is not None:
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED IN A GAME")
                self.ingameStartedAt = time.time()

                self.mutevalorant()

                if cfg.debugWebhook:
                    debugmessage = "In a match"
                    self.debugwebhookpush(debugmessage)

                activeactivity = "In Match"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbotpremium",
                                    large_text=self.version, details=activeactivity, buttons=self.discordbutton)

                except Exception:
                    pass

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=cfg.webhook,
                            username="Valbot")
                        embed = DiscordEmbed(color=0x90ee90, title="Match Found",
                                             description="A match has been found.\nWaiting for the match to end.")
                        authorname = self.version + " " + self.premiumnumber
                        embed.set_author(
                            name=authorname,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbotlogo_22plusnobg.png",
                        )
                        textforfooter = self.computer_name
                        embed.set_footer(text=textforfooter,
                                         icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                print(Style.RESET_ALL)
                print(Fore.YELLOW + " [-] WAITING FOR THE GAME TO END")

                if cfg.debugWebhook:
                    debugmessage = "Waiting for game to end"
                    self.debugWebhookpush(debugmessage)

                time.sleep(25)  # so it doesnt detect the end game screen as soon as it searches
                print(Style.RESET_ALL)
                print(Fore.YELLOW + Style.BRIGHT + " [-] TO PAUSE THE BOT HOLD F3")
                print(Fore.YELLOW + Style.BRIGHT + " [-] TO RESUME THE BOT HOLD F4")
                self.deathmatch_duration = time.time()
                self.deathmatch_duration += 780
                self.endofgame()
            if checkingame is True:
                self.playbutton()

    def forceclose(self):

        try:
            if keyboard.is_pressed('f5'):
                os.system('cls' if os.name == 'nt' else 'clear')
                print (Style.RESET_ALL)
                print(Fore.RED + " [!] FORCE STOPPING VALBOT")

                if cfg.debugWebhook:
                    debugmessage = "Valbot has been force stopped"
                    self.debugwebhookpush(debugmessage)

                pyautogui.keyUp('w')
                pyautogui.keyUp('a')
                pyautogui.keyUp('s')
                pyautogui.keyUp('d')
                pyautogui.keyUp('space')

                time.sleep(2)

                quit()

            else:
                # force close key check completed, f5 wasnt pressed so resume
                return
        except Exception as e:
            print()
            print(Fore.RED, "[!]", e)
            return

    def pause(self):

        if cfg.debugWebhook:
            debugmessage = "Valbot has been paused"
            self.debugwebhookpush(debugmessage)
        print(Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + " [!] PAUSING BOT")
        print(Fore.RED + Style.BRIGHT + " [!] HOLD F4 TO RESUME THE BOT")
        pyautogui.keyUp('w')
        pyautogui.keyUp('a')
        pyautogui.keyUp('s')
        pyautogui.keyUp('d')

        while True:
            self.forceclose()
            time.sleep(1)
            try:
                if keyboard.is_pressed('f4'):
                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] RESUMING BOT")
                    print(Fore.GREEN + " [√] TO PAUSE THE BOT AGAIN HOLD F3")

                    if cfg.debugWebhook:
                        debugmessage = "Valbot has been resumed"
                        self.debugwebhookpush(debugmessage)
                    break
            except Exception as e:
                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        menu = pyautogui.locateOnScreen(self.play_png, grayscale=True)
        menu2 = pyautogui.locateOnScreen(self.play_png, confidence=0.7, grayscale=True)
        q = pyautogui.locateOnScreen(self.inqueue_png, grayscale=True)
        q2 = pyautogui.locateOnScreen(self.inqueue_png, grayscale=True, confidence=0.6)

        if menu is not None or menu2 is not None:

            if cfg.debugWebhook:
                debugmessage = "Resuming to self.playbutton()"
                self.debugwebhookpush(debugmessage)
            self.playbutton()

        if q is not None or q2 is not None:
            if cfg.debugWebhook:
                debugmessage = "Resuming to self.inqueue()"
                self.debugwebhookpush(debugmessage)
            self.inqueue()

        if q is None or q2 is None or menu is None or menu2 is None:
            if cfg.debugWebhook:
                debugmessage = "Resuming to self.antiafk()"
                self.debugwebhookpush(debugmessage)
            self.antiafk()

    def pausepressed(self):

        if keyboard.is_pressed('f3'):
            self.pause()
        return

    def randommessage(self):
        pass

    def endofgame(self):

        time.sleep(.5)
        self.afk_buyweapon()

        while True:
            self.forceclose()
            self.pausepressed()

            if time.time() > self.deathmatch_duration:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            menu = pyautogui.locateOnScreen(self.play_png, grayscale=True)
            menu2 = pyautogui.locateOnScreen(self.play_png, confidence=0.6, grayscale=True)
            self.fullscreenval()

            if menu is not None or menu2 is not None:

                if (
                        time.time() - self.ingameStartedAt) < 120:  # if the game lasted less than 2 minutes then there is an issue
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] GAME ENDED PREMATURELY")

                    if self.foundwebhook == True:
                        try:
                            desc = "Current match ended prematurely\nReturning to play button and resuming"
                            webhook = DiscordWebhook(
                                url=cfg.webhook,
                                username="Valbot")
                            embed = DiscordEmbed(color=0x842bd7, title="Match Error", description=desc)
                            authorname = self.version + " " + self.premiumnumber
                            embed.set_author(
                                name=authorname,
                                url="https://github.com/MrFums/Valbot",
                                icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                            )
                            textforfooter = self.computer_name

                            embed.set_footer(text=textforfooter,
                                             icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                            embed.set_timestamp()
                            embed.set_thumbnail(
                                url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_curved.png')
                            webhook.add_embed(embed)
                            webhook.execute()
                        except Exception:
                            print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                    self.playbutton()

                if cfg.debugWebhook:
                    debugmessage = "At menu / end game screen"
                    self.debugwebhookpush(debugmessage)
                activeactivity = "At Menu"

                earned = "{:,}".format(self.xpamount)

                try:

                    self.RPC.update(state=("Earned " + earned + " XP"), start=self.timestarted, large_image="valbotpremium",
                                    large_text=self.version, details=activeactivity, buttons=self.discordbutton)


                except Exception as e:
                    print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

                self.gamesplayed += 1
                self.xpamount += 900

                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED AT END GAME SCREEN")
                self.unmutevalorant()
                self.xpscreen()

            else:
                self.antiafk()

    def xptargethook(self):

        print(Style.RESET_ALL)
        print(Fore.GREEN + " [!] XP TARGET HAS BEEN REACHED")

        if os.path.exists('config.ini'):
            config = ConfigParser(allow_no_value=True)
            config.read('config.ini')
            try:
                config.set('settings', 'xptarget', '0')
                config.set('settings', 'xptarget_remaining', '0')

                config.set('settings', 'xptarget_activated', 'false')

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


            except Exception as e:
                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        if self.foundwebhook == True:
            try:
                desc = "Target of " + str(self.xptarget) + " XP has been reached!\nValbot will resume until stopped."
                webhook = DiscordWebhook(
                    url=cfg.webhook,
                    username="Valbot")
                embed = DiscordEmbed(color=0x842bd7, title="XP Target Notification", description=desc)
                authorname = self.version + " " + self.premiumnumber
                embed.set_author(
                    name=authorname,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                )
                textforfooter = self.computer_name

                embed.set_footer(text=textforfooter,
                                 icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                embed.set_thumbnail(
                    url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_curved.png')
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")
            try:
                webhook = DiscordWebhook(url=cfg.webhook, username="Valbot", content=self.userid)
                response = webhook.execute()
            except:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK MENTION BUT IT IS NOT SETUP")

    def matchlimit(self):

        print(Style.RESET_ALL)
        print(Fore.RED + " [!] XP LIMIT HAS BEEN REACHED")
        print(Fore.RED + " [!] PC WILL NOW SHUTDOWN")

        if os.path.exists('config.ini'):
            config = ConfigParser(allow_no_value=True)
            config.read('config.ini')
            try:
                config.set('settings', 'matchlimit', '0')
                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


            except Exception as e:
                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
        if self.foundwebhook == True:
            try:
                webhook = DiscordWebhook(
                    url=cfg.webhook,
                    username="Valbot")
                embed = DiscordEmbed(color=0x842bd7, title="XP Limit Reached",
                                     description="The XP limit has been reached.\nPC has been shutdown.")
                authorname = self.version + " " + self.premiumnumber
                embed.set_author(
                    name=authorname,
                    url="https://github.com/MrFums/Valbot",
                    icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                )
                textforfooter = self.computer_name

                embed.set_footer(text=textforfooter,
                                 icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                embed.set_timestamp()
                embed.set_thumbnail(
                    url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_curved.png')
                webhook.add_embed(embed)
                webhook.execute()
            except Exception:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")
            try:
                webhook = DiscordWebhook(url=cfg.webhook, username="Valbot", content=self.userid)
                response = webhook.execute()
            except:
                print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK MENTION BUT IT IS NOT SETUP")

        time.sleep(10)
        os.system('shutdown /p /f')

    def afk_buyweapon(self):

        weaponselect = [['680', '200', 'Stinger'], ['680', '360', 'Spectre'], ['680', '520', 'Bucky'], ['680', '680', 'Judge'], ['900', '200', 'Bulldog'], ['900', '360', 'Guardian'],
                        ['900', '520', 'Phantom'], ['900', '680', 'Vandal'], ['1180', '200', 'Marshal'], ['1180', '360', 'Operator'], ['1180', '520', 'Ares'],
                        ['1180', '680', 'Odin']]

        # for 2560 x 1440, you must multiply each coordinate by 1.22 to convert 1920 x 1080 coordinates to 2560 x 1440.
        # this is because a 1440p monitor has 78% more pixels than a 1080p monitor and 1.22 represents 122% in scale.

        randomweapon = random.choice(weaponselect)

        x, y, weaponname = randomweapon

        x = int(x) * self.scaleFloat
        y = int(y) * self.scaleFloat

        # print (f'Buying {weaponname} at coordinates X: {x} Y: {y}')

        pyautogui.keyDown(cfg.buyMenuButton)
        time.sleep(randint(6, 7) / 150)
        pyautogui.keyUp(cfg.buyMenuButton)
        time.sleep(randint(5, 8) / 150)
        pyautogui.moveTo(x, y, (randint(1, 3) / 7), pyautogui.easeOutQuad)
        time.sleep(randint(5, 8) / 15)
        pyautogui.moveTo(x, y, (randint(1, 3) / 7), pyautogui.easeOutQuad)
        time.sleep(randint(5, 8) / 150)
        pyautogui.click()
        time.sleep(randint(6, 9) / 150)
        pyautogui.keyDown(cfg.buyMenuButton)
        time.sleep(randint(6, 7) / 150)
        pyautogui.keyUp(cfg.buyMenuButton)
        return

    def sendmessage(self):

        while self.messagelistBAK:  # while the list has things in it
            # time.sleep(5)

            listLen = len(self.messagelistBAK) - 1  # as the first item in a list is at position 0,
            # we need to -1 from the total length of the list

            pos = random.randint(0, listLen)  # finds a random position for the list
            selection = self.messagelistBAK[pos]  # selection is now at that value of position

            pyautogui.press('enter')  # open chat to start typing

            for char in selection:  # types each character from the selection out individually

                if char == '':  # if the char is a space, we need to tell python that it is the KEY space
                    char = 'SPACE'

                pyautogui.press(char)  # key down and then key up the character we are currently on
                ranSleep = random.randint(2, 5) / 50  # random delay between 40ms and 100 ms
                time.sleep(ranSleep)  # sleep for time we set above

            # self.messagelistBAK.pop(pos) #pop the currently used message from the list
            # so it wont send it again during the match
            self.messagelistBAK = []

            pyautogui.press('enter')  # send the message when its fully typed!
            break

        return

    def antiafk(self):
        n = randint(6, 10)
        a = 0
        activation = False

        cheater = pyautogui.locateOnScreen(self.cheaterdetected_png, grayscale=True)
        cheater1 = pyautogui.locateOnScreen(self.cheaterdetected_png, grayscale=True, confidence=0.6)

        cheatercontinue = pyautogui.locateOnScreen(self.continueterminated_png, grayscale=True)
        cheatercontinue1 = pyautogui.locateOnScreen(self.continueterminated_png, grayscale=True, confidence=0.6)

        while a <= n:
            self.forceclose()
            self.pausepressed()

            if cheater is not None or cheater1 is not None:

                if self.foundwebhook == True:
                    try:
                        webhook = DiscordWebhook(
                            url=cfg.webhook,
                            username="Valbot")
                        embed = DiscordEmbed(color=0xFF0000, title="Cheater Detected",
                                             description="A cheater was detected in your game.\nMatch has been cancelled.\nRestarting Valorant and resuming.")
                        authorname = self.version + " " + self.premiumnumber
                        embed.set_author(
                            name=authorname,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                        )
                        textforfooter = self.computer_name

                        embed.set_footer(text=textforfooter,
                                         icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")
                    try:
                        webhook = DiscordWebhook(url=cfg.webhook, username="Valbot", content=self.userid)
                        response = webhook.execute()
                    except:
                        print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK MENTION BUT IT IS NOT SETUP")

                print(Style.RESET_ALL)
                print(Fore.RED + " [!] CHEATER DETECTED IN GAME")
                time.sleep(1)
                self.startvalorant()

            a += 1  # adds a counter so it can check if the match is finished.
            n2 = randint(1, 11)  # the second value should be the same as the amount of selection you have
            if (n2 % 2) == 0:
                activation = not activation
            self.forceclose()
            self.pausepressed()

            if n2 == 1:
                self.afk_buyweapon()

            if n2 == 2:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('a')
                time.sleep((uniform(1, 3) / 6))
                pyautogui.click()
                pyautogui.keyUp('a')

            if n2 == 3:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('d')
                time.sleep((uniform(1, 3) / 6))
                pyautogui.click()
                pyautogui.keyUp('d')

            if n2 == 4:
                self.forceclose()
                self.pausepressed()

                pyautogui.click()
                pyautogui.keyDown('w')
                time.sleep((uniform(3, 8) / 6))
                pyautogui.keyUp('w')

            if n2 == 5:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('s')
                pyautogui.mouseDown(button='left')
                time.sleep((uniform(7, 8) / 6))
                pyautogui.keyUp('s')
                pyautogui.mouseUp(button='left')

            if n2 == 6:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('w')
                time.sleep(uniform(1, 3) / 100)
                pyautogui.keyDown('d')
                time.sleep((uniform(2, 4) / 6))
                pyautogui.keyUp('w')
                time.sleep(uniform(1, 3) / 100)
                pyautogui.keyUp('d')

            if n2 == 7:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('w')
                time.sleep(uniform(1, 3) / 100)
                pyautogui.keyDown('a')
                time.sleep((uniform(2, 4) / 6))
                pyautogui.keyUp('w')
                time.sleep(uniform(1, 3) / 100)
                pyautogui.keyUp('a')
                pyautogui.click()

            if n2 == 8:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('3')
                time.sleep(uniform(2, 4) / 100)
                pyautogui.keyUp('3')
                time.sleep(uniform(1, 3) / 30)
                pyautogui.click()
                time.sleep(uniform(1, 3) / 50)
                pyautogui.keyDown('1')
                time.sleep(uniform(4, 6) / 100)
                pyautogui.keyUp('1')

            if n2 == 8:
                self.forceclose()
                self.pausepressed()

                pyautogui.mouseDown(button='left')
                time.sleep(uniform(2, 20) / 100)
                pyautogui.mouseUp(button='left')
                time.sleep(uniform(2, 4) / 10)

            if n2 == 9:
                self.forceclose()
                self.pausepressed()

                pyautogui.keyDown('space')
                time.sleep(uniform(6, 9) / 100)
                pyautogui.keyUp('space')
                time.sleep(uniform(2, 4) / 20)

            if n2 == 10 or activation is True:
                self.forceclose()
                self.pausepressed()

                pyautogui.click()
                time.sleep(uniform(2, 20) / 200)
                pyautogui.click()
                time.sleep(uniform(2, 20) / 200)
                self.forceclose()
                self.pausepressed()

                pyautogui.click()
                time.sleep(uniform(2, 20) / 200)
                activation = not activation
                time.sleep(uniform(2, 20) / 200)
            if n2 == 11:
                self.sendmessage()

        self.endofgame()

    def xpscreen(self):

        runtimeraw = time.time() - self.start_time
        runtimeint = int(runtimeraw)
        runtime = str(datetime.timedelta(seconds=runtimeint))

        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                totalxp = config.getint('lifetime_values', 'totalxpamount')
                totalxp += self.xpamount

                totalgamesplayed = config.getint('lifetime_values', 'totalgamesplayed')
                totalgamesplayed += self.gamesplayed

                runtimeafterestarts = config.getfloat('lifetime_values', 'totalruntime')
                runtimeafterestarts = int(runtimeraw + runtimeafterestarts)
                totalruntime = str(datetime.timedelta(seconds=runtimeafterestarts))

                if cfg.debugWebhook:
                    debugmessage = "Written lifetime values to config"
                    self.debugwebhookpush(debugmessage)


            except Exception as e:
                print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

        global line
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [-] SEARCHING FOR THE XP SCREEN")
        if cfg.debugWebhook:
            debugmessage = "Searching for XP screen"
            self.debugwebhookpush(debugmessage)
        time.sleep(1)

        now = time.time()

        future = now + 600
        while True:
            self.forceclose()
            if keyboard.is_pressed('f3'):
                self.pause()
            if time.time() > future:
                # detects possible issue with valorant and restarts the game
                print(Style.RESET_ALL)
                print(Fore.RED + " [!] FOUND A POSSIBLE ERROR WITH VALORANT")
                self.startvalorant()
                break

            xpscreen = pyautogui.locateOnScreen(self.play_png, grayscale=True)
            xpscreen2 = pyautogui.locateOnScreen(self.play_png, confidence=0.6, grayscale=True)

            if xpscreen is not None or xpscreen2 is not None:
                if cfg.debugWebhook:
                    debugmessage = "XP screen has been found"
                    self.debugwebhookpush(debugmessage)
                print(Style.RESET_ALL)
                print(Fore.GREEN + " [√] DETECTED THE XP SCREEN")

                if os.path.exists('config.ini'):
                    try:
                        config = ConfigParser(allow_no_value=True)
                        config.read('config.ini')

                        config.set('runtime_values', 'restarted', str(self.restarted))
                        config.set('runtime_values', 'gamesplayed', str(self.gamesplayed))
                        config.set('runtime_values', 'xpamount', str(self.xpamount))
                        config.set('runtime_values', 'runtime', str(runtimeint))
                        if cfg.debugWebhook:
                            debugmessage = "Written runtime values to config"
                            self.debugwebhookpush(debugmessage)
                        with open('config.ini', 'w+') as configfile:
                            config.write(configfile)
                    except Exception as d:
                        if cfg.debugWebhook:
                            debugmessage = "Couldnt write runtime values to file " + str(d)
                            self.debugwebhookpush(debugmessage)

                # exact = start.strftime("%H:%M:%S")
                # dat = start.strftime("%d %h %Y")

                webhookruntime = str(datetime.timedelta(seconds=int(time.time() - self.timestarted)))
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)
                print(
                    Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + " Earned",
                      Style.BRIGHT + Fore.YELLOW + str(self.xpamount) + " XP" + Style.RESET_ALL + Fore.YELLOW,
                      "this session")
                try:
                    print(Fore.YELLOW + " Earned", Style.BRIGHT + Fore.YELLOW + str(totalxp),
                          "XP" + Style.RESET_ALL + Fore.YELLOW, "in total")
                except:
                    pass
                print(Fore.YELLOW + " Bot has been running for",
                      Style.BRIGHT + Fore.YELLOW + str(webhookruntime) + Style.RESET_ALL + Fore.YELLOW)
                # print(Fore.YELLOW + " Bot was started at", Style.BRIGHT + Fore.YELLOW + str(exact),
                #    Style.RESET_ALL + Fore.YELLOW + "on the" + Style.BRIGHT + Fore.YELLOW,
                #     dat + Style.RESET_ALL + Fore.YELLOW)
                print(Fore.YELLOW + " Played", Style.BRIGHT + Fore.YELLOW + str(self.gamesplayed),
                      "games" + Style.RESET_ALL + Fore.YELLOW)
                print(" Valorant has been", Style.BRIGHT + Fore.YELLOW + "restarted", self.restarted, "times")
                print(Style.RESET_ALL)
                print(Style.RESET_ALL + Fore.YELLOW + "——————————————————————————————————————————————————————")
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "                     " + self.version)
                print(Style.RESET_ALL)
                print(Style.RESET_ALL)

                if self.foundwebhook is True:
                    restartstring = (str(self.restarted) + " times")
                    if self.restarted == 0:
                        restartstring = "Not yet restarted"
                    elif self.restarted == 1:
                        restartstring = "1 time"

                    try:
                        webhook = DiscordWebhook(
                            url=cfg.webhook,
                            username="Valbot")

                        embed = DiscordEmbed(title='Valbot Summary', description='Valbot has completed a match loop!',
                                             color=34343)
                        authorname = self.version + " " + self.premiumnumber
                        embed.set_author(
                            name=authorname,
                            url="https://github.com/MrFums/Valbot",
                            icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                        )
                        textforfooter = self.computer_name

                        embed.set_footer(text=textforfooter,
                                         icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                        embed.set_timestamp()
                        embed.set_thumbnail(
                            url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_curved.png')

                        embed.add_embed_field(name="XP Earned", value=self.xpamount, inline=False)
                        embed.add_embed_field(name="Games Played", value=self.gamesplayed, inline=False)
                        try:

                            embed.add_embed_field(name="Runtime", value=webhookruntime, inline=False)
                        except Exception as e:
                            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
                        try:
                            embed.add_embed_field(name="Total XP Earned", value=totalxp, inline=False)
                            embed.add_embed_field(name="Total Games Played", value=totalgamesplayed, inline=False)

                            embed.add_embed_field(name="Total Runtime", value=totalruntime, inline=False)
                        except Exception as e:
                            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

                        timestarted_format = time.strftime('%H:%M:%S, %d %B %Y', time.localtime(self.timestarted))
                        embed.add_embed_field(name="Started At", value=timestarted_format, inline=False)

                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception as e:
                        print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

                    # except Exception:
                    #   print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " [!] DISCORD WEBHOOK IS NOT SETUP")

                time.sleep(2)

                if os.path.exists('config.ini'):
                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')

                    try:
                        self.xptarget = config.getint('settings', 'xptarget')
                        targetactive = config.getboolean('settings', 'xptarget_activated')
                        xpremaining = config.getint('settings', 'xptarget_remaining')

                        xpremaining -= 900

                        if cfg.debugWebhook:
                            debugmessage = "XP remaining for target is " + str(xpremaining)
                            self.debugwebhookpush(debugmessage)

                        if xpremaining < 1 and targetactive is True:
                            self.xptargethook()

                        elif xpremaining > 0 and targetactive is True:

                            matchRemain = xpremaining / 900  # finds how many games it needs to play by xptarget left

                            matchRemain = math.ceil(matchRemain)  # rounds to nearest int

                            timeRemain = str(matchRemain / 4.5)  # you play roughly 4.5 games per hour (13~ min a game)
                            decimal = float(timeRemain) % 1  # gets the decimal using modulus
                            timeRemain = math.trunc(float(timeRemain))  # truncates the value
                            timeRemainMin = decimal * 60  # finds time in minutes

                            timeRemaining = '~' + str(timeRemain) + " hours and " + str(int(timeRemainMin)) + ' minutes'
                            # ~1 hours and 56 minutes

                            if self.foundwebhook == True:
                                try:

                                    webhook = DiscordWebhook(
                                        url=cfg.webhook,
                                        username="Valbot")
                                    embed = DiscordEmbed(color=0xCDB7F6, title="XP Target Notification",
                                                         description='Valbot is working towards an XP target!')
                                    authorname = self.version + " " + self.premiumnumber
                                    embed.set_author(
                                        name=authorname,
                                        url="https://github.com/MrFums/Valbot",
                                        icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_noBG.png",
                                    )
                                    textforfooter = self.computer_name

                                    embed.set_footer(text=textforfooter,
                                                     icon_url="https://raw.githubusercontent.com/MrFums/ValbotAssets/main/fumspfp.png")
                                    embed.set_timestamp()
                                    embed.set_thumbnail(
                                        url='https://raw.githubusercontent.com/MrFums/ValbotAssets/main/valbot_premium_curved.png')
                                    embed.add_embed_field(name="XP Target:", value=str(self.xptarget), inline=False)
                                    embed.add_embed_field(name="XP Remaining:", value=str(xpremaining), inline=False)

                                    embed.add_embed_field(name="Time Left:", value=timeRemaining, inline=False)
                                    embed.add_embed_field(name="Games Left:", value='~' + str(matchRemain),
                                                          inline=False)
                                    webhook.add_embed(embed)
                                    webhook.execute()
                                except Exception:
                                    print(Fore.RED + " [!] TRIED TO SEND A WEBHOOK BUT IT IS NOT SETUP")

                            if os.path.exists('config.ini'):
                                config = ConfigParser(allow_no_value=True)
                                config.read('config.ini')

                                config.set('settings', 'xptarget_remaining', str(xpremaining))

                                with open('config.ini', 'w+') as configfile:
                                    config.write(configfile)
                    except Exception as e:
                        print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
                        # could not find xp target in config file

                if os.path.exists('config.ini'):
                    config = ConfigParser(allow_no_value=True)
                    config.read('config.ini')
                    try:
                        matchlimit = config.getint('settings', 'matchlimit')

                        if matchlimit != 0:  # check if there is a match limit set
                            matchlimit -= 1  # match limit found so remove 1 from it

                            if matchlimit == 0:  # if match limit is now 1, stop bot.
                                self.matchlimit()

                            else:  # if match limit continued tell user how many matches left
                                config.set('settings', 'matchlimit', str(matchlimit))

                                with open('config.ini', 'w+') as configfile:
                                    config.write(configfile)

                                print(Style.RESET_ALL)
                                print(Fore.BLUE + Style.BRIGHT,
                                      "[√]" + str(matchlimit) + " MATCHES" + Style.RESET_ALL + Fore.YELLOW,
                                      "UNTIL LIMIT REACHED")
                        else:
                            print(Style.RESET_ALL)
                            print(Fore.BLUE + Style.BRIGHT, "[√] NO XP LIMIT FOUND")


                    except Exception as e:
                        print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)
                        # could not find xp limit in config file

                self.resttimecheck()

                if time.time() > self.restarttime:
                    self.titlescreen()
                    self.restartbot()
                else:
                    gc.collect()
                    if cfg.debugWebhook:
                        debugmessage = "Collecting garbage"
                        self.debugwebhookpush(debugmessage)

                time.sleep(1)
                if cfg.debugWebhook:
                    debugmessage = "Running loop again"
                    self.debugwebhookpush(debugmessage)

                self.playagain()


if __name__ == '__main__':
    bot = bot()
    if os.path.exists('config.ini'):
        try:
            config = ConfigParser(allow_no_value=True)
            config.read('config.ini')

            startatrest = config.getboolean('rest_cycle', 'rest_start')

            if startatrest:
                bot.resttimecheck()
            # otherwise resume the bot like starting for the first time


        except Exception as e:
            print(Style.BRIGHT + Fore.RED, '[!]', e, Style.RESET_ALL)

    bot.firststart()
