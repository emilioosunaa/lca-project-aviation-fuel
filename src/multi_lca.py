import bw2data as bd
import bw2calc as bc
import pandas as pd
import matplotlib.pyplot as plt
import re

# Import databases
bd.projects.set_current("LCA_EPE")
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

# Definition of the functional unit
jet_fuel_all = project_af.get(name='jet fuel production, all processes')
jet_fuel_fossil = project_af.get(name='jet fuel production fossil')
jet_fuel_fossil_2 = project_af.get(name='jet fuel production fossil 2')
jet_fuel_bio1 = project_af.get(name='jet fuel production bio 1')
jet_fuel_bio2 = project_af.get(name='jet fuel production bio 2')
jet_fuel_bio3 = project_af.get(name='jet fuel production bio 3')
jet_fuel_co2 = project_af.get(name='jet fuel production co2')
functional_units = {
    "jet_fuel_fossil": {jet_fuel_fossil.id: 1},
    "jet_fuel_fossil_2": {jet_fuel_fossil_2.id: 1},
    "jet_fuel_bio1": {jet_fuel_bio1.id: 1},
    "jet_fuel_bio2": {jet_fuel_bio2.id: 1},
    "jet_fuel_bio3": {jet_fuel_bio3.id: 1},
    "jet_fuel_co2": {jet_fuel_co2.id: 1},
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
    clean_impact_category = re.sub(r"no LT", "", impact_hierarchy[1]).strip().title()
    records.append({
        'Functional Unit': functional_unit,
        'Impact Category': clean_impact_category,  # Remove "no LT"
        'Score': value
    })

df_scores = pd.DataFrame(records)
df_pivot = df_scores.pivot(index='Functional Unit', columns='Impact Category', values='Score')
df_pivot = df_pivot.sort_index(axis=1)
print(df_pivot)

# Export the results to an Excel file with multiple sheets
with pd.ExcelWriter("data//MultiLCA_all_categoiries.xlsx") as writer:
    # Write all results grouped by Impact Category in "All Results" sheet
    all_results = []
    for impact_category in df_scores['Impact Category'].unique():
        df_category = df_scores[df_scores['Impact Category'] == impact_category]
        all_results.append(pd.concat([pd.DataFrame({"Impact Category": [impact_category]}), df_category]))
    final_results = pd.concat(all_results, axis=0)
    final_results.to_excel(writer, sheet_name="All Results", index=False)

    # Write each functional unit to its own sheet
    for functional_unit in df_scores['Functional Unit'].unique():
        df_subset = df_scores[df_scores['Functional Unit'] == functional_unit]
        df_subset.to_excel(writer, sheet_name=functional_unit, index=False)

# Plotting
df_pivot.T.plot(kind='barh', figsize=(12, 8))
plt.xlabel('Impact Score')
plt.title('Impact Categories per Functional Unit')
plt.legend(title='Functional Units', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("plots//multilca_impact_categories_per_functional_unit.png", dpi=300, bbox_inches='tight')
plt.show()