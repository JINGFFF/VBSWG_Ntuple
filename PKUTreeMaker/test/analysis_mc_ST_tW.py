import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),
				     SkipEvent = cms.untracked.vstring('ProductNotFound'))
corrJetsOnTheFly = True
runOnMC = True
chsorpuppi = True  # AK4Chs or AK4Puppi
#****************************************************************************************************#
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("RecoTracker.CkfPattern.CkfTrackCandidates_cff")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")

from Configuration.AlCa.GlobalTag import GlobalTag
if runOnMC:
	process.GlobalTag.globaltag = '102X_mcRun2_asymptotic_v8'
elif not(runOnMC):
	process.GlobalTag.globaltag = '102X_dataRun2_v13'

##########			                                                             
hltFiltersProcessName = 'RECO'
if runOnMC:
	hltFiltersProcessName = 'PAT' #'RECO'
reducedConversionsName = 'RECO'
if runOnMC:
	reducedConversionsName= 'PAT' #'RECO'

process.load("VAJets.PKUCommon.goodMuons_cff")
process.load("VAJets.PKUCommon.goodElectrons_cff")
process.load("VAJets.PKUCommon.goodPhotons_cff")
process.load("VAJets.PKUCommon.leptonicW_cff")
process.load("VAJets.PKUCommon.goodJets_cff")

#for egamma smearing
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
						runVID=True,
						runEnergyCorrections=False, #no point in re-running them, they are already fine
						era='2016-Legacy')  #era is new to select between 2016 / 2017,  it defaults to 2017
#for egamma smearing

# If Update
process.goodMuons.src = "slimmedMuons"
process.goodElectrons.src = "slimmedElectrons"
process.goodPhotons.src = "slimmedPhotons"
process.Wtoenu.MET  = "slimmedMETs"
process.Wtomunu.MET = "slimmedMETs"

# jerc uncer 2017/5/7
if chsorpuppi:
		jLabel = "slimmedJets"
		jetAlgo    = 'AK4PFchs'
else:
		jLabel = "slimmedJetsPuppi"
		jetAlgo    = 'AK4PFPuppi'

jer_era = "Summer16_07Aug2017_V11_MC"
triggerResultsLabel      = "TriggerResults"
triggerSummaryLabel      = "hltTriggerSummaryAOD"
hltProcess = "HLT"

if runOnMC:
	jecLevelsAK4chs = [
			'Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFchs.txt',
			'Summer16_07Aug2017_V11_MC_L2Relative_AK4PFchs.txt',
			'Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFchs.txt'
	]

	jecLevelsAK4puppi = [
			'Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFPuppi.txt',
			'Summer16_07Aug2017_V11_MC_L2Relative_AK4PFPuppi.txt',
			'Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFPuppi.txt'
	]
else:
	jecLevelsAK4chs = [
			'Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFchs.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFchs.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFchs.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFchs.txt'
	]

	jecLevelsAK4puppi = [
			'Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFPuppi.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFPuppi.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFPuppi.txt',
			'Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFPuppi.txt'
	]


process.JetUserData = cms.EDProducer(
	'JetUserData',
	jetLabel          = cms.InputTag(jLabel),
	rho               = cms.InputTag("fixedGridRhoFastjetAll"),
	coneSize          = cms.double(0.4),
	getJERFromTxt     = cms.bool(False),
	jetCorrLabel      = cms.string(jetAlgo),
	jerLabel          = cms.string(jetAlgo),
	resolutionsFile   = cms.string(jer_era+'_PtResolution_'+jetAlgo+'.txt'),
	scaleFactorsFile  = cms.string(jer_era+'_SF_'+jetAlgo+'.txt'),
	### TTRIGGER ###
	triggerResults = cms.InputTag(triggerResultsLabel,"",hltProcess),
	triggerSummary = cms.InputTag(triggerSummaryLabel,"",hltProcess),
	hltJetFilter       = cms.InputTag("hltPFHT"),
	hltPath            = cms.string("HLT_PFHT800"),
	hlt2reco_deltaRmax = cms.double(0.2),
	candSVTagInfos         = cms.string("pfInclusiveSecondaryVertexFinder"), 
	jecAK4chsPayloadNames_jetUserdata = cms.vstring( jecLevelsAK4chs ),
	vertex_jetUserdata = cms.InputTag("offlineSlimmedPrimaryVertices"),
	)

