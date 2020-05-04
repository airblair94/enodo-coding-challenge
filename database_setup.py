import sys

#for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table, Date, Boolean

#for configurations and class code
from sqlalchemy.ext.declarative import declarative_base

#for determining order status
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

#for configuration
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from datetime import datetime

from sqlalchemy.inspection import inspect

import json

#create declarative_base instance
Base = declarative_base()

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)

class Property(Base):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    full_address = Column(String(250), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    zip = Column(Integer)
    rec_type = Column(String(250))
    pin = Column(Integer)
    ovacls = Column(Integer)
    class_description = Column(String(250))
    current_land = Column(Integer)
    current_building = Column(Integer)
    current_total = Column(Integer)
    estimated_market_value = Column(Integer)
    prior_land = Column(Integer)
    prior_building = Column(Integer)
    prior_total = Column(Integer)
    pprior_land = Column(Integer)
    pprior_building = Column(Integer)
    pprior_total = Column(Integer)
    pprior_year = Column(Integer)
    town = Column(Integer)
    volume = Column(Integer)
    loc = Column(String(250))
    tax_code = Column(Integer)
    neighborhood = Column(Integer)
    house_number = Column(Integer)
    dir = Column(String(250))
    street = Column(String(250))
    suffix = Column(String(250))
    apt = Column(String(250))
    city = Column(String(250))
    res_type = Column(String(250))
    bldg_type = Column(String(250))
    apt_desc = Column(Integer)
    comm_units = Column(Integer)
    ext_desc = Column(Integer)
    full_bath = Column(Integer)
    half_bath = Column(Integer)
    bsmt_desc = Column(String(250))
    attic_desc = Column(String(250))
    ac = Column(Integer)
    fireplace = Column(Integer)
    garage_desc = Column(String(250))
    age = Column(Integer)
    building_sq_ft = Column(Integer)
    land_sq_ft = Column(Integer)
    bldg_sf = Column(Integer)
    units_tot = Column(Integer)
    multi_sale = Column(Boolean)
    deed_type = Column(Integer)
    sale_date = Column(Date)
    sale_amount = Column(Integer)
    appcnt = Column(Boolean)
    appeal_a = Column(Integer)
    appeal_a_status = Column(String(250))
    appeal_a_result = Column(String(250))
    appeal_a_reason = Column(Integer)
    appeal_a_pin_result = Column(String(250))
    appeal_a_propav = Column(Integer)
    appeal_a_currav = Column(Integer)
    appeal_a_resltdate = Column(Date)

    def __init__(self, full_address, longitude, latitude, zip, rec_type, pin, ovacls, class_description, current_land, current_building, current_total, estimated_market_value, prior_land, prior_building, prior_total, pprior_land, pprior_building, pprior_total, pprior_year, town, volume, loc, tax_code, neighborhood, house_number, dir, street, suffix, apt, city, res_type, bldg_type, apt_desc, comm_units, ext_desc, full_bath, half_bath, bsmt_desc, attic_desc, ac, fireplace, garage_desc, age, building_sq_ft, land_sq_ft, bldg_sf, units_tot, multi_sale, deed_type, sale_date, sale_amount, appcnt, appeal_a, appeal_a_status, appeal_a_result, appeal_a_reason, appeal_a_pin_result, appeal_a_propav, appeal_a_currav, appeal_a_resltdate):
      self.full_address = full_address
      self.longitude = longitude
      self.latitude = latitude
      self.zip = zip
      self.rec_type = rec_type
      self.pin = pin
      self.ovacls = ovacls
      self.class_description = class_description
      self.current_land = current_land
      self.current_building = current_building
      self.current_total = current_total
      self.estimated_market_value = estimated_market_value
      self.prior_land = prior_land
      self.prior_building = prior_building
      self.prior_total = prior_total
      self.pprior_land = pprior_land
      self.pprior_building = pprior_building
      self.pprior_total = pprior_total
      self.pprior_year = pprior_year
      self.town = town
      self.volume = volume
      self.loc = loc
      self.tax_code = tax_code
      self.neighborhood = neighborhood
      self.house_number = house_number
      self.dir = dir
      self.street = street
      self.suffix = suffix
      self.apt = apt
      self.city = city
      self.res_type = res_type
      self.bldg_type = bldg_type
      self.apt_desc = apt_desc
      self.comm_units = comm_units
      self.ext_desc = ext_desc
      self.full_bath = full_bath
      self.half_bath = half_bath
      self.bsmt_desc = bsmt_desc
      self.attic_desc = attic_desc
      self.ac = ac
      self.fireplace = fireplace
      self.garage_desc = garage_desc
      self.age = age
      self.building_sq_ft = building_sq_ft
      self.land_sq_ft = land_sq_ft
      self.bldg_sf = bldg_sf
      self.units_tot = units_tot
      self.multi_sale = multi_sale
      self.deed_type = deed_type
      self.sale_date = sale_date
      self.sale_amount = sale_amount
      self.appcnt = appcnt
      self.appeal_a = appeal_a
      self.appeal_a_status = appeal_a_status
      self.appeal_a_result = appeal_a_result
      self.appeal_a_reason = appeal_a_reason
      self.appeal_a_pin_result = appeal_a_pin_result
      self.appeal_a_propav = appeal_a_propav
      self.appeal_a_currav = appeal_a_currav
      self.appeal_a_resltdate = appeal_a_resltdate

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

engine = create_engine('sqlite:///enodo-collection.db')

Base.metadata.create_all(engine)



