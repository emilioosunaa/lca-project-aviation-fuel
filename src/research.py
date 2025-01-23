#imports brightway packages
import bw2data as bd  # for everything related to the database

#Sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

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


print("Cerium oxide unit:", input_cerium_oxide["unit"])
print("Lanthanum oxide unit:", input_lanthanum_oxide["unit"])
print("Gadolinium oxide unit:", input_gadolinium_oxide["unit"])
print("Yttrium oxide unit:", input_yttrium_oxide["unit"])
print("Strontium carbonate unit:", input_strontium_carbonate["unit"])
print("Iron(III) oxide-hydroxide (Portafer) unit:", input_iron_oxide_hydroxide["unit"])
print("Nickel mix unit:", input_nickel_mix["unit"])
print("Cobalt hydroxide unit:", input_cobalt_hydroxide["unit"])
print("Zirconium oxide unit:", input_zirconium_oxide["unit"])
print("Manganese dioxide unit:", input_manganese_dioxide["unit"])
print("Copper oxide unit:", input_copper_oxide["unit"])
print("Nitric acid (98% substitute) unit:", input_nitric_acid["unit"])
print("MEK unit:", input_mek["unit"])
print("CMC unit:", input_cmc["unit"])
print("Ethanol unit:", input_ethanol["unit"])
print("Benzyl alcohol unit:", input_benzyl_alcohol["unit"])
print("Sea transport unit:", input_sea_transport["unit"])
print("Lorry transport unit:", input_lorry_transport["unit"])
print("Train transport unit:", input_train_transport["unit"])
print("Electricity unit:", input_electricity["unit"])
print("Inert waste treatment unit:", input_inert_waste_treatment["unit"])

print("Nitrogen oxides emission flow unit:", output_nitrogen_oxides["unit"])
print("NMVOC emission flow unit:", output_nmvoc["unit"])