#jerc uncer Meng
process.load("VAJets.PKUCommon.goodJets_cff") 
if chsorpuppi:
	#process.goodAK4Jets.src = "slimmedJets"
	process.goodAK4Jets.src = "JetUserData"
else:
	process.goodAK4Jets.src = "slimmedJetsPuppi"
 
#process.goodOfflinePrimaryVertex = cms.EDFilter("VertexSelector",
#                                       src = cms.InputTag("offlineSlimmedPrimaryVertices"),
#                                       cut = cms.string("chi2!=0 && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0"),
#                                       filter = cms.bool(False)
#                                       )

WBOSONCUT = "pt > 0.0"

process.leptonicVSelector = cms.EDFilter("CandViewSelector",
										src = cms.InputTag("leptonicV"),
										cut = cms.string( WBOSONCUT ), 
										filter = cms.bool(False)
										)

process.leptonicVFilter = cms.EDFilter("CandViewCountFilter",
										src = cms.InputTag("leptonicV"),
										minNumber = cms.uint32(0),
										#filter = cms.bool(False)
										)


process.leptonSequence = cms.Sequence(process.muSequence +
										process.egammaPostRecoSeq*#process.slimmedElectrons*process.slimmedPhotons+
										process.eleSequence +
										process.leptonicVSequence +
										process.leptonicVSelector +
										process.leptonicVFilter )

process.jetSequence = cms.Sequence(process.NJetsSequence)


process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
process.load("RecoMET.METFilters.BadChargedCandidateFilter_cfi")
process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
process.metfilterSequence = cms.Sequence(process.BadPFMuonFilter+process.BadChargedCandidateFilter)

if chsorpuppi:
	ak4jecsrc = jecLevelsAK4chs
else:
	ak4jecsrc = jecLevelsAK4puppi

process.load("RecoEgamma/PhotonIdentification/photonIDValueMapProducer_cff")
#from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD 
## Example 1: If you only want to re-correct MET and get the proper uncertainties [e.g. when updating JEC]
#runMetCorAndUncFromMiniAOD(process,
#                           isData=False,
#                           )
   
# L1 prefiring
from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
	DataEra = cms.string("2016BtoH"), #Use 2016BtoH for 2016
	UseJetEMPt = cms.bool(False),
	PrefiringRateSystematicUncty = cms.double(0.2),
	SkipWarnings = False)

