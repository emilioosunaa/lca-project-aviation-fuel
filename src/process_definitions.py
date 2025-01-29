import bw2data as bd

# Lists all projects and then sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database('project_af')
data = {}
project_af.write(data)
bd.Database('project_af').metadata['depends'] = ['ecoinvent-3.10-biosphere',
                                                 'ecoinvent-3.10-cutoff',
                                                 'ei310_IMAGE_SSP2_RCP26_2035',
                                                 'ei310_IMAGE_SSP2_RCP26_2050']

# Check if processes already exist, if they exist delete
process_name = ['syngas production scenarios', 'syngas production fossil',
                'syngas production fossil 2',
                'syngas production CO2', 'h2 production, fischer tropsch conversion',
                'syncrude production, fischer tropsch conversion',
                'h2o production, hydrocracking and destillation',
                'naphta production, hydrocracking and destillation',
                'c1c4 production, hydrocracking and destillation',
                'jet fuel production, hydrocracking and destillation',
                'heat production, combined heat and power production',
                'electricity production, combined heat and power production',
                'syngas production bio, miscanthus','jet fuel production, all processes', 
                'jet fuel production fossil', 'jet fuel production fossil 2', 
                'jet fuel production bio 1', 'jet fuel production bio 2',
                'jet fuel production bio 3', 'jet fuel production co2', 
                'direct air capture facility production', 'combined heat and power unit',
                'cell production', 'stack production', 'HT co-electrolysis balance of plant']


# in case the process already exists, delets it to avoid errors
def delete_exprocesses():
    for i in process_name:
        print(i)
        try:
            bd.get_activity(('project_af', i)).delete()
            print('deleted preexisting process')
        except:
            pass

delete_exprocesses()

