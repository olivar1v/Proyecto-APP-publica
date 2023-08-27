from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String,DATE,FLOAT
from config.db import meta, engine_cloud


tenenciasCompras = Table(
    "tenenciasCompras",
    meta,
    Column("ticker", String(50)),
    Column("tipoInstrumento", String(50)),
    Column("fecha",DATE),
    Column("precio", FLOAT),
    Column("cantidad", FLOAT),
    Column("moneda", String(50)),
    Column("comision", FLOAT)
)

meta.create_all(engine_cloud)
