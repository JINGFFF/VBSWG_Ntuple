import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/20000/0056F0F4-4F44-E811-B415-FA163E5B5253.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.ChargeSignificanceTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ChargeSignificanceTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0)
)

process.CkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.CkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    updator = cms.string('KFUpdator')
)

process.CompositeTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet()
)

process.EmptyJetIdParams = cms.PSet(
    Pt010_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt010_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt010_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
)

process.GroupedCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.JetIdParams = cms.PSet(
    Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
    Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
    Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
    Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
    Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
    Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
    Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
    Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
    Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
    Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
    Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
    Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
)

process.MaxCCCLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxCCCLostHitsTrajectoryFilter'),
    maxCCCLostHits = cms.int32(3),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    )
)

process.MaxConsecLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxConsecLostHitsTrajectoryFilter'),
    maxConsecLostHits = cms.int32(1)
)

process.MaxHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxHitsTrajectoryFilter'),
    maxNumberOfHits = cms.int32(100)
)

process.MaxLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxLostHitsTrajectoryFilter'),
    maxLostHits = cms.int32(2)
)

process.MinHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinHitsTrajectoryFilter'),
    minimumNumberOfHits = cms.int32(5)
)

process.MinPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinPtTrajectoryFilter'),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0),
    nSigmaMinPt = cms.double(5.0)
)

process.PhilV0 = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt010_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt010_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
    ),
    cutBased = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    tmvaMethod = cms.string('JetID'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/mva_JetID.weights.xml.gz'),
    version = cms.int32(0)
)

process.PhilV1 = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
        Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
        Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
        Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
        Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
        Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
        Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
        Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
        Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
        Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
        Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
        Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('philv1'),
    tmvaMethod = cms.string('JetID'),
    tmvaSpectators = cms.vstring(),
    tmvaVariables = cms.vstring(
        'nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'd0', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dRMean', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/mva_JetID_v1.weights.xml.gz'),
    version = cms.int32(-1)
)

process.PuJetIdCutBased_wp = cms.PSet(
    Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
    Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
    Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
    Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
    Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
    Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
    Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
    Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
)

process.PuJetIdMinMVA_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
    Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
    Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
    Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
    Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
    Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
)

process.PuJetIdOptMVA_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
    Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
    Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
    Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
    Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
    Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
)

process.SiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.SiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.SiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.SiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.ThresholdPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ThresholdPtTrajectoryFilter'),
    minHitsThresholdPt = cms.int32(3),
    nSigmaThresholdPt = cms.double(5.0),
    thresholdPt = cms.double(10.0)
)

process.ckfBaseInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.cutbased = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
        Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
        Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
        Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
        Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
        Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
        Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
        Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
    ),
    cutBased = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('cutbased')
)

process.full = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
        Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
        Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
        Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
        Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
        Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('PuJetIdOptMVA'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_PuJetIdOptMVA.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_102x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
        Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
        Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_102X_Eta0p0To2p5_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_102X_Eta2p5To2p75_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_102X_Eta2p75To3p0_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_102X_Eta3p0To5p0_chs_BDT.weights.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.full_53x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt010_MET = cms.vdouble(0.0, -0.6, -0.4, -0.4),
        Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt1020_MET = cms.vdouble(0.3, -0.2, -0.4, -0.4),
        Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt2030_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
        Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        Pt2030_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
        Pt2030_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42),
        Pt3050_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
        Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2),
        Pt3050_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
        Pt3050_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full53x'),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta', 
        'jetPhi'
    ),
    tmvaVariables = cms.vstring(
        'nvtx', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'
    ),
    tmvaWeights = cms.string('CondFormats/JetMETObjects/data/TMVAClassificationCategory_JetID_53X_Dec2012.weights.xml'),
    version = cms.int32(-1)
)

process.full_53x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt2030_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
        Pt2030_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
        Pt2030_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17),
        Pt3050_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
        Pt3050_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
        Pt3050_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta', 
        'jetPhi'
    ),
    tmvaVariables = cms.vstring(
        'nvtx', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'
    ),
    tmvaWeights = cms.string('CondFormats/JetMETObjects/data/TMVAClassificationCategory_JetID_53X_chs_Dec2012.weights.xml'),
    version = cms.int32(-1)
)

