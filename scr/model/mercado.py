from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String,DateTime,FLOAT
from config.db import meta,cnn_cloud


mercado = Table(
    "mercado",
    meta,
    Column("ticker",String(50)),
    Column("ultimaCotizacion", FLOAT),
    Column("fecha", DateTime),
    Column("tipoInstrumento", String(50)),
    Column("fechaDescarga", DateTime)

)

meta.create_all(cnn_cloud)