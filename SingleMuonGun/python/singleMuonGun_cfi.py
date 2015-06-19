import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("SingleMuonGun",
  Verbosity = cms.untracked.int32(0),  # 1  - print begin and end of event
                                       # 10 - print type of gun (constant or spectrum)
                                       # 20 - print muon parameters (q, pt, eta, phi)
                                       # 30 - print CMSSW event info
  # IMPORTANT! *****************************************************************
  ConstPt_eq_MinPt = cms.bool(False), # if TRUE  then generate muons with CONSTANT pT = MinPt
                                      # if FALSE then generate muons with pT spectrum of muons as in 2012 data (hardcoded in SingleMuonGun/plugins/SingleMuonGun.cc)
  # ****************************************************************************
  MinPt  = cms.double(30.0),
  MaxPt  = cms.double(200.0),
  MinEta = cms.double(-2.5),
  MaxEta = cms.double(2.5),
  MinPhi = cms.double(-3.14159265359),
  MaxPhi = cms.double(3.14159265359)
)
