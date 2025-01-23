#Import of Brightway to build coding-enviroment.
import bw2io as bi
FILEPATH = "lca-epe-databases.tar.gz"
bi.restore_project_directory(fp=FILEPATH, project_name="LCA_EPE", overwrite_existing=True)

#imports brightway packages
import bw2data as bd  # for everything related to the database
import bw2calc as bc  # for the actual LCA calculations
import bw2analyzer as bwa

#Lists all projects and then sets current project as LCA_EPE
bd.projects  # if this list does not include LCA_EPE, please take another look at the welcome.ipynb notebook
bd.projects.set_current("LCA_EPE")
#del bd.databases["project_af"]
print(bd.databases)

#del bd.databases["project_af"]

#Import of bio- and technosphere.
eidb = bd.Database("ecoinvent-3.10-cutoff")
bsdb = bd.Database("ecoinvent-3.10-biosphere")

project_af = bd.Database('project_af')
data = {}  # we start with no data, so data is empty
project_af.write(data)
bd.Database('project_af').metadata['depends'] = ['ecoinvent-3.10-biosphere',
  'ecoinvent-3.10-cutoff',
  'ei310_IMAGE_SSP2_RCP26_2035',
  'ei310_IMAGE_SSP2_RCP26_2050']

print(bd.databases)
print(bd.Database('project_af').metadata)