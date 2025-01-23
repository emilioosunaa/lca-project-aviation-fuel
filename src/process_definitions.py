import bw2data as bd  # for everything related to the database
import bw2calc as bc  # for the actual LCA calculations
import bw2analyzer as bwa

# Lists all projects and then sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

# Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")

project_af = bd.Database('project_af')
data = {}  # we start with no data, so data is empty
project_af.write(data)
bd.Database('project_af').metadata['depends'] = ['ecoinvent-3.10-biosphere',
                                                 'ecoinvent-3.10-cutoff',
                                                 'ei310_IMAGE_SSP2_RCP26_2035',
                                                 'ei310_IMAGE_SSP2_RCP26_2050']

# Check if processes already exist, if they exist delete
process_name = ['syngas production scenarios', 'syngas production fossil', 'syngas production bio',
                'syngas production CO2', 'h2 production, fischer tropsch conversion',
                'hydrocarbon production, fischer tropsch conversion',
                'h2o production, hydrockracking and destillation',
                'naphta production, hydrockracking and destillation',
                'c1c4 production, hydrockracking and destillation',
                'jet fuel production, hydrockracking and destillation',
                'heat production, combined heat and power production',
                'electricity production, combined heat and power production',
                'syngas production bio, miscanthus',
                'jet fuel production, all processes',
                'direct air capture facility production',
                'cell production',]


# in case the process already exists, delets it to avoid errors
def delet_exprocesses():
    for i in process_name:
        print(i)
        try:
            bd.get_activity(('project_af', i)).delete()
            print('deleted preexisting process')
        except:
            pass


delet_exprocesses()

#------------- DCA production ----------------
input_DAC_concrete = eidb.get(name="market for concrete, normal strength", location="CH")
input_DAC_chromsteel = eidb.get(name="steel production, chromium steel 18/8, hot rolled", location="RER")
input_DAC_alu = eidb.get(name="aluminium production, primary, ingot", location="IAI Area, EU27 & EFTA")
input_DAC_steel = eidb.get(name="market for steel, low-alloyed", location="GLO")
# In the paper the use version 3.5 of ecoinvent, in this version the process is not available. 
# But, the contribution to this was added to the wire drawing process
# input_DAC_copper = eidb.get(name="copper production, primary", location="RER")
input_DAC_wire = eidb.get(name="wire drawing, copper", location="RER")
input_DAC_gravel = eidb.get(name="market for gravel, crushed", location="CH")
input_DAC_sand = [act for act in eidb if 'gravel and sand quarry operation' in act["name"] and "CH" in act["location"]][0] 
input_DAC_sand = eidb.get(name="market for gravel, crushed", location="CH")
input_DAC_stonewool = eidb.get(name="stone wool production", location="CH")
input_DAC_ethylenglyocol = eidb.get(name="market for ethylene glycol", location="RER")
input_DAC_silicone = eidb.get(name="silicone product production", location="RER")
input_DAC_waste = eidb.get(name="market for inert waste, for final disposal", location="CH")
input_DAC_transportlorry = eidb.get(name="transport, freight, lorry 16-32 metric ton, EURO5", location="RER")
input_DAC_transporttrain = eidb.get(name="transport, freight train, electricity", location="Europe without Switzerland")

process_DAC = project_af.new_activity(
    code="direct air capture facility production",
    name="direct air capture facility production",
    unit='unit',
)

# Technosphere
process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_concrete["name"],
    unit=input_DAC_concrete["unit"],
    amount=34.6666667,  #m3/ unit
    input=input_DAC_concrete,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_chromsteel["name"],
    unit=input_DAC_chromsteel["unit"],
    amount=36300,  # kg/ unit
    input=input_DAC_chromsteel,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_alu["name"],
    unit=input_DAC_alu["unit"],
    amount=262000,  # kg/ unit
    input=input_DAC_alu,
).save()
process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_steel["name"],
    unit=input_DAC_steel["unit"],
    amount=303000,  # kg/ unit
    input=input_DAC_steel,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_wire["name"],
    unit=input_DAC_wire["unit"],
    amount=3400,  # kg/ unit
    input=input_DAC_wire,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_gravel["name"],
    unit=input_DAC_gravel["unit"],
    amount=93100,  # kg/ unit
    input=input_DAC_gravel,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_sand["name"],
    unit=input_DAC_sand["unit"],
    amount=89600,  # kg/ unit
    input=input_DAC_sand,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_stonewool["name"],
    unit=input_DAC_stonewool["unit"],
    amount=8700,  # kg/unit
    input=input_DAC_stonewool,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_ethylenglyocol["name"],
    unit=input_DAC_ethylenglyocol["unit"],
    amount=15000,  # kg/unit
    input=input_DAC_ethylenglyocol,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_silicone["name"],
    unit=input_DAC_silicone["unit"],
    amount=1100,  # kg/ unit
    input=input_DAC_silicone,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_waste["name"],
    unit=input_DAC_waste["unit"],
    amount=243400,  # kg/ unit
    input=input_DAC_waste,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_transportlorry["name"],
    unit=input_DAC_transportlorry["unit"],
    amount=244895 / 1000,  # tkm/ unit
    input=input_DAC_transportlorry,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_DAC_transporttrain["name"],
    unit=input_DAC_transporttrain["unit"],
    amount=37412 / 1000,  # tkm/ unit
    input=input_DAC_transporttrain,
).save()

