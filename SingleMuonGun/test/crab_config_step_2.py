from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_94X_phase1_design_2017_design_22p5M_step2' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.psetName = 'step2_singleMuonGun_94X_phase1_2017_design_RAW2DIGI_RECO.py'
config.JobType.pluginName = 'Analysis'



config.section_("Data")
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '<sample here>'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
