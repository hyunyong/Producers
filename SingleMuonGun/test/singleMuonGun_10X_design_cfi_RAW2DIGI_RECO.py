# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase1_2018_design -n 10 --eventcontent RECOSIM -s RAW2DIGI,RECO --datatier RECO --era Run2_2018 --beamspot GaussSigmaZ4cm --geometry DB:Extended --fileout file:step2.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('singleMuongun step 2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

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

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = outputEventContent,
    splitLevel = cms.untracked.int32(0)
)


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_design', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
