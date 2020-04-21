from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_1102_phase1_2021_realistic_step1' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_1102_phase1_2021_realistic_cfi_GEN_SIM_DIGI_L1_DIGI2RAW.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = 'singleMuonGun_1102_phase1_2021_realistic_step1'
config.Data.publication = True
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/user/hyunyong/singleMuonGun_1102_phase1_2021_realistic'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_KR_KISTI'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