# Inputs
input_co = eidb.get(name="market for carbon monoxide", location="RER", unit="kilogram")
input_h2 = eidb.get(name="hydrogen production, steam methane reforming", location="RER", unit="kilogram")
input_h2_coal = [act for act in eidb if 'hydrogen production, coal gasification' in act["name"] and "RoW" in act["location"]][0]
input_water = eidb.get(name="market for tap water", location="Europe without Switzerland")
input_oxygen = eidb.get(name="market for oxygen, liquid", location="RER")
input_miscanthus = eidb.get(name="market for miscanthus, chopped", location="GLO")
input_electricity_low = eidb.get(name="market for electricity, low voltage", location="DE")
input_electricity_medium = eidb.get(name="market for electricity, medium voltage", location="DE")
input_heat_CO2 = eidb.get(name="market for heat, district or industrial, natural gas", location="CH")
input_resin = eidb.get(name="market for anionic resin", location="RER")
input_water_deionized = eidb.get(name="market for water, deionised", location="Europe without Switzerland")
input_concrete = eidb.get(name="market for concrete, normal strength", location="CH")
input_chromsteel_rolled = eidb.get(name="steel production, chromium steel 18/8, hot rolled", location="RER")
input_aluminium = eidb.get(name="aluminium production, primary, ingot", location="IAI Area, EU27 & EFTA")
input_steel = eidb.get(name="market for steel, low-alloyed", location="GLO")
input_copper = eidb.get(name="wire drawing, copper", location="RER")
input_gravel = eidb.get(name="market for gravel, crushed", location="CH")
input_gravel_operation = [act for act in eidb if 'gravel and sand quarry operation' in act["name"] and "CH" in act["location"]][0] 
input_stonewool = eidb.get(name="stone wool production", location="CH")
input_ethyleneglycol = eidb.get(name="market for ethylene glycol", location="RER")
input_silicone = eidb.get(name="silicone product production", location="RER")
input_waste = eidb.get(name="market for inert waste, for final disposal", location="RoW")
input_waste_ch = eidb.get(name="market for inert waste, for final disposal", location="CH")
input_lorry_transport = eidb.get(name="transport, freight, lorry 16-32 metric ton, EURO5", location="RER")
input_transport_train_electricity = eidb.get(name="transport, freight train, electricity", location="Europe without Switzerland")
input_cerium_oxide = eidb.get(name="market for cerium oxide", location="GLO")
input_lanthanum_oxide = eidb.get(name="market for lanthanum oxide", location="GLO")
input_gadolinium_oxide = eidb.get(name="market for gadolinium oxide", location="GLO")
input_yttrium_oxide = eidb.get(name="market for yttrium oxide", location="GLO")
input_strontium_carbonate = eidb.get(name="market for strontium carbonate", location="GLO")
input_iron_oxide_hydroxide = eidb.get(name="market for portafer", location="GLO")
input_nickel_mix = eidb.get(name="nickel concentrate, 16% Ni to generic market for nickel-rich materials", location="GLO") 
input_cobalt_hydroxide = eidb.get(name="market for cobalt hydroxide", location="GLO")
input_zirconium_oxide = eidb.get(name="market for zirconium oxide", location="GLO")
input_manganese_dioxide = [act for act in eidb if 'manganese dioxide production' in act["name"] and "GLO" in act["location"]][0] 
input_copper_oxide = eidb.get(name="copper oxide production", location="RER")
input_nitric_acid = [act for act in eidb if "nitric acid production, product in 50% solution state" in act["name"] and "RER w/o RU" in act["location"]][0]
input_mek = eidb.get(name="methyl ethyl ketone production", location="RER")
input_cmc = eidb.get(name="carboxymethyl cellulose production, powder", location="RER")
input_ethanol = eidb.get(name="market for ethanol, without water, in 99.7% solution state, from ethylene", location="RER")
input_benzyl_alcohol = eidb.get(name="benzyl alcohol production", location="RER")
input_sea_transport = eidb.get(name="transport, freight, sea, container ship", location="GLO")
input_train_transport = eidb.get(name="transport, freight train", location="DE")
input_inert_waste_treatment = eidb.get(name="treatment of inert waste, inert material landfill", location="CH")
input_cast_iron = eidb.get(name="cast iron production", location="RER")
input_chromium = eidb.get(name="chromium production", location="RER")
input_titanium = eidb.get(name="market for titanium", location="GLO")
input_manganese = eidb.get(name="manganese production", location="RER")
input_cobalt = [act for act in eidb if act["name"] == "cobalt production" and act["location"] == "GLO" and act.get("reference product") == "cobalt"][0]  # from cell production
input_chromsteel_sheet = eidb.get(name="sheet rolling, chromium steel", location="RER")
input_natural_gas_heat = eidb.get(name="heat production, natural gas, at industrial furnace low-NOx >100kW", location="Europe without Switzerland")
input_building_hall = eidb.get(name="building construction, hall, steel construction", location="CH")
input_building_multistorey = eidb.get(name="building construction, multi-storey", location="RER")
input_industrial_area = bsdb.get(name="Occupation, industrial area")
input_area_transformation_from = bsdb.get(name="Transformation, from unspecified")
input_area_transformation_to = bsdb.get(name="Transformation, to industrial area")
input_chemicals = eidb.get(name="market for chemical, inorganic", location="GLO")
input_petroleum_refinery = eidb.get(name="market for petroleum refinery", location="GLO")
input_chromsteel = eidb.get(name="steel production, electric, chromium steel 18/8", location="RER")
input_wastewater_treatment = eidb.get(name="treatment of wastewater, unpolluted, wastewater treatment",location="CH")
input_passenger_car = eidb.get(name="transport, passenger car, large size, diesel, EURO 5", location="RER")
input_heat_fuel_oil = eidb.get(name="heat production, light fuel oil, at boiler 100kW condensing, non-modulating", location="CH")
input_cogen_unit = eidb.get(name="construction work, heat and power co-generation unit, 160kW electrical", location="RER")
input_inverter = eidb.get(name="inverter production, 500kW", location="RER")
input_plant = eidb.get(name="gas power plant construction, combined cycle, 400MW electrical", location="RER")
input_cooling_tower = eidb.get(name="market for residue from cooling tower", location="RoW")
input_softened_water = eidb.get(name="market for water, completely softened", location="RER")
input_decarbonised_water = eidb.get(name="market for water, decarbonised", location="DE")
emission_o2 = bsdb.get(name="Oxygen", categories=("air",))
emission_nitrogen_oxides = bsdb.get(name="Nitrogen oxides", categories=("air",))
emission_nmvoc = bsdb.get(name="NMVOC, non-methane volatile organic compounds", categories=("air",))
gas_ext = eidb.get(name="market for natural gas, high pressure", location="DE")
emission_acenaphtene = bsdb.get(name="Acenaphthene", categories=("air",))
emission_acetaldehyde = bsdb.get(name="Acetaldehyde", categories=("air",))
emission_acetic_acid = bsdb.get(name="Acetic acid", categories=("air",))
emission_arsenic_ion = bsdb.get(name="Arsenic ion", categories=("air",))
emission_benzene = bsdb.get(name="Benzene", categories=("air",))
emission_benzoapyrene = bsdb.get(name="Benzo(a)pyrene", categories=("air",))
emission_berylliumII = bsdb.get(name="Beryllium II", categories=("air",))
emission_butane = bsdb.get(name="Butane", categories=("air",))
emission_cadmiumII = bsdb.get(name="Cadmium II", categories=("air",))
emission_carbondioxide = bsdb.get(name='Carbon dioxide, in air')
emission_carbondioxidefossil = bsdb.get(name="Carbon dioxide, fossil", categories=("air",))
emission_carbonmonoxidefossil = bsdb.get(name="Carbon monoxide, fossil", categories=("air",))
emission_chromiumIII = bsdb.get(name="Chromium III", categories=("air",))
emission_cobaltII= bsdb.get(name="Cobalt II", categories=("air",))
emission_dinitrogenmonoxide = bsdb.get(name="Dinitrogen monoxide", categories=("air",))
emission_dioxins = bsdb.get(name="Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin", categories=("air",))
emission_ethane = bsdb.get(name="Ethane", categories=("air",))
emission_formaldehyde = bsdb.get(name="Formaldehyde", categories=("air",))
emission_hexane = bsdb.get(name="Hexane", categories=("air",))
emission_leadII = bsdb.get(name="Lead II", categories=("air",))
emission_manganeseII = bsdb.get(name="Manganese II", categories=("air",))
emission_mercuryII = bsdb.get(name="Mercury II", categories=("air",))
emission_methanefossil = bsdb.get(name="Methane, fossil", categories=("air",))
emission_nickelII = bsdb.get(name="Nickel II", categories=("air",))
emission_particulatematter = bsdb.get(name="Particulate Matter, < 2.5 um", categories=("air",))
emission_pentane = bsdb.get(name="Pentane", categories=("air",))
emission_propane = bsdb.get(name="Propane", categories=("air",))
emission_propionicacid = bsdb.get(name="Propionic acid", categories=("air",))
emission_seleniumIV = bsdb.get(name="Selenium IV", categories=("air",))
emission_sulfurdioxide = bsdb.get(name="Sulfur dioxide", categories=("air",))
emission_toluene = bsdb.get(name="Toluene", categories=("air",))
emission_water_air = bsdb.get(name="Water", categories=("air",))
emission_water_water = bsdb.get(name="Water", categories=("water",))
emission_water_cooling = bsdb.get(name="Water, cooling, unspecified natural origin")

