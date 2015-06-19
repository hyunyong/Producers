#
# Event Content definition for Muon Alignment samples
#

import FWCore.ParameterSet.Config as cms

# Generic CMSSW Event Content definitions
from Configuration.EventContent.EventContent_cff import *

# Define empty RAWSIM event content
MuAl_RAWSIMEventContent = cms.PSet(
  outputCommands = cms.untracked.vstring('drop *'),
  splitLevel = cms.untracked.int32(0),
  eventAutoFlushCompressedSize=cms.untracked.int32(5*1024*1024)
)

# Extend  RAWSIM event content following definition in Configuration/EventContent/python/EventContent_cff.py
# Note, collections not required for Muon Alignmnet are commented out to reduce event size
MuAl_RAWSIMEventContent.outputCommands.extend(RAWEventContent.outputCommands)        # Generic RAW collections inside. Defined in Configuration/EventContent/python/EventContentCosmics_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimG4CoreRAW.outputCommands)           # Sim tracks and vertexes collections inside. Defined in SimG4Core/Configuration/python/SimG4Core_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimTrackerRAW.outputCommands)          # Tracker collections inside. Defined in SimTracker/Configuration/python/SimTracker_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimMuonRAW.outputCommands)             # CSC, DT and RPD collections inside. Defined in SimMuon/Configuration/python/SimMuon_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(SimCalorimetryRAW.outputCommands)     # Calorimeter collections inside. Defined in SimCalorimetry/Configuration/python/SimCalorimetry_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(SimGeneralRAW.outputCommands)          # Several collections inside. Something for pile up? Defined in SimGeneral/Configuration/python/SimGeneral_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(GeneratorInterfaceRAW.outputCommands)  # Generator collections inside. Defined in GeneratorInterface/Configuration/python/GeneratorInterface_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(RecoGenJetsFEVT.outputCommands)       # GenJets collections inside. Defined in RecoJets/Configuration/python/RecoJets_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(RecoGenMETFEVT.outputCommands)        # GenMET collections inside. Defined in RecoMET/Configuration/python/RecoMET_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(DigiToRawFEVT.outputCommands)          # Two collections inside. Defined in 'EventFilter/Configuration/python/DigiToRaw_EventContent_cff.py'
#MuAl_RAWSIMEventContent.outputCommands.extend(MEtoEDMConverterFEVT.outputCommands)  # Only one collection inside 'MEtoEDMConverter'. Defined in DQMOffline/Configuration/python/DQMOffline_EventContent_cff.py
#MuAl_RAWSIMEventContent.outputCommands.extend(IOMCRAW.outputCommands)               # Only one HUGE collection inside 'randomEngineStateProducer'. Defined in IOMC/RandomEngine/python/IOMC_EventContent_cff.py
MuAl_RAWSIMEventContent.outputCommands.extend(CommonEventContent.outputCommands)     # Only one collection inside 'logErrorHarvester'. Something for pile up? Defined in Configuration/EventContent/python/EventContent_cff.py