# Production
process_DAC.new_exchange(
    type="production",
    name="direct air capture facility",
    unit='unit',
    amount=1,
    input=process_DAC,
).save()

process_DAC['reference product'] = 'direct air capture facility'
process_DAC.save()
#----------------------------------------------

#------------- Cell production ----------------
input_cerium_oxide = eidb.get(name="market for cerium oxide", location="GLO")
input_lanthanum_oxide = eidb.get(name="market for lanthanum oxide", location="GLO")
input_gadolinium_oxide = eidb.get(name="market for gadolinium oxide", location="GLO")
input_yttrium_oxide = eidb.get(name="market for yttrium oxide", location="GLO")
input_strontium_carbonate = eidb.get(name="market for strontium carbonate", location="GLO")
# substitute for iron(III) oxide-hydroxide:
input_iron_oxide_hydroxide = eidb.get(name="market for portafer", location="GLO")
input_nickel_mix = eidb.get(name="nickel concentrate, 16% Ni to generic market for nickel-rich materials", location="GLO") 
input_cobalt_hydroxide = eidb.get(name="market for cobalt hydroxide", location="GLO")
input_zirconium_oxide = eidb.get(name="market for zirconium oxide", location="GLO")
input_manganese_dioxide = [act for act in eidb if 'manganese dioxide production' in act["name"] and "GLO" in act["location"]][0] 
input_copper_oxide = eidb.get(name="copper oxide production", location="RER")
# substitute for nitric acid 98%:
input_nitric_acid = [act for act in eidb if "nitric acid production, product in 50% solution state" in act["name"] and "RER w/o RU" in act["location"]][0]
input_mek = eidb.get(name="methyl ethyl ketone production", location="RER")
input_cmc = eidb.get(name="carboxymethyl cellulose production, powder", location="RER")
input_ethanol = eidb.get(name="market for ethanol, without water, in 99.7% solution state, from ethylene", location="RER")
input_benzyl_alcohol = eidb.get(name="benzyl alcohol production", location="RER")
# Transports
input_sea_transport = eidb.get(name="transport, freight, sea, container ship", location="GLO")
input_lorry_transport = eidb.get(name="transport, freight, lorry 16-32 metric ton, EURO5", location="RER")
input_train_transport = eidb.get(name="transport, freight train", location="DE")
# Electricity
input_electricity = eidb.get(name="market for electricity, low voltage", location="DE")
# Waste treatment
input_inert_waste_treatment = eidb.get(name="treatment of inert waste, inert material landfill", location="CH")
output_nitrogen_oxides = bsdb.get(name="Nitrogen oxides", categories=("air",))
output_nmvoc = bsdb.get(name="NMVOC, non-methane volatile organic compounds", categories=("air",))

process_cell = project_af.new_activity(
    code="cell production",
    name="cell production",
    unit='unit',
)

# Technosphere
process_cell.new_exchange(
    type="technosphere",
    name=input_cerium_oxide["name"],
    unit=input_cerium_oxide["unit"],
    amount=0.000201, # kg/unit
    input=input_cerium_oxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_lanthanum_oxide["name"],
    unit=input_lanthanum_oxide["unit"],
    amount=0.00198, # kg/unit
    input=input_lanthanum_oxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_gadolinium_oxide["name"],
    unit=input_gadolinium_oxide["unit"],
    amount=0.000053, # kg/unit
    input=input_gadolinium_oxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_yttrium_oxide["name"],
    unit=input_yttrium_oxide["unit"],
    amount=0.00242, # kg/unit
    input=input_yttrium_oxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_strontium_carbonate["name"],
    unit=input_strontium_carbonate["unit"],
    amount=0.000324, # kg/unit
    input=input_strontium_carbonate,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_iron_oxide_hydroxide["name"],
    unit=input_iron_oxide_hydroxide["unit"],
    amount=0.000389, # kg/unit
    input=input_iron_oxide_hydroxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_nickel_mix["name"],
    unit=input_nickel_mix["unit"],
    amount=0.0179, # kg/unit
    input=input_nickel_mix,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_cobalt_hydroxide["name"],
    unit=input_cobalt_hydroxide["unit"],
    amount=0.000394, # kg/unit
    input=input_cobalt_hydroxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_zirconium_oxide["name"],
    unit=input_zirconium_oxide["unit"],
    amount=0.0149, # kg/unit
    input=input_zirconium_oxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_manganese_dioxide["name"],
    unit=input_manganese_dioxide["unit"],
    amount=0.000351, # kg/unit
    input=input_manganese_dioxide,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_copper_oxide["name"],
    unit=input_copper_oxide["unit"],
    amount=0.000143, # kg/unit
    input=input_copper_oxide,
).save()

