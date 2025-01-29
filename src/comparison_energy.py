import bw2data as bd  # for everything related to the database
import bw2calc as bc
import pandas as pd
import matplotlib.pyplot as plt

# Lists all projects and then sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database('project_af')
data = {}  # we start with no data, so data is empty
project_af.write(data)
bd.Database('project_af').metadata['depends'] = ['ecoinvent-3.10-biosphere',
                                                 'ecoinvent-3.10-cutoff',
                                                 'ei310_IMAGE_SSP2_RCP26_2035',
                                                 'ei310_IMAGE_SSP2_RCP26_2050']

electricity_import_AT = eidb.get(name="electricity, high voltage, import from AT", location="DE")
#electricity_import_BE = eidb.get(name="electricity, high voltage, import from BE", location="DE")
electricity_import_NO = eidb.get(name="electricity, high voltage, import from NO", location="DE")
electricity_import_CH = eidb.get(name="electricity, high voltage, import from CH", location="DE")
electricity_import_CZ = eidb.get(name="electricity, high voltage, import from CZ", location="DE")
electricity_import_DK = eidb.get(name="electricity, high voltage, import from DK", location="DE")
electricity_import_FR = eidb.get(name="electricity, high voltage, import from FR", location="DE")
electricity_import_LU = eidb.get(name="electricity, high voltage, import from LU", location="DE")
electricity_import_NL = eidb.get(name="electricity, high voltage, import from NL", location="DE")
electricity_import_PL = eidb.get(name="electricity, high voltage, import from PL", location="DE")
electricity_import_SE = eidb.get(name="electricity, high voltage, import from SE", location="DE")

electricity_productionmix = eidb.get(name="electricity, high voltage, production mix", location="DE")
electricity_residualmix = eidb.get(name="electricity, high voltage, residual mix", location="DE")

