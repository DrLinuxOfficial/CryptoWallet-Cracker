# ================================================== #
# Crypto Wallet Private Key Cracker .
# ------------------------------------
# 2020-2022 Copyright (Dr.Linux) .
# ------------------------------------
# Coded By : Dr.Liux !
#
# GitHub Page ==> https://github.com/DrLinuxOfficial/CryptoWallet-Cracker
#
#
# Thank You For Use My Project :) !
# ================================================== #


import subprocess
import sys
import os
import pip
import platform
import time


def PackageInstaller(Package):
    try:
        pip.main(["install",  Package])
    except AttributeError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", Package])
    os.execl(sys.executable, sys.executable, *sys.argv)


try:
    __import__("requests")
except ModuleNotFoundError:
    PackageInstaller("requests")

try:
    __import__("bs4")
except ModuleNotFoundError:
    PackageInstaller("beautifulsoup4")

try:
    __import__("bitcoinaddress")
except ModuleNotFoundError:
    PackageInstaller("bitcoinaddress")

if (platform.uname()[0]) == "Windows":
    try:
        from colorama import init
    except ModuleNotFoundError:
        PackageInstaller("colorama")
    init()


from Core import BTCCracker


class Crack:
    def __init__(self):
        self.__Clear__()
        self.__Writer__("\033[37;1mCreated\033[0;m \033[36;1mBy\033[0;m : \033[33;1mDr\033[0;m.\033[33;1mLinux\033[0;m\n\n")
        self.bot_token = input("Your \033[34;1mTelegram\033[0;m Bot \033[32;1mToken\033[0;m : ")
        self.user_id = input("Your \033[34;1mTelegram\033[0;m \033[32;1mNumber\033[0;m \033[36;1mID\033[0;m : ")
        self.__Clear__()

    def __Clear__(self):
        if (platform.uname()[0]) == "Linux":
            os.system("clear")
        if (platform.uname()[0]) == "Windows":
            os.system("cls")

    def __Writer__(self, data):
        for i in data:
            print(i, end="", flush=True)
            time.sleep(0.1)

    def __Banner__(self):
        self.__Clear__()
        self.__Writer__("""\033[32;1m   ____                  _        
  / ___|_ __ _   _ _ __ | |_ ___  
 | |   | '__| | | | '_ \| __/ _ \ 
 | |___| |  | |_| | |_) | || (_) |
  \____|_|   \__, | .__/ \__\___/ 
             |___/|_|\033[0;m\n""")
        self.__Writer__("""\033[36;1m .o88b. d8888b.  .d8b.   .o88b. db   dD d88888b d8888b. 
d8P  Y8 88  `8D d8' `8b d8P  Y8 88 ,8P' 88'     88  `8D 
8P      88oobY' 88ooo88 8P      88,8P   88ooooo 88oobY' 
8b      88`8b   88~~~88 8b      88`8b   88~~~~~ 88`8b   
Y8b  d8 88 `88. 88   88 Y8b  d8 88 `88. 88.     88 `88. 
 `Y88P' 88   YD YP   YP  `Y88P' YP   YD Y88888P 88   YD\033[0;m
                                                        \033[34;1mv\033[0;m\033[33;1m2.0\033[0;m
                \033[35;1mCreated\033[0;m By : \033[33;1mDr\033[0;m.\033[33;1mLinux\033[0;m
                My \033[34;1mGitHub\033[0;m ID \033[35;1m==>\033[0;m \033[37;1mDrLinuxOfficial\033[0;m\n\n""")

    def __Tool__(self):
        print("\033[33;1m1\033[0;m. \033[32;1mBTC\033[0;m\n")
        tool_num = [1]
        tool_user = int(input("Which One Do You Want ? "))
        if tool_user in tool_num:
            if tool_user == 1:
                self.__Clear__()
                print("""\033[33;1m1\033[0;m. \033[32;1mBase58(P2PKH) Wallet Offline Crack\033[0;m
\033[33;1m2\033[0;m. \033[32;1mBech32(P2WPKH) Wallet Offline Crack\033[0;m
\033[33;1m3\033[0;m. \033[32;1mBase58(P2PKH) Wallet Online Crack\033[0;m
\033[33;1m4\033[0;m. \033[32;1mBech32(P2WPKH) Wallet Online Crack\033[0;m
\033[33;1m5\033[0;m. \033[32;1mBase58(P2PKH) Genearte And Check Balance\033[0;m
\033[33;1m6\033[0;m. \033[32;1mBech32(P2WPKH) Genearte And Check Balance\033[0;m
\033[33;1m7\033[0;m. \033[32;1mBase58(P2PKH) Online Genearte And Check Balance\033[0;m
\033[33;1m8\033[0;m. \033[32;1mBech32(P2WPKH) Online Genearte And Check Balance\033[0;m\n""")
                option_num = [1,2,3,4,5,6,7,8]
                option_user = int(input("Which One Do You Want ? "))
                if option_user in option_num:
                    self.__Banner__()
                    if option_user == 1:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        target_wallet = input("Enter Base58(P2PKH) Target Wallet : ")
                        btc_handler.P2PKH_OfflineAttack(target_wallet)
                    elif option_user == 2:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        target_wallet = input("Enter Bech32(P2WPKH) Target Wallet : ")
                        btc_handler.P2WPKH_OfflineAttack(target_wallet)
                    elif option_user == 3:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        target_wallet = input("Enter Base58(P2PKH) Target Wallet : ")
                        btc_handler.P2PKH_OnlineAttack(target_wallet)
                    elif option_user == 4:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        target_wallet = input("Enter Bech32(P2WPKH) Target Wallet : ")
                        btc_handler.P2WPKH_OnlineAttack(target_wallet)
                    elif option_user == 5:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        btc_handler.P2PKH_BalanceAttack()
                    elif option_user == 6:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        btc_handler.P2WPKH_BalanceAttack()
                    elif option_user == 7:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        btc_handler.P2PKH_DatabaseBalanceAttack()
                    elif option_user == 8:
                        btc_handler = BTCCracker(bot_token=(self.bot_token), chat_id=(self.user_id))
                        btc_handler.P2WPKH_DatabaseBalanceAttack()

cracker_handler = Crack()
cracker_handler.__Tool__()
