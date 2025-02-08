try:
    import pathlib
    import requests
    import webbrowser
    import math
    import keyboard
    import psutil
    import pyautogui
    import pygetwindow as gw
    import os
    import time
    import urllib.request


    from PIL import Image
    from pathlib import Path
    from datetime import datetime
    from random import randint
    from time import sleep
    from colorama import Fore, Style
    from colorama import init
    from configparser import ConfigParser
    from pycaw.pycaw import AudioUtilities

except Exception as e: print(e), print("Package(s) needs downloading"), print("Run PackageInstaller.bat"), input(), quit()

init()  # not a clue what init function its loading but its needed lol
# ---------------------------------------------------------------

def main():

    config = ConfigParser(allow_no_value=True)
    config.read('config.ini')

    if not os.path.exists('config.ini'):
        open('config.ini','a+')
        try:
            config.add_section('settings')
        except Exception: pass
        config.set('settings', 'webhook', 'EMPTY_WEBHOOK')
        config.set('settings', 'userid', 'EMPTY_ID')
        config.set('settings', 'rpc_enabled', 'True')
        config.set('settings', 'matchlimit', '0')
        config.set('settings', 'xptarget', '0')
        config.set('settings', 'xptarget_activated', 'False')
        config.set('settings', 'xptarget_remaining', '0')
        config.set('settings', 'buymenu_button', 'b')
        config.set('settings', 'rpc_enabled', 'True')
        config.set('settings', 'mute_valorant_ingame', 'False')
        config.set('settings', 'debug_webhook', 'False')

        try:
            config.add_section('runtime_values')
        except Exception: pass
        config.set('runtime_values', '; you do not need to touch these, they are for when the bot restarts', None)
        config.set('runtime_values', 'restarted', '0')
        config.set('runtime_values', 'gamesplayed', '0')
        config.set('runtime_values', 'xpamount', '0')
        config.set('runtime_values', 'runtime', '0')
        config.set('runtime_values', 'starttime', '0')

        try:        
            config.add_section('lifetime_values')
        except Exception: pass
        config.set('lifetime_values', 'totalrestarted', '0')
        config.set('lifetime_values', 'totalgamesplayed', '0')
        config.set('lifetime_values', 'totalxpamount', '0')
        config.set('lifetime_values', 'totalruntime', '0')

        
        with open('config.ini', 'w+') as configfile:
            config.write(configfile)
    
    

    version = "Valbot Premium"
    versionstripped = version.replace("Valbot ", "")
    print(Style.RESET_ALL) 
    os.system('mode con: cols=39 lines=31')
    title = "title " + version
    os.system(title)
    print(Fore.YELLOW + """
    ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
    ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
    ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
     ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
     ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
      ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝
                           """ + Style.NORMAL + Fore.RED, Style.RESET_ALL)

    print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "     " + version + "       Fums#0888")
    print(Style.RESET_ALL) 
    print(Style.RESET_ALL)
    print(Style.RESET_ALL + Fore.YELLOW + "———————————————————————————————————————")

    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [1]", Style.BRIGHT + "Start Bot")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [2]", Style.BRIGHT + "Information")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [3]", Style.BRIGHT + "Discord Manager")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [4]", Style.BRIGHT + "XP Settings")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [5]", Style.BRIGHT + "Safe Cycle Manager")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [6]", Style.BRIGHT + "Toggle RPC")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [7]", Style.BRIGHT + "Toggle Mute Valorant")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + " [8]", Style.BRIGHT + "Exit Bot")
    print(Style.RESET_ALL)
    
    print(Fore.RED + "")
    try:
        menu = int(input(" > "))
    except ValueError:
        print(" Error 2: You must enter an integer!")
        time.sleep(2)
        main()
        
    if menu == 1:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)
        print(Fore.YELLOW + Style.BRIGHT, "Valbot will now initialize.")

        print(Fore.YELLOW + Style.BRIGHT, "Please do not interfere from now on." + Style.RESET_ALL + "\n\n")
        
        print(Fore.YELLOW, "Hotkey Controls (HOLD KEY): \n")
        print(' F3 >> Pause Bot')
        print(' F4 >> Resume Bot')
        print(' F5 >> Force Stop Bot')
        
        time.sleep(8)

        print(Style.RESET_ALL)
        root = str(pathlib.Path(__file__).parent.absolute())
        fullpath = root + "\Valorant.lnk"
        vallnk = Path(fullpath)
        if vallnk.is_file():
            # file exists
            config = ConfigParser(allow_no_value=True)
            
            config.read('config.ini')


            totalrestarted = config.getint('lifetime_values', 'totalrestarted')
            totalgamesplayed = config.getint('lifetime_values', 'totalgamesplayed')
            totalxpamount = config.getint('lifetime_values', 'totalxpamount')
            totalruntime = config.getint('lifetime_values', 'totalruntime')

            restartedlast = config.getint('runtime_values', 'restarted')
            gamesplayedlast = config.getint('runtime_values', 'gamesplayed')
            xpamountlast = config.getint('runtime_values', 'xpamount')
            runtimelast = config.getint('runtime_values', 'runtime')

            try:
                playtime = config.getint('rest_cycle', 'play_time')
                resttime = config.getint('rest_cycle', 'rest_time')
                
                playtime *= 3600
                resttime *= 3600
                
                resttime += playtime + time.time()

                playtime += time.time()
                
                
                config.set('rest_cycle', 'play_time_secs', str(playtime))
                config.set('rest_cycle', 'rest_time_secs', str(resttime))

            except Exception: pass

            totalrestarted += restartedlast
            totalgamesplayed += gamesplayedlast
            totalxpamount += xpamountlast
            totalruntime += runtimelast

            try:
                config.set('rest_cycle', 'rest_start', 'False')
            except Exception:
                pass
    

            config.set('lifetime_values', 'totalrestarted', str(totalrestarted))
            config.set('lifetime_values', 'totalgamesplayed', str(totalgamesplayed))
            config.set('lifetime_values', 'totalxpamount', str(totalxpamount))
            config.set('lifetime_values', 'totalruntime', str(totalruntime))

            config.set('runtime_values', 'restarted', '0')
            config.set('runtime_values', 'gamesplayed', '0')
            config.set('runtime_values', 'xpamount', '0')
            config.set('runtime_values', 'runtime', '0')
            timenow = time.time()
            config.set('runtime_values', 'starttime', str(timenow))
            
            with open('config.ini', 'w+') as configfile:
                config.write(configfile)


            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')
                try:
                    matchlimit = config.getint('settings', 'matchlimit')
                    
                    if matchlimit != 0:
                        print(Style.RESET_ALL)
                        print(Fore.GREEN, "Stopping after" + Style.BRIGHT, str(matchlimit), "matches", Style.RESET_ALL + Fore.GREEN + "played")
                    else:
                        pass

                except:
                    pass

            os.startfile(os.getcwd() + "\\bot.py")
            
            quit()
        else:
            print(Fore.RED, 'You do not have a Valorant shortcut')
            print(' named "Valorant" in the bots folder')
            print(Fore.RED, 'Add one now to continue')
            time.sleep(5)
            print(Style.RESET_ALL)
            time.sleep(5)
            main()


    elif menu == 2:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL + "")
        print(Fore.RED + " IMPORTANT INFORMATION")
        print("")
        print(Fore.WHITE + " 1)", Fore.CYAN + "Put your Valorant shortcut")
        print("    in the same folder as the bot.", Style.RESET_ALL)
        print("")
        print(Fore.WHITE + " 2)", Fore.CYAN + "Must be in English and ")
        print("    1920x1080 resolution")
        print("")
        print(Fore.WHITE + " 3)", Fore.CYAN + "Valorant must be windowed ")
        print("    fullscreen and focused")
        print("")
        print(Fore.BLUE + " My Discord :", Fore.YELLOW + "Fums#0888")
        print(Fore.BLUE + " Discord :", Fore.YELLOW + "https://gg.gg/valbotserver")
        print(Fore.CYAN, Fore.BLUE + "Github :", Fore.YELLOW + "https://github.com/MrFums/", Style.RESET_ALL)
        print(Style.RESET_ALL)
        print(Style.BRIGHT, Fore.RED)
        print("")
        print(" Input anything to return...")
        print(Fore.RED, Style.NORMAL + "")
        input(" > ")
        main()

    elif menu == 4:
        os.system('mode con: cols=39 lines=31')
        title = "title " + version
        os.system(title)
        print(Fore.YELLOW + """
    ╔╗  ╔╗╔═══╗╔╗   ╔══╗ ╔═══╗╔════╗
    ║╚╗╔╝║║╔═╗║║║   ║╔╗║ ║╔═╗║║╔╗╔╗║
    ╚╗║║╔╝║║ ║║║║   ║╚╝╚╗║║ ║║╚╝║║╚╝
     ║╚╝║ ║╚═╝║║║ ╔╗║╔═╗║║║ ║║  ║║  
     ╚╗╔╝ ║╔═╗║║╚═╝║║╚═╝║║╚═╝║  ║║  
      ╚╝  ╚╝ ╚╝╚═══╝╚═══╝╚═══╝  ╚╝
                       """ + Style.NORMAL + Fore.RED, Style.RESET_ALL)

        print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "     " + version + "       Fums#0888")
        print(Style.RESET_ALL) 
        print(Style.RESET_ALL)
        print(Style.RESET_ALL + Fore.YELLOW + "———————————————————————————————————————")

        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [1]", Style.BRIGHT + "XP Calculator")
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [2]", Style.BRIGHT + "Change XP Limit")
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [3]", Style.BRIGHT + "Change XP Target")
        print(Style.RESET_ALL)
        print(Fore.YELLOW + " [4]", Style.BRIGHT + "Return to Menu")
        print(Style.RESET_ALL)
        
        print(Fore.RED + "")
        try:
            menusmall = int(input(" > "))
        except ValueError:
            main()

        if menusmall == 1:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL + "")
            print(Fore.RED + " XP CALCULATOR")
            print("")

            print(Fore.WHITE + " 1)", Fore.CYAN + "Here you can calculate how much")
            print("    time it will take to reach")
            print ("    a certain amount of XP", Style.RESET_ALL)
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Enter the amount of XP you ")
            print("    want to earn below")
            print("")
            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()

            xpa = xpai / 900
            xpau = (math.ceil(xpa))
            print(Style.RESET_ALL)
            print(Fore.BLUE, "Required Games: " + Style.BRIGHT + str(xpau), Fore.BLUE + "games")
            print(Style.RESET_ALL)
            print(Fore.BLUE, "ETA:", Style.BRIGHT + str(xpau / 4), Fore.BLUE + "hours")
            time.sleep(7)
            print(Style.RESET_ALL)
            main()
            
        if menusmall == 2:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Fore.RED + " XP LIMITER")
            print("")
            print(Fore.WHITE + " 1)", Fore.CYAN + "Here you can limit the maximum")
            print("    amount of XP to earn")
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "When this limit has been ")
            print("    reached, your PC will shutdown")
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "If you don't want a limit, enter 0")
            print("")
            print(Fore.WHITE + " 4)", Fore.CYAN + "Enter XP limit below") 

            print(Style.RESET_ALL)

            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()

            xpa = xpai / 900
            xpau = (math.ceil(xpa))

            if xpai < 0:
                xpau = 0

            # need to write to config

            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                config.set('settings', 'matchlimit', str(xpau))

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)


            os.system('cls' if os.name=='nt' else 'clear')

            if xpai > 0:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "Set to stop after", str(xpau), "games played")
            else:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "No XP limit set. PC will not shutdown")

            time.sleep(4)
            main()
        elif menusmall == 3:
            os.system('cls' if os.name=='nt' else 'clear')
                        
            print(Style.RESET_ALL)

            print(Fore.RED + " XP TARGET")
            print("")

            print(Fore.WHITE + " 1)", Fore.CYAN + "Set a notification to be sent once ")
            print("    you reach a certain amount of XP")
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "If you don't want a notification,")
            print("    enter 0")
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "A DISCORD WEBHOOK IS REQUIRED!")
            print("")
            print(Fore.WHITE + " 4)", Fore.CYAN + "Enter XP target below") 

            print(Style.RESET_ALL)

            try:
                print(Style.RESET_ALL)
                print(Fore.RED + "")
                xpai = int(input(" > "))
            except ValueError:
                print(" Error 2: You must enter an integer!")
                time.sleep(2)
                main()


            if xpai < 0:
                xpai = 0
                
            os.system('cls' if os.name=='nt' else 'clear')

            if xpai > 0:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "Target of", str(xpai), "XP has been set")
                target = True
            else:
                print(Style.RESET_ALL)
                print(Fore.GREEN + Style.BRIGHT, "No target set.")
                target = False


            # need to write to config

            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                config.set('settings', 'xptarget', str(xpai))
                config.set('settings', 'xptarget_remaining', str(xpai))

                config.set('settings', 'xptarget_activated', str(target))


                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)
                    
            time.sleep(4)
            main()
            
        elif menusmall == 4:
            main()
        else:
            print(" You must enter a valid integer!")
            time.sleep(2)
            main()
            
        


            
    elif menu == 5:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)
        print(Fore.RED + " VALBOT SAFE CYCLE")
        print(Style.RESET_ALL)
        print(Fore.WHITE + " 1)", Fore.CYAN + "Safe cycle makes it so")
        print("    the bot will run and have")
        print("    a rest for an amount of time")
        print("")
        print(Fore.WHITE + " 2)", Fore.CYAN + "This will make it seem ")
        print('    that you are playing')
        print('    legit (eating, sleeping etc)')
        print("")
        print(Fore.WHITE + " 3)", Fore.CYAN + "Keep in mind that the")
        print('    efficiency of Valbot will be')
        print('    greatly decreased when activated')
        print("")
        print(Fore.WHITE + " 4)", Fore.CYAN + "This is recommended")
        print('    for when leaving Valbot running')
        print('    for an extended amount of time ')
        print('    (days at a time)')
        print("")
        print(Fore.WHITE + " 5)", Fore.CYAN + "A good example is running")
        print('    for 10 hours and then resting')
        print('    for 4 hours')
        print("")
        print(Style.BRIGHT, Fore.RED +  "Would you like to enable it (Y/N)?")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)
        print(Fore.RED + "")
        inputanswer = input(" > ").lower()
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)

        if inputanswer == "y" or inputanswer == "yes":
            
            print(Style.BRIGHT, Fore.BLUE +  "Time to play in hours:")
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.RED + "")
            playtime = input(" > ")
            try:
                playtime = int(playtime)
            except:
                print("You must enter an integer!")
                time.sleep(2)
                main()
                
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)

            print(Style.BRIGHT, Fore.BLUE +  "Time to rest in hours:")
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.RED + "")
            resttime = input(" > ")
            try:
                resttime = int(resttime)
            except:
                print("You must enter an integer!")
                time.sleep(2)
                main()
            
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)

            
            
            
            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')
                try:
                    config.add_section('rest_cycle')
                except Exception: pass
                config.set('rest_cycle', 'safe_cycle', 'True')
                config.set('rest_cycle', 'play_time', str(playtime))
                config.set('rest_cycle', 'rest_time', str(resttime))

                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)
                    
            else:
                print (Fore.RED, "Config file not found, this should not happen")
                
            print(Fore.GREEN, Style.BRIGHT + "Activated safe cycle.")
            print(' Bot will run for',str(playtime),'hours and then')
            print(' rest for',str(resttime),'hours.')
            
            
            time.sleep(5)
            main()
            
        else:
            
            if os.path.exists('config.ini'):
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')


                config.set('rest_cycle', 'safe_cycle', 'False')


                with open('config.ini', 'w+') as configfile:
                    config.write(configfile)
                    
            else:
                print (Fore.RED, "Config file not found, this should not happen")
            print(Style.RESET_ALL)
            print(Fore.RED + " Not activated.")
            print(Fore.RED + " Returning to menu...")
            time.sleep(3)
            main()
        
     
    elif menu == 3:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)
        print(Fore.RED + " DISCORD WEBHOOK MANAGER")
        print(Style.RESET_ALL)
        print(Fore.WHITE + " 1)", Fore.CYAN + "Open Discord, go to a server where")
        print("    you have permission to create")
        print("    and manage a webhook")
        print("")
        print(Fore.WHITE + " 2)", Fore.CYAN + "Either create and / or edit an ")
        print('    existing channel and go to')
        print('    "Integrations"')
        print("")
        print(Fore.WHITE + " 3)", Fore.CYAN + "Click webhooks and then click")
        print('    "Create Webhook", select the right')
        print('    channel, and then click')
        print('    "Copy Webhook URL"')
        print("")
        print(Fore.WHITE + " 4)", Fore.CYAN + "Paste your webhook below")
        print(Style.RESET_ALL)
        print(Style.BRIGHT, Fore.RED)
        print(" Paste a webhook to save or enter")
        print(" anything else to cancel")
        print(Style.RESET_ALL)
        print(Style.RESET_ALL)

        urlcheck = "https://discord.com/api/webhooks/"
        print(Fore.RED + "")
        inputwebhook = input(" > ")
        inputwebhook = inputwebhook.replace("https://discordapp.com/api/webhooks/", "https://discord.com/api/webhooks/")


        config = ConfigParser(allow_no_value=True)
        
        if urlcheck in inputwebhook:
            print(Style.RESET_ALL)
            config.read('config.ini')


            config.set('settings', 'webhook', inputwebhook)

            with open('config.ini', 'w+') as configfile:
                config.write(configfile)

            print(Style.RESET_ALL)
            print(Fore.GREEN + " [√] Webhook added")
            print(Style.RESET_ALL)
            time.sleep(3)

            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.RESET_ALL)
            print(Fore.RED + " USER TAG MANAGER")
            print(Style.RESET_ALL)
            print(Fore.WHITE + " 1)", Fore.CYAN + "Open Discord, go to Settings >")
            print("    Advanced and enable Developer Mode")
            print("")
            print(Fore.WHITE + " 2)", Fore.CYAN + "Go back to the main page and ")
            print('    right click your name and press')
            print('    "Copy ID" to copy the ID')
            print("")
            print(Fore.WHITE + " 3)", Fore.CYAN + "Paste your ID below")
            print(Style.RESET_ALL)
            print(Style.BRIGHT, Fore.RED)
            print(" Paste a valid id to save or enter")
            print(" anything else to cancel")
            print(Style.RESET_ALL)
            print(Style.RESET_ALL)
            print(Fore.RED + "")
            
            inputid = input(" > ")

            try:
                inputid = int(inputid)
                    
                if len(str(inputid)) > 16 and len(str(inputid)) < 21:
                    print(Style.RESET_ALL)
                    config.read('config.ini')


                    config.set('settings', 'userid', str(inputid))

                    with open('config.ini', 'w+') as configfile:
                        config.write(configfile)

                    print(Style.RESET_ALL)
                    print(Fore.GREEN + " [√] User ID added")
                    print(Style.RESET_ALL)
                    time.sleep(3)
                    
                    

                else:
                    print(Style.RESET_ALL)
                    print(Fore.RED + " Not a valid discord User ID,")
                    print(Fore.RED + " returning to menu...")
                    time.sleep(3)
                    main()

            except:
                print(Style.RESET_ALL)
                print(Fore.RED + " Not a valid discord User ID,")
                print(Fore.RED + " returning to menu...")
                time.sleep(3)
                main()
            
            main()
            
        else:
            print(Style.RESET_ALL)
            print(Fore.RED + " Not a valid discord webhook")
            print(Fore.RED + " webhook, returning to menu...")
            time.sleep(3)
            main()
                    
    
    elif menu == 6:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)
        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                rpc_enabled = config.getboolean('settings', 'rpc_enabled') 
            except Exception:
                print(Style.RESET_ALL + Fore.RED + " Record not in config. Added now.")
                rpc_enabled = False
        else:
            rpc_enabled = True
            
        rpc_enabled = not rpc_enabled
        
        if rpc_enabled is True:
        
            print(Style.BRIGHT + Fore.GREEN + " Discord Rich Presence is now on!")
        else:
            print(Style.BRIGHT + Fore.RED + " Discord Rich Presence is now off!")

        
        try:
            open('config.ini','a+')
            config.set('settings', 'rpc_enabled', str(rpc_enabled))
            with open('config.ini', 'w+') as configfile:
                config.write(configfile)
                
        except Exception:
            print(Style.RESET_ALL + Fore.RED + " Could not write to config file!")
        
        time.sleep(5)
        main()
        
        
    elif menu == 7:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.RESET_ALL)
        if os.path.exists('config.ini'):
            try:
                config = ConfigParser(allow_no_value=True)
                config.read('config.ini')

                mute_valorant_ingame = config.getboolean('settings', 'mute_valorant_ingame') 
            except Exception:
                print(Style.RESET_ALL + Fore.RED + " Record not in config. Added now.")
                mute_valorant_ingame = False
        else:
            mute_valorant_ingame = True
            
        mute_valorant_ingame = not mute_valorant_ingame
        
        if mute_valorant_ingame is True:
        
            print(Style.BRIGHT + Fore.GREEN + " Valorant will be muted in game!")
        else:
            print(Style.BRIGHT + Fore.RED + " Valorant will be unmuted in game!")

        
        try:
            open('config.ini','a+')
            config.set('settings', 'mute_valorant_ingame', str(mute_valorant_ingame))
            with open('config.ini', 'w+') as configfile:
                config.write(configfile)
                
        except Exception:
            print(Style.RESET_ALL + Fore.RED + " Could not write to config file!")
        
        time.sleep(5)
        main()
    

    elif menu == 8:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.BRIGHT + Fore.RED + " Quitting...")
        time.sleep(1)
        quit()

    else:
        print(" Error 1: Enter a valid integer within the range 1 - 8!")
        time.sleep(2)
        main()




if __name__ == "__main__":
    main()
