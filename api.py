import requests
import datetime
import time

class Interface():

    def __init__(self, API_KEY: str, mode="LIVE"):

        print("Initialising API Interface")

        #SET URL TO GRAB FROM T212 API
        if mode == "LIVE":
            self.URL_Base = "https://live.trading212.com/"
        elif mode == "DEMO":
            self.URL_Base = "https://demo.trading212.com/"

        # API DICTIONARY HOLDS API CALL DIRECTORIES
        # WILL BE LOADED BY EXTERNAL FILE EVENTUALLY
        self.apiDict = {
            "EXCHANGE" : "api/v0/equity/metadata/exchanges",
            "INSTRUMENTS" : "api/v0/equity/metadata/instruments",
            "PIES" : "api/v0/equity/pies",
            "EQUITY_ORDERS" : "api/v0/equity/orders",
            "ACCOUNT" : "api/v0/equity/account",
            "PORTFOLIO" : "api/v0/equity/portfolio",
            "EQUITY_HISTORY" : "api/v0/equity/history",
            "OTHER_HISTORY" : "api/v0/history"
        }

        self.__EXCHANGES = None
        self.__PIES = None
        self.__EQUITY_ORDERS =  None
        self.__ACCOUNT_DATA = None
        self.__PERSONAL_PORTFOLIO = None
        self.__HISTORY = None

        

        print("Setting API Key")

        self.__API_KEY = API_KEY

        print("Testing API Key")

        url = self.URL_Base + self.apiDict["EXCHANGE"]

        headers = {
            "Authorization":self.__API_KEY
        }

        response = requests.get(url, headers=headers)
        self.__LAST_REQUEST = datetime.datetime.now()

        if response.status_code == 200:
            print("API Key Working, storing intial data")
            self.__EXCHANGES = response.json()
        else:
            raise Exception(f"ERROR, CODE {response.status_code}, PLEASE REFER TO USER MANUAL OR INTERNET AND ENSURE API KEY IS VALID")
            
    def queueRequest(self, url, headers):
        while True:
            currTime = datetime.datetime.now()
            deltaT = currTime - self.__LAST_REQUEST
            if deltaT.seconds > 1/30: # IF TOO QUICK
                time.sleep(1/60) # WAIT
            else:
                response = requests.get(url, headers=headers)
                self.__LAST_REQUEST = datetime.datetime.now()

                return response


    def refreshExchanges(self):
        url = self.URL_Base + self.apiDict["EXCHANGE"]

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            self.__EXCHANGES = data.json()

        return data

    def getExchanges(self):
        return self.__EXCHANGES
    
    def refreshInstruments(self):
        url = self.URL_Base + self.apiDict["INSTRUMENT"]

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            self.__INSTRUMENTS = data.json()

        return data
    
    def getInstruments(self):
        return self.__INSTRUMENTS