electricity_from_lignite = eidb.get(name="electricity production, lignite", location="DE")
electricity_from_oil = eidb.get(name="electricity production, oil", location="DE")
electricity_from_deepgeothermal = eidb.get(name="electricity production, deep geothermal", location="DE")
electricity_from_hardcoal = eidb.get(name="electricity production, hard coal", location="DE")
electricity_from_hydropumpedstorage = eidb.get(name="electricity production, hydro, pumped storage", location="DE")
electricity_from_hydrorunofriver = eidb.get(name="electricity production, hydro, run-of-river", location="DE")
electricity_from_naturalgas10MW = eidb.get(name="electricity production, natural gas, 10MW", location="DE")
electricity_from_nuclearboilingwaterreactor = eidb.get(name="electricity production, nuclear, boiling water reactor", location="DE")
electricity_from_nuclearpressurewaterreactor = eidb.get(name="electricity production, nuclear, pressure water reactor", location="DE")
electricity_from_wind1MWturbineonshore = eidb.get(name="electricity production, wind, <1MW turbine, onshore", location="DE")
electricity_from_wind3MWturbineonshore = eidb.get(name="electricity production, wind, >3MW turbine, onshore", location="DE")
electricity_from_hydroreservoirnonalpineregion = eidb.get(name="electricity production, hydro, reservoir, non-alpine region", location="DE")
electricity_from_naturalgasconventionalpowerplant = eidb.get(name="electricity production, natural gas, conventional power plant", location="DE")
electricity_from_wind1to3MWturbineoffshore = eidb.get(name="electricity production, wind, 1-3MW turbine, offshore", location="DE")
electricity_from_wind1to3MWturbineonshore = eidb.get(name="electricity production, wind, 1-3MW turbine, onshore", location="DE")
electricity_from_naturalgascombinedcyclepowerplant = eidb.get(name="electricity production, natural gas, combined cycle power plant", location="DE")
electricity_from_heatandpowercogenerationbiogasgasengine = [act for act in eidb if act["name"] == "heat and power co-generation, biogas, gas engine" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationhardcoal = [act for act in eidb if act["name"] == "heat and power co-generation, hard coal" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationlignite = [act for act in eidb if act["name"] == "heat and power co-generation, lignite" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationnaturalgascombinedcyclepowerplant400MWelectrical = [act for act in eidb if act["name"] == "heat and power co-generation, natural gas, combined cycle power plant, 400MW electrical" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationnaturalgasconventionalpowerplant100MWelectrical = [act for act in eidb if act["name"] == "heat and power co-generation, natural gas, conventional power plant, 100MW electrical" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationoil = [act for act in eidb if act["name"] == "heat and power co-generation, oil" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_heatandpowercogenerationwoodchips6667kWstateoftheart2014 = [act for act in eidb if act["name"] == "heat and power co-generation, wood chips, 6667 kW, state-of-the-art 2014" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_treatmentofblastfurnacegasinpowerplant = [act for act in eidb if act["name"] == "treatment of blast furnace gas, in power plant" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]
electricity_from_treatmentofcoalgasinpowerplant = [act for act in eidb if act["name"] == "treatment of coal gas, in power plant" and act["location"] == "DE" and act.get("reference product") == "electricity, high voltage"][0]

functional_units = {
    "electricity_import_AT": {electricity_import_AT.id: 1},
    "electricity_import_NO": {electricity_import_NO.id: 1},
    "electricity_import_CH": {electricity_import_CH.id: 1},
    "electricity_import_CZ": {electricity_import_CZ.id: 1},
    "electricity_import_DK": {electricity_import_DK.id: 1},
    "electricity_import_FR": {electricity_import_FR.id: 1},
    "electricity_import_LU": {electricity_import_LU.id: 1},
    "electricity_import_NL": {electricity_import_NL.id: 1},
    "electricity_import_PL": {electricity_import_PL.id: 1},
    "electricity_import_SE": {electricity_import_SE.id: 1},
    "electricity_productionmix": {electricity_productionmix.id: 1},
    "electricity_residualmix": {electricity_residualmix.id: 1},
    "electricity_from_lignite": {electricity_from_lignite.id: 1},
    "electricity_from_oil": {electricity_from_oil.id: 1},
    "electricity_from_deepgeothermal": {electricity_from_deepgeothermal.id: 1},
    "electricity_from_hardcoal": {electricity_from_hardcoal.id: 1},
    "electricity_from_hydropumpedstorage": {electricity_from_hydropumpedstorage.id: 1},
    "electricity_from_hydrorunofriver": {electricity_from_hydrorunofriver.id: 1},
    "electricity_from_naturalgas10MW": {electricity_from_naturalgas10MW.id: 1},
    "electricity_from_nuclearboilingwaterreactor": {electricity_from_nuclearboilingwaterreactor.id: 1},
    "electricity_from_nuclearpressurewaterreactor": {electricity_from_nuclearpressurewaterreactor.id: 1},
    "electricity_from_wind1MWturbineonshore": {electricity_from_wind1MWturbineonshore.id: 1},
    "electricity_from_wind3MWturbineonshore": {electricity_from_wind3MWturbineonshore.id: 1},
    "electricity_from_hydroreservoirnonalpineregion": {electricity_from_hydroreservoirnonalpineregion.id: 1},
    "electricity_from_naturalgasconventionalpowerplant": {electricity_from_naturalgasconventionalpowerplant.id: 1},
    "electricity_from_wind1to3MWturbineoffshore": {electricity_from_wind1to3MWturbineoffshore.id: 1},
    "electricity_from_wind1to3MWturbineonshore": {electricity_from_wind1to3MWturbineonshore.id: 1},
    "electricity_from_naturalgascombinedcyclepowerplant": {electricity_from_naturalgascombinedcyclepowerplant.id: 1},
    "electricity_from_heatandpowercogenerationbiogasgasengine": {electricity_from_heatandpowercogenerationbiogasgasengine.id: 1},
    "electricity_from_heatandpowercogenerationhardcoal": {electricity_from_heatandpowercogenerationhardcoal.id: 1},
    "electricity_from_heatandpowercogenerationlignite": {electricity_from_heatandpowercogenerationlignite.id: 1},
    "electricity_from_heatandpowercogenerationnaturalgascombinedcyclepowerplant400MWelectrical": {electricity_from_heatandpowercogenerationnaturalgascombinedcyclepowerplant400MWelectrical.id: 1},
    "electricity_from_heatandpowercogenerationnaturalgasconventionalpowerplant100MWelectrical": {electricity_from_heatandpowercogenerationnaturalgasconventionalpowerplant100MWelectrical.id: 1},
    "electricity_from_heatandpowercogenerationoil": {electricity_from_heatandpowercogenerationoil.id: 1},
    "electricity_from_heatandpowercogenerationwoodchips6667kWstateoftheart2014": {electricity_from_heatandpowercogenerationwoodchips6667kWstateoftheart2014.id: 1},
    "electricity_from_treatmentofblastfurnacegasinpowerplant": {electricity_from_treatmentofblastfurnacegasinpowerplant.id: 1},
    "electricity_from_treatmentofcoalgasinpowerplant": {electricity_from_treatmentofcoalgasinpowerplant.id: 1},
}

# Definition of the impact categories
climate_change_categories = [met for met in bd.methods if 'EF v3.1 no LT' in str(met)]
chosen_methods = climate_change_categories

# Multi-LCA
config = {
    "impact_categories": chosen_methods,
}

data_objs = bd.get_multilca_data_objs(
    functional_units=functional_units, method_config=config
)

mlca = bc.MultiLCA(demands=functional_units, method_config=config, data_objs=data_objs)
mlca.lci()
mlca.lcia()

scores = mlca.scores

records = []
for key, value in mlca.scores.items():
    impact_hierarchy, functional_unit = key
    impact_category = ' > '.join(impact_hierarchy)
    records.append({
        'Functional Unit': functional_unit,
        'Impact Category': impact_category,
        'Score': value
    })
df_scores = pd.DataFrame(records)
df_pivot = df_scores.pivot(index='Functional Unit', columns='Impact Category', values='Score')
df_pivot = df_pivot.sort_index(axis=1)
print(df_pivot)

# Exporting data to Excel
output_path = r'C:\Users\matal\anaconda3\LCAs_project\lca_project_fisher\data\Electricity_comparison.xlsx'
df_pivot.to_excel(output_path, sheet_name='Electricity Comparison')

# Plotting
df_pivot.T.plot(kind='barh', figsize=(12, 8))
plt.xlabel('Impact Score')
plt.title('Impact Categories per Functional Unit')
plt.legend(title='Functional Units', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
