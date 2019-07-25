from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_110X_design_step2' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.psetName = 'singleMuonGun_110X_design_cfi_RAW2DIGI_RECO.py'
config.JobType.pluginName = 'Analysis'



config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/singleMuonGun_10_1_0_pre3_realistic_ideal_22p5M_2018_ideal_step1/rymuelle-crab_singleMuonGun_10_1_0_pre3_ideal_22p5M_2018_ideal_step1-04eefdff102d9d646f7587d5d4b04f2f/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 5000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.publishDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'singleMuonGun_10_1_0_pre3_realistic_ideal_22p5M_2018_ideal_step2_ALCARECO'
config.Data.publication = True
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
