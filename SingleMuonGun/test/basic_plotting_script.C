#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "TTree.h"

void basic_plotting_script()
{

//inilize variables
bool printTTree = false; //warning, prints a lot of stuff

//these will be used in later loacations. It's nice to use variables or constants rather than numbers when coding for clarity
int nXbins = 200;
int minPt = 30;
int maxPt = 500;
int canvasWidth = 600;
int canvasHeight = 600;
int nEntries;

//This will be a variable we will read from the TTree later. Malachi, you will need to add more of these. Hint: look at the output from myTTree->Print();
Float_t sta_pt;
Float_t glb_pt;
Float_t glb_eta;

//This sets up the files to write later on
TFile * outputFile = new TFile("rootOutput.root", "recreate");
TDirectory * outputDir = outputFile->mkdir("outputFileDirectory");

//This sets up the hisograms to write later on. Has to be made after the TFile above to write to it. Malachi, you will need to add more TH1F's and TH2F's.
TCanvas * myCanvas = new TCanvas("name", "title", canvasWidth, canvasHeight);
TH1F * exampleHistogram = new TH1F("histo_name", "histo title e.g. Dimuon standalone pT", nXbins, minPt, maxPt);
TH1F * th1f_pt = new TH1F("th1f_pt", "th1f_pt", nXbins, minPt, maxPt);
TH1F * th1f_eta = new TH1F("th1f_eta", "th1f_eta", nXbins, -3, 3);


//open the file containing the TTree and print what is in the file
//TFile *myFile = new TFile("refit_MC_3DOF_DT_misaligned_FIDT0fix_out.root");
TFile *myFile = new TFile("FINALFILE_DT3DOF_CSC3DOF_02.root");
std::cout << "\n --- Contents of myFile: ---" << std::endl;
myFile->ls();
std::cout << "\n";

//load the TTree from the file
TDirectory *myTDirectory = (TDirectory*)myFile->Get("muAlAnalyzer");
std::cout << "--- Contents of myTDirectory: ---" << std::endl;
myTDirectory->ls();
std::cout << "\n";

//TTree *myTTree = (TTree*)myTDirectory->Get("recoDimuons");
TTree *myTTree = (TTree*)myTDirectory->Get("recoMuons");
nEntries = myTTree->GetEntries();
if ( printTTree )
{
    std::cout << "--- Contents of myTTree: ---" << std::endl;
    myTTree->Print();
    std::cout << "\n";
}

//get the branches from the ttree we are interested in. Malachi, you will need one of these for each variable we want to read from above.
myTTree->SetBranchAddress("sta_pt",&sta_pt);
myTTree->SetBranchAddress("glb_pt",&glb_pt);
myTTree->SetBranchAddress("glb_eta",&glb_eta);

//outputDir->cd();

//loop over the events and fill the histogram
for ( int i = 0; i < nEntries; i++)
{
    myTTree->GetEntry(i);
    //fills the histogram. Malachi, you will need to fill each histogram defined above here
    exampleHistogram->Fill(sta_pt);
    if(glb_pt >30 and glb_pt < 500){
        th1f_pt->Fill(glb_pt);
        th1f_eta->Fill(glb_eta);
        th1f_eta->Fill(-glb_eta);
    }
}

//draw histogram and save as an image. Malachi, you will need to add these 2 lines for each histogram defined above to save it as an image.
th1f_pt->Draw();
th1f_eta->Fit("pol4","", "", -2,2);
th1f_eta->Draw();
myCanvas->SaveAs("th1f_eta.png");
th1f_eta->Smooth(200);
th1f_eta->Draw();
myCanvas->SaveAs("th1f_eta_smooth.png");
exampleHistogram->Draw();
myCanvas->SaveAs("exampleHistogram.png");


//th1f_pt->Scale(1.0/(th1f_pt->GetEntries()));
//for(int i =1; i < 203; i++){
//    std::cout << th1f_eta->GetBinContent(i) <<", ";

//}
//
double bin_length = 3.0/100;
double bin_value;
for(int i =0; i < 200; i++){
    bin_length = 3.0/100.0;
    bin_value = (i-100.0)*bin_length+.015;
    std::cout << 82021-8648.43*bin_value*bin_value << ", "; 
}


//write file
outputFile->Write();
delete outputFile;

}
