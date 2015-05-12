from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_FullRECO_CMSSW_7_3_5_DESRUN2_73_V3_5M_v1'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_RECO.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.publishDataName = 'CRAB3_singleMuonGun_FullRECO_CMSSW_7_3_5_DESRUN2_73_V3_5M_v1'
config.Data.outLFN = '/store/user/[BRAZOS_USERNAME]/'

config.section_("Site")
config.Site.storageSite = 'T3_US_TAMU'
