#imports brightway packages
import bw2data as bd  # for everything related to the database

#Sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")


input_plant = [act for act in eidb if 'hydrogen production, coal gasification' in act["name"] and "RoW" in act["location"]][0]

