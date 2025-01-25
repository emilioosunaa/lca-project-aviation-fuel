import bw2io as bi
import bw2data as bd

FILEPATH = "lca-epe-databases.tar.gz"
bi.restore_project_directory(fp=FILEPATH, project_name="LCA_EPE", overwrite_existing=True)

#Lists all projects and then sets current project as LCA_EPE
bd.projects  # if this list does not include LCA_EPE, please take another look at the welcome.ipynb notebook
bd.projects.set_current("LCA_EPE")
print(bd.databases)

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