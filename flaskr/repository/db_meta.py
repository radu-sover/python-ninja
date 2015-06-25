from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
entries = Table('entries', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('text', String)
    )