# Factors
kWh_to_MJ = 3.6
molmass_h20 = 18.01528  #g/mol
molmass_h2 = 2.016  #g/mol
norm_m3_h2 = 0.08988 * 1000  #g http://www.leonland.de/elements_by_price/de/conversion
roh_biogas = 1.3  #kg/m3 https://www.umweltbundesamt.de/sites/default/files/medien/pdfs/biogas_stoerfallv_1_2_erlaeuterungen.pdf

#------------- DCA production ----------------
process_DAC = project_af.new_activity(
    code="direct air capture facility production",
    name="direct air capture facility production",
    unit='unit',
)

# Technosphere
process_DAC.new_exchange(
    type="technosphere",
    name=input_concrete["name"],
    unit=input_concrete["unit"],
    amount=34.6666667,  #m3/ unit
    input=input_concrete,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_chromsteel_rolled["name"],
    unit=input_chromsteel_rolled["unit"],
    amount=36300,  # kg/ unit
    input=input_chromsteel_rolled,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_aluminium["name"],
    unit=input_aluminium["unit"],
    amount=262000,  # kg/ unit
    input=input_aluminium,
).save()
process_DAC.new_exchange(
    type="technosphere",
    name=input_steel["name"],
    unit=input_steel["unit"],
    amount=303000,  # kg/ unit
    input=input_steel,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_copper["name"],
    unit=input_copper["unit"],
    amount=3400,  # kg/ unit
    input=input_copper,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_gravel["name"],
    unit=input_gravel["unit"],
    amount=93100,  # kg/ unit
    input=input_gravel,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_gravel_operation["name"],
    unit=input_gravel_operation["unit"],
    amount=89600,  # kg/ unit
    input=input_gravel_operation,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_stonewool["name"],
    unit=input_stonewool["unit"],
    amount=8700,  # kg/unit
    input=input_stonewool,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_ethyleneglycol["name"],
    unit=input_ethyleneglycol["unit"],
    amount=15000,  # kg/unit
    input=input_ethyleneglycol,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_silicone["name"],
    unit=input_silicone["unit"],
    amount=1100,  # kg/ unit
    input=input_silicone,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_waste_ch["name"],
    unit=input_waste_ch["unit"],
    amount=243400,  # kg/ unit
    input=input_waste_ch,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_lorry_transport["name"],
    unit=input_lorry_transport["unit"],
    amount=244895 / 1000,  # tkm/ unit
    input=input_lorry_transport,
).save()

process_DAC.new_exchange(
    type="technosphere",
    name=input_transport_train_electricity["name"],
    unit=input_transport_train_electricity["unit"],
    amount=37412 / 1000,  # tkm/ unit
    input=input_transport_train_electricity,
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
    name=input_electricity_low["name"],
    unit=input_electricity_low["unit"],
    amount=0.12,    # kWh/unit
    input=input_electricity_low,
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
    name=emission_nitrogen_oxides["name"],
    unit=emission_nitrogen_oxides["unit"],
    amount=0.00032,  # kg/unit
    input=emission_nitrogen_oxides,
).save()

process_cell.new_exchange(
    type="biosphere",
    name=emission_nmvoc["name"],
    unit=emission_nmvoc["unit"],
    amount=0.00638,  # kg/unit
    input=emission_nmvoc,
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
# input_glass_cermet = eidb.get(name="market for glass-ceramic", location="GLO")
# own source (Harboe et al., 2020), category: glass-ceramic materials
# In order to analyse whether we can implement this in the paper, a manual implementation is needed. # To-Do
# Metals
process_stack = project_af.new_activity(
    code="stack production",
    name="HT-co-electrolysis stack production",
    unit='unit',
)

# Technosphere
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
    name=input_chromsteel_sheet["name"],
    unit=input_chromsteel_sheet["unit"],
    amount=534,  # kg
    input=input_chromsteel_sheet,
).save()

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

process_stack.new_exchange(
    type="technosphere",
    name=input_electricity_low["name"],
    unit=input_electricity_low["unit"],
    amount=3611.5,  # kWh
    input=input_electricity_low,
).save()

process_stack.new_exchange(
    type="technosphere",
    name=input_natural_gas_heat["name"],
    unit=input_natural_gas_heat["unit"],
    amount=606 * kWh_to_MJ,  # MJ
    input=input_natural_gas_heat,
).save()

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

process_stack.new_exchange(
    type="production",
    name="HT-co-electrolysis stack 150 kW",
    unit='unit',
    amount=1,  # Single unit
    input=process_stack,
).save()

process_stack['reference product'] = 'HT-co-electrolysis stack 150 kW'
process_stack.save()
# ----------------------------------------------

# ---------- Balance-of-Plant production -------
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
# ----------------------------------------------

# ------------ Scenarios - Syngas ---------------
# --------- Fossil syngas production ------------
process_syngas_fossil = project_af.new_activity(
    code="syngas production fossil",
    name="syngas production fossil",
    unit='kilogram',
)

# Technosphere
process_syngas_fossil.new_exchange(
    type="technosphere",
    name=input_co["name"],
    unit=input_co["unit"],
    amount=0.95775295,  #kg/ kg(syngas)
    input=input_co,
).save()

process_syngas_fossil.new_exchange(
    type="technosphere",
    name=input_h2["name"],
    unit=input_h2["unit"],
    amount=0.00045589,  # kg/kg(syngas)
    input=input_h2,
).save()

# Biosphere
process_syngas_fossil.new_exchange(
    type="biosphere",
    name=emission_carbonmonoxidefossil["name"],
    unit=emission_carbonmonoxidefossil["unit"],
    amount=-1.87E-08,  # kg/kg(syngas)
    input=emission_carbonmonoxidefossil,
).save()

