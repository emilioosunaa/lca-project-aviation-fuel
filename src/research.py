#imports brightway packages
import bw2data as bd  # for everything related to the database

#Sets current project as LCA_EPE
bd.projects.set_current("LCA_EPE")

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")
project_af = bd.Database("project_af")


input_plant = eidb.get(name="synthetic fuel production, from coal, high temperature Fisher-Tropsch operations", location="ZA")

