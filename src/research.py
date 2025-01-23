#imports brightway packages
import bw2data as bd  # for everything related to the database

#Sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

# -------------------------------------------
# Example: Creation of a BoP process 
# for HT-co-electrolysis stack (150 kW)
# -------------------------------------------

# 1) Retrieve required activities from ecoinvent
input_steel_prod = eidb.get(name="steel production, electric, chromium steel 18/8", location="RER")
input_sheet_rolling = eidb.get(name="sheet rolling, chromium steel", location="RER")
input_tap_water = eidb.get(name="market for tap water", location="Europe without Switzerland")
input_wastewater_treatment = eidb.get(name="treatment of wastewater, unpolluted, wastewater treatment",location="CH")
input_freight_lorry = eidb.get(name="transport, freight, lorry 16-32 metric ton, EURO5", location="RER")
input_freight_train = eidb.get(name="transport, freight train", location="DE")
input_passenger_car = eidb.get(name="transport, passenger car, large size, diesel, EURO 5", location="RER")
input_elec_lv = eidb.get(name="market for electricity, low voltage", location="DE")
input_elec_mv = eidb.get(name="market for electricity, medium voltage", location="DE")
input_heat_ng = eidb.get(name="heat production, natural gas, at industrial furnace low-NOx >100kW", location="Europe without Switzerland")
input_heat_fuel_oil = eidb.get(name="heat production, light fuel oil, at boiler 100kW condensing, non-modulating", location="CH")
input_building_hall = eidb.get(name="building construction, hall, steel construction", location="CH")
input_building_multi = eidb.get(name="building construction, multi-storey", location="RER")
input_cogen_unit = eidb.get(name="construction work, heat and power co-generation unit, 160kW electrical", location="RER")
input_inverter = eidb.get(name="inverter production, 500kW", location="RER")

# These three land-transformation/occupation activities may not match exactly in ecoinvent:
# If they do not exist in your database as typed below, 
# you might need to adapt the names or omit them.
input_transform_from = eidb.get(name="From unspecified (regionalized, DE) [Transformation]", location="DE")
input_occupation_indust_area = eidb.get(name="Industrial area (regionalized, DE) [Occupation]", location="DE")
input_transform_to = eidb.get(name="To industrial area (regionalized, DE) [Transformation]", location="DE")

# 2) Create the new activity (process) for the BoP
process_bop = project_af.new_activity(
    code="HT-Co-Electrolysis_BoP",
    name="HT-Co-Electrolysis balance-of-plant (150 kW)",
    unit="piece",
)

# 3) Add technosphere exchanges using the amounts from your table
process_bop.new_exchange(
    type="technosphere",
    name=input_steel_prod["name"],
    unit=input_steel_prod["unit"],
    amount=1875,  # kg
    input=input_steel_prod
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_sheet_rolling["name"],
    unit=input_sheet_rolling["unit"],
    amount=1875,  # kg
    input=input_sheet_rolling
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_tap_water["name"],
    unit=input_tap_water["unit"],
    amount=4086,  # kg
    input=input_tap_water
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_wastewater_treatment["name"],
    unit=input_wastewater_treatment["unit"],
    amount=4.09,  # m3
    input=input_wastewater_treatment
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_freight_lorry["name"],
    unit=input_freight_lorry["unit"],
    amount=188,  # tkm
    input=input_freight_lorry
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_freight_train["name"],
    unit=input_freight_train["unit"],
    amount=375,  # tkm
    input=input_freight_train
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_passenger_car["name"],
    unit=input_passenger_car["unit"],
    amount=3600,  # km
    input=input_passenger_car
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_elec_lv["name"],
    unit=input_elec_lv["unit"],
    amount=1440,  # kWh
    input=input_elec_lv
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_elec_mv["name"],
    unit=input_elec_mv["unit"],
    amount=7242,  # kWh
    input=input_elec_mv
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_heat_ng["name"],
    unit=input_heat_ng["unit"],
    amount=3535 * kWh_to_MJ,  # MJ
    input=input_heat_ng
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_heat_fuel_oil["name"],
    unit=input_heat_fuel_oil["unit"],
    amount=3000 * kWh_to_MJ,  # MJ
    input=input_heat_fuel_oil
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_building_hall["name"],
    unit=input_building_hall["unit"],
    amount=0.672,  # m2
    input=input_building_hall
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_building_multi["name"],
    unit=input_building_multi["unit"],
    amount=4.08,   # m3
    input=input_building_multi
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_cogen_unit["name"],
    unit=input_cogen_unit["unit"],
    amount=4.2,    # piece
    input=input_cogen_unit
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_inverter["name"],
    unit=input_inverter["unit"],
    amount=0.3,    # piece
    input=input_inverter
).save()

# Land transformation / occupation
process_bop.new_exchange(
    type="technosphere",
    name=input_transform_from["name"],
    unit=input_transform_from["unit"],
    amount=2.42,  # m2
    input=input_transform_from
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_occupation_indust_area["name"],
    unit=input_occupation_indust_area["unit"],
    amount=121,   # m2*y
    input=input_occupation_indust_area
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_transform_to["name"],
    unit=input_transform_to["unit"],
    amount=2.42,  # m2
    input=input_transform_to
).save()

# 4) Add the production exchange
process_bop.new_exchange(
    type="production",
    name="Balance-of-plant of HT-co-electrolysis stack 150 kW",
    unit="piece",
    amount=1,  # As per your table
    input=process_bop
).save()

# 5) Set reference product and save
process_bop["reference product"] = "Balance-of-plant of HT-co-electrolysis stack 150 kW"
process_bop.save()
