from configparser import ConfigParser

config = ConfigParser(allow_no_value=True)
config.read('config.ini')

webhook = config.get('settings', 'webhook')
buyMenuButton = config.get('settings', 'buymenu_button')
debugWebhook = config.getboolean('settings', 'debug_webhook')
rpcEnabled = config.getboolean('settings', 'rpc_enabled')
muteInGame = config.getboolean('settings', 'mute_valorant_ingame')
discordID = config.get('settings', 'userid')

restarted = config.getint('runtime_values', 'restarted')
timestarted = config.getfloat('runtime_values', 'starttime')
gamesplayed = config.getint('runtime_values', 'gamesplayed')
xpamount = config.getint('runtime_values', 'xpamount')
xptarget = config.getint('settings', 'xptarget')
