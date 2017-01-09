# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Producers/Configuration/python/singleMuonGun_V2_cfi.py --mc -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO -n 10 --no_exec --conditions=auto:run2_mc --eventcontent RECO --pileup=NoPileUp --era Run2_25ns
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_25ns)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
#process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.VtxSmeared.src = cms.InputTag("generator")
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(40)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Producers/Configuration/python/singleMuonGun_V2_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)
# IMPORTANT! Define output event content ***************************************
fullRECO = False
if (fullRECO == True):
  print "WARNING! Output format: FULL RECO"
  outputEventContent = process.RECOEventContent.outputCommands
  oututFileName = cms.untracked.string('singleMuonGun_FullRECO.root')
else:
  print "WARNING! Output format: REDUCED RECO aka ALCARECO"
  oututFileName = cms.untracked.string('singleMuonGun_ReducedRECO.root')
  outputEventContent = cms.untracked.vstring('drop *',
      # Keep all type of muons
      'keep *_muons_*_*',
#      'keep *_muonsFromCosmics_*_*',
#      'keep *_muonsFromCosmics1Leg_*_*',
      # Keep general tracks
      'keep *_generalTracks_*_*',
      # Keep muon tracks
      'keep *_globalMuons_*_*',
      'keep *_standAloneMuons_*_*',
#      'keep *_refittedStandAloneMuons_*_*',
#      'keep *_displacedStandAloneMuons_*_*',
#      'keep *_standAloneSETMuons_*_*',
#`      'keep *_globalSETMuons_*_*',
#      'keep *_tevMuons_*_*',
#      'keep *_cosmicMuons_*_*',
#      'keep *_cosmicMuons1Leg_*_*',
#      'keep *_globalCosmicMuons_*_*',
#      'keep *_globalCosmicMuons1Leg_*_*',
      # Keep all muon hits information
      'keep *_muonCSCDigis_*_*',
      'keep *_muonDTDigis_*_*',
      'keep *_muonRPCDigis_*_*',
      'keep *_dt1DRecHits_*_*',
      'keep *_dt2DSegments_*_*',
      'keep *_dt4DSegments_*_*',
      'keep *_csc2DRecHits_*_*',
      'keep *_cscSegments_*_*',
      'keep *_rpcRecHits_*_*',
      # Keep tracker hits information
      'keep SiPixelClusteredmNewDetSetVector_siPixelClusters_*_*',
      'keep SiStripClusteredmNewDetSetVector_siStripClusters_*_*',
      # Keep trigger information
      'keep *_TriggerResults_*_*',
      'keep L1AcceptBunchCrossings_*_*_*',
      'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
      # Keep DCS information
      'keep DcsStatuss_scalersRawToDigi_*_*',
      # Keep beam spot and vertices
      'keep *_offlineBeamSpot_*_*',
      'keep *_offlinePrimaryVertices_*_*',
      # Keep generator level information
      'keep *_genParticles_*_*',
      'keep *_generator_*_*',
      'drop edmHepMCProduct_generator_*_*',
    )
# ******************************************************************************





# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    #fileName = cms.untracked.string('singleMuonGun_V2_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_RECO.root'),
    fileName = oututFileName,
    outputCommands = outputEventContent,
    #outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
#from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_design_v18::All', '')

process.generator = cms.EDProducer("SingleMuonGun",
    ConstPt_eq_MinPt = cms.bool(False),
    MaxEta = cms.double(2.6),
    MaxPhi = cms.double(3.14159265359),
    MaxPt = cms.double(500.0),
    MinEta = cms.double(-2.6),
    MinPhi = cms.double(-3.14159265359),
    MinPt = cms.double(30.0),
    Run1_distribution = cms.bool(False),
    Verbosity = cms.untracked.int32(11),
    mirror_eta = cms.bool(True)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)
#print process.paths
# End of customisation functions

