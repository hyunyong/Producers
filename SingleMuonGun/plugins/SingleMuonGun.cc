// -*- C++ -*-
//
// Package:    SingleMuonGun
// Class:      SingleMuonGun
// 
/**\class SingleMuonGun SingleMuonGun.cc SingleMuonGun/src/SingleMuonGun.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Yuriy Pakhotin,,,
//         Created:  Sat Apr 11 12:15:53 CDT 2015
//
//

// system include files
#include <string>
#include <ostream>
#include <iostream>
#include <memory>
#include "boost/shared_ptr.hpp"

// user include files
#include "HepPDT/defs.h"
#include "HepPDT/TableBuilder.hh"
#include "HepPDT/ParticleDataTable.hh"

#include "HepMC/GenEvent.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include <TFile.h>
#include <TH2F.h>
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "SimGeneral/HepPDTRecord/interface/ParticleDataTable.h"

#include <TRandom3.h>
#include "CLHEP/Random/RandFlat.h"
#include "CLHEP/Random/RandGeneral.h"

using namespace edm;
using namespace std;
using namespace CLHEP;

//
// class declaration
//

class SingleMuonGun : public edm::EDProducer {
  public:
    explicit SingleMuonGun(const edm::ParameterSet&);
    ~SingleMuonGun();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
  private:
    virtual void beginJob() override;
    virtual void produce(edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    
    virtual void beginRun(edm::Run&, edm::EventSetup const&);
    virtual void endRun(edm::Run&, edm::EventSetup const&);
      
  // ----------member data ---------------------------
  
  // the event format itself
  HepMC::GenEvent* m_Evt;
  //file 
  TFile *f; 
  TFile *eta_distributions;

  // parameters
  int    m_Verbosity;
  int    m_partID;
  int    m_charge;
  bool   m_mirror_eta;
  bool   m_ConstPt_eq_MinPt;
  bool   m_Run1_distribution;
  double m_minPt;
  double m_maxPt;
  double m_minEta;
  double m_maxEta;
  double m_minPhi;
  double m_maxPhi;
  
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SingleMuonGun::SingleMuonGun(const edm::ParameterSet& iConfig)
  : m_Evt(0)
  , m_Verbosity(        iConfig.getUntrackedParameter<int>( "Verbosity",0 ) )
  , m_mirror_eta(       iConfig.getParameter<bool>("mirror_eta") )
  , m_ConstPt_eq_MinPt( iConfig.getParameter<bool>("ConstPt_eq_MinPt") )
  , m_Run1_distribution( iConfig.getParameter<bool>("Run1_distribution") )
  , m_minPt(            iConfig.getParameter<double>("MinPt") )
  , m_maxPt(            iConfig.getParameter<double>("MaxPt") )
  , m_minEta(           iConfig.getParameter<double>("MinEta") )
  , m_maxEta(           iConfig.getParameter<double>("MaxEta") )
  , m_minPhi(           iConfig.getParameter<double>("MinPhi") )
  , m_maxPhi(           iConfig.getParameter<double>("MaxPhi") )
{
  
  //f = new TFile("/afs/cern.ch/work/r/rymuelle/public/test_74Producer/CMSSW_7_4_6_patch3/src/Producers/SingleMuonGun/test/pt_v_eta_rebin.root", "READ");
  //eta_distributions = new TFile("/afs/cern.ch/work/r/rymuelle/public/74Producers/beamspot_fix/CMSSW_7_4_6_patch3/src/Producers/SingleMuonGun/test/eta_distribution.root", "READ");

  Service<RandomNumberGenerator> rng;
  if(!rng.isAvailable()) {
    throw cms::Exception("Configuration")
      << "The RandomNumberProducer module requires the RandomNumberGeneratorService\n"
         "which appears to be absent. Please add that service to your configuration\n"
         "or remove the modules that require it.";
  }

  produces<HepMCProduct>();
  produces<GenEventInfoProduct>();
  produces<GenRunInfoProduct, InRun>();
   
}


SingleMuonGun::~SingleMuonGun()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//


// ------------ method called once each job just before starting event loop  ------------
void 
SingleMuonGun::beginJob()
{
}


// ------------ method called on each new Event  ------------
void SingleMuonGun::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  edm::Service<edm::RandomNumberGenerator> rng;
  CLHEP::HepRandomEngine* engine = &rng->getEngine(iEvent.streamID());
  
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Begin New Event Generation" << endl;
  
  m_Evt = new HepMC::GenEvent();
  
  HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.0322161,-1.10814e-05, -0.0146611) );
  
  
  double muon_sign_double = CLHEP::RandFlat::shoot(engine, -1.0, 1.0) ;
  if ( muon_sign_double < 0 ) {
    m_partID = -13;
    m_charge =   1;
  } else {
    m_partID = 13;
    m_charge = -1;
  }
  m_charge = -1; 
  double pt;
  double eta; 
  double random_number;
  int nBins = 200;
  double ptPDF [] = {388659, 429532, 470100, 519630, 568477, 590070, 532182, 386678, 264139, 187921, 140145, 109196, 87042, 70803, 58433, 48816, 41722, 35575, 30516, 26303, 22942, 20080, 17891, 15540, 13877, 12564, 10914, 9906, 8635, 8003, 7137, 6648, 5957, 5433, 4781, 4474, 4012, 3780, 3371, 3105, 2715, 2634, 2489, 2273, 2137, 1987, 1742, 1645, 1517, 1378, 1295, 1159, 1187, 980, 987, 920, 887, 804, 731, 673, 656, 665, 557, 530, 547, 510, 434, 465, 417, 367, 385, 356, 316, 298, 290, 285, 246, 229, 262, 207, 212, 203, 194, 160, 150, 178, 147, 150, 146, 126, 140, 122, 104, 116, 113, 98, 94, 108, 79, 85, 87, 75, 84, 64, 64, 57, 60, 60, 64, 66, 45, 42, 49, 35, 49, 48, 34, 50, 43, 42, 42, 28, 36, 30, 24, 17, 24, 28, 23, 25, 22, 22, 23, 23, 22, 12, 17, 14, 17, 14, 13, 21, 17, 8, 13, 9, 8, 12, 20, 12, 9, 12, 9, 6, 12, 8, 7, 8, 10, 9, 7, 8, 8, 5, 11, 8, 7, 8, 10, 10, 2, 2, 4, 6, 6, 14, 5, 3, 4, 7, 4, 5, 4, 8, 2, 6, 4, 1, 2, 2, 2, 1, 2, 6, 2, 4, 3, 2, 0, 1}; 

  double etaPDF [] = {4961.54, 6502.69, 8028.28, 9538.29, 11032.7, 12511.6, 13974.9, 15422.7, 16854.9, 18271.5, 19672.5, 21058, 22427.9, 23782.3, 25121, 26444.2, 27751.9, 29044, 30320.5, 31581.4, 32826.8, 34056.6, 35270.8, 36469.5, 37652.6, 38820.1, 39972.1, 41108.5, 42229.4, 43334.6, 44424.3, 45498.5, 46557, 47600, 48627.5, 49639.3, 50635.6, 51616.4, 52581.5, 53531.1, 54465.2, 55383.6, 56286.5, 57173.8, 58045.6, 58901.8, 59742.4, 60567.5, 61377, 62170.9, 62949.3, 63712.1, 64459.3, 65190.9, 65907, 66607.6, 67292.5, 67961.9, 68615.7, 69254, 69876.7, 70483.8, 71075.3, 71651.3, 72211.7, 72756.6, 73285.9, 73799.6, 74297.7, 74780.3, 75247.3, 75698.8, 76134.7, 76555, 76959.7, 77348.9, 77722.5, 78080.6, 78423, 78749.9, 79061.3, 79357.1, 79637.3, 79901.9, 80151, 80384.5, 80602.4, 80804.8, 80991.6, 81162.9, 81318.5, 81458.6, 81583.2, 81692.1, 81785.5, 81863.4, 81925.7, 81972.4, 82003.5, 82019.1, 82019.1, 82003.5, 81972.4, 81925.7, 81863.4, 81785.5, 81692.1, 81583.2, 81458.6, 81318.5, 81162.9, 80991.6, 80804.8, 80602.4, 80384.5, 80151, 79901.9, 79637.3, 79357.1, 79061.3, 78749.9, 78423, 78080.6, 77722.5, 77348.9, 76959.7, 76555, 76134.7, 75698.8, 75247.3, 74780.3, 74297.7, 73799.6, 73285.9, 72756.6, 72211.7, 71651.3, 71075.3, 70483.8, 69876.7, 69254, 68615.7, 67961.9, 67292.5, 66607.6, 65907, 65190.9, 64459.3, 63712.1, 62949.3, 62170.9, 61377, 60567.5, 59742.4, 58901.8, 58045.6, 57173.8, 56286.5, 55383.6, 54465.2, 53531.1, 52581.5, 51616.4, 50635.6, 49639.3, 48627.5, 47600, 46557, 45498.5, 44424.3, 43334.6, 42229.4, 41108.5, 39972.1, 38820.1, 37652.6, 36469.5, 35270.8, 34056.6, 32826.8, 31581.4, 30320.5, 29044, 27751.9, 26444.2, 25121, 23782.3, 22427.9, 21058, 19672.5, 18271.5, 16854.9, 15422.7, 13974.9, 12511.6, 11032.7, 9538.29, 8028.28, 6502.69, 4961.54};

  //double etaLowPDF [] = {0, 0, 0, 3085.7133385, 4123.35957864, 5101.41022519, 6022.30734849, 6888.43875062, 7702.13796546, 8465.68425865, 9181.30262759, 9851.16380146, 10477.3842412, 11062.0261396, 11607.097421, 12114.5517419, 12586.2884901, 13024.1527855, 13429.9354796, 13805.3731559, 14152.1481294, 14471.888447, 14766.1678874, 15036.5059609, 15284.3679098, 15511.1647081, 15718.2530615, 15906.9354075, 16078.4599153, 16234.0204861, 16374.7567526, 16501.7540795, 16616.043563, 16718.6020314, 16810.3520445, 16892.1618939, 16964.8456033, 17029.1629276, 17085.819354, 17135.4661012, 17178.7001198, 17216.0640919, 17248.0464317, 17275.081285, 17297.5485294, 17315.7737743, 17330.0283609, 17340.529362, 17347.4395823, 17350.8675584, 17350.8675584, 17347.4395823, 17340.529362, 17330.0283609, 17315.7737743, 17297.5485294, 17275.081285, 17248.0464317, 17216.0640919, 17178.7001198, 17135.4661012, 17085.819354, 17029.1629276, 16964.8456033, 16892.1618939, 16810.3520445, 16718.6020314, 16616.043563, 16501.7540795, 16374.7567526, 16234.0204861, 16078.4599153, 15906.9354075, 15718.2530615, 15511.1647081, 15284.3679098, 15036.5059609, 14766.1678874, 14471.888447, 14152.1481294, 13805.3731559, 13429.9354796, 13024.1527855, 12586.2884901, 12114.5517419, 11607.097421, 11062.0261396, 10477.3842412, 9851.16380146, 9181.30262759, 8465.68425865, 7702.13796546, 6888.43875062, 6022.30734849, 5101.41022519, 4123.35957864, 3085.7133385, 0, 0, 0};

//double etaHighPDF [] ={0, 0, 0, 1563.50252667, 1551.62893947, 1550.39456133, 1559.11492495, 1577.12077339, 1603.7580601, 1638.38794892, 1680.38681409, 1729.14624021, 1784.07302227, 1844.58916565, 1910.13188611, 1980.15360981, 2054.12197328, 2131.51982344, 2211.84521758, 2294.61142339, 2379.34691896, 2465.59539272, 2552.91574354, 2640.88208062, 2729.08372359, 2817.12520244, 2904.62625755, 2991.22183969, 3076.56211, 3160.31244002, 3242.15341168, 3321.78081727, 3398.90565949, 3473.2541514, 3544.56771648, 3612.60298855, 3677.13181186, 3737.94124102, 3794.83354101, 3847.62618723, 3896.15186544, 3940.2584718, 3979.80911284, 4014.68210548, 4044.77097703, 4069.98446518, 4090.24651802, 4105.49629399, 4115.68816194, 4120.79170111, 4120.79170111, 4115.68816194, 4105.49629399, 4090.24651802, 4069.98446518, 4044.77097703, 4014.68210548, 3979.80911284, 3940.2584718, 3896.15186544, 3847.62618723, 3794.83354101, 3737.94124102, 3677.13181186, 3612.60298855, 3544.56771648, 3473.2541514, 3398.90565949, 3321.78081727, 3242.15341168, 3160.31244002, 3076.56211, 2991.22183969, 2904.62625755, 2817.12520244, 2729.08372359, 2640.88208062, 2552.91574354, 2465.59539272, 2379.34691896, 2294.61142339, 2211.84521758, 2131.51982344, 2054.12197328, 1980.15360981, 1910.13188611, 1844.58916565, 1784.07302227, 1729.14624021, 1680.38681409, 1638.38794892, 1603.7580601, 1577.12077339, 1559.11492495, 1550.39456133, 1551.62893947, 1563.50252667, 0, 0, 0};

  if ( m_ConstPt_eq_MinPt == true ) {
    // Gun with constant pT of muons
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with constant pT of muons" << endl;
    pt = m_minPt;
    eta = CLHEP::RandFlat::shoot(engine, m_minEta, m_maxEta);

  } else if (m_Run1_distribution == false) {
  // Gun with pT spectrum of muons as in 2012 data
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with pT spectrum of muons as in 2015 data (13TeV)" << endl;
//    TFile *f = new TFile("/afs/cern.ch/work/r/rymuelle/public/74Producers/beamspot_fix/CMSSW_7_4_6_patch3/src/Producers/SingleMuonGun/test/MC_distribution.root", "READ");
//    TFile *eta_distributions = new TFile("/afs/cern.ch/work/r/rymuelle/public/74Producers/beamspot_fix/CMSSW_7_4_6_patch3/src/Producers/SingleMuonGun/test/eta_distribution.root", "READ");

    //TFile *f = new TFile("/afs/cern.ch/work/r/rymuelle/public/test_74Producer/CMSSW_7_4_6_patch3/src/Producers/SingleMuonGun/test/pt_v_eta_rebin.root", "READ");
    //
//    TH2F *MC_distribution = (TH2F*)f->Get("pt_v_eta_mc");
//    MC_distribution->GetRandom2(pt, eta);
//    TH1F *eta_distribution_0to45 = (TH1F*)eta_distributions->Get("etaDistribution_0to45");
//    TRandom3 *r = new TRandom3();
//    r->SetSeed(0);
//    eta = eta_distribution_0to45->GetRandom();
//    std::cout << pt << " " << eta << std::endl;
////
    //TH1F *eta_distribution_45to250 = (TH1F*)eta_distributions->Get("etaDistribution_45to250");
    RandGeneral ptDistribution(ptPDF,nBins);
    RandGeneral etaDistribution(etaPDF,nBins);
    //RandGeneral etaLowDistribution(etaLowPDF,nBins);
    //RandGeneral etaHighDistribution(etaHighPDF,nBins);
    pt = ptDistribution.shoot(engine);
    eta = 0;
    //std::cout << " pt: " << pt << std::endl;

    pt = pt*(500.0-30.0)+30.0;
    //pt  = 500.0/200*(pt);


//    if ( pt < 45){
//        //eta = CLHEP::RandFlat::shoot(engine, 0, 1);
//    //    eta = eta_distribution_0to45->GetRandom();
//        //std::cout <<     eta_distribution_0to45->GetEntries() << std::endl;
//        eta = etaLowDistribution.shoot(); 
//    }else if ( pt > 45){
//        eta = etaHighDistribution.shoot(); 
//        //eta = CLHEP::RandFlat::shoot(engine, 0, 1);
//    //    eta = eta_distribution_45to250->GetRandom();
//        //std::cout <<     eta_distribution_45to250->GetRandom() << std::endl;
//    }


    eta = etaDistribution.shoot(engine);
    //eta = eta*200;
    eta = (eta-.5)*6.0;
    //eta = 3.0/100.0*(float(eta)-(float(100)/2.0)+.5);
    //std::cout << CLHEP::RandFlat::shoot(engine, 0, 1) << std::endl;
    //std::cout << pt << " 13 TeV " << eta << std::endl;
    random_number = CLHEP::RandFlat::shoot(engine, 0, 1); 

    if ( m_Verbosity >= 10 ) cout << "Run 2: " << eta << " " << pt <<std::endl;
  //std::cout << random_number << std::endl;
    if ( random_number < .5){
        eta = eta*-1;
    }


  } else if (m_Run1_distribution == true) {
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with pT spectrum of muons as in 2012 data" << endl;

    double pt_bin_probability = 0.0;
    while(1) {
      pt    = CLHEP::RandFlat::shoot(engine, m_minPt, m_maxPt);
      pt_bin_probability = CLHEP::RandFlat::shoot(engine, 0.0, 0.46684); // simulate pT spectrum of muons as in 2012 data
      if (pt >= 30.0  && pt < 40.0  && pt_bin_probability < 0.46684     ) break;
      if (pt >= 40.0  && pt < 50.0  && pt_bin_probability < 0.3498604   ) break;
      if (pt >= 50.0  && pt < 60.0  && pt_bin_probability < 0.09976921  ) break;
      if (pt >= 60.0  && pt < 70.0  && pt_bin_probability < 0.03986568  ) break;
      if (pt >= 70.0  && pt < 80.0  && pt_bin_probability < 0.0186057   ) break;
      if (pt >= 80.0  && pt < 90.0  && pt_bin_probability < 0.009773275 ) break;
      if (pt >= 90.0  && pt < 100.0 && pt_bin_probability < 0.0055456   ) break;
      if (pt >= 100.0 && pt < 110.0 && pt_bin_probability < 0.003377719 ) break;
      if (pt >= 110.0 && pt < 120.0 && pt_bin_probability < 0.002205957 ) break;
      if (pt >= 120.0 && pt < 130.0 && pt_bin_probability < 0.001352316 ) break;
      if (pt >= 130.0 && pt < 140.0 && pt_bin_probability < 0.0008818916) break;
      if (pt >= 140.0 && pt < 150.0 && pt_bin_probability < 0.0006362394) break;
      if (pt >= 150.0 && pt < 160.0 && pt_bin_probability < 0.0004544567) break;
      if (pt >= 160.0 && pt < 170.0 && pt_bin_probability < 0.0002898697) break;
      if (pt >= 170.0 && pt < 180.0 && pt_bin_probability < 0.0002481088) break;
      if (pt >= 180.0 && pt < 190.0 && pt_bin_probability < 0.0001658153) break;
      if (pt >= 190.0 && pt < 200.0 && pt_bin_probability < 0.0001277392) break;
    }
    eta = CLHEP::RandFlat::shoot(engine, m_minEta, m_maxEta);

    //std::cout << pt << " 8 TeV " << eta << std::endl;
  }
  
    //std::cout << "pt" << pt << " eta " << eta << std::endl;
  double phi = CLHEP::RandFlat::shoot(engine, m_minPhi, m_maxPhi);
  
  double muon_eta_sign_double = CLHEP::RandFlat::shoot(engine, -1.0, 1.0);
    
  if (muon_eta_sign_double < 0 and m_mirror_eta == true) eta *= -1;
  if ( m_Verbosity >= 20 ) cout << " SingleMuonGunProducer : muon ID = " << m_partID << " q = " << m_charge << " pT = " << pt << " eta = " << eta << " phi = " << phi << endl;
     
  //eta = 0;
  //pt=50;
 // phi = -1.80;
  double mass    = 0.1056583715;
  double theta   = 2.*atan(exp(-eta));
  double mom     = pt/sin(theta);
  double px      = pt*cos(phi);
  double py      = pt*sin(phi);
  double pz      = mom*cos(theta);
  double energy2 = mom*mom + mass*mass;
  double energy  = sqrt(energy2); 
  HepMC::FourVector p(px,py,pz,energy);
  HepMC::GenParticle* Part = new HepMC::GenParticle(p,m_partID,1);
  Part->suggest_barcode( 1 ) ;
  Vtx->add_particle_out(Part);
  
  m_Evt->add_vertex(Vtx) ;
  m_Evt->set_event_number(iEvent.id().event()) ;
  m_Evt->set_signal_process_id(20) ; 
  
  if ( m_Verbosity >= 30 ) m_Evt->print() ;  
  
  auto_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
  BProduct->addHepMCData( m_Evt );
  iEvent.put(BProduct);

  auto_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(m_Evt));
  iEvent.put(genEventInfo);
  
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Event Generation Done" << endl;

}


// ------------ method called once each job just after ending the event loop  ------------
void 
SingleMuonGun::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void 
SingleMuonGun::beginRun(edm::Run& iRun, edm::EventSetup const& iSetup)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SingleMuonGun::endRun(edm::Run& iRun, edm::EventSetup const& iSetup)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SingleMuonGun::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SingleMuonGun);