# Transports
process_cell.new_exchange(
    type="technosphere",
    name=input_sea_transport["name"],
    unit=input_sea_transport["unit"],
    amount=0.401,   # tkm/unit
    input=input_sea_transport,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_lorry_transport["name"],
    unit=input_lorry_transport["unit"],
    amount=6.9e-03, # tkm/unit
    input=input_lorry_transport,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_train_transport["name"],
    unit=input_train_transport["unit"],
    amount=0.014,   # tkm/unit
    input=input_train_transport,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_electricity["name"],
    unit=input_electricity["unit"],
    amount=0.12,    # kWh/unit
    input=input_electricity,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_inert_waste_treatment["name"],
    unit=input_inert_waste_treatment["unit"],
    amount=0.0386,  # kg/unit
    input=input_inert_waste_treatment,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_nitric_acid["name"],
    unit=input_nitric_acid["unit"],
    amount=0.00873,  # kg/unit
    input=input_nitric_acid,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_mek["name"],
    unit=input_mek["unit"],
    amount=0.00762,  # kg/unit
    input=input_mek,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_cmc["name"],
    unit=input_cmc["unit"],
    amount=0.00301,  # kg/unit
    input=input_cmc,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_ethanol["name"],
    unit=input_ethanol["unit"],
    amount=0.00762,  # kg/unit
    input=input_ethanol,
).save()

process_cell.new_exchange(
    type="technosphere",
    name=input_benzyl_alcohol["name"],
    unit=input_benzyl_alcohol["unit"],
    amount=0.00301,  # kg/unit
    input=input_benzyl_alcohol,
).save()

# Biosphere
process_cell.new_exchange(
    type="biosphere",
    name=output_nitrogen_oxides["name"],
    amount=0.00032,  # kg/unit
    input=output_nitrogen_oxides,
).save()

process_cell.new_exchange(
    type="biosphere",
    name=output_nmvoc["name"],
    amount=0.00638,  # kg/unit
    input=output_nmvoc,
).save()

# Production
process_cell.new_exchange(
    type="production",
    name="cell",  
    unit='unit',
    amount=1,
    input=process_cell,
).save()

process_cell['reference product'] = 'cell'
process_cell.save()
# ----------------------------------------------
# -------------- Stack production --------------
# Inputs from the ecoinvent database

# Glass-Ceramic Materials
#input_glass_cermet = eidb.get(name="market for glass-ceramic", location="GLO")
    #own source (Harboe et al., 2020), category: glass-ceramic materials
    # #In order to analyse whether we can implement this in the paper, a manual implementation is needed. # To-Do
# Metals
input_cast_iron = eidb.get(name="cast iron production", location="RER")
input_chromium = eidb.get(name="chromium production", location="RER")
input_titanium = eidb.get(name="market for titanium", location="GLO")
input_manganese = eidb.get(name="manganese production", location="RER")
input_cobalt = [act for act in eidb if act["name"] == "cobalt production" and act["location"] == "GLO" and act.get("reference product") == "cobalt"][0]  # from cell production
input_chromium_steel = eidb.get(name="sheet rolling, chromium steel", location="RER")

# Energy
input_natural_gas_heat = eidb.get(name="heat production, natural gas, at industrial furnace low-NOx >100kW", location="Europe without Switzerland")

# Building Construction
input_building_hall = eidb.get(name="building construction, hall, steel construction", location="CH")
input_building_multistorey = eidb.get(name="building construction, multi-storey", location="RER")

# Land Use
input_industrial_area = bsdb.get(name="Occupation, industrial area")
input_area_transformation_from = bsdb.get(name="Transformation, from unspecified")
input_area_transformation_to = bsdb.get(name="Transformation, to industrial area")

process_stack = project_af.new_activity(
    code="stack production",
    name="HT-co-electrolysis stack production",
    unit='unit',
)

# Technosphere Inputs
process_stack.new_exchange(
    type="technosphere",
    name=input_cast_iron["name"],
    unit=input_cast_iron["unit"],
    amount=414,  # kg
    input=input_cast_iron,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_chromium["name"],
    unit=input_chromium["unit"],
    amount=117,  # kg
    input=input_chromium,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_titanium["name"],
    unit=input_titanium["unit"],
    amount=0.374,  # kg
    input=input_titanium,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_manganese["name"],
    unit=input_manganese["unit"],
    amount=2.84,  # kg
    input=input_manganese,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_nickel_mix["name"],
    unit=input_nickel_mix["unit"],
    amount=19.8,  # kg
    input=input_nickel_mix,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_lanthanum_oxide["name"],
    unit=input_lanthanum_oxide["unit"],
    amount=0.483,  # kg
    input=input_lanthanum_oxide,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_cobalt["name"],
    unit=input_cobalt["unit"],
    amount=1.5,  # kg
    input=input_cobalt,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_chromium_steel["name"],
    unit=input_chromium_steel["unit"],
    amount=534,  # kg
    input=input_chromium_steel,
).save()

