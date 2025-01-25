#imports brightway packages
import bw2data as bd  # for everything related to the database

#Sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")


input_plant = eidb.get(name="gas power plant construction, combined cycle, 400MW electrical", location="RER")
input_cooling_tower = eidb.get(name="market for residue from cooling tower", location="RoW")
input_softened_water = eidb.get(name="market for water, completely softened", location="RER")
input_decarbonised_water = eidb.get(name="market for water, decarbonised", location="DE")

emission_acenaphtene = bsdb.get(name="Acenaphthene", categories=("air",))
emission_acetaldehyde = bsdb.get(name="Acetaldehyde", categories=("air",))
emission_acetic_acid = bsdb.get(name="Acetic acid", categories=("air",))
emission_arsenic_ion = bsdb.get(name="Arsenic ion", categories=("air",))
emission_benzene = bsdb.get(name="Benzene", categories=("air",))
emission_benzoapyrene = bsdb.get(name="Benzo(a)pyrene", categories=("air",))
emission_berylliumII = bsdb.get(name="Beryllium II", categories=("air",))
emission_butane = bsdb.get(name="Butane", categories=("air",))
emission_cadmiumII = bsdb.get(name="Cadmium II", categories=("air",))
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


#------------- CHPU ----------------
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

process_CHPUO['reference product'] = 'direct air capture facility'
process_CHPUO.save()
#----------------------------------------------