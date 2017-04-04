from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CRAB3_singleMuonGun_FullRECO_CMSSW_8_0_24_ZPrimeToMuMu_m_5000_raw2reco_RECOSIM_3' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_RECO.py'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_ME_1_3_17.py'
#config.JobType.psetName = 'singleMuonGun_V2_cfi_DT_0_4_11.py'
#config.JobType.psetName = 'singleMuonGun_13TeV_realistic.py'
config.JobType.psetName = 'reco_RAW2DIGI_RECO.py'


config.section_("Data")
config.Data.splitting = 'FileBased'
#config.Data.inputDataset = '/ZprimeToMuMu_M-5000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16DR80Premix-PUMoriond17RAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/RAWAODSIM'
config.Data.inputDataset = '/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/Fall13dr-tsg_PU20bx25_POSTLS162_V2-v1/GEN-SIM-RAW'
#config.Data.inputDataset = '/ZprimeToMuMu_M-5000_TuneCUETP8M1_13TeV-pythia8/RunIISpring16DR80-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/RAWAODSIM'
#config.Data.inputDataset = '/ZprimeToMuMu_M-5000_TuneCUETP8M1_13TeV-pythia8/RunIISummer16DR80Premix-PUMoriond17RAW_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/GEN-SIM-RAW'
#config.Data.inputDataset = '/ZprimeToMuMu_M-5000_TuneCUETP8M1_13TeV-pythia8/RunIISpring16DR80-PU2016_Classic_withHLT_80X_mcRun2_asymptotic_v14-v1/GEN-SIM-RAW'
#config.Data.unitsPerJob = 45000 # 22 percent succedded 77.6 percent failed- wall time
config.Data.unitsPerJob = 1
NJOBS = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publishDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'CRAB3_singleMuonGun_FullRECO_CMSSW_8_0_24_ZPrimeToMuMu_m_5000_raw2reco' #name here'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_singleMuonGun_FullRECO_CMSSW_8_0_24_ZPrimeToMuMu_m_5000_raw2reco_RECOSIM' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