# Production
process_syngas_fossil.new_exchange(
    type="production",
    name="syngas fossil",
    unit='kilogram',
    amount=1,
    input=process_syngas_fossil,
).save()

process_syngas_fossil['reference product'] = 'syngas fossil'
process_syngas_fossil.save()

process_syngas_fossil_2 = project_af.new_activity(
    code="syngas production fossil 2",
    name="syngas production fossil 2",
    unit='kilogram',
)

# Technosphere
process_syngas_fossil_2.new_exchange(
    type="technosphere",
    name=input_co["name"],
    unit=input_co["unit"],
    amount=0.95775295,  #kg/ kg(syngas)
    input=input_co,
).save()

process_syngas_fossil_2.new_exchange(
    type="technosphere",
    name=input_h2_coal["name"],
    unit=input_h2_coal["unit"],
    amount=0.00045589,  # kg/kg(syngas)
    input=input_h2_coal,
).save()

# Biosphere
# process_syngas_fossil_2.new_exchange(
#     type="biosphere",
#     name=emission_carbonmonoxidefossil["name"],
#     unit=emission_carbonmonoxidefossil["unit"],
#     amount=-1.87E-08,  # kg/kg(syngas)
#     input=emission_carbonmonoxidefossil,
# ).save()

# Production
process_syngas_fossil_2.new_exchange(
    type="production",
    name="syngas fossil",
    unit='kilogram',
    amount=1,
    input=process_syngas_fossil_2,
).save()

process_syngas_fossil_2['reference product'] = 'syngas fossil 2' # To-Do: check if this is correct
process_syngas_fossil_2.save()

# --------- Bio syngas production ------------
# To-Do: consider plant/unit production, otherwise not comparable
process_syngas_bio = project_af.new_activity(
    code="syngas production bio, miscanthus",
    name="syngas production bio, miscanthus",
    unit='kilogram',
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
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=0.2055556,  #kWh/ kg(syngas)
    input=input_electricity_medium,
).save()

# Production
process_syngas_bio.new_exchange(
    type="production",
    name=process_syngas_bio['name'],
    unit=process_syngas_bio['unit'],
    amount=1,  # kg/ kg(syngas)
    input=process_syngas_bio,
).save()

process_syngas_bio['reference product'] = 'syngas bio'
process_syngas_bio.save()


# --------- CO2 syngas production ------------
input_DAC = project_af.get(name="direct air capture facility production")
factor_CO2 = 1.38  # kgCO2/kgSyngas

process_syngas_CO2 = project_af.new_activity(
    code="syngas production CO2",
    name="syngas production CO2",
    unit='kilogram',
)

# Technosphere
process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_resin["name"],
    unit=input_resin["unit"],
    amount=3.75E-3 * factor_CO2,  # kg/kgCO2
    input=input_resin,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=0.5 * factor_CO2,  # kWh/kgCO2
    input=input_electricity_medium,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_heat_CO2["name"],
    unit=input_heat_CO2["unit"],
    amount=1.5 * factor_CO2,  # kWh/kgCO2
    input=input_heat_CO2,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_DAC["name"],
    unit=input_DAC["unit"],
    amount=9.3E-8 * factor_CO2,  # kWh/kgCO2
    input=input_DAC,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_water_deionized["name"],
    unit=input_water_deionized["unit"],
    amount=1.13,  # kg/ kg(Syngas)
    input=input_water_deionized,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=8.82,  # kWh/ kg(syngas)
    input=input_electricity_medium,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=process_cell["name"],
    unit=process_cell["unit"],
    amount=0.00203,  # units/ kg(syngas)
    input=process_cell,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=process_stack["name"],
    unit=process_stack["unit"],
    amount=1.4E-06,  # units/ kg(syngas)
    input=process_stack,
).save()

process_syngas_CO2.new_exchange(
    type="technosphere",
    name=process_bop["name"],
    unit=process_bop["unit"],
    amount=3.4E-07,  # units/ kg(syngas)
    input=process_bop,
).save()

# Biosphere
process_syngas_CO2.new_exchange(type='biosphere',
    name=emission_o2['name'],
    unit=emission_o2['unit'],
    amount=1.15,  # kg/kg(syngas)
    input=emission_o2,
    ).save()