process.full_53x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt2030_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
    Pt2030_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
    Pt2030_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17),
    Pt3050_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
    Pt3050_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
    Pt3050_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17)
)

process.full_53x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt010_MET = cms.vdouble(0.0, -0.6, -0.4, -0.4),
    Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt1020_MET = cms.vdouble(0.3, -0.2, -0.4, -0.4),
    Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt2030_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
    Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    Pt2030_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
    Pt2030_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42),
    Pt3050_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
    Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2),
    Pt3050_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
    Pt3050_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42)
)

process.full_5x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
        Pt010_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
        Pt010_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
        Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
        Pt1020_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
        Pt1020_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
        Pt2030_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
        Pt2030_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
        Pt2030_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74),
        Pt3050_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
        Pt3050_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
        Pt3050_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('BDT_fullPlusRMS'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'dR2Mean', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_5x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
        Pt010_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
        Pt010_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
        Pt1020_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
        Pt1020_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
        Pt1020_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
        Pt2030_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.75),
        Pt2030_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
        Pt2030_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45),
        Pt3050_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.57),
        Pt3050_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
        Pt3050_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('BDT_chsFullPlusRMS'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'dR2Mean', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_chsFullPlusRMS.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_5x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
    Pt010_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
    Pt010_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
    Pt1020_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
    Pt1020_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
    Pt1020_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
    Pt2030_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.75),
    Pt2030_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
    Pt2030_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45),
    Pt3050_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.57),
    Pt3050_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
    Pt3050_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45)
)

process.full_5x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
    Pt010_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
    Pt010_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
    Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
    Pt1020_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
    Pt1020_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
    Pt2030_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
    Pt2030_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
    Pt2030_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74),
    Pt3050_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
    Pt3050_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
    Pt3050_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74)
)

process.full_74x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt010_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt010_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt1020_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt1020_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt1020_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt2030_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt2030_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt2030_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt3050_Loose = cms.vdouble(-0.8, -0.95, -0.97, -0.99),
        Pt3050_Medium = cms.vdouble(-0.6, -0.85, -0.85, -0.99),
        Pt3050_Tight = cms.vdouble(-0.5, -0.77, -0.8, -0.98)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta', 
        'nTrueInt', 
        'dRMatch'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.0),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'dR2Mean', 
                'rho', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'betaStar', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_0_2_newNames.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(2.0),
            tmvaVariables = cms.vstring(
                'dR2Mean', 
                'rho', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'betaStar', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_2_2p5_newNames.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'dR2Mean', 
                'rho', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'betaStar', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_2p5_3_newNames.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'dR2Mean', 
                'rho', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_3_5_newNames.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.full_74x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt010_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt010_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt1020_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt1020_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt1020_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt2030_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt2030_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt2030_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt3050_Loose = cms.vdouble(-0.8, -0.95, -0.97, -0.99),
    Pt3050_Medium = cms.vdouble(-0.6, -0.85, -0.85, -0.99),
    Pt3050_Tight = cms.vdouble(-0.5, -0.77, -0.8, -0.98)
)

process.full_76x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt010_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt010_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt1020_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt1020_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt1020_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt2030_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt2030_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt2030_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt3050_Loose = cms.vdouble(-0.93, -0.52, -0.39, -0.31),
        Pt3050_Medium = cms.vdouble(-0.2, -0.39, -0.24, -0.19),
        Pt3050_Tight = cms.vdouble(0.52, -0.19, -0.06, -0.03)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta0to2p5_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta3to5_BDT.weights.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.full_76x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt010_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt010_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt1020_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt1020_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt1020_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt2030_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt2030_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt2030_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt3050_Loose = cms.vdouble(-0.93, -0.52, -0.39, -0.31),
    Pt3050_Medium = cms.vdouble(-0.2, -0.39, -0.24, -0.19),
    Pt3050_Tight = cms.vdouble(0.52, -0.19, -0.06, -0.03)
)

