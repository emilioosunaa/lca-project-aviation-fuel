import bw2data as bd
import bw2calc as bc
import bw2io as bi
import bw2analyzer as bwa
import pandas as pd

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

fu = {jet_fuel_all:1}
functional_units = {
    "jet_fuel_fossil": {jet_fuel_fossil.id: 1},
    "jet_fuel_bio1": {jet_fuel_bio1.id: 1},
    "jet_fuel_bio2": {jet_fuel_bio2.id: 1},
    "jet_fuel_bio3": {jet_fuel_bio3.id: 1},
    "jet_fuel_co2": {jet_fuel_co2.id: 1},
}

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

# To-Do: improve the output of the Multi-LCA
print(mlca.scores)
