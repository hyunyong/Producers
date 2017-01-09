from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_FullRECO_CMSSW_8_0_24_13_TeV_realistic_10M_v7' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_RECO.py'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_ME_1_3_17.py'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_DT_0_4_11.py'
config.JobType.psetName = 'singleMuonGun_13TeV_realistic.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 45000 # 22 percent succedded 77.6 percent failed- wall time
config.Data.unitsPerJob = 1000
NJOBS = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = 'CRAB3_singleMuonGun_FullRECO_CMSSW_8_0_24_13_TeV_realistic_10M_v7' #name here'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_singleMuonGun_FullRECO_CMSSW_8_0_24_13_TeV_realistic_10M_v7' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
