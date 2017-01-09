import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("SingleMuonGun",
  Verbosity = cms.untracked.int32(30),  # 1  - print begin and end of event
                                       # 10 - print type of gun (constant or spectrum)
                                       # 20 - print muon parameters (q, pt, eta, phi)
                                       # 30 - print CMSSW event info
  # IMPORTANT! *****************************************************************
  ConstPt_eq_MinPt = cms.bool(True), # if TRUE  then generate muons with CONSTANT pT = MinPt
                                      # if FALSE then generate muons with pT spectrum of muons as in 2012 dat    a (hardcoded in SingleMuonGun/plugins/SingleMuonGun.cc)
  Run1_distribution = cms.bool(True), # use technique used in run 1
  mirror_eta = cms.bool(True),       # mirror eta, turn off to only produce muons on one side of the detector
  # ****************************************************************************
  MinPt  = cms.double(20.0),
  #MinPt  = cms.double(20.0),
  MaxPt  = cms.double(200.0),
  MinEta = cms.double(-2.5),
  MaxEta = cms.double(2.5),
 # MaxEta = cms.double(-.8),
  MinPhi = cms.double(-3.14159265359),
  MaxPhi = cms.double(3.14159265359)
)

#generator = cms.EDProducer("FlatRandomPtGunProducer",
#    PGunParameters = cms.PSet(
#        MaxPt = cms.double(10.01),
#        MinPt = cms.double(9.99),
#        PartID = cms.vint32(-13),
#        MaxEta = cms.double(2.5),
#        MaxPhi = cms.double(3.14159265359),
#        MinEta = cms.double(-2.5),
#        MinPhi = cms.double(-3.14159265359) ## in radians
#
#    ),
#    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
#
#    psethack = cms.string('single mu pt 10'),
#    AddAntiParticle = cms.bool(True),
#    firstRun = cms.untracked.uint32(1)
#)
