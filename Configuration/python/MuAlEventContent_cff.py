#
# Event Content definition for Muon Alignment samples
#

import FWCore.ParameterSet.Config as cms

# Generic CMSSW Event Content definitions
from Configuration.EventContent.EventContent_cff import *

################################################################################
#                                   RAWSIM                                      
################################################################################

# Define empty RAWSIM event content
MuAl_RAWSIMEventContent = cms.PSet(
  outputCommands = cms.untracked.vstring('drop *'),
  splitLevel = cms.untracked.int32(0),
  eventAutoFlushCompressedSize=cms.untracked.int32(5*1024*1024)
)

# Extend  RAWSIM event content following definition of RAWSIMEventContent in Configuration/EventContent/python/EventContent_cff.py
#  - collections not required for Muon Alignmnet are commented out to reduce event size
MuAl_RAWSIMEventContent.outputCommands.extend(RAWEventContent.outputCommands)        # Generic RAW collections. Defined in Configuration/EventContent/python/EventContentCosmics_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimG4CoreRAW.outputCommands)           # Sim tracks and vertexes collections. Defined in SimG4Core/Configuration/python/SimG4Core_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimTrackerRAW.outputCommands)          # Tracker collections. Defined in SimTracker/Configuration/python/SimTracker_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimMuonRAW.outputCommands)             # CSC, DT and RPD collections. Defined in SimMuon/Configuration/python/SimMuon_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(SimCalorimetryRAW.outputCommands)     # Calorimeter collections. Defined in SimCalorimetry/Configuration/python/SimCalorimetry_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimGeneralRAW.outputCommands)          # Several collections. Something for pile up? Defined in SimGeneral/Configuration/python/SimGeneral_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(GeneratorInterfaceRAW.outputCommands)  # Generator collections. Defined in GeneratorInterface/Configuration/python/GeneratorInterface_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(RecoGenJetsFEVT.outputCommands)       # GenJets collections. Defined in RecoJets/Configuration/python/RecoJets_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(RecoGenMETFEVT.outputCommands)        # GenMET collections. Defined in RecoMET/Configuration/python/RecoMET_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(DigiToRawFEVT.outputCommands)          # Two collections. Defined in 'EventFilter/Configuration/python/DigiToRaw_EventContent_cff.py'
#MuAl_RAWSIMEventContent.outputCommands.extend(MEtoEDMConverterFEVT.outputCommands)  # Only one collection 'MEtoEDMConverter'. Defined in DQMOffline/Configuration/python/DQMOffline_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(IOMCRAW.outputCommands)               # Only one HUGE collection 'randomEngineStateProducer'. Defined in IOMC/RandomEngine/python/IOMC_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(CommonEventContent.outputCommands)     # Only one collection 'logErrorHarvester'. Something for pile up? Defined in Configuration/EventContent/python/EventContent_cff.py

################################################################################
#                                   RECO                                        
################################################################################

# Define empty RECO event content following definition of RECOEventContent in Configuration/EventContent/python/EventContent_cff.py
MuAl_RECOEventContent = cms.PSet(
  outputCommands = cms.untracked.vstring('drop *'),
  splitLevel = cms.untracked.int32(0),
  eventAutoFlushCompressedSize=cms.untracked.int32(5*1024*1024)
)

# Extend  RECO event content following definition of RECOEventContent in Configuration/EventContent/python/EventContent_cff.py
#  - collections not required for Muon Alignmnet are commented out to reduce event size
MuAl_RECOEventContent.outputCommands.extend(RecoLocalTrackerRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(RecoLocalMuonRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoLocalCaloRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoEcalRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(TrackingToolsRECO.outputCommands)     # Collections for electron tracks. Defined in TrackingTools/Configuration/python/TrackingTools_EventContent_cff.py
MuAl_RECOEventContent.outputCommands.extend(RecoTrackerRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoJetsRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoMETRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(RecoMuonRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoBTauRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoBTagRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoTauTagRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(RecoVertexRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoEgammaRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(RecoPixelVertexingRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(RecoParticleFlowRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(BeamSpotRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(L1TriggerRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(HLTriggerRECO.outputCommands)
#MuAl_RECOEventContent.outputCommands.extend(MEtoEDMConverterRECO.outputCommands)
MuAl_RECOEventContent.outputCommands.extend(EvtScalersRECO.outputCommands)        # Collections 'L1AcceptBunchCrossings', 'DcsStatuss', etc. Defined in EventFilter/ScalersRawToDigi/python/Scalers_EventContent_cff.py
MuAl_RECOEventContent.outputCommands.extend(CommonEventContent.outputCommands)

################################################################################
#                                   RECOSIM                                     
################################################################################

# Define empty RECOSIM event content following definition of RECOSIMEventContent in Configuration/EventContent/python/EventContent_cff.py
MuAl_RECOSIMEventContent = cms.PSet(
  outputCommands = cms.untracked.vstring('drop *'),
  splitLevel = cms.untracked.int32(0),
  eventAutoFlushCompressedSize=cms.untracked.int32(5*1024*1024)
)

# Extend  RECOSIM event content following definition of RECOEventContent in Configuration/EventContent/python/EventContent_cff.py
#  - collections not required for Muon Alignmnet are commented out to reduce event size
MuAl_RECOSIMEventContent.outputCommands.extend(MuAl_RECOSIMEventContent.outputCommands)
MuAl_RECOSIMEventContent.outputCommands.extend(GeneratorInterfaceRECO.outputCommands)
#MuAl_RECOSIMEventContent.outputCommands.extend(RecoGenMETRECO.outputCommands)
#MuAl_RECOSIMEventContent.outputCommands.extend(RecoGenJetsRECO.outputCommands)
MuAl_RECOSIMEventContent.outputCommands.extend(SimG4CoreRECO.outputCommands)
MuAl_RECOSIMEventContent.outputCommands.extend(SimTrackerRECO.outputCommands)
MuAl_RECOSIMEventContent.outputCommands.extend(SimMuonRECO.outputCommands)
#MuAl_RECOSIMEventContent.outputCommands.extend(SimCalorimetryRECO.outputCommands)
MuAl_RECOSIMEventContent.outputCommands.extend(SimGeneralRECO.outputCommands)
#MuAl_RECOSIMEventContent.outputCommands.extend(MEtoEDMConverterRECO.outputCommands)