process.full_80x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt010_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt010_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt1020_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt1020_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt1020_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt2030_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt2030_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt2030_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt3050_Loose = cms.vdouble(-0.92, -0.56, -0.44, -0.39),
        Pt3050_Medium = cms.vdouble(-0.06, -0.42, -0.3, -0.23),
        Pt3050_Tight = cms.vdouble(0.62, -0.21, -0.07, -0.03)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta0to2p5_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta3to5_BDT.weights.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.full_80x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt010_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt010_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt1020_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt1020_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt1020_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt2030_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt2030_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt2030_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt3050_Loose = cms.vdouble(-0.92, -0.56, -0.44, -0.39),
    Pt3050_Medium = cms.vdouble(-0.06, -0.42, -0.3, -0.23),
    Pt3050_Tight = cms.vdouble(0.62, -0.21, -0.07, -0.03)
)

process.full_81x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
        Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
        Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.full_81x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
    Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
    Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
)

process.full_94x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
        Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
        Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    trainings = cms.VPSet(
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_94X_Eta0p0To2p5_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_94X_Eta2p5To2p75_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_94X_Eta2p75To3p0_chs_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring(
                'nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'
            ),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_94X_Eta3p0To5p0_chs_BDT.weights.xml.gz')
        )
    ),
    version = cms.int32(-1)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.met_53x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
        Pt010_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
        Pt1020_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_MET = cms.vdouble(-0.2, -0.2, -0.2, 0.1),
        Pt2030_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_MET = cms.vdouble(-0.2, -0.2, 0.0, 0.2),
        Pt3050_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Tight = cms.vdouble(-2, -2, -2, -2, -2)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('met53x'),
    tmvaMethod = cms.string('JetIDMVAMET'),
    tmvaSpectators = cms.vstring(),
    tmvaVariables = cms.vstring(
        'nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml.gz'),
    version = cms.int32(-1)
)

process.met_53x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
    Pt010_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt010_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
    Pt1020_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_MET = cms.vdouble(-0.2, -0.2, -0.2, 0.1),
    Pt2030_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_MET = cms.vdouble(-0.2, -0.2, 0.0, 0.2),
    Pt3050_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Tight = cms.vdouble(-2, -2, -2, -2, -2)
)

process.metfull_53x_wp = cms.PSet(
    Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
    Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
    Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2)
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
)

process.pfJetIDSelector = cms.PSet(
    quality = cms.string('TIGHT'),
    version = cms.string('WINTER17')
)

process.simple = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
        Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
        Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
        Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
        Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
        Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('PuJetIdMinMVA'),
    tmvaSpectators = cms.vstring(
        'nvtx', 
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'beta', 
        'betaStar'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_PuJetIdMinMVA.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
        Pt010_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
        Pt010_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
        Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
        Pt1020_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
        Pt1020_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
        Pt2030_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
        Pt2030_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
        Pt2030_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74),
        Pt3050_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
        Pt3050_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
        Pt3050_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74)
    ),
    cutBased = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('BDT_simpleNoVtxCat'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'beta', 
        'betaStar'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_simpleNoVtxCat.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
        Pt010_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
        Pt010_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
        Pt1020_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
        Pt1020_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
        Pt1020_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
        Pt2030_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
        Pt2030_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
        Pt2030_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47),
        Pt3050_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
        Pt3050_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
        Pt3050_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('BDT_chsSimpleNoVtxCat'),
    tmvaSpectators = cms.vstring(
        'jetPt', 
        'jetEta'
    ),
    tmvaVariables = cms.vstring(
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'beta', 
        'betaStar'
    ),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_chsSimpleNoVtxCat.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
    Pt010_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
    Pt010_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
    Pt1020_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
    Pt1020_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
    Pt1020_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
    Pt2030_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
    Pt2030_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
    Pt2030_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47),
    Pt3050_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
    Pt3050_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
    Pt3050_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47)
)

process.simple_5x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
    Pt010_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
    Pt010_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
    Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
    Pt1020_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
    Pt1020_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
    Pt2030_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
    Pt2030_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
    Pt2030_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74),
    Pt3050_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
    Pt3050_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
    Pt3050_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74)
)