# Transportation
process_stack.new_exchange(
    type="technosphere",
    name=input_sea_transport["name"],
    unit=input_sea_transport["unit"],
    amount=9.89,  # tkm
    input=input_sea_transport,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_lorry_transport["name"],
    unit=input_lorry_transport["unit"],
    amount=55.6,  # tkm
    input=input_lorry_transport,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_train_transport["name"],
    unit=input_train_transport["unit"],
    amount=111,  # tkm
    input=input_train_transport,
).save()

# Energy Inputs
process_stack.new_exchange(
    type="technosphere",
    name=input_electricity["name"],
    unit=input_electricity["unit"],
    amount=3611.5,  # kWh
    input=input_electricity,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_natural_gas_heat["name"],
    unit=input_natural_gas_heat["unit"],
    amount=606,  # kWh
    input=input_natural_gas_heat,
).save()

# Building Construction and Area Transformation
process_stack.new_exchange(
    type="technosphere",
    name=input_building_hall["name"],
    unit=input_building_hall["unit"],
    amount=0.029,  # m2
    input=input_building_hall,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_building_multistorey["name"],
    unit=input_building_multistorey["unit"],
    amount=0.175,  # m3
    input=input_building_multistorey,
).save()

process_stack.new_exchange(
    type="biosphere",
    name=input_industrial_area["name"],
    unit=input_industrial_area["unit"],
    amount=5.26,  # m2*year
    input=input_industrial_area,
).save()

process_stack.new_exchange(
    type="biosphere",
    name=input_area_transformation_from["name"],
    unit=input_area_transformation_from["unit"],
    amount=0.105,  # m2
    input=input_area_transformation_from,
).save()

process_stack.new_exchange(
    type="biosphere",
    name=input_area_transformation_to["name"],
    unit=input_area_transformation_to["unit"],
    amount=0.105,  # m2
    input=input_area_transformation_to,
).save()

# Output: HT-co-electrolysis stack
process_stack.new_exchange(
    type="production",
    name="HT-co-electrolysis stack 150 kW",
    unit='unit',
    amount=1,  # Single unit
    input=process_stack,
).save()

# Finalize process
process_stack['reference product'] = 'HT-co-electrolysis stack 150 kW'
process_stack.save()
# ----------------------------------------------

# ---------- Balance-of-Plant production ------- # To-Do
# ----------------------------------------------

# inputs
input_co = eidb.get(name="market for carbon monoxide", location="RER", unit="kilogram")
input_h2 = eidb.get(name="hydrogen production, steam methane reforming", location="RER", unit="kilogram")
input_water = eidb.get(name="market for tap water", location="Europe without Switzerland")
input_oxygen = eidb.get(name="market for oxygen, liquid", location="RER")
input_miscanthus = eidb.get(name="market for miscanthus, chopped", location="GLO")
input_electrictity = eidb.get(name="market for electricity, medium voltage", location="DE")
input_heat_CO2 = eidb.get(name="market for heat, district or industrial, natural gas", location="CH")

input_resin = eidb.get(name="market for anionic resin", location="RER")
input_water_deionized = eidb.get(name="market for water, deionised", location="Europe without Switzerland")
input_DAC = project_af.get(name="direct air capture facility production")
emission_o2 = bsdb.get(name="Oxygen", categories=("air",))

# factors
molmass_h20 = 18.01528  #g/mol
molmass_h2 = 2.016  #g/mol
norm_m3_h2 = 0.08988 * 1000  #g http://www.leonland.de/elements_by_price/de/conversion
roh_biogas = 1.3  #kg/m3 https://www.umweltbundesamt.de/sites/default/files/medien/pdfs/biogas_stoerfallv_1_2_erlaeuterungen.pdf

# ------------ Scenarios - Syngas ----------------
# --------- Fossil syngas production ------------
process_syngas_fossil = project_af.new_activity(
    code="syngas production fossil",
    name="syngas production fossil",
    unit='kilogramm',
)

# Technosphere
process_syngas_fossil.new_exchange(
    type="technosphere",
    name=input_co["name"],
    unit=input_co["unit"],
    amount=0.95775295,  #kg/ kg(syngas)
    input=input_co,
).save()

# Technosphere
process_syngas_fossil.new_exchange(
    type="technosphere",
    name=input_h2["name"],
    unit=input_h2["unit"],
    amount=0.00045589,  # kg/kg(syngas)
    input=input_h2,
).save()

# Production
process_syngas_fossil.new_exchange(
    type="production",
    name="syngas fossil",
    unit='kilogramm',
    amount=1,
    input=process_syngas_fossil,
).save()

process_syngas_fossil['reference product'] = 'syngas fossil'
process_syngas_fossil.save()

# --------- Bio syngas production ------------
process_syngas_bio = project_af.new_activity(
    code="syngas production bio, miscanthus",
    name="syngas production bio, miscanthus",
    unit='kilogramm',
)

