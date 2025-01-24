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
input_chromsteel = eidb.get(name="steel production, electric, chromium steel 18/8", location="RER")
input_wastewater_treatment = eidb.get(name="treatment of wastewater, unpolluted, wastewater treatment",location="CH")
input_passenger_car = eidb.get(name="transport, passenger car, large size, diesel, EURO 5", location="RER")
input_heat_fuel_oil = eidb.get(name="heat production, light fuel oil, at boiler 100kW condensing, non-modulating", location="CH")
input_cogen_unit = eidb.get(name="construction work, heat and power co-generation unit, 160kW electrical", location="RER")
input_inverter = eidb.get(name="inverter production, 500kW", location="RER")


process_bop = project_af.new_activity(
    code="HT co-electrolysis balance of plant",
    name="HT co-electrolysis balance of plant",
    unit="unit",
)

# Technosphere
process_bop.new_exchange(
    type="technosphere",
    name=input_chromsteel["name"],
    unit=input_chromsteel["unit"],
    amount=1875,  # kg
    input=input_chromsteel
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_chromsteel_sheet["name"],
    unit=input_chromsteel_sheet["unit"],
    amount=1875,  # kg
    input=input_chromsteel_sheet
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_water["name"],
    unit=input_water["unit"],
    amount=4086,  # kg
    input=input_water
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
    name=input_lorry_transport["name"],
    unit=input_lorry_transport["unit"],
    amount=188,  # tkm
    input=input_lorry_transport
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_train_transport["name"],
    unit=input_train_transport["unit"],
    amount=375,  # tkm
    input=input_train_transport
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
    name=input_electricity_low["name"],
    unit=input_electricity_low["unit"],
    amount=1440,  # kWh
    input=input_electricity_low
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=7242,  # kWh
    input=input_electricity_medium
).save()

process_bop.new_exchange(
    type="technosphere",
    name=input_natural_gas_heat["name"],
    unit=input_natural_gas_heat["unit"],
    amount=3535 * kWh_to_MJ,  # MJ
    input=input_natural_gas_heat
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
    name=input_building_multistorey["name"],
    unit=input_building_multistorey["unit"],
    amount=4.08,   # m3
    input=input_building_multistorey
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

# Biosphere
process_bop.new_exchange(
    type="biosphere",
    name=input_area_transformation_from["name"],
    unit=input_area_transformation_from["unit"],
    amount=2.42,  # m2
    input=input_area_transformation_from
).save()

process_bop.new_exchange(
    type="biosphere",
    name=input_industrial_area["name"],
    unit=input_industrial_area["unit"],
    amount=121,   # m2*y
    input=input_industrial_area
).save()

process_bop.new_exchange(
    type="biosphere",
    name=input_area_transformation_to["name"],
    unit=input_area_transformation_to["unit"],
    amount=2.42,  # m2
    input=input_area_transformation_to
).save()

# Production
process_bop.new_exchange(
    type="production",
    name=process_bop["name"],
    unit="unit",
    amount=1,
    input=process_bop
).save()

process_bop["reference product"] = "Balance-of-plant of HT-co-electrolysis stack 150 kW"
process_bop.save()
