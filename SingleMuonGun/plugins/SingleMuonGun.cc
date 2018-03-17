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

#include "TRandom.h"
#include "TF2.h"

#include "CLHEP/Random/RandFlat.h"

using namespace edm;
using namespace std;
using namespace CLHEP;

//
// class declaration
//

class SingleMuonGun : public edm::one::EDProducer<edm::one::SharedResources> { //understand <> better 
  public:
    explicit SingleMuonGun(const edm::ParameterSet&);
    ~SingleMuonGun();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
  private:
    virtual void beginJob() override;
    virtual void produce( edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    
    virtual void beginRun(edm::Run&, edm::EventSetup const&);
    virtual void endRun(edm::Run&, edm::EventSetup const&);
      
  // ----------member data ---------------------------
  
  // the event format itself
  HepMC::GenEvent* m_Evt; 
  
  // parameters
  int    m_Verbosity;
  bool   m_ConstPt_eq_MinPt;
  double m_minPt;
  double m_maxPt;
  double m_minEta;
  double m_maxEta;
  double m_minPhi;
  double m_maxPhi;

  //const Int_t npar = 3;
  Double_t f2params[3] = {360.884, .0639069, .00437602 }; 
  TF2 *f2 =  new TF2("f2","[0]*exp(-([1]+[2]*y*y)*x)", 30, 250, -2.5, 2.5);

  int    m_partID;
  int    m_charge;
  double pt;
  double eta; 
  double phi; 
  double muon_sign_double;
  double muon_eta_sign_double;

 
  
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
  //: m_Evt(0)
  : m_Verbosity(        iConfig.getUntrackedParameter<int>( "Verbosity",0 ) )
  , m_ConstPt_eq_MinPt( iConfig.getParameter<bool>("ConstPt_eq_MinPt") )
  , m_minPt(            iConfig.getParameter<double>("MinPt") )
  , m_maxPt(            iConfig.getParameter<double>("MaxPt") )
  , m_minEta(           iConfig.getParameter<double>("MinEta") )
  , m_maxEta(           iConfig.getParameter<double>("MaxEta") )
  , m_minPhi(           iConfig.getParameter<double>("MinPhi") )
  , m_maxPhi(           iConfig.getParameter<double>("MaxPhi") )
{
  
  Service<RandomNumberGenerator> rng;
  if(!rng.isAvailable()) {
    throw cms::Exception("Configuration")
      << "The RandomNumberProducer module requires the RandomNumberGeneratorService\n"
         "which appears to be absent. Please add that service to your configuration\n"
         "or remove the modules that require it.";
  }

  produces<HepMCProduct>("unsmeared");
  produces<GenEventInfoProduct>();
  //produces<GenRunInfoProduct, InRun>();

  f2->SetParameters(f2params);
  f2->SetNpx(200);
  f2->SetNpy(200);


  usesResource("SingleMuonGun");
  
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
void SingleMuonGun::produce( edm::Event& iEvent, const edm::EventSetup& iSetup)  
{



  edm::Service<edm::RandomNumberGenerator> rng;
  CLHEP::HepRandomEngine* engine = &rng->getEngine(iEvent.streamID());

  gRandom->SetSeed(0);
  if ( m_Verbosity > 0 ) cout << " SingleMuonGunProducer : Begin New Event Generation" << endl;
  
  HepMC::GenEvent* m_Evt = new HepMC::GenEvent();
  
  //HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.0322161,-1.10814e-05, -0.0146611) );
  HepMC::GenVertex* Vtx = new HepMC::GenVertex( HepMC::FourVector(0.0, 0.0, 0.0) );
  
  muon_sign_double = CLHEP::RandFlat::shoot(engine, -1.0, 1.0) ;
  if ( muon_sign_double < 0 ) {
    m_partID = -13;
    m_charge =   1;
  } else {
    m_partID = 13;
    m_charge = -1;
  }
  
  eta = CLHEP::RandFlat::shoot(engine, m_minEta, m_maxEta);
  phi = CLHEP::RandFlat::shoot(engine, m_minPhi, m_maxPhi);
 
  muon_eta_sign_double = CLHEP::RandFlat::shoot(engine, -1.0, 1.0);
  
  if ( m_ConstPt_eq_MinPt == true ) {
    // Gun with constant pT of muons
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with constant pT of muons" << endl;
    pt = m_minPt;
  } else { 
    if ( m_Verbosity >= 10 ) cout << " SingleMuonGunProducer : Gun with simulated 13TeV (Run2)" << endl;
    

  
    f2->GetRandom2(pt,eta);
    if (muon_eta_sign_double < 0) eta *= -1;
  }

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

    unique_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
    BProduct->addHepMCData( m_Evt );
    iEvent.put(std::move(BProduct), "unsmeared");
  
    unique_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(m_Evt));
    iEvent.put(std::move(genEventInfo));
  //unique_ptr<HepMCProduct> BProduct(new HepMCProduct()) ;
  //BProduct->addHepMCData( m_Evt );
  //iEvent.put(std::move(BProduct));
//
  //unique_ptr<GenEventInfoProduct> genEventInfo(new GenEventInfoProduct(m_Evt));
  //iEvent.put(std::move(genEventInfo));
  
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
