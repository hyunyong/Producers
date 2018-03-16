# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleMuPt10_pythia8_cfi --conditions auto:phase1_2017_design -n 10 --eventcontent RECOSIM -s GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,RECO --datatier GEN-SIM-RAW-RECO --era Run2_2017 --beamspot GaussSigmaZ4cm --geometry DB:Extended --fileout file:step1.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedGaussSigmaZ4cm_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleMuGun'),
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

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = outputEventContent,
    splitLevel = cms.untracked.int32(0)
)



# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_design', '')

process.generator = cms.EDProducer("SingleMuonGun",
  Verbosity = cms.untracked.int32(0),  # 1  - print begin and end of event
                                       # 10 - print type of gun (constant or spectrum)
                                       # 20 - print muon parameters (q, pt, eta, phi)
                                       # 30 - print CMSSW event info
  # IMPORTANT! *****************************************************************
  ConstPt_eq_MinPt = cms.bool(False), # if TRUE  then generate muons with CONSTANT pT = MinPt
                                      # if FALSE then generate muons with pT spectrum of muons as in 2012 data (hardcoded in SingleMuonGun/plugins/SingleMuonGun.cc)
  # ****************************************************************************
  MinPt  = cms.double(1000.0),
  MaxPt  = cms.double(200.0),
  MinEta = cms.double(-2.5),
  MaxEta = cms.double(2.5),
  MinPhi = cms.double(-3.14159265359),
  MaxPhi = cms.double(3.14159265359)
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
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
