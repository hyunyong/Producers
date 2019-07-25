# Producers

##Setup crab3
```bash
source /cvmfs/cms.cern.ch/crab3/crab.sh 
```
##GEM 2021 Geometry Single Muon Gun
```bash
scram p -n gemSingleMuon CMSSW CMSSW_11_0_0_pre3
cd gemSingleMuon/src
cmsenv
git clone git@github.com:hyunyong/Producers.git -b GEM2021_CMSSW_11_0_0_pre3
scram b -j8
cd Producers/SingleMuonGun/test
crab submit -c crabConfig_step1.py
```
##crab config
config.Data.outLFNDirBase = '/store/group/lpcgem/singleMuonGun_110X_2021_design_step1'
config.Site.storageSite = 'T3_US_FNALLPC'