process.JetUserData = cms.EDProducer("JetUserData",
    candSVTagInfos = cms.string('pfInclusiveSecondaryVertexFinder'),
    coneSize = cms.double(0.4),
    getJERFromTxt = cms.bool(False),
    hlt2reco_deltaRmax = cms.double(0.2),
    hltJetFilter = cms.InputTag("hltPFHT"),
    hltPath = cms.string('HLT_PFHT800'),
    jecAK4chsPayloadNames_jetUserdata = cms.vstring(
        'Fall17_17Nov2017_V32_MC_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L3Absolute_AK4PFchs.txt'
    ),
    jerLabel = cms.string('AK4PFchs'),
    jetCorrLabel = cms.string('AK4PFchs'),
    jetLabel = cms.InputTag("slimmedJets"),
    resolutionsFile = cms.string('Fall17_17Nov2017_V32_MC_PtResolution_AK4PFchs.txt'),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    scaleFactorsFile = cms.string('Fall17_17Nov2017_V32_MC_SF_AK4PFchs.txt'),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    triggerSummary = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    vertex_jetUserdata = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.Wtoenu = cms.EDProducer("PKUWLepProducer",
    MET = cms.InputTag("slimmedMETs"),
    cut = cms.string(''),
    leptons = cms.InputTag("goodElectrons")
)


process.Wtomunu = cms.EDProducer("PKUWLepProducer",
    MET = cms.InputTag("slimmedMETs"),
    cut = cms.string(''),
    leptons = cms.InputTag("goodMuons")
)


process.ckfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalMixedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.cleanAK4Jets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.4),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("goodElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.4),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(True),
            src = cms.InputTag("goodMuons")
        ),
        photons = cms.PSet(

        ),
        taus = cms.PSet(

        ),
        tkIsoElectrons = cms.PSet(

        )
    ),
    finalCut = cms.string('pt > 20 && abs(eta) < 4.7'),
    preselection = cms.string(''),
    src = cms.InputTag("goodAK4Jets")
)


process.goodElectrons = cms.EDProducer("PATElectronIdSelector",
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    idLabel = cms.string('tight'),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.goodMuons = cms.EDProducer("PATMuonIdSelector",
    idLabel = cms.string('tight'),
    src = cms.InputTag("slimmedMuons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.leptonicV = cms.EDProducer("CandViewMerger",
    cut = cms.string(''),
    src = cms.VInputTag("Wtoenu", "Wtomunu")
)


process.looseMuons = cms.EDProducer("PATMuonIdSelector",
    idLabel = cms.string('loose'),
    src = cms.InputTag("slimmedMuons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsReapplyJEC = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetsReapplyJEC = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pileupJetId = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
                Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
                Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
            ),
            cutBased = cms.bool(False),
            etaBinnedWeights = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('full'),
            nEtaBins = cms.int32(4),
            tmvaMethod = cms.string('JetIDMVAHighPt'),
            tmvaSpectators = cms.vstring(
                'jetPt', 
                'jetEta'
            ),
            trainings = cms.VPSet(
                cms.PSet(
                    jEtaMax = cms.double(2.5),
                    jEtaMin = cms.double(0.0),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(2.75),
                    jEtaMin = cms.double(2.5),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(3.0),
                    jEtaMin = cms.double(2.75),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(5.0),
                    jEtaMin = cms.double(3.0),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'pull', 
                        'jetR'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
                )
            ),
            version = cms.int32(-1)
        ), 
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
                Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )
    ),
    applyJec = cms.bool(False),
    inputIsCorrected = cms.bool(True),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("cleanAK4Jets"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pileupJetIdCalculator = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(cms.PSet(
        JetIdParams = cms.PSet(
            Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
            Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
            Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
            Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
            Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
            Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
            Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
            Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
        ),
        cutBased = cms.bool(True),
        impactParTkThreshold = cms.double(1.0),
        label = cms.string('cutbased')
    )),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(False),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("ak4PFJetsCHS"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(False),
    vertexes = cms.InputTag("offlinePrimaryVertices")
)


process.pileupJetIdEvaluator = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
                Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
                Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
                Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
                Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
                Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
            ),
            cutBased = cms.bool(False),
            etaBinnedWeights = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('full'),
            nEtaBins = cms.int32(4),
            tmvaMethod = cms.string('JetIDMVAHighPt'),
            tmvaSpectators = cms.vstring(
                'jetPt', 
                'jetEta'
            ),
            trainings = cms.VPSet(
                cms.PSet(
                    jEtaMax = cms.double(2.5),
                    jEtaMin = cms.double(0.0),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(2.75),
                    jEtaMin = cms.double(2.5),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(3.0),
                    jEtaMin = cms.double(2.75),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'nCharged', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'beta', 
                        'pull', 
                        'jetR', 
                        'jetRchg'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
                ), 
                cms.PSet(
                    jEtaMax = cms.double(5.0),
                    jEtaMin = cms.double(3.0),
                    tmvaVariables = cms.vstring(
                        'nvtx', 
                        'dR2Mean', 
                        'nParticles', 
                        'majW', 
                        'minW', 
                        'frac01', 
                        'frac02', 
                        'frac03', 
                        'frac04', 
                        'ptD', 
                        'pull', 
                        'jetR'
                    ),
                    tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
                )
            ),
            version = cms.int32(-1)
        ), 
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
                Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )
    ),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(False),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag("pileupJetIdCalculator"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    produceJetIds = cms.bool(False),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    vertexes = cms.InputTag("offlinePrimaryVertices")
)


