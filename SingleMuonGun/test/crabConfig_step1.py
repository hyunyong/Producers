from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_110X_2021_design_step1' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_110X_design_cfi_GEN_SIM_DIGI_L1_DIGI2RAW.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2500
NJOBS = 5000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = 'singleMuonGun_110X_2021_design_step1'
config.Data.publication = True
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign/hyunyong/singleMuonGun_110X_2021_design_step1'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
