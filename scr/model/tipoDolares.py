from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String,DateTime,FLOAT
from config.db import meta,cnn_cloud



tipoDolares = Table(
    "tipoDolares",
    meta,
    Column("Tipo",String(50)),
    Column("UltimaCotizacion", FLOAT),
    Column("FechaDescarga", DateTime)

)

meta.create_all(cnn_cloud)