process.prefiringweight = cms.EDProducer("L1ECALPrefiringWeightProducer",
    DataEra = cms.string('2017BtoF'),
    L1Maps = cms.string('L1PrefiringMaps.root'),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = cms.bool(False),
    TheJets = cms.InputTag("slimmedJets"),
    ThePhotons = cms.InputTag("slimmedPhotons"),
    UseJetEMPt = cms.bool(False)
)


process.slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.updatedPatJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.updatedPatJets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("updatedPatJetCorrFactors")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.vetoElectrons = cms.EDProducer("PATElectronIdSelector",
    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    idLabel = cms.string('veto'),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.BadChargedCandidateFilter = cms.EDFilter("BadParticleFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    filterType = cms.string('BadChargedCandidate'),
    innerTrackRelErr = cms.double(1.0),
    maxDR = cms.double(1e-05),
    minMuonPt = cms.double(100.0),
    minMuonTrackRelErr = cms.double(2.0),
    minPtDiffRel = cms.double(1e-05),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(False)
)


process.BadPFMuonFilter = cms.EDFilter("BadParticleFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    algo = cms.int32(14),
    filterType = cms.string('BadPFMuon'),
    innerTrackRelErr = cms.double(1.0),
    maxDR = cms.double(0.001),
    minMuonPt = cms.double(100),
    minMuonTrackRelErr = cms.double(2.0),
    minPtDiffRel = cms.double(0.0),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(False)
)


process.ecalBadCalibFilter = cms.EDFilter("EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEcalRecHitsEE"),
    baddetEcal = cms.vuint32(),
    debug = cms.bool(False),
    ecalMinEt = cms.double(50.0),
    taggingMode = cms.bool(False)
)


process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter("EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma","reducedEERecHits"),
    baddetEcal = cms.vuint32(
        872439604, 872422825, 872420274, 872423218, 872423215, 
        872416066, 872435036, 872439336, 872420273, 872436907, 
        872420147, 872439731, 872436657, 872420397, 872439732, 
        872439339, 872439603, 872422436, 872439861, 872437051, 
        872437052, 872420649, 872422436, 872421950, 872437185, 
        872422564, 872421566, 872421695, 872421955, 872421567, 
        872437184, 872421951, 872421694, 872437056, 872437057, 
        872437313
    ),
    debug = cms.bool(False),
    ecalMinEt = cms.double(50.0),
    taggingMode = cms.bool(True)
)