process.treeDumper = cms.EDAnalyzer("PKUTreeMaker",
									originalNEvents = cms.int32(1),
									crossSectionPb = cms.double(1),
									targetLumiInvPb = cms.double(1.0),
									PKUChannel = cms.string("VW_CHANNEL"),
									isGen = cms.bool(False),
									RunOnMC = cms.bool(runOnMC), 
									generator =  cms.InputTag("generator"),
									genJet =  cms.InputTag("slimmedGenJets"),
									lhe =  cms.InputTag("externalLHEProducer"),  #for multiple weight
									pileup  =   cms.InputTag("slimmedAddPileupInfo"),  
									leptonicVSrc = cms.InputTag("leptonicV"),
									rho = cms.InputTag("fixedGridRhoFastjetAll"),   
									ak4jetsSrc = cms.InputTag("cleanAK4Jets"),      
									#photonSrc = cms.InputTag("goodPhotons"),
									photonSrc = cms.InputTag("slimmedPhotons"),
									genSrc =  cms.InputTag("prunedGenParticles"),  
									jecAK4chsPayloadNames = cms.vstring( jecLevelsAK4chs ),
									jecAK4PayloadNames = cms.vstring( ak4jecsrc ),
									metSrc = cms.InputTag("slimmedMETs"),
									vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
									t1jetSrc_user = cms.InputTag("JetUserData"),
									t1jetSrc = cms.InputTag("slimmedJets"),      
									t1muSrc = cms.InputTag("slimmedMuons"),       
									looseelectronSrc = cms.InputTag("vetoElectrons"),
									electrons = cms.InputTag("slimmedElectrons"),
									conversions = cms.InputTag("reducedEgamma","reducedConversions",reducedConversionsName),
									beamSpot = cms.InputTag("offlineBeamSpot","","RECO"),
									loosemuonSrc = cms.InputTag("looseMuons"),

									goodmuonSrc = cms.InputTag("goodMuons"),
									goodeleSrc = cms.InputTag("goodElectrons"),

									hltToken    = cms.InputTag("TriggerResults","","HLT"),
									elPaths1     = cms.vstring("HLT_Ele23_WPTight_Gsf_v*"),
									elPaths2     = cms.vstring("HLT_Ele27_WPTight_Gsf_v*"),
									muPaths1     = cms.vstring("HLT_IsoMu20_v*","HLT_IsoTkMu20_v*"),
									muPaths2     = cms.vstring("HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"),
									muPaths3     = cms.vstring("HLT_IsoMu27_v*","HLT_IsoTkMu27_v*"),
				    				
									noiseFilter = cms.InputTag('TriggerResults','', hltFiltersProcessName),
									noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
									noiseFilterSelection_HBHENoiseIsoFilter = cms.string("Flag_HBHENoiseIsoFilter"),
									noiseFilterSelection_globalTightHaloFilter = cms.string('Flag_globalTightHalo2016Filter'),
									noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
									noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
									noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
									noiseFilterSelection_badMuon = cms.InputTag('BadPFMuonFilter'),
									
									noiseFilterSelection_badChargedHadron = cms.InputTag('BadChargedCandidateFilter'),
									full5x5SigmaIEtaIEtaMap   = cms.InputTag("photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta"),
									phoChargedIsolation = cms.InputTag("photonIDValueMapProducer:phoChargedIsolation"),
									phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer:phoNeutralHadronIsolation"),
									phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),
									effAreaChHadFile = cms.FileInPath("RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt"),
									effAreaNeuHadFile= cms.FileInPath("RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt"),
									effAreaPhoFile   = cms.FileInPath("RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt")
                                    )

process.analysis = cms.Path(
							process.JetUserData +
							process.leptonSequence +
							process.jetSequence +
							process.metfilterSequence + #*process.treeDumper)
							process.prefiringweight*process.treeDumper)

