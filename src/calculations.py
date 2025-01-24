import bw2data as bd
import bw2calc as bc
import pandas as pd

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
for m in list(climate_change_categories):
    lcabev = bc.LCA(fu, m)

    lcabev.lci()
    lcabev.lcia()
    lcabev.score

    results = []
    for exc in jet_fuel_all.technosphere():  # search for all technosphere exchanges in the "transport, passenger car, electric" process
        lcabev.redo_lcia(
            {exc.input.id: exc['amount']})  # Redo lca for each technosphere exchanges with the corresponding amount
        results.append(
            (lcabev.score, exc.input['reference product']))  # Create list with GHG-emissions and exchange name

    results.sort(reverse=True)  # sort results in descending order

    # write results in pandas datafrane
    df = pd.DataFrame.from_dict(results)
    df.columns = [m, 'Exchange']
    print(df)