# CO2 negative emissions because of DAC
process_syngas_CO2.new_exchange(
    type="biosphere",
    name=emission_carbondioxide["name"],
    unit=emission_carbondioxide["unit"],
    amount=-1.38,  # kg/kg(syngas)
    input=emission_carbondioxide,
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

# --------- Syngas scenarios ------------
syngas_fossil = project_af.get(name="syngas production fossil")
syngas_fossil_2 = project_af.get(name="syngas production fossil 2")
syngas_bio_1 = eidb.get(name="synthetic gas production, from wood, at fixed bed gasifier", location="RoW")
syngas_bio_2 = eidb.get(name="synthetic gas production, from wood, at fluidized bed gasifier", location="RoW")
syngas_bio_3 = project_af.get(name="syngas production bio, miscanthus")
syngas_CO2 = project_af.get(name="syngas production CO2")

process_syngas_scenarios = project_af.new_activity(
    code="syngas production scenarios",
    name="syngas production scenarios",
    unit='kilogram',
)

# Define a named parameter for syngas input
process_syngas_scenarios["parameters"] = {
    "status_fossil_1": int(input("Enter a number between 0 and 1 for status fossil: ")),
    "status_fossil_2": int(input("Enter a number between 0 and 1 for status fossil 2: ")),
    "status_bio_1": int(input("Enter a number between 0 and 1 for status bio 1: ")),
    "status_bio_2": int(input("Enter a number between 0 and 1 for status bio 2: ")),
    "status_bio_3": int(input("Enter a number between 0 and 1 for status bio 3: ")),
    "status_CO2": int(input("Enter a number between 0 and 1 for status CO2: "))
}

status_fossil_1 = process_syngas_scenarios["parameters"]["status_fossil_1"]
status_fossil_2 = process_syngas_scenarios["parameters"]["status_fossil_2"]
status_bio_1 = process_syngas_scenarios["parameters"]["status_bio_1"]
status_bio_2 = process_syngas_scenarios["parameters"]["status_bio_2"]
status_bio_3 = process_syngas_scenarios["parameters"]["status_bio_3"]
status_CO2 = process_syngas_scenarios["parameters"]["status_CO2"]

# Technosphere
process_syngas_scenarios.new_exchange(
    type="technosphere",
    name=syngas_fossil["name"],
    unit=syngas_fossil["unit"],
    amount=12.038517 * status_fossil_1,  # kg/L(Fuel)
    input=syngas_fossil,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name=syngas_fossil_2["name"],
    unit=syngas_fossil_2["unit"],
    amount=12.038517 * status_fossil_2,  # kg/L(Fuel)
    input=syngas_fossil_2,
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
    name=syngas_bio_3["name"],
    unit=syngas_bio_3["unit"],
    amount=12.038517 * status_bio_3,  # kg/L(Fuel)
    input=syngas_bio_3,
).save()

process_syngas_scenarios.new_exchange(
    type="technosphere",
    name=syngas_CO2["name"],
    unit=syngas_CO2["unit"],
    amount=12.038517 * status_CO2,  # kg/L(Fuel)
    input=syngas_CO2,
).save()

# Production
process_syngas_scenarios.new_exchange(
    type="production",
    name="syngas",
    unit="kilogram",
    amount=1,
    input=process_syngas_scenarios,
).save()

process_syngas_scenarios['reference product'] = 'syngas'
process_syngas_scenarios.save()

# ------------- Combined Heat and Power Unit production -----
process_CHPUO = project_af.new_activity(
    code="combined heat and power unit",
    name="combined heat and power unit",
    unit='unit',
)

# Technosphere
process_CHPUO.new_exchange(
    type="technosphere",
    name=input_plant["name"],
    unit=input_plant["unit"],
    amount=1.2094181828820287e-11,  #items/ kWh electricity
    input=input_plant,
).save()

process_CHPUO.new_exchange(
    type="technosphere",
    name=input_cooling_tower["name"],
    unit=input_cooling_tower["unit"],
    amount=-6.269623860060432e-06,  #kg/ kWh electricity
    input=input_cooling_tower,
).save()

process_CHPUO.new_exchange(
    type="technosphere",
    name=input_softened_water["name"],
    unit=input_softened_water["unit"],
    amount=0.03761774316036259,  # kg/ kWh electricity
    input=input_softened_water,
).save()

process_CHPUO.new_exchange(
    type="technosphere",
    name=input_decarbonised_water["name"],
    unit=input_decarbonised_water["unit"],
    amount=1.2539247720120863,  # kg/ kWh electricity
    input=input_decarbonised_water,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_acenaphtene["name"],
    unit=emission_acenaphtene["unit"],
    amount=4.971811721027923e-12,  # kg/ kWh electricity
    input=emission_acenaphtene,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_acetaldehyde["name"],
    unit=emission_acetaldehyde["unit"],
    amount=5.015699088048345e-09,  # kg/ kWh electricity
    input=emission_acetaldehyde,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_acetic_acid["name"],
    unit=emission_acetic_acid["unit"],
    amount=7.586244870673122e-07,  # kg/ kWh electricity
    input=emission_acetic_acid,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_arsenic_ion["name"],
    unit=emission_arsenic_ion["unit"],
    amount=2.5768154064848377e-10,  # kg/ kWh electricity
    input=emission_arsenic_ion,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_benzene["name"],
    unit=emission_benzene["unit"],
    amount=5.65520072177451e-09,  # kg/ kWh electricity
    input=emission_benzene,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_benzoapyrene["name"],
    unit=emission_benzoapyrene["unit"],
    amount=3.3166310219719684e-12,  # kg/ kWh electricity
    input=emission_benzoapyrene,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_berylliumII["name"],
    unit=emission_berylliumII["unit"],
    amount=1.548597093434927e-11,  # kg/ kWh electricity
    input=emission_berylliumII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_butane["name"],
    unit=emission_butane["unit"],
    amount=5.80567169441596e-06,  # kg/ kWh electricity
    input=emission_butane,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_cadmiumII["name"],
    unit=emission_cadmiumII["unit"],
    amount=1.4169349923736575e-09,  # kg/ kWh electricity
    input=emission_cadmiumII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_carbondioxidefossil["name"],
    unit=emission_carbondioxidefossil["unit"],
    amount=0.3347979141272271,  # kg/ kWh electricity
    input=emission_carbondioxidefossil,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_carbonmonoxidefossil["name"],
    unit=emission_carbonmonoxidefossil["unit"],
    amount=1.3793172492132951e-05,  # kg/ kWh electricity
    input=emission_carbonmonoxidefossil,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_chromiumIII["name"],
    unit=emission_chromiumIII["unit"],
    amount=1.7993820478373438e-09,  # kg/ kWh electricity
    input=emission_chromiumIII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_cobaltII["name"],
    unit=emission_cobaltII["unit"],
    amount=1.0783753039303944e-10,  # kg/ kWh electricity
    input=emission_cobaltII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_dinitrogenmonoxide["name"],
    unit=emission_dinitrogenmonoxide["unit"],
    amount=6.125422511279042e-06,  # kg/ kWh electricity
    input=emission_dinitrogenmonoxide,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_dioxins["name"],
    unit=emission_dioxins["unit"],
    amount=1.8181909194175255e-16,  # kg/ kWh electricity
    input=emission_dioxins,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_ethane["name"],
    unit=emission_ethane["unit"],
    amount=8.589384688282792e-06,  # kg/ kWh electricity
    input=emission_ethane,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_formaldehyde["name"],
    unit=emission_formaldehyde["unit"],
    amount=2.0250885067995196e-07,  # kg/ kWh electricity
    input=emission_formaldehyde,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_hexane["name"],
    unit=emission_hexane["unit"],
    amount=4.971811721027923e-06,  # kg/ kWh electricity
    input=emission_hexane,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_leadII["name"],
    unit=emission_leadII["unit"],
    amount=6.457712575862245e-10,  # kg/ kWh electricity
    input=emission_leadII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_manganeseII["name"],
    unit=emission_manganeseII["unit"],
    amount=4.896576234707198e-10,  # kg/ kWh electricity
    input=emission_manganeseII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_mercuryII["name"],
    unit=emission_mercuryII["unit"],
    amount=4.3135012157215775e-10,  # kg/ kWh electricity
    input=emission_mercuryII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_methanefossil["name"],
    unit=emission_methanefossil["unit"],
    amount=6.087804768118679e-06,  # kg/ kWh electricity
    input=emission_methanefossil,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_nickelII["name"],
    unit=emission_nickelII["unit"],
    amount=2.7022078836860462e-09,  # kg/ kWh electricity
    input=emission_nickelII,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_nitrogen_oxides["name"],
    unit=emission_nitrogen_oxides["unit"],
    amount=0.000159875408431541,  # kg/ kWh electricity
    input=emission_nitrogen_oxides,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_particulatematter["name"],
    unit=emission_particulatematter["unit"],
    amount=3.0783853152896724e-06,  # kg/ kWh electricity
    input=emission_particulatematter,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_pentane["name"],
    unit=emission_pentane["unit"],
    amount=7.210067439069497e-06,  # kg/ kWh electricity
    input=emission_pentane,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_propane["name"],
    unit=emission_propane["unit"],
    amount=4.420084821342605e-06,  # kg/ kWh electricity
    input=emission_propane,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_propionicacid["name"],
    unit=emission_propionicacid["unit"],
    amount=1.0031398176096691e-07,  # kg/ kWh electricity
    input=emission_propionicacid,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_seleniumIV["name"],
    unit=emission_seleniumIV["unit"],
    amount=3.078385315289672e-11,  # kg/ kWh electricity
    input=emission_seleniumIV,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_sulfurdioxide["name"],
    unit=emission_sulfurdioxide["unit"],
    amount=3.5862248479545673e-06,  # kg/ kWh electricity
    input=emission_sulfurdioxide,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_toluene["name"],
    unit=emission_toluene["unit"],
    amount=9.404435790090649e-09,  # kg/ kWh electricity
    input=emission_toluene,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_water_air["name"],
    unit=emission_water_air["unit"],
    amount=0.0005688087233777747,  # m3/ kWh electricity
    input=emission_water_air,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_water_water["name"],
    unit=emission_water_water["unit"],
    amount=0.047187040777352036,  # m3/ kWh electricity
    input=emission_water_water,
).save()

process_CHPUO.new_exchange(
    type="biosphere",
    name=emission_water_cooling["name"],
    unit=emission_water_cooling["unit"],
    amount=0.046464306985557396,  # m3/ kWh electricity
    input=emission_water_cooling,
).save()

# Production
process_CHPUO.new_exchange(
    type="production",
    name="combined heat and power unit and operation",
    unit='kilowatt hour',
    amount=1,
    input=process_CHPUO,
).save()

process_CHPUO['reference product'] = 'combined heat and power unit'
process_CHPUO.save()
# -----------------------------------------------------------

# ------------- Combined Heat and Power ---------------------
# Define the heat-to-electricity ratio (based on CHPU specifications)
electricity_ratio = 0.61111111
heat_ratio = 0.527777778

# Normalize the ratios to ensure the total equals 1
total_ratio = electricity_ratio + heat_ratio
normalized_electricity_ratio = electricity_ratio / total_ratio
normalized_heat_ratio = heat_ratio / total_ratio

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
    amount=0.0,  # m3/ L(Fuel)
    input=gas_ext,
).save()