process.goodAK4Jets = cms.EDFilter("PFJetIDSelectionFunctorFilter",
    filterParams = cms.PSet(
        quality = cms.string('TIGHT'),
        version = cms.string('WINTER17')
    ),
    src = cms.InputTag("JetUserData")
)


process.goodPhotons = cms.EDFilter("PATPhotonSelector",
    cut = cms.string('pt > 15 && fabs(eta) < 2.5'),
    src = cms.InputTag("slimmedPhotons")
)


process.leptonicVFilter = cms.EDFilter("CandViewCountFilter",
    minNumber = cms.uint32(0),
    src = cms.InputTag("leptonicV")
)


process.leptonicVSelector = cms.EDFilter("CandViewSelector",
    cut = cms.string('pt > 0.0'),
    filter = cms.bool(False),
    src = cms.InputTag("leptonicV")
)


process.treeDumper = cms.EDAnalyzer("PKUTreeMaker",
    PKUChannel = cms.string('VW_CHANNEL'),
    RunOnMC = cms.bool(True),
    ak4jetsSrc = cms.InputTag("cleanAK4Jets"),
    beamSpot = cms.InputTag("offlineBeamSpot","","RECO"),
    conversions = cms.InputTag("reducedEgamma","reducedConversions","PAT"),
    crossSectionPb = cms.double(1),
    effAreaChHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
    effAreaNeuHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
    effAreaPhoFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
    elPaths1 = cms.vstring('HLT_L1SingleEGOrFilter_v*'),
    elPaths2 = cms.vstring('HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*'),
    electrons = cms.InputTag("slimmedElectrons"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    genJet = cms.InputTag("slimmedGenJets"),
    genSrc = cms.InputTag("prunedGenParticles"),
    generator = cms.InputTag("generator"),
    goodeleSrc = cms.InputTag("goodElectrons"),
    goodmuonSrc = cms.InputTag("goodMuons"),
    hltToken = cms.InputTag("TriggerResults","","HLT"),
    isGen = cms.bool(False),
    jecAK4PayloadNames = cms.vstring(
        'Fall17_17Nov2017_V32_MC_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L3Absolute_AK4PFchs.txt'
    ),
    jecAK4chsPayloadNames = cms.vstring(
        'Fall17_17Nov2017_V32_MC_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017_V32_MC_L3Absolute_AK4PFchs.txt'
    ),
    leptonicVSrc = cms.InputTag("leptonicV"),
    lhe = cms.InputTag("externalLHEProducer"),
    looseelectronSrc = cms.InputTag("vetoElectrons"),
    loosemuonSrc = cms.InputTag("looseMuons"),
    metSrc = cms.InputTag("slimmedMETs"),
    muPaths1 = cms.vstring(
        'HLT_IsoMu20_v*', 
        'HLT_IsoTkMu20_v*'
    ),
    muPaths2 = cms.vstring(
        'HLT_IsoMu24_v*', 
        'HLT_IsoTkMu24_v*'
    ),
    muPaths3 = cms.vstring('HLT_IsoMu27_v*'),
    noiseFilter = cms.InputTag("TriggerResults","","PAT"),
    noiseFilterSelection_EcalDeadCellTriggerPrimitiveFilter = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    noiseFilterSelection_HBHENoiseFilter = cms.string('Flag_HBHENoiseFilter'),
    noiseFilterSelection_HBHENoiseIsoFilter = cms.string('Flag_HBHENoiseIsoFilter'),
    noiseFilterSelection_badChargedHadron = cms.InputTag("BadChargedCandidateFilter"),
    noiseFilterSelection_badMuon = cms.InputTag("BadPFMuonFilter"),
    noiseFilterSelection_eeBadScFilter = cms.string('Flag_eeBadScFilter'),
    noiseFilterSelection_globalTightHaloFilter = cms.string('Flag_globalTightHalo2016Filter'),
    noiseFilterSelection_goodVertices = cms.string('Flag_goodVertices'),
    originalNEvents = cms.int32(1),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    photonSrc = cms.InputTag("slimmedPhotons"),
    pileup = cms.InputTag("slimmedAddPileupInfo"),
    pileupJetId = cms.InputTag("pileupJetId"),
    pileupJetIdDiscriminant = cms.InputTag("pileupJetId","fullDiscriminant"),
    pileupJetIdFlag = cms.InputTag("pileupJetId","fullId"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    t1jetSrc = cms.InputTag("slimmedJets"),
    t1jetSrc_user = cms.InputTag("JetUserData"),
    t1muSrc = cms.InputTag("slimmedMuons"),
    targetLumiInvPb = cms.double(1.0),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(99999999),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('treePKU.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string(''),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Fastjet', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Offset', 
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute'
    )
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative', 
        'ak10PFCHSL3Absolute', 
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Fastjet', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Offset', 
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative', 
        'ak10PFL3Absolute'
    )
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative', 
        'ak10PFL3Absolute', 
        'ak10PFResidual'
    )
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Fastjet', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Offset', 
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute'
    )
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative', 
        'ak1PFCHSL3Absolute', 
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Fastjet', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Offset', 
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative', 
        'ak1PFL3Absolute'
    )
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative', 
        'ak1PFL3Absolute', 
        'ak1PFResidual'
    )
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Fastjet', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Offset', 
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute'
    )
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative', 
        'ak2PFCHSL3Absolute', 
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Fastjet', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Offset', 
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative', 
        'ak2PFL3Absolute'
    )
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative', 
        'ak2PFL3Absolute', 
        'ak2PFResidual'
    )
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Fastjet', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Offset', 
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute'
    )
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative', 
        'ak3PFCHSL3Absolute', 
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Fastjet', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Offset', 
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative', 
        'ak3PFL3Absolute'
    )
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative', 
        'ak3PFL3Absolute', 
        'ak3PFResidual'
    )
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset', 
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative', 
        'ak4CaloL3Absolute', 
        'ak4CaloResidual'
    )
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset', 
        'ak4JPTL2Relative', 
        'ak4JPTL3Absolute', 
        'ak4JPTResidual'
    )
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Fastjet')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset', 
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative', 
        'ak4PFCHSL3Absolute', 
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB'
    )
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset', 
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute'
    )
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFL6SLB'
    )
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative', 
        'ak4PFL3Absolute', 
        'ak4PFResidual'
    )
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4TrackL2Relative', 
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Fastjet', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Offset', 
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute'
    )
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative', 
        'ak5PFCHSL3Absolute', 
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Fastjet', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Offset', 
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative', 
        'ak5PFL3Absolute'
    )
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative', 
        'ak5PFL3Absolute', 
        'ak5PFResidual'
    )
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Fastjet', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Offset', 
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute'
    )
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative', 
        'ak6PFCHSL3Absolute', 
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Fastjet', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Offset', 
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative', 
        'ak6PFL3Absolute'
    )
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative', 
        'ak6PFL3Absolute', 
        'ak6PFResidual'
    )
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Fastjet', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset', 
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative', 
        'ak7CaloL3Absolute', 
        'ak7CaloResidual'
    )
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual'
    )
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute', 
        'ak7JPTResidual'
    )
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset', 
        'ak7JPTL2Relative', 
        'ak7JPTL3Absolute'
    )
)


