from sqlalchemy import create_engine, MetaData
from config.credential import db_cloud_usr,db_cloud_pass


#Production
engine_cloud = create_engine(f'postgresql+psycopg2://{db_cloud_usr}:{db_cloud_pass}@tuffi.db.elephantsql.com/zwmcuswf')



meta = MetaData()

cnn_cloud = engine_cloud.connect()




