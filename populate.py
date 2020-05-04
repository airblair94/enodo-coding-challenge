from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Property, Base
from datetime import datetime
import csv

engine = create_engine('sqlite:///enodo-collection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

def get_date(datestr):
  if (datestr.replace(' ', '') != ''):
    return datetime.strptime(datestr, '%m/%d/%Y')
  else:
    return None

with open('Enodo_Skills_Assessment_Data_File.csv', 'r') as f:
  reader = csv.reader(f)
  next(reader)
  for row in reader:
    new_property = Property(full_address=row[0], longitude=row[1], latitude=row[2], zip=row[3], rec_type=row[4], pin=row[5], ovacls=row[6], class_description=row[7], current_land=row[8], current_building=row[9], current_total=row[10], estimated_market_value=row[11], prior_land=row[12], prior_building=row[13], prior_total=row[14], pprior_land=row[15], pprior_building=row[16], pprior_total=row[17], pprior_year=row[18], town=row[19], volume=row[20], loc=row[21], tax_code=row[22], neighborhood=row[23], house_number=row[24], dir=row[25], street=row[26], suffix=row[27], apt=row[28], city=row[29], res_type=row[30], bldg_type=row[31], apt_desc=row[32], comm_units=row[33], ext_desc=row[34], full_bath=row[35], half_bath=row[36], bsmt_desc=row[37], attic_desc=row[38], ac=row[39], fireplace=row[40], garage_desc=row[41], age=row[42], building_sq_ft=row[43], land_sq_ft=row[44], bldg_sf=row[45], units_tot=row[46], multi_sale=row[47] == '1', deed_type=row[48], sale_date=get_date(row[49]), sale_amount=row[50], appcnt=row[51] == '1', appeal_a=row[52], appeal_a_status=row[53], appeal_a_result=row[54], appeal_a_reason=row[55], appeal_a_pin_result=row[56], appeal_a_propav=row[57], appeal_a_currav=row[58], appeal_a_resltdate=get_date(row[59]))
    session.add(new_property)

session.commit()