process.ak7L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Fastjet')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Fastjet', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Offset', 
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative', 
        'ak7PFCHSL3Absolute', 
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB'
    )
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Fastjet', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset', 
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute'
    )
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFL6SLB'
    )
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative', 
        'ak7PFL3Absolute', 
        'ak7PFResidual'
    )
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Fastjet', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Offset', 
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute'
    )
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative', 
        'ak8PFCHSL3Absolute', 
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Fastjet', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Offset', 
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative', 
        'ak8PFL3Absolute'
    )
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative', 
        'ak8PFL3Absolute', 
        'ak8PFResidual'
    )
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Fastjet', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Offset', 
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute'
    )
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative', 
        'ak9PFCHSL3Absolute', 
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Fastjet', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Offset', 
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative', 
        'ak9PFL3Absolute'
    )
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative', 
        'ak9PFL3Absolute', 
        'ak9PFResidual'
    )
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.beamHaloNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('BeamHaloNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("SkippingLayerCosmicNavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    allSelf = cms.bool(True),
    noPXB = cms.bool(False),
    noPXF = cms.bool(False),
    noTEC = cms.bool(False),
    noTIB = cms.bool(False),
    noTID = cms.bool(False),
    noTOB = cms.bool(False),
    selfSearch = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Fastjet', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset', 
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative', 
        'ic5CaloL3Absolute', 
        'ic5CaloResidual'
    )
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB'
    )
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Fastjet', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset', 
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute'
    )
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFL6SLB'
    )
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative', 
        'ic5PFL3Absolute', 
        'ic5PFResidual'
    )
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Fastjet', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset', 
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative', 
        'kt4CaloL3Absolute', 
        'kt4CaloResidual'
    )
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB'
    )
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Fastjet', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset', 
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute'
    )
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFL6SLB'
    )
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative', 
        'kt4PFL3Absolute', 
        'kt4PFResidual'
    )
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Fastjet', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset', 
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative', 
        'kt6CaloL3Absolute', 
        'kt6CaloResidual'
    )
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB'
    )
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Fastjet', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset', 
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute'
    )
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFL6SLB'
    )
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative', 
        'kt6PFL3Absolute', 
        'kt6PFResidual'
    )
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    )
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('102X_mc2017_realistic_v8'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.556668),
            tmax = cms.double(10.0),
            tzero = cms.double(13.307784)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.egammaUpdatorTask = cms.Task()


