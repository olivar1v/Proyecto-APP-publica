import requests
from datetime import datetime
from config.endpoints import url_criptoya,url_criptoya_usdt,url_criptoya_dolares
class Dolar:

    def __init__(self):
        self.__url = url_criptoya
        self.__enpoint_usdt = url_criptoya_usdt
        self.__enpoint_dolares = url_criptoya_dolares

    def __get_usdt(self):
        response = requests.get(url=self.__url+self.__enpoint_usdt).json()
        meanPrice = 0
        cantPrice = 0 
        for price in response['data']:
            meanPrice +=float(price['adv']['price'])
            cantPrice +=1

        return round(meanPrice/cantPrice,2)
    
    def obtengo_cotizaciones(self):
        dolares = requests.get(url=self.__url+self.__enpoint_dolares).json()
        p2pBinance = self.__get_usdt()
        fecha = datetime.now()

        return [
            {"Tipo":"Oficial","UltimaCotizacion":dolares["oficial"],"FechaDescarga":fecha},
            {"Tipo":"Blue","UltimaCotizacion":dolares["blue"],"FechaDescarga":fecha},
            {"Tipo":"MEP","UltimaCotizacion":dolares["mep"],"FechaDescarga":fecha},
            {"Tipo":"CCL","UltimaCotizacion":dolares["ccl"],"FechaDescarga":fecha},
            {"Tipo":"Binance P2P","UltimaCotizacion":p2pBinance,"FechaDescarga":fecha},

            ]