### Source
process.load("VAJets.PKUCommon.data.RSGravitonToWW_kMpl01_M_1000_Tune4C_13TeV_pythia8")
process.source.fileNames = [
#"root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E6440217-0405-E811-8404-A0369F7F8E80.root "
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/0C8C71F6-4DC2-E811-838D-0025901C1B7E.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/0E6B3A73-54C2-E811-81D0-0CC47AB3608C.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/22451B8B-54C2-E811-8E7A-0CC47AB35D34.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/2661BD7B-6FC2-E811-AD8F-0CC47AB36142.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/266CF065-24C2-E811-8DEC-0CC47AB35C3C.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/32D3D348-59C2-E811-8AE9-0CC47AB35F24.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/3E15B529-4EC2-E811-A2BC-0CC47AB35A82.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/44FAEA91-FCC1-E811-96DE-0CC47AB35DC0.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/463C6DE3-98C2-E811-A3C3-0025901D2940.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/68B6DBDF-E7C1-E811-8B87-0CC47AB35D34.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/6C784F0E-F3C1-E811-A7F2-0CC47AB35A82.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/9005CA48-55C2-E811-B234-0025901C187A.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/906E17F4-52C2-E811-B3EB-0CC47AB35C32.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/AEB2FB45-29C2-E811-BF53-0CC47AB35D34.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/C889E0E9-54C2-E811-B53A-0CC47AB35CC8.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/CEA6CA65-92BF-E811-9E15-0CC47AB35A82.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/E29E137A-F9C1-E811-A6EA-0CC47AB35EF0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/E2C673A2-F3C1-E811-A12C-0025901CFBCC.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/EAC34CEA-AEC2-E811-86D4-0025901D0126.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/FC44983D-4FBE-E811-BF3E-0CC47AB35F24.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/06E51F63-D8BF-E811-A6BE-0CC47AB3605A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/12D35494-08C1-E811-AFD7-0CC47AB3608C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/2431A38B-66C1-E811-9E8A-0CC47AB360C6.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/284EFAC2-63BF-E811-BD2D-003048C9A070.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/28BA38E1-86BF-E811-9873-0CC47AB360C6.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/2CC73D0F-82C1-E811-A86F-0CC47AB35C32.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/3A6DBF99-91BF-E811-AA8F-0CC47AB35CE8.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/3CF409F4-E4C0-E811-BFE6-0025901D293A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/405F50CE-3DBF-E811-9C0C-0CC47AB3605A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/48B1548C-83C1-E811-A18C-0CC47AB35A82.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/56EE13CD-C0C0-E811-80A9-0025901D2940.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5A5CBD16-5DBF-E811-AD6D-003048C9A070.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5A966EDF-1AC1-E811-B50B-0CC47AB35EF0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5C4B3D5D-91BF-E811-8906-0CC47AB35C66.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5E67B6A5-EDBF-E811-8B10-0CC47AB35DC0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/60F36A03-65C1-E811-B1D1-0CC47AB35EF0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/68FC34C3-1AC1-E811-92E1-0CC47AB35C3C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/6C4F0E6B-8ABF-E811-93E0-0025901D26F4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/6C939427-54BF-E811-829D-003048C9A070.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/6E0EE9BD-0EC0-E811-AB46-0CC47AB35C66.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7E5BA39D-C1C0-E811-B317-0CC47AB3608C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/886C1C5F-86BF-E811-A6FD-0CC47AB35DC0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/9496B156-73BF-E811-9AFA-0025901D0BA4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/980FF9B5-B8BF-E811-9BE3-0CC47AB360C6.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/983426A4-67C1-E811-9BC4-0CC47AB35C3C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/AA3E90B4-AABF-E811-BCB6-0CC47AB35CE8.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/AA60238B-32C0-E811-9EC9-0CC47AB3605A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/ACDBB68E-9CBF-E811-A986-0CC47AB3605A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/AE212A8B-83C1-E811-8757-0CC47AB35A82.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/B0ED2818-1BC1-E811-AC4D-0CC47AB360C6.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/B220DE50-86BF-E811-8B37-0CC47AB35CE8.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/BCC214F4-1CC1-E811-93B9-0025901D2940.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C44CDDBD-4DC1-E811-9F80-0025901D293A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C8BE1368-16C0-E811-9C14-0CC47AB36142.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CA6AEC75-B4BF-E811-BC03-0CC47AB35DC0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CEC8D235-4DBF-E811-A80D-0CC47AB35C3C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/D4E4B544-2ABF-E811-8F8A-0025901D012C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/DAE972D6-CABF-E811-9651-0CC47AB35C66.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F47AC68B-43C0-E811-9A4F-0CC47AB35DC0.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F6CF438E-4DC1-E811-89BC-0CC47AB3608C.root"
]

process.maxEvents.input = -1  #-1
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.cerr.FwkReport.limit = 99999999

process.TFileService = cms.Service("TFileService",
									fileName = cms.string("/eos/user/j/jipeng/2016_ST_tW_treePKU1.root")
									)