process_CHPU_heat.new_exchange(
    type="technosphere",
    name=process_CHPUO["name"],
    unit=process_CHPUO["unit"],
    amount=normalized_heat_ratio,  # kWh/ L (Fuel)
    input=process_CHPUO,
).save()

# Production
process_CHPU_heat.new_exchange(
    type="production",
    name="heat CHP",
    unit="kilowatt hour", # check
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
    amount=0.0,  # m3/ L(Fuel)
    input=gas_ext,
).save()

process_CHPU_elect.new_exchange(
    type="technosphere",
    name=process_CHPUO["name"],
    unit=process_CHPUO["unit"],
    amount=normalized_electricity_ratio,  # kWh/ L (Fuel)
    input=process_CHPUO,
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

process_FT_h2 = project_af.new_activity(
    code="h2 production, fischer tropsch conversion",
    name="h2 production, fischer tropsch conversion",
    unit='kilogram',
)

# Auxillary materials
process_FT_h2.new_exchange(
    type="technosphere",
    name=input_chemicals["name"],
    unit=input_chemicals["unit"],
    amount=0.07706479,  # kg/ L(Fuel)
    input=input_chemicals,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=1.56E-10,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_industrial_area["name"],
    unit=input_industrial_area["unit"],
    amount=0.00154229,  # m2-year/ L (Fuel)
    input=input_industrial_area,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_area_transformation_from["name"],
    unit=input_area_transformation_from["unit"],
    amount=1.74E-5,  # m2/ L (Fuel)
    input=input_area_transformation_from,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_area_transformation_to["name"],
    unit=input_area_transformation_to["unit"],
    amount=1.74E-5,  # m2/ L (Fuel)
    input=input_area_transformation_to,
).save()

process_FT_h2.new_exchange(
    type="biosphere",
    name=input_waste["name"],
    unit=input_waste["unit"],
    amount=-2.88E-3,  # m2/ L (Fuel)
    input=input_waste,
).save()

# Technosphere
process_FT_h2.new_exchange(
    type="technosphere",
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=0.02150107,  # kWh/ L (Fuel)
    input=input_electricity_medium,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name=electricity_int["name"],
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=electricity_int,
).save()

process_FT_h2.new_exchange(
    type="technosphere",
    name=syngas_int["name"],
    unit=syngas_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=syngas_int,
).save()

# Production
process_FT_h2.new_exchange(
    type="production",
    name="H2",
    unit='kilogram',
    amount=0.0268128, # kg/ L (Fuel)
    input=process_FT_h2,
).save()

process_FT_h2['reference product'] = 'H2'
process_FT_h2.save()

process_FT_syncrude = project_af.new_activity(
    code="syncrude production, fischer tropsch conversion",
    name="syncrude production, fischer tropsch conversion",
    unit='kilogram',
)
# Auxillary materials
process_FT_syncrude.new_exchange(
    type="technosphere",
    name=input_chemicals["name"],
    unit=input_chemicals["unit"],
    amount=2.218603,  # kg/ L(Fuel)
    input=input_chemicals,
).save()

process_FT_syncrude.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=4.49E-9,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
).save()

