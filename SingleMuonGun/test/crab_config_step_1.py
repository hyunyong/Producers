from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_94X_phase1_design_2017_design_22p5M_step1' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_94X_phase1_2017_design_GEN_SIM_DIGI_L1_DIGI2RAW.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2500
NJOBS = 9000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outputPrimaryDataset = 'singleMuonGun_94X_phase1_design_2017_design_22p5M_step1'
config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
