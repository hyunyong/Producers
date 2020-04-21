from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_1102_phase1_2021_realistic_step2' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_1102_phase1_2021_realistic_cfi_RAW2DIGI_RECO.py'



config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/singleMuonGun_1102_phase1_2021_realistic_step1/XXX'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10000
NJOBS = 500
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.publishDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'singleMuonGun_10_1_0_pre3_realistic_ideal_22p5M_2018_ideal_step2_ALCARECO'
config.Data.publication = True
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/user/hyunyong/singleMuonGun_1102_phase1_2021_realistic'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_KR_KISTI'
#config.Site.storageSite = 'T2_CH_CERN'