# Biosphere
process_syngas_bio.new_exchange(
    type="biosphere",
    name=input_oxygen["name"],
    unit=input_oxygen["unit"],
    amount=0.84,  #kg/ kg(syngas)
    input=input_oxygen,
).save()

# Technosphere
process_syngas_bio.new_exchange(
    type="technosphere",
    name=input_miscanthus["name"],
    unit=input_miscanthus["unit"],
    amount=1.95,  #kg/ kg(syngas)
    input=input_miscanthus,
).save()

process_syngas_bio.new_exchange(
    type="technosphere",
    name=input_water["name"],
    unit=input_water["unit"],
    amount=1.23,  #kg/ kg(syngas)
    input=input_water,
).save()

process_syngas_bio.new_exchange(
    type="technosphere",
    name=input_electrictity["name"],
    unit=input_electrictity["unit"],
    amount=0.2055556,  #kWh/ kg(syngas)
    input=input_electrictity,
).save()

# Production
process_syngas_bio.new_exchange(
    type="production",
    name="syngas bio",
    unit='kilogramm',
    amount=1,  # kg/ kg(syngas)
    input=process_syngas_bio,
).save()

process_syngas_bio['reference product'] = 'syngas bio'
process_syngas_bio.save()


# --------- CO2 syngas production ------------
process_syngas_CO2 = project_af.new_activity(
    code="syngas production CO2",
    name="syngas production CO2",
    unit='kilogramm',
)

# Technosphere
process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_resin["name"],
    unit=input_resin["unit"],
    amount=3.75E-3,  # kg/kgCO2
    input=input_resin,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_electrictity["name"],
    unit=input_electrictity["unit"],
    amount=0.5,  # kWh/kgCO2
    input=input_electrictity,
).save()

# To-Do: heat
process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_heat_CO2["name"],
    unit=input_heat_CO2["unit"],
    amount=1.5,  # kWh/kgCO2
    input=input_heat_CO2,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_DAC["name"],
    unit=input_DAC["unit"],
    amount=9.3E-8,  # kWh/kgCO2
    input=input_DAC,
).save()

# BoP

# Cells

# Stack

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_water_deionized["name"],
    unit=input_water_deionized["unit"],
    amount=1.13,  # kg/ kg(Syngas)
    input=input_water_deionized,
).save()

process_syngas_CO2.new_exchange(type="technosphere",
    name=input_electrictity["name"],
    unit=input_electrictity["unit"],
    amount=8.82,  # kWh/ kg(syngas)
    input=input_electrictity,
).save()

# Biosphere
process_syngas_CO2.new_exchange(type='biosphere',
    name=emission_o2['name'],
    unit=emission_o2['unit'],
    amount=1.15,  # kg/kg(syngas)
    input=emission_o2,
    ).save()

# Production
process_syngas_CO2.new_exchange(
    type="production",
    name="syngas CO2",
    unit='kilogram',
    amount=1,  # kg/ kg(syngas)
    input=process_syngas_CO2,
).save()

process_syngas_CO2['reference product'] = 'syngas CO2'
process_syngas_CO2.save()

syngas_fossil = project_af.get(name="syngas production fossil")
syngas_bio_1 = eidb.get(name="synthetic gas production, from wood, at fixed bed gasifier", location="RoW")
syngas_bio_2 = eidb.get(name="synthetic gas production, from wood, at fluidized bed gasifier", location="RoW")
syngas_bio_3 = project_af.get(name="syngas production bio, miscanthus")
syngas_CO2 = project_af.get(name="syngas production CO2")

process_syngas_scenarios = project_af.new_activity(
    code="syngas production scenarios",
    name="syngas production scenarios",
    unit='kilogramm',
)

# Define a named parameter for energy input
process_syngas_scenarios["parameters"] = {
    "status_fossil_1": int(input("Enter a number between 0 and 1 for status fossil: ")),
    "status_bio_1": int(input("Enter a number between 0 and 1 for status bio 1: ")),
    "status_bio_2": int(input("Enter a number between 0 and 1 for status bio 2: ")),
    "status_bio_3": int(input("Enter a number between 0 and 1 for status bio 3: ")),
    "status_CO2": int(input("Enter a number between 0 and 1 for status CO2: "))
}

status_fossil_1 = process_syngas_scenarios["parameters"]["status_fossil_1"]
status_bio_1 = process_syngas_scenarios["parameters"]["status_bio_1"]
status_bio_2 = process_syngas_scenarios["parameters"]["status_bio_2"]
status_bio_3 = process_syngas_scenarios["parameters"]["status_bio_3"]
status_CO2 = process_syngas_scenarios["parameters"]["status_CO2"]

