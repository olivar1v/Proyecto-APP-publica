import requests
from config.credential import user_iol,pass_iol
from config.endpoints import url_iol,url_iol_token

class invertirOnline:
    def __init__(self):
        self.__user: str = user_iol
        self.__pass: str = pass_iol
        self.__url: str = url_iol
        self.__endpoint_token: str = url_iol_token
        self.__token: str

    def obtengo_token(self):
        task = {"username": self.__user,"password": self.__pass,"grant_type": 'password' }
        respToken = requests.post(url=self.__url+self.__endpoint_token, data=task,timeout =10)
        authJson = respToken.json()
        api_key = str(authJson['access_token'])
        self.__token = api_key

    
    def obtener_cotizaciones(self,instrumento:str,pais:str):
        
        ##########################################
        # Instrumento = "acciones"
        # Pais ="estados_Unidos"
        ##########################################
        # Instrumento = "cedears"
        # Pais ="argentina"
        ##########################################
        # Instrumento = "acciones"
        # Pais ="argentina"
        ##########################################
        # Instrumento = "obligacionesNegociables"
        # Pais ="argentina"
        ##########################################


        head = {'Authorization':f'Bearer {self.__token}'}
        parametros = {'panelCotizacion.instrumento':instrumento,'panelCotizacion.pais':pais,'api_key':self.__token}
        url =  f'{self.__url}/api/v2/Cotizaciones/{instrumento}/{pais}/Todos'

        
        response = requests.get(url= url,params=parametros,headers=head)

        if response.status_code==200:
            return response.json()
        return {"message":"error","status code":response.status_code}