
import sqlite3

from database.CitiesDBQueries import CitiesDBQueries
from database.CountryDBQueries import CountryDBQueries
from database.DistrictDBQueries import DistrictDBQueries
from database.PopulationDBQueries import PopulationDBQueries

if __name__ == "__main__":
    db=PopulationDBQueries()
    db.create_population_table()




    db.close_connection()