# Technosphere
process_syngas_scenarios.new_exchange(
    type="technosphere",
    name="syngas production fossil",
    unit=syngas_fossil["unit"],
    amount=12.038517 * status_fossil_1,  # kg/L(Fuel)
    input=syngas_fossil,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name=syngas_bio_1["name"],
    unit=syngas_bio_1["unit"],
    amount=12.038517 * status_bio_1,  # kg/L(Fuel)
    input=syngas_bio_1,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name=syngas_bio_2["name"],
    unit=syngas_bio_2["unit"],
    amount=12.038517 * status_bio_2,  # kg/L(Fuel)
    input=syngas_bio_2,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name="syngas production bio",
    unit=syngas_bio_3["unit"],
    amount=12.038517 * status_bio_3,  # kg/L(Fuel)
    input=syngas_bio_3,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name="syngas production CO2",
    unit=syngas_CO2["unit"],
    amount=12.038517 * status_CO2,  # kg/L(Fuel)
    input=syngas_CO2,
).save()

# Production
process_syngas_scenarios.new_exchange(
    type="production",
    name="syngas",
    unit="kilogramm",
    amount=1,
    input=process_syngas_scenarios,
).save()

process_syngas_scenarios['reference product'] = 'syngas'
process_syngas_scenarios.save()

#  ------------- Combined Heat and Power Unit ----------------
gas_ext = eidb.get(name="market for natural gas, high pressure", location="DE")

process_CHPU_heat = project_af.new_activity(
    code="heat production, combined heat and power production",
    name="heat production, combined heat and power production",
    unit="kilowatt hour",
)

# Technosphere
process_CHPU_heat.new_exchange(
    type="technosphere",
    name=gas_ext["name"],
    unit=gas_ext["unit"],
    amount=0.0695122,  # m3/ L(Fuel)
    input=gas_ext,
).save()

# Production
process_CHPU_heat.new_exchange(
    type="production",
    name="heat CHP",
    unit="kilowatt hour",
    amount=0.527777778,  # kWh/ L (Fuel)
    input=process_CHPU_heat,
).save()

process_CHPU_heat['reference product'] = 'heat CHP'
process_CHPU_heat.save()

process_CHPU_elect = project_af.new_activity(
    code="electricity production, combined heat and power production",
    name="electricity production, combined heat and power production",
    unit='kilowatt hour',
)

# Technosphere
process_CHPU_elect.new_exchange(
    type="technosphere",
    name=gas_ext["name"],
    unit=gas_ext["unit"],
    amount=0.09166667,  # m3/ L(Fuel)
    input=gas_ext,
).save()

# Production
process_CHPU_elect.new_exchange(
    type="production",
    name="electricity CHP",
    unit='kilowatt hour',
    amount=0.61111111, # kWh/ L (Fuel)
    input=process_CHPU_elect,
).save()
process_CHPU_elect['reference product'] = 'electricity CHP'
process_CHPU_elect.save()

# ----------------- Fischer Tropsch Conversion -----------------
electricity_int = project_af.get(name="electricity production, combined heat and power production")
syngas_int = project_af.get(name="syngas production scenarios")
input_FT_chemicals = eidb.get(name="market for chemical, inorganic", location="GLO")
input_FT_factory = eidb.get(name="market for petroleum refinery", location="GLO")
input_FT_land = bsdb.get(name="Occupation, industrial area")
input_FT_landtransffrom = bsdb.get(name="Transformation, from unspecified")
input_FT_landtransfto = bsdb.get(name="Transformation, to industrial area")
output_FT_waste = eidb.get(name="market for inert waste, for final disposal", location="RoW") # check

process_FT_h2 = project_af.new_activity(
    code="h2 production, fischer tropsch conversion",
    name="h2 production, fischer tropsch conversion",
    unit='kilogramm',
)

# Auxillary materials
process_FT_h2.new_exchange(
    type="technosphere",
    name=input_FT_chemicals["name"],
    unit=input_FT_chemicals["unit"],
    amount=0.07706479,  # kg/ L(Fuel)
    input=input_FT_chemicals,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name=input_FT_factory["name"],
    unit=input_FT_factory["unit"],
    amount=1.56E-10,  # unit/ L (Fuel)
    input=input_FT_factory,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_FT_land["name"],
    unit=input_FT_land["unit"],
    amount=0.00154229,  # m2-year/ L (Fuel)
    input=input_FT_land,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_FT_landtransffrom["name"],
    unit=input_FT_landtransffrom["unit"],
    amount=1.74E-5,  # m2/ L (Fuel)
    input=input_FT_landtransffrom,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_FT_landtransfto["name"],
    unit=input_FT_landtransfto["unit"],
    amount=1.74E-5,  # m2/ L (Fuel)
    input=input_FT_landtransfto,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=output_FT_waste["name"],
    unit=output_FT_waste["unit"],
    amount=-2.88E-3,  # m2/ L (Fuel)
    input=output_FT_waste,
).save()

# Technosphere
process_FT_h2.new_exchange(
    type="technosphere",
    name=input_electrictity["name"],
    unit=input_electrictity["unit"],
    amount=0.02150107,  # kWh/ L (Fuel)
    input=input_electrictity,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name="electricity production, combined heat and power production",
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=electricity_int,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name="syngas production scenarios",
    unit=syngas_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=syngas_int,
).save()

