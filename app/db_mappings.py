from sqlalchemy.ext.automap import automap_base
from . import extensions


Base = automap_base()

def map_existing_tables():
    Base.prepare(extensions.db.engine, reflect=True)


def TargetKeywords():
	return Base.classes.target_keywords