process_FT_syncrude.new_exchange(
    type="biosphere",
    name=input_industrial_area["name"],
    unit=input_industrial_area["unit"],
    amount=0.04428566,  # m2-year/ L (Fuel)
    input=input_industrial_area,
).save()

process_FT_syncrude.new_exchange(
    type="biosphere",
    name=input_area_transformation_from["name"],
    unit=input_area_transformation_from["unit"],
    amount=4.99E-4,  # m2/ L (Fuel)
    input=input_area_transformation_from,
).save()

process_FT_syncrude.new_exchange(
    type="biosphere",
    name=input_area_transformation_to["name"],
    unit=input_area_transformation_to["unit"],
    amount=4.99E-4,  # m2/ L (Fuel)
    input=input_area_transformation_to,
).save()

process_FT_syncrude.new_exchange(
    type="technosphere",
    name=input_waste["name"],
    unit=input_waste["unit"],
    amount=-8.27E-2,  # m2/ L (Fuel)
    input=input_waste,
).save()

# Technosphere
process_FT_syncrude.new_exchange(
    type="technosphere",
    name=input_electricity_medium["name"],
    unit=input_electricity_medium["unit"],
    amount=0.61738782,  # kWh/ L (Fuel)
    input=input_electricity_medium,
).save()

process_FT_syncrude.new_exchange(
    type="technosphere",
    name=electricity_int["name"],
    unit=electricity_int["unit"],
    amount=0,  # kWh/ L (Fuel)
    input=electricity_int,
).save()

process_FT_syncrude.new_exchange(
    type="technosphere",
    name=syngas_int["name"],
    unit=syngas_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=syngas_int,
).save()

# Production
process_FT_syncrude.new_exchange(
    type="production",
    name="syncrude",
    unit='kilogram',
    amount=18.4932478,  # kg/ L (Fuel)
    input=process_FT_syncrude,
).save()

process_FT_syncrude['reference product'] = 'syncrude'
process_FT_syncrude.save()

# --------------- Hydrocracking and Destillation ------------
heat_int = project_af.get(name="heat production, combined heat and power production")
H2_int = project_af.get(name="h2 production, fischer tropsch conversion")
syncrude_int = project_af.get(name="syncrude production, fischer tropsch conversion")

process_HandD_h20 = project_af.new_activity(
    code="h2o production, hydrocracking and destillation",
    name="h2o production, hydrocracking and destillation",
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
    name="syncrude production, fischer tropsch conversion",
    unit=syncrude_int["unit"],
    amount=0,  # kg/ L (Fuel)
    input=syncrude_int,
).save()

process_HandD_h20.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=8.347E-11,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
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
    code="naphta production, hydrocracking and destillation",
    name="naphta production, hydrocracking and destillation",
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
    name="syncrude production, fischer tropsch conversion",
    unit=syncrude_int["unit"],
    amount=0,  # kg/ L(Fuel)
    input=syncrude_int,
).save()

process_HandD_naphta.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=2.428E-11,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
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
    code="c1c4 production, hydrocracking and destillation",
    name="c1c4 production, hydrocracking and destillation",
    unit='kilogram',
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
    name="syncrude production, fischer tropsch conversion",
    unit=syncrude_int["unit"],
    amount=0,  # kg/ l (Fuel)
    input=syncrude_int,
).save()

process_HandD_c1c4.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=5.980E-12,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
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
    code="jet fuel production, hydrocracking and destillation",
    name="jet fuel production, hydrocracking and destillation",
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
    name="syncrude production, fischer tropsch conversion",
    unit=syncrude_int["unit"],
    amount=0,  # kg/L Fuel
    input=syncrude_int,
).save()

