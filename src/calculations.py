import bw2data as bd
import bw2calc as bc
import bw2analyzer as bwa
import pandas as pd
import seaborn as sns

# Import databases
bd.projects.set_current("LCA_EPE")
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

# Definition of the functional unit
jet_fuel_all = project_af.get(name='jet fuel production, all processes')
fu = {jet_fuel_all:1}

# Definition of the impact categories
climate_change_categories = [met for met in bd.methods if 'EF v3.1 no LT' in str(met)]
chosen_methods = climate_change_categories

# Single-LCA
contribution_analysis_results = []
supply_chain_analysis_results = []

# Perform LCA for each impact category
for category in climate_change_categories:
    lca = bc.LCA(fu, category)
    lca.lci()
    lca.lcia()
    total_score = lca.score

    # -------- Supply Chain Analysis --------
    ca = bwa.ContributionAnalysis()
    top_processes = ca.annotated_top_processes(lca, limit=10)
    for process in top_processes:
        supply_chain_analysis_results.append({
            "Category": category,
            "Score": process[0],
            "Process": process[2]["name"],
        })

    # -------- Contribution Analysis --------
    category_results = []
    for exchange in jet_fuel_all.technosphere():
        lca.redo_lcia({exchange.input.id: exchange['amount']})
        category_results.append({
            "Category": category,
            "Score": lca.score,
            "Exchange": exchange.input['reference product'],
            "Contribution": lca.score / total_score * 100 if total_score else 0,
        })

    contribution_analysis_results.extend(category_results)

# Convert results to DataFrames for better reporting
df_contribution_analysis = pd.DataFrame(contribution_analysis_results)
df_supply_chain_analysis = pd.DataFrame(supply_chain_analysis_results)
df_contribution_analysis.to_csv("data\\contribution_analysis_results.csv", index=False)
df_supply_chain_analysis.to_csv("data\\supply_chain_analysis_results.csv", index=False)