# Production
process_FT_h2.new_exchange(
    type="production",
    name="H2",
    unit='kilogramm',
    amount=0.0268128, # kg/ L (Fuel)
    input=process_FT_h2,
).save()

process_FT_h2['reference product'] = 'H2'
process_FT_h2.save()

process_FT_hydrocarbon = project_af.new_activity(
    code="hydrocarbon production, fischer tropsch conversion",
    name="hydrocarbon production, fischer tropsch conversion",
    unit='kilogramm',
)
# Auxillary materials
process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name=input_FT_chemicals["name"],
    unit=input_FT_chemicals["unit"],
    amount=2.218603,  # kg/ L(Fuel)
    input=input_FT_chemicals,
).save()

process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name=input_FT_factory["name"],
    unit=input_FT_factory["unit"],
    amount=4.49E-9,  # unit/ L (Fuel)
    input=input_FT_factory,
).save()

process_FT_hydrocarbon.new_exchange(
    type="biosphere",
    name=input_FT_land["name"],
    unit=input_FT_land["unit"],
    amount=0.04428566,  # m2-year/ L (Fuel)
    input=input_FT_land,
).save()

process_FT_hydrocarbon.new_exchange(
    type="biosphere",
    name=input_FT_landtransffrom["name"],
    unit=input_FT_landtransffrom["unit"],
    amount=4.99E-4,  # m2/ L (Fuel)
    input=input_FT_landtransffrom,
).save()

process_FT_hydrocarbon.new_exchange(
    type="biosphere",
    name=input_FT_landtransfto["name"],
    unit=input_FT_landtransfto["unit"],
    amount=4.99E-4,  # m2/ L (Fuel)
    input=input_FT_landtransfto,
).save()

process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name=output_FT_waste["name"],
    unit=output_FT_waste["unit"],
    amount=-8.27E-2,  # m2/ L (Fuel)
    input=output_FT_waste,
).save()

# Technosphere
process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name=input_electrictity["name"],
    unit=input_electrictity["unit"],
    amount=0.61738782,  # kWh/ L (Fuel)
    input=input_electrictity,
).save()

process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name=electricity_int["name"],
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=electricity_int,
).save()

process_FT_hydrocarbon.new_exchange(
    type="technosphere",
    name="syngas production scenarios",
    unit=syngas_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=syngas_int,
).save()

# Production
process_FT_hydrocarbon.new_exchange(
    type="production",
    name="hydrocarbon",
    unit='kilogramm',
    amount=18.4932478,  # kg/ L (Fuel)
    input=process_FT_hydrocarbon,
).save()

process_FT_hydrocarbon['reference product'] = 'hydrocarbon'
process_FT_hydrocarbon.save()

# --------------- Hydrockracking and Destillation ------------
heat_int = project_af.get(name="heat production, combined heat and power production")
H2_int = project_af.get(name="h2 production, fischer tropsch conversion")
hydrocarbon_int = project_af.get(name="hydrocarbon production, fischer tropsch conversion")

process_HandD_h20 = project_af.new_activity(
    code="h2o production, hydrockracking and destillation",
    name="h2o production, hydrockracking and destillation",
    unit='liter',
)

# Technosphere
process_HandD_h20.new_exchange(
    type="technosphere",
    name="electricity production, combined heat and power production",
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=electricity_int,
).save()

process_HandD_h20.new_exchange(
    type="technosphere",
    name="heat production, combined heat and power production",
    unit=heat_int["unit"],
    amount=0,  # KWh/ L (Fuel)
    input=heat_int,
).save()

process_HandD_h20.new_exchange(
    type="technosphere",
    name="h2 production, fischer tropsch conversion",
    unit=H2_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=H2_int,
).save()

process_HandD_h20.new_exchange(
    type="technosphere",
    name="hydrocarbon production, fischer tropsch conversion",
    unit=hydrocarbon_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=hydrocarbon_int,
).save()

# Production
process_HandD_h20.new_exchange(
    type="production",
    name="H20",
    unit='L',
    amount=2.1,  # L/ L(Fuel)
    input=process_HandD_h20,
).save()

process_HandD_h20['reference product'] = 'H20'
process_HandD_h20.save()

process_HandD_naphta = project_af.new_activity(
    code="naphta production, hydrockracking and destillation",
    name="naphta production, hydrockracking and destillation",
    unit='liter',
)

# Technosphere
process_HandD_naphta.new_exchange(
    type="technosphere",
    name="electricity production, combined heat and power production",
    unit=electricity_int["unit"],
    amount=0, # kWh/ L(Fuel)
    input=electricity_int,
).save()

process_HandD_naphta.new_exchange(
    type="technosphere",
    name="heat production, combined heat and power production",
    unit=heat_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=heat_int,
).save()

process_HandD_naphta.new_exchange(
    type="technosphere",
    name="h2 production, fischer tropsch conversion",
    unit=H2_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=H2_int,
).save()