process_HandD_jetfuel.new_exchange(
    type="technosphere",
    name=input_petroleum_refinery["name"],
    unit=input_petroleum_refinery["unit"],
    amount=3.189E-11,  # unit/ L (Fuel)
    input=input_petroleum_refinery,
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
input_FTC_syncrude=project_af.get(name="syncrude production, fischer tropsch conversion")
input_FTC_H2=project_af.get(name="h2 production, fischer tropsch conversion")
input_hydro_c1c4=project_af.get(name="c1c4 production, hydrocracking and destillation")
input_hydro_H2O=project_af.get(name="h2o production, hydrocracking and destillation")
input_hydro_naphta=project_af.get(name="naphta production, hydrocracking and destillation")
input_hydro_jetfuel=project_af.get(name="jet fuel production, hydrocracking and destillation")

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
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
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
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel 
    input=input_hydro_naphta,
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
    name=process_full["name"],
    unit=process_full["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full,
).save()

process_full['reference product'] = 'jet fuel, all processes'
process_full.save()

# ----------------- Hardcoded scenarios -----------------
# bio 1
process_full_bio1 = project_af.new_activity(
    code="jet fuel production bio 1",
    name="jet fuel production bio 1",
    unit='liter',
)

# Technosphere
process_full_bio1.new_exchange(
    type="technosphere",
    name=syngas_bio_1["name"],
    unit=syngas_bio_1["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_bio_1,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_bio1.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_bio1.new_exchange(
    type="production",
    name=process_full_bio1["name"],
    unit=process_full_bio1["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_bio1,
).save()

process_full_bio1['reference product'] = 'jet fuel, bio1'
process_full_bio1.save()

# bio 2
process_full_bio2 = project_af.new_activity(
    code="jet fuel production bio 2",
    name="jet fuel production bio 2",
    unit='liter',
)

# Technosphere
process_full_bio2.new_exchange(
    type="technosphere",
    name=syngas_bio_2["name"],
    unit=syngas_bio_2["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_bio_2,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_bio2.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_bio2.new_exchange(
    type="production",
    name=process_full_bio2["name"],
    unit=process_full_bio2["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_bio2,
).save()

process_full_bio2['reference product'] = 'jet fuel, bio2'
process_full_bio2.save()

# bio 3
process_full_bio3 = project_af.new_activity(
    code="jet fuel production bio 3",
    name="jet fuel production bio 3",
    unit='liter',
)

# Technosphere
process_full_bio3.new_exchange(
    type="technosphere",
    name=syngas_bio_3["name"],
    unit=syngas_bio_3["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_bio_3,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_bio3.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_bio3.new_exchange(
    type="production",
    name=process_full_bio3["name"],
    unit=process_full_bio3["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_bio3,
).save()

process_full_bio3['reference product'] = 'jet fuel, bio3'
process_full_bio3.save()

# CO2
process_full_co2 = project_af.new_activity(
    code="jet fuel production co2",
    name="jet fuel production co2",
    unit='liter',
)

# Technosphere
process_full_co2.new_exchange(
    type="technosphere",
    name=syngas_CO2["name"],
    unit=syngas_CO2["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_CO2,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_co2.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_co2.new_exchange(
    type="production",
    name=process_full_co2["name"],
    unit=process_full_co2["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_co2,
).save()

process_full_co2['reference product'] = 'jet fuel, co2'
process_full_co2.save()

# Fossil
process_full_fossil = project_af.new_activity(
    code="jet fuel production fossil",
    name="jet fuel production fossil",
    unit='liter',
)

# Technosphere
process_full_fossil.new_exchange(
    type="technosphere",
    name=syngas_fossil["name"],
    unit=syngas_fossil["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_fossil,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_fossil.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_fossil.new_exchange(
    type="production",
    name=process_full_fossil["name"],
    unit=process_full_fossil["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_fossil,
).save()

process_full_fossil['reference product'] = 'jet fuel, fossil'
process_full_fossil.save()

# Fossil
process_full_fossil_2 = project_af.new_activity(
    code="jet fuel production fossil 2",
    name="jet fuel production fossil 2",
    unit='liter',
)

# Technosphere
process_full_fossil_2.new_exchange(
    type="technosphere",
    name=syngas_fossil_2["name"],
    unit=syngas_fossil_2["unit"],
    amount=4.1109582,  # kg/ L(Fuel)
    input=syngas_fossil_2,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_CHPU_heat["name"],
    unit=input_CHPU_heat["unit"],
    amount=0.52777778,  # kWh/ L(Fuel)
    input=input_CHPU_heat,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_CHPU_elect["name"],
    unit=input_CHPU_elect["unit"],
    amount=0.611111,  # kg/L (Fuel)
    input=input_CHPU_elect,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_FTC_syncrude["name"],
    unit=input_FTC_syncrude["unit"],
    amount=18.4932478,  # kg/L Fuel
    input=input_FTC_syncrude,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_FTC_H2["name"],
    unit=input_FTC_H2["unit"],
    amount=0.0268128,  # kg/L Fuel
    input=input_FTC_H2,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_hydro_c1c4["name"],
    unit=input_hydro_c1c4["unit"],
    amount=0.15,  # kg/L Fuel
    input=input_hydro_c1c4,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_hydro_H2O["name"],
    unit=input_hydro_H2O["unit"],
    amount=2.0937,  # kg/L Fuel
    input=input_hydro_H2O,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_hydro_naphta["name"],
    unit=input_hydro_naphta["unit"],
    amount=0.609,  # L/L Fuel
    input=input_hydro_naphta,
).save()

process_full_fossil_2.new_exchange(
    type="technosphere",
    name=input_hydro_jetfuel["name"],
    unit=input_hydro_jetfuel["unit"],
    amount=1,  # L/L
    input=input_hydro_jetfuel,
).save()

# Production
process_full_fossil_2.new_exchange(
    type="production",
    name=process_full_fossil_2["name"],
    unit=process_full_fossil_2["unit"],
    amount=1,  # L = 0,775 kg
    input=process_full_fossil_2,
).save()

process_full_fossil_2['reference product'] = 'jet fuel, fossil 2'
process_full_fossil_2.save()