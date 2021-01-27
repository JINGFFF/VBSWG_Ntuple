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
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/06D08F8C-FBC2-E811-AC7B-0090FAA57460.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/188BD0F9-F8C2-E811-9D89-AC1F6B0DE2AA.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/1CD85304-F7C2-E811-930C-F02FA768CC54.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/245E647C-EFC2-E811-BB95-A0369FD0B124.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/2CF92A46-DAC2-E811-B202-AC1F6B0DE34C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/2EBE1EFA-CFC2-E811-96B1-0090FAA57FA4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/324AC4F3-72C3-E811-BC22-0090FAA57FA4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/4AA6FF06-BAC3-E811-922A-48D539F38630.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/4CC4C56F-CFBE-E811-B9BE-0090FAA58824.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/4CFB763D-38C3-E811-B8FA-0090FAA57FA4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/50A3E5B0-96BD-E811-9E04-F02FA768CB4A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/5C12B4CF-C3C3-E811-85F8-A0369FE2C148.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/5E17E67C-D4C2-E811-A778-0090FAA57460.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/60B9E56E-CFBE-E811-80ED-48FD8E2824A9.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/64115F8D-86C3-E811-B561-F02FA768CC54.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/726B9A73-CFBE-E811-84EB-48D539F3863E.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/7817B622-62C3-E811-BA4F-AC1F6B0DE340.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/784907E2-D4C2-E811-85B5-AC1F6B0DE2F4.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/7C1543DF-1AC4-E811-8C11-A0369FD0B330.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/7C31B769-5BC3-E811-B99C-48FD8EE739AD.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/80C6A494-FAC2-E811-B42C-AC1F6B0DE224.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/8417DEE3-F9C2-E811-A221-48FD8EE739AD.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/9042840A-E2C2-E811-BA9E-48FD8E2824C9.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/9685ED39-F1C2-E811-9908-AC1F6B0DE340.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/96E6A490-DCC2-E811-AE76-F02FA78BAFA8.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/A2BE4B85-A8BD-E811-9B86-48FD8EE739B5.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/A81CFCCB-FCC2-E811-8DB0-0090FAA57FA4.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/A8E4835E-B0C3-E811-B401-48D539F38546.root",
"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/ACA6787C-D3C2-E811-BD4F-AC1F6B0F676A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/B2134918-ADC3-E811-B452-0090FAA57FA4.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/C0107655-D3C3-E811-99BF-F02FA768CC54.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/C216FA5E-DAC2-E811-A284-AC1F6B0DE3F8.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/C824A88D-CBC2-E811-A04E-AC1F6B0DE340.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E46F702B-3AC3-E811-8BFD-AC1F6B0F676A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E49590B0-F6C2-E811-8EC7-AC1F6B0F676A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E4DE2015-B3C3-E811-92C1-AC1F6B0DE340.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E4F19147-DAC2-E811-AF07-AC1F6B0DE4A8.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E675A702-F2C2-E811-B382-F02FA768CF8A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E6C43BC6-30C4-E811-B906-48FD8E282979.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/E80938EE-CFC3-E811-862E-AC1F6B0F676A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/EABDE2D7-3AC3-E811-B629-F02FA768CF8A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/00000/EEB14BB1-AFC3-E811-9B99-48FD8EE739A9.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/06C7CC15-5DBD-E811-9794-0090FAA58274.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/0A02812C-62BD-E811-9662-48FD8EE73ACD.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/40720903-5DBD-E811-9C9F-A0369FE2C210.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/62186448-5EBD-E811-B23D-A0369FD0B29E.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/6C428014-60BD-E811-9CF2-AC1F6B0DE4A6.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/74155A32-60BD-E811-899C-AC1F6B0DE22A.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/7A4F3855-60BD-E811-BFFA-0090FAA57B20.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/A47FB22D-63BD-E811-AA6E-A0369FD0B142.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/AE380934-5CBD-E811-93C0-A0369FE2C042.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/B43F7D44-5CBD-E811-AD51-A0369FD0B12C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/B48EEE2C-63BD-E811-8F56-0090FAA57C20.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/BC215A21-A9BD-E811-B244-0CC47A4D9A1E.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/C0683B58-5FBD-E811-A00A-48FD8EE739B1.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/C88510AA-63BD-E811-891F-48D539F38672.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/DA13CC37-5CBD-E811-872C-AC1F6B0DE45C.root",
#"/store/mc/RunIISummer16MiniAODv3/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/270000/F097B2B6-5CBD-E811-90EA-AC1F6B0DE2AA.root"
]

process.maxEvents.input = -1  #-1
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.cerr.FwkReport.limit = 99999999

process.TFileService = cms.Service("TFileService",
									fileName = cms.string("/eos/user/j/jipeng/2016_ST_tbarW_treePKU2.root")
									)