process_HandD_naphta.new_exchange(
    type="technosphere",
    name="hydrocarbon production, fischer tropsch conversion",
    unit=hydrocarbon_int["unit"],
    amount=0,  # kg/ L(Fuel)
    input=hydrocarbon_int,
).save()

process_HandD_naphta.new_exchange(
    type="production",
    name="naphta",
    unit='L',
    amount=0.87,  # L/L (Fuel)
    input=process_HandD_naphta,
).save()

process_HandD_naphta['reference product'] = 'naphta'
process_HandD_naphta.save()

process_HandD_c1c4 = project_af.new_activity(
    code="c1c4 production, hydrockracking and destillation",
    name="c1c4 production, hydrockracking and destillation",
    unit='kilogramm',
)

# Technosphere
process_HandD_c1c4.new_exchange(
    type="technosphere",
    name="electricity production, combined heat and power production",
    unit=electricity_int["unit"],
    amount=0, # kg/ L (Fuel)
    input=electricity_int,
).save()

process_HandD_c1c4.new_exchange(
    type="technosphere",
    name="heat production, combined heat and power production",
    unit=heat_int["unit"],
    amount=0, # kg/ L (fuel)
    input=heat_int,
).save()

process_HandD_c1c4.new_exchange(
    type="technosphere",
    name="h2 production, fischer tropsch conversion",
    unit=H2_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=H2_int,
).save()

process_HandD_c1c4.new_exchange(
    type="technosphere",
    name="hydrocarbon production, fischer tropsch conversion",
    unit=hydrocarbon_int["unit"],
    amount=0,  # kg/ l (Fuel)
    input=hydrocarbon_int,
).save()

process_HandD_c1c4.new_exchange(
    type="production",
    name="C1C4",
    unit='kg',
    amount=0.15, # kg/L (Fuel)
    input=process_HandD_c1c4,
).save()

process_HandD_c1c4['reference product'] = 'C1C4'
process_HandD_c1c4.save()

process_HandD_jetfuel = project_af.new_activity(
    code="jet fuel production, hydrockracking and destillation",
    name="jet fuel production, hydrockracking and destillation",
    unit='liter',
)

# Technosphere
process_HandD_jetfuel.new_exchange(
    type="technosphere",
    name="electricity production, combined heat and power production",
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L(Fuel)
    input=electricity_int,
).save()

process_HandD_jetfuel.new_exchange(
    type="technosphere",
    name="heat production, combined heat and power production",
    unit=heat_int["unit"],
    amount=0,  # kWh/ L(Fuel)
    input=heat_int,
).save()

process_HandD_jetfuel.new_exchange(
    type="technosphere",
    name="h2 production, fischer tropsch conversion",
    unit=H2_int["unit"],
    amount=0,  # kg/L (Fuel)
    input=H2_int,
).save()

process_HandD_jetfuel.new_exchange(
    type="technosphere",
    name="hydrocarbon production, fischer tropsch conversion",
    unit=hydrocarbon_int["unit"],
    amount=0,  # kg/L Fuel
    input=hydrocarbon_int,
).save()

process_HandD_jetfuel.new_exchange(
    type="production",
    name="jet fuel",
    unit='L',
    amount=1,  # L = 0,775 kg
    input=process_HandD_jetfuel,
).save()

process_HandD_jetfuel['reference product'] = 'jet fuel'
process_HandD_jetfuel.save()

# Processes
input_syngas=project_af.get(name="syngas production scenarios")

input_CHPU_elect=project_af.get(name="electricity production, combined heat and power production")
input_CHPU_heat=project_af.get(name="heat production, combined heat and power production")

input_FTC_hydrocarbon=project_af.get(name="hydrocarbon production, fischer tropsch conversion")
input_FTC_H2=project_af.get(name="h2 production, fischer tropsch conversion")

input_hydro_c1c4=project_af.get(name="c1c4 production, hydrockracking and destillation")
input_hydro_H2O=project_af.get(name="h2o production, hydrockracking and destillation")
input_Hydro_naphta=project_af.get(name="naphta production, hydrockracking and destillation")
input_hydro_jetfuel=project_af.get(name="jet fuel production, hydrockracking and destillation")

process_full = project_af.new_activity(
    code="jet fuel production, all processes",
    name="jet fuel production, all processes",
    unit='liter',
)

# Technosphere
process_full.new_exchange(
    type="technosphere",
    name=input_syngas["name"],
    unit=input_syngas["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=input_syngas,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel) 
    input=input_CHPU_elect,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_FTC_hydrocarbon["name"],
    unit=input_FTC_hydrocarbon["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_hydrocarbon,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_Hydro_naphta["name"],
    unit=input_Hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel 
    input=input_Hydro_naphta,
).save()

process_full.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L 
    input=input_hydro_jetfuel,
).save()

# Production
process_full.new_exchange(
    type="production",
    name="jet fuel, all processes",
    unit='L',
    amount=1,  # L = 0,775 kg
    input=process_full,
).save()

process_full['reference product'] = 'jet fuel, all processes'
process_full.save()