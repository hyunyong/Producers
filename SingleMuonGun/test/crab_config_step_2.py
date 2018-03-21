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
config.Data.inputDataset = '/singleMuonGun_94X_phase1_design_2017_design_22p5M_step1/lpernie-crab_singleMuonGun_94X_phase1_design_2017_design_22p5M_step1-48e4db3006d93c4af28df7e92adbd116/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 100
config.Data.publication = False
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ["T2_AT_Vienna","T2_BE_IIHE","T2_BE_UCL", "T2_BR_SPRACE", "T2_BR_UERJ", "T2_CH_CERN", "T2_CH_CERN_AI", "T2_CH_CERN_HLT",  "T2_CH_CSCS", "T2_CH_CSCS_HPC", "T2_CN_Beijing", "T2_DE_DESY", "T2_DE_RWTH", "T2_EE_Estonia", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_FI_HIP", "T2_FR_CCIN2P3", "T2_FR_GRIF_IRFU", "T2_FR_GRIF_LLR", "T2_FR_IPHC", "T2_GR_Ioannina", "T2_HU_Budapest", "T2_IN_TIFR", "T2_IT_Bari", "T2_IT_Legnaro", "T2_IT_Pisa", "T2_IT_Rome", "T2_KR_KISTI", "T2_KR_KNU", "T2_MY_UPM_BIRUNI", "T2_PK_NCP", "T2_PL_Swierk", "T2_PL_Warsaw", "T2_PT_NCG_Lisbon", "T2_RU_IHEP", "T2_RU_INR", "T2_RU_ITEP", "T2_RU_JINR", "T2_RU_PNPI", "T2_RU_SINP", "T2_TH_CUNSTDA", "T2_TR_METU", "T2_TW_NCHC", "T2_UA_KIPT", "T2_UK_London_Brunel", "T2_UK_London_IC", "T2_UK_SGrid_Bristol", "T2_UK_SGrid_RALPP"]
config.Site.whitelist = ["T2_*"]
config.Site.blacklist = ["T2_US_*"]
