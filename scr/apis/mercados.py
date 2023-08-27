from datetime import datetime

from apis.binance import Binance
from apis.iol import invertirOnline



class Mercados:
    def __init__(self):
        self.__iol = invertirOnline()
        self.__binance = Binance()


    def descargo_cotizaciones(self):

        self.__iol.obtengo_token()

        acciones_usa = self.__iol.obtener_cotizaciones("acciones","estados_Unidos")
        merval = self.__iol.obtener_cotizaciones("acciones","argentina")
        cedears = self.__iol.obtener_cotizaciones("cedears","argentina")
        ons = self.__iol.obtener_cotizaciones("obligacionesNegociables","argentina")


        cripto = self.__binance.obtener_cotizaciones()

        columnas = ["ticker","ultimaCotizacion","fecha","tipoInstrumento","fechaDescarga"]
        datos =[]
        fecha = datetime.now()

        for i in ons["titulos"]:
            cotizacion = [i["simbolo"],i["ultimoPrecio"],datetime.strptime(str(i["fecha"]).replace("T"," ")[:16],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M"),"ON",fecha]
            datos.append(cotizacion)
        for i in cedears["titulos"]:
            cotizacion = [i["simbolo"],i["ultimoPrecio"], datetime.strptime(str(i["fecha"]).replace("T"," ")[:16],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M"),"CEDEAR",fecha]
            datos.append(cotizacion)
        for i in merval["titulos"]:
            cotizacion = [i["simbolo"],i["ultimoPrecio"],datetime.strptime(str(i["fecha"]).replace("T"," ")[:16],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M"),"MERVAL",fecha]
            datos.append(cotizacion)


        for i in acciones_usa["titulos"]:
            cotizacion = [i["simbolo"],i["ultimoPrecio"], datetime.strptime(str(i["fecha"]).replace("T"," ")[:16],"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M"),"USA",fecha]
            datos.append(cotizacion)


        for i in cripto:
            if "USDT" == i["symbol"][-4:]:
                cotizacion = [i["symbol"],i["lastPrice"],datetime.fromtimestamp(i["closeTime"]/1000).strftime("%Y-%m-%d %H:%M"),"CRIPTO",fecha]
                datos.append(cotizacion)

        return [dict(zip(columnas, values)) for values in datos] 
    