process.patJetCorrectionsTask = cms.Task(process.patJetCorrFactors)


process.egammaPostRecoPatUpdatorTask = cms.Task()


process.egammaScaleSmearTask = cms.Task()


process.egammaVIDTask = cms.Task()


process.pileUpJetIDTask = cms.Task(process.pileupJetId, process.pileupJetIdCalculator, process.pileupJetIdEvaluator)


process.egammaUpdatorSeq = cms.Sequence(process.egammaUpdatorTask)


process.patJetCorrections = cms.Sequence(process.patJetCorrectionsTask)


process.NJetsSequence = cms.Sequence(process.goodAK4Jets+process.cleanAK4Jets)


process.leptonicVSequence = cms.Sequence(process.Wtomunu+process.Wtoenu+process.leptonicV)


process.cleanJets = cms.Sequence(process.NJetsSequence)


process.photonSequence = cms.Sequence(process.goodPhotons)


process.makeUpdatedPatJets = cms.Sequence(process.updatedPatJetCorrFactors+process.updatedPatJets)


process.muSequence = cms.Sequence(process.goodMuons+process.looseMuons)


process.eleSequence = cms.Sequence(process.goodElectrons+process.vetoElectrons)


process.jetSequence = cms.Sequence(process.patJetCorrFactorsReapplyJEC+process.patJetsReapplyJEC+process.goodAK4Jets+process.cleanJets+process.pileupJetId)


process.egammaVIDSeq = cms.Sequence(process.egammaVIDTask)


process.egammaScaleSmearSeq = cms.Sequence(process.egammaScaleSmearTask)


process.egammaPostRecoPatUpdatorSeq = cms.Sequence(process.egammaPostRecoPatUpdatorTask)


process.metfilterSequence = cms.Sequence(process.BadPFMuonFilter+process.BadChargedCandidateFilter)


process.egammaPostRecoSeq = cms.Sequence(process.egammaUpdatorSeq+process.egammaScaleSmearSeq+process.egammaVIDSeq+process.egammaPostRecoPatUpdatorSeq)


process.leptonSequence = cms.Sequence(process.muSequence+process.eleSequence+process.leptonicVSequence+process.leptonicVSelector+process.leptonicVFilter)


process.analysis = cms.Path(process.JetUserData+process.leptonSequence+process.jetSequence+process.metfilterSequence+process.ecalBadCalibReducedMINIAODFilter+process.prefiringweight+process.treeDumper)


