#imports brightway packages
import bw2data as bd  # for everything related to the database
import bw2calc as bc  # for the actual LCA calculations
import bw2io as bi
import bw2analyzer as bwa
import pandas as pd

# sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

# import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")

# multi-LCA
aviationfuel_syngas = project_af.get(name='jet fuel production, all processes')

functional_units = {
    "aviation_fuel": {aviationfuel_syngas.id: 1}
}

fu = {aviationfuel_syngas:1}

climate_change_categories = [met for met in bd.methods if 'EF v3.1 no LT' in str(met)]
chosen_methods = climate_change_categories


config = {
    "impact_categories": chosen_methods,
}

data_objs = bd.get_multilca_data_objs(
    functional_units=functional_units, method_config=config
)

for m in list(climate_change_categories):
    lcabev = bc.LCA(fu, m)

    lcabev.lci()
    lcabev.lcia()
    lcabev.score

    results = []
    for exc in aviationfuel_syngas.technosphere():  # search for all technosphere exchanges in the "transport, passenger car, electric" process
        lcabev.redo_lcia(
            {exc.input.id: exc['amount']})  # Redo lca for each technosphere exchanges with the corresponding amount
        results.append(
            (lcabev.score, exc.input['reference product']))  # Create list with GHG-emissions and exchange name

    results.sort(reverse=True)  # sort results in descending order

    # write results in pandas datafrane
    df = pd.DataFrame.from_dict(results)
    df.columns = [m, 'Exchange']
    print(df)






# mlca = bc.MultiLCA(demands=functional_units, method_config=config, data_objs=data_objs)
# mlca.lci()
# mlca.lcia()

# print(mlca.scores)
