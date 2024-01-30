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
        url = self.URL_Base + self.apiDict["INSTRUMENTS"]

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            self.__INSTRUMENTS = data.json()

        return data
    
    def getInstruments(self):
        return self.__INSTRUMENTS

    def refreshPies(self):
        url = self.URL_Base + self.apiDict["PIES"]

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            self.__PIES = data.json()
        
        return data
    
    def getPies(self):
        return self.__PIES

    def getPieById(self, id=0):
        url = self.URL_Base + self.apiDict["PIES"]
        url += f'/{id}'

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            return data.json()
        return

    def createPie(self):
        pass

    def deletePie(self):
        pass

    def updatePie(self):
        pass

    def refreshEquity(self):
        url = self.__URL_BASE + self.apiDict["EQUITY_ORDERS"]

        headers = {
            "Authorization" : self.__API_KEY
        }

        data = self.queueRequest(url, headers)

        if data.status_code == 200:
            self.__EQUITY_ORDERS = data.json()
        
        return data

    def getEquityOrders(self):
        return self.__EQUITY_ORDERS
    
    def placeLimitOrder(self):
        pass

    def placeMarketOrder(self):
        pass

    def placeStopOrder(self):
        pass

    def placeStopLimitOrder(self):
        pass

    def cancelByID(self):
        pass

    def fetchByID(self):
        pass

    def fetchAccountCash(self):
        pass

    def fetchAccountMetadata(self):
        pass

    def fetchAllOpenPositions(self):
        pass

    def fetchSpecificPosition(self):
        pass

    def refreshHistoricalOrderData(self):
        pass

    def getHistoricalOrderData(self):
        pass

    def getPaidOutDividends(self):
        pass

    def getExportsList(self):
        pass

    def getExportCSV(self):
        pass

    def getTransactionList(self):
        pass