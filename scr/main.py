
from config.db import cnn_cloud
from model.tenenciasCompras import tenenciasCompras
from model.mercado import mercado
from model.tipoDolares import tipoDolares
from apis.mercados import Mercados
from apis.dolar import Dolar


def main():


    try:

        mercados = Mercados()
        tenencias = cnn_cloud.execute(tenenciasCompras.select().distinct(tenenciasCompras.c.ticker,tenenciasCompras.c.tipoInstrumento))
        cotizacionesMercado = mercados.descargo_cotizaciones()

        tenencias = [dict(r._mapping) for r in tenencias]

        cotizacionActuales = []

        for cotizacion in cotizacionesMercado:
            for activo in tenencias:
                if cotizacion["ticker"]==activo["ticker"] and cotizacion["tipoInstrumento"]==activo["tipoInstrumento"]:
                    cotizacionActuales.append(cotizacion)

        if len(cotizacionActuales)>0:
            cnn_cloud.execute(mercado.delete())
            cnn_cloud.execute(mercado.insert().values(cotizacionActuales))





        ############### dolares
        dolar = Dolar()

        cotizacion_dolares=dolar.obtengo_cotizaciones()

        cnn_cloud.execute(tipoDolares.delete())
        cnn_cloud.execute(tipoDolares.insert().values(cotizacion_dolares))
        cnn_cloud.commit()


        print("Ejecuccion OK")

    except Exception as e:
        cnn_cloud.rollback()
        error = "Error: "+str(e)
        print(f"Error {datetime.now()}: {error}")
    finally:
        cnn_cloud.close()
        print(f"Finishing script at {datetime.now()}")






if __name__=="__main__":
    from datetime import datetime
    print(f"Running script at {datetime.now()}")
    main()   


