# Producers

In order to generate the single muon gun sample there are several steps to follow:

1) First - check out this package into an appropriate CMSSW release (73X), cmsenv, compile.

2) Setup crab & voms: 
source /cvmfs/cms.cern.ch/crab3/crab.sh 
voms-proxy-init -voms cms -valid 192:00

3) You can switch between full and filtered output via a flag in here:
Producers/SingleMuonGun/test/singleMuonGun_RECO.py

4) Configure the number of events to be generated and the path for the output here:
Producers/SingleMuonGun/test/crabConfig.py

5) From inside the Producers/SingleMuonGun/test/ directory you can submit the jobs via the command 'crab submit'


Instructions for producing single muon.py file for new releases:

Get singleMuon.Py file from CMSSW-> e.g. SingleMuPt10_cfi.py

Run e.g. cmsDriver.py SingleMuPt10_cfi.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --conditions auto:run2_mc --eventcontent RECO --datatier RECO -n 10 --no_exec --pileup=NoPileUp

works: cmsDriver.py SingleMuPt10_cfi.py --conditions auto:mc -n 800 --datatier GEN-SIM-RECO -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,RAW2DIGI,L1Reco,RECO --fileout file:SingleMuPt10_cfi.root --no_exec

