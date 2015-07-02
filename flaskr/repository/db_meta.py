from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
entries = Table('entries', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('text', String)
    )

statistics = Table('statistics', metadata,
    Column('name', String, primary_key=True),
    Column('count', Integer, nullable=False)
    )
