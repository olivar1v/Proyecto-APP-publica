import requests
from config.endpoints import url_binance,url_binance_change24r,url_binance_klines

class Binance():
    def __init__(self):
        self.__url =url_binance
        self.__endpoint_cotizacion = url_binance_change24r
        self.__historico = url_binance_klines
        
    def obtener_cotizaciones(self):
        endpoint: str = self.__url + self.__endpoint_cotizacion
        return requests.get(endpoint).json()

    def Candlestick_Data(self,symbol: str,fechaInicial=None,fechaFinal=None):
        endpoint: str = self.__url + self.__historico
        
        if(fechaInicial is None):
            params = {"symbol":symbol,"interval":"1d"}
        else:
            params = {"symbol":symbol,"startTime":fechaInicial,"endTime":fechaFinal,"interval":"1d"}
        return requests.get(endpoint,params=params).json()
