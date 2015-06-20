import FWCore.ParameterSet.Config as cms 

generator = cms.EDProducer("SingleMuonGun",
  Verbosity = cms.untracked.int32(0),
  ConstPt_eq_MinPt = cms.bool(False),
  MinPt  = cms.double(30.0),
  MaxPt  = cms.double(200.0),
  MinEta = cms.double(-1.4),
  MaxEta = cms.double(1.4),
  MinPhi = cms.double(-3.14159265359),
  MaxPhi = cms.double(3.14159265359)
)
