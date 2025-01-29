import bw2data as bd
import bw2calc as bc
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Import databases
bd.projects.set_current("LCA_EPE")
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

# Definition of the functional unit
jet_fuel_all = project_af.get(name='jet fuel production, all processes')
jet_fuel_fossil = project_af.get(name='jet fuel production fossil')
jet_fuel_bio1 = project_af.get(name='jet fuel production bio 1')
jet_fuel_bio2 = project_af.get(name='jet fuel production bio 2')
jet_fuel_bio3 = project_af.get(name='jet fuel production bio 3')
jet_fuel_co2 = project_af.get(name='jet fuel production co2')
functional_units = {
    "jet_fuel_fossil": {jet_fuel_fossil.id: 1},
    "jet_fuel_bio1": {jet_fuel_bio1.id: 1},
    "jet_fuel_bio2": {jet_fuel_bio2.id: 1},
    "jet_fuel_bio3": {jet_fuel_bio3.id: 1},
    "jet_fuel_co2": {jet_fuel_co2.id: 1},
}

# Definition of the wanted impact categories
selected_categories = [
    "acidification no LT",
    "climate change no LT",
    "climate change: biogenic no LT",
    "climate change: fossil no LT",
    "climate change: land use and land use change no LT",
    "energy resources: non-renewable no LT",
    "eutrophication: freshwater no LT",
    "eutrophication: marine no LT",
    "human toxicity: carcinogenic no LT",
    "human toxicity: non-carcinogenic no LT",
    "land use no LT",
    "ozone depletion no LT",
    "particulate matter formation no LT",
    "water use no LT"
]

# Match selected categories to methods in the database
matched_categories = []
for category in selected_categories:
    matches = [method for method in bd.methods if category in method[1]]
    if matches:
        matched_categories.append(matches[0])  # Take the first match if multiple exist

# Multi-LCA
config = {
    "impact_categories": matched_categories,
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
    clean_impact_category = re.sub(r"no LT", "", impact_hierarchy[1]).strip().title()#
    if impact_hierarchy in matched_categories:  # Only include matched categories
        records.append({
            'Functional Unit': functional_unit,
            'Impact Category': clean_impact_category,
            'Score': value
        })

df_scores = pd.DataFrame(records)
df_pivot = df_scores.pivot(index='Functional Unit', columns='Impact Category', values='Score')
df_pivot = df_pivot.sort_index(axis=1)
print(df_pivot)

# Normalize results relative to the maximum score of each impact category
df_relative = df_pivot.div(df_pivot.max(axis=0), axis=1) * 100

# Export the filtered and relative results to an Excel file
with pd.ExcelWriter("data//Filtered_MultiLCA_selected_categories.xlsx") as writer:
    # Write all absolute results grouped by Impact Category in "Filtered Results" sheet
    df_scores.to_excel(writer, sheet_name="Filtered Results", index=False)

    # Write relative results to a separate sheet
    df_relative.to_excel(writer, sheet_name="Relative Results", index=True)

    # Write each functional unit's absolute results to its own sheet
    for functional_unit in df_scores['Functional Unit'].unique():
        df_subset = df_scores[df_scores['Functional Unit'] == functional_unit]
        df_subset.to_excel(writer, sheet_name=functional_unit, index=False)

# Plot normalized results
df_relative.T.plot(kind='barh', figsize=(12, 8))
plt.xlabel('Relative Impact (%)')
plt.title('Relative Impact Categories per Functional Unit')
plt.legend(title='Functional Units', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("plots//filtered_multilca_impact_categories_per_functional_unit_selected_categories.png", dpi=300, bbox_inches='tight')
plt.show()
