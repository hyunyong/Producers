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

#include "FWCore/Framework/interface/Frameworkfwd.h" // works in CMSSW_5_3_X
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

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

#include "CLHEP/Random/RandFlat.h"

using namespace edm;
using namespace std;
using namespace CLHEP;

namespace {
  CLHEP::HepRandomEngine& getEngineReference()
  {

    Service<RandomNumberGenerator> rng;
    if(!rng.isAvailable()) {
      throw cms::Exception("Configuration")
       << "The RandomNumberProducer module requires the RandomNumberGeneratorService\n"
          "which appears to be absent.  Please add that service to your configuration\n"
          "or remove the modules that require it.";
    }
    // The Service has already instantiated an engine.  Make contact with it.
    return (rng->getEngine());
  }
}

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

  CLHEP::HepRandomEngine& m_RandomEngine;
  CLHEP::RandFlat*        m_RandomGenerator;

  // parameters
  int    m_Verbosity;
  int    m_partID;
  int    m_charge;
  bool   m_ConstPt_eq_MinPt;
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
  , m_RandomEngine( getEngineReference() )
  , m_RandomGenerator(0)
  , m_Verbosity(        iConfig.getUntrackedParameter<int>( "Verbosity",0 ) )
  , m_ConstPt_eq_MinPt( iConfig.getParameter<bool>("ConstPt_eq_MinPt") )
  , m_minPt(            iConfig.getParameter<double>("MinPt") )
  , m_maxPt(            iConfig.getParameter<double>("MaxPt") )
  , m_minEta(           iConfig.getParameter<double>("MinEta") )
  , m_maxEta(           iConfig.getParameter<double>("MaxEta") )
  , m_minPhi(           iConfig.getParameter<double>("MinPhi") )
  , m_maxPhi(           iConfig.getParameter<double>("MaxPhi") )
{
  
  m_RandomGenerator = new CLHEP::RandFlat(m_RandomEngine);

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

// ------------ method called on each new Event  ------------
void SingleMuonGun::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Begin New Event Generation" << endl;
  
  m_Evt = new HepMC::GenEvent();
  
  HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.,0.,0.) );
  
  double muon_sign_double = m_RandomGenerator->fire(-1.0,  1.0);
  if ( muon_sign_double < 0 ) {
    m_partID = -13;
    m_charge =   1;
  } else {
    m_partID = 13;
    m_charge = -1;
  }
  
  double pt;
  
  if ( m_ConstPt_eq_MinPt == true ) {
    // Gun with constant pT of muons
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with constant pT of muons" << endl;
    pt = m_minPt;
  } else {
  // Gun with pT spectrum of muons as in 2012 data
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with pT spectrum of muons as in 2012 data" << endl;
    double pt_bin_probability = 0.0;
    while(1) {
      pt    = m_RandomGenerator->fire(m_minPt,  m_maxPt);
      pt_bin_probability = m_RandomGenerator->fire(0.0, 0.46684); // simulate pT spectrum of muons as in 2012 data
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
  }
  
  double eta = m_RandomGenerator->fire(m_minEta, m_maxEta);
  double phi = m_RandomGenerator->fire(m_minPhi, m_maxPhi);
  
  if ( m_Verbosity >= 20 ) cout << " SingleMuonGunProducer : muon ID = " << m_partID << " q = " << m_charge << " pT = " << pt << " eta = " << eta << " phi = " << phi << endl;
  
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

// ------------ method called once each job just before starting event loop  ------------
void 
SingleMuonGun::beginJob()
{
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
