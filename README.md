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


