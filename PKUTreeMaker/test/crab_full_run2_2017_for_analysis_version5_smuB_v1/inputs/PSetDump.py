import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2017B/SingleElectron/MINIAOD/31Mar2018-v1/30000/04B05308-0038-E811-99AB-008CFAC94314.root'),
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
    input = cms.untracked.int32(1000)
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

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1_producer_config = cms.PSet(
    ebeeSplit = cms.double(1.479),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1'),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_producer_config = cms.PSet(
    ebeeSplit = cms.double(1.479),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1p1'),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1p1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_producer_config = cms.PSet(
    ebeeSplit = cms.double(1.479),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v2'),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v2_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(0.42, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(-0.02, -0.26),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    ebeeSplit = cms.double(1.479),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring16NonTrigV1'),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
    )
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

process.trkIsol03CfgV2 = cms.PSet(
    barrelCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.1),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    ),
    endcapCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.5),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
        )
    )
)

process.mvaConfigsForPhoProducer = cms.VPSet(
    cms.PSet(
        ebeeSplit = cms.double(1.479),
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring16NonTrigV1'),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        ebeeSplit = cms.double(1.479),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1'),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        ebeeSplit = cms.double(1.479),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1p1'),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        ebeeSplit = cms.double(1.479),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v2'),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
        )
    )
)

process.JetUserData = cms.EDProducer("JetUserData",
    candSVTagInfos = cms.string('pfInclusiveSecondaryVertexFinder'),
    coneSize = cms.double(0.4),
    getJERFromTxt = cms.bool(False),
    hlt2reco_deltaRmax = cms.double(0.2),
    hltJetFilter = cms.InputTag("hltPFHT"),
    hltPath = cms.string('HLT_PFHT800'),
    jecAK4chsPayloadNames_jetUserdata = cms.vstring(
        'Fall17_17Nov2017B_V32_DATA_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L3Absolute_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2L3Residual_AK4PFchs.txt'
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


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(35.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.4442),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.566)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(0.006),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.06),
                        dPhiInCutValueEE = cms.double(0.06),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaWithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        maxSigmaIEtaIEtaEB = cms.double(9999),
                        maxSigmaIEtaIEtaEE = cms.double(0.03),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5E2x5OverE5x5WithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        minE1x5OverE5x5EB = cms.double(0.83),
                        minE1x5OverE5x5EE = cms.double(-1.0),
                        minE2x5OverE5x5EB = cms.double(0.94),
                        minE2x5OverE5x5EE = cms.double(-1.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.0),
                        constTermEE = cms.double(5),
                        cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.05),
                        slopeTermEE = cms.double(0.05)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(5.0),
                        constTermEE = cms.double(5.0),
                        cutName = cms.string('GsfEleValueMapIsoRhoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag(""),
                        rhoEAEB = cms.double(0.0),
                        rhoEAEE = cms.double(0.0),
                        rhoEtStartEB = cms.double(999999.0),
                        rhoEtStartEE = cms.double(999999.0),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.0),
                        slopeTermEE = cms.double(0.0),
                        value = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.0),
                        constTermEE = cms.double(2.5),
                        cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        rhoConstant = cms.double(0.28),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(50.0),
                        slopeTermEB = cms.double(0.03),
                        slopeTermEE = cms.double(0.03)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.02),
                        dxyCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEcalDrivenCut'),
                        ecalDrivenEB = cms.int32(1),
                        ecalDrivenEE = cms.int32(1),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('heepElectronID-HEEPV70'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('49b6b60e9f16727f241eb34b9d345a8f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00387),
                        dEtaInSeedCutValueEE = cms.double(0.0072),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0716),
                        dPhiInCutValueEE = cms.double(0.147),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0414),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.133),
                        isoCutEBLowPt = cms.double(0.133),
                        isoCutEEHighPt = cms.double(0.146),
                        isoCutEELowPt = cms.double(0.146),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9530240956555949 - exp(-pt / 2.7591425841003647) *  0.4669644718545271', 
                        '0.9336564763961019 - exp(-pt /  2.709276284272272) * 0.33512286599215946', 
                        '0.9313133688365339 - exp(-pt / 1.5821934800715558) *  3.8889462619659265', 
                        '0.9825268564943458 - exp(-pt /  8.702601455860762) *  1.1974861596609097', 
                        '0.9727509457929913 - exp(-pt /  8.179525631018565) *  1.7111755094657688', 
                        '0.9562619539540145 - exp(-pt /  8.109845366281608) *   3.013927699126942'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9165112826974601 - exp(-pt / 2.7381703555094217) *    1.03549199648109', 
                        '0.8655738322220173 - exp(-pt / 2.4027944652597073) *  0.7975615613282494', 
                        '-3016.035055227131 - exp(-pt / -52140.61856333602) * -3016.3029387236506', 
                        '0.9616542816132922 - exp(-pt /  8.757943837889817) *  3.1390200321591206', 
                        '0.9319258011430132 - exp(-pt /  8.846057432565809) *  3.5985063793347787', 
                        '0.8899260780999244 - exp(-pt / 10.124234115859881) *   4.352791250718547'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.13285867293779202', 
                        '-0.31765300958836074', 
                        '-0.0799205914718861', 
                        '-0.856871961305474', 
                        '-0.8107642141584835', 
                        '-0.7179265933023059'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9725509559754997 - exp(-pt /  2.976593261509491) *  0.2653858736397496', 
                        '0.9508038141601247 - exp(-pt / 2.6633500558725713) *  0.2355820499260076', 
                        '0.9365037167596238 - exp(-pt / 1.5765442323949856) *   3.067015289215309', 
                        '0.9896562087723659 - exp(-pt / 10.342490511998674) * 0.40204156417414094', 
                        '0.9819232656533827 - exp(-pt /   9.05548836482051) *   0.772674931169389', 
                        '0.9625098201744635 - exp(-pt /   8.42589315557279) *  2.2916152615134173'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9387070396095831 - exp(-pt /   2.6525585228167636) *  0.8222647164151365', 
                        '0.8948802925677235 - exp(-pt /   2.7645670358783523) *  0.4123381218697539', 
                        '-1830.8583661119892 - exp(-pt /   -36578.11055382301) * -1831.2083578116517', 
                        '0.9717674837607253 - exp(-pt /    8.912850985100356) *  1.9712414940437244', 
                        '0.9458745023265976 - exp(-pt /     8.83104420392795) *    2.40849932040698', 
                        '0.8979112012086751 - exp(-pt /    9.814082144168015) *   4.171581694893849'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.09564086146419018', 
                        '-0.28229916981926795', 
                        '-0.05466682296962322', 
                        '-0.833466688584422', 
                        '-0.7677000247570116', 
                        '-0.6917305995653829'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.940962684155', 
                        '0.899208843708', 
                        '0.758484721184'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.836695742607', 
                        '0.715337944031', 
                        '0.356799721718'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.211', 
                        '-0.396', 
                        '-0.215', 
                        '-0.870', 
                        '-0.838', 
                        '-0.763'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-HZZ-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1797cc03eb62387e10266fca72ea10cd'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00377),
                        dEtaInSeedCutValueEE = cms.double(0.00674),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0884),
                        dPhiInCutValueEE = cms.double(0.169),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0112),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0425),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0441),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.111),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.112),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.108),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('5547e2c8b5c222192519c41bff05bc2e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.0032),
                        dEtaInSeedCutValueEE = cms.double(0.00632),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0547),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0106),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0387),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.046),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0275),
                        endcapCE = cms.double(2.52),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.184),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0721),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0478),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0658),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('48702f025a8df2c527f53927af8b66d0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00255),
                        dEtaInSeedCutValueEE = cms.double(0.00501),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.022),
                        dPhiInCutValueEE = cms.double(0.0236),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0353),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.15),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0188),
                        endcapCE = cms.double(2.06),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.159),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0197),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0287),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0445),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c06761e199f084f5b0f7868ac48a3e19'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00463),
                        dEtaInSeedCutValueEE = cms.double(0.00814),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.148),
                        dPhiInCutValueEE = cms.double(0.19),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0126),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0457),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.209),
                        eInverseMinusPInverseCutValueEE = cms.double(0.132),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.198),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.203),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('74e217e3ece16b49bd337026a29fc3e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.26449620468 - exp(-pt / 3.32657149223) * 8.84669783568', 
                        '2.83557838497 - exp(-pt / 2.15150487651) * 11.0978016567', 
                        '2.91994945177 - exp(-pt / 1.69875477522) * 24.024807824', 
                        '7.1336238874 - exp(-pt / 16.5605268797) * 8.22531222391', 
                        '6.18638275782 - exp(-pt / 15.2694634284) * 7.49764565324', 
                        '5.43175865738 - exp(-pt / 15.4290075949) * 7.56899692285'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.77072387339 - exp(-pt / 3.81500912145) * 8.16304860178', 
                        '1.85602317813 - exp(-pt / 2.18697654938) * 11.8568936824', 
                        '1.73489307814 - exp(-pt / 2.0163211971) * 17.013880078', 
                        '5.9175992258 - exp(-pt / 13.4807294538) * 9.31966232685', 
                        '5.01598837255 - exp(-pt / 13.1280451502) * 8.79418193765', 
                        '4.16921343208 - exp(-pt / 13.2017224621) * 9.00720913211'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.894411158628', 
                        '0.791966464633', 
                        '1.47104857173', 
                        '-0.293962958665', 
                        '-0.250424758584', 
                        '-0.130985179031'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.53495358797 - exp(-pt / 3.07272325141) * 9.94262764352', 
                        '3.06015605623 - exp(-pt / 1.95572234114) * 14.3091184421', 
                        '3.02052519639 - exp(-pt / 1.59784164742) * 28.719380105', 
                        '7.35752275071 - exp(-pt / 15.87907864) * 7.61288809226', 
                        '6.41811074032 - exp(-pt / 14.730562874) * 6.96387331587', 
                        '5.64936312428 - exp(-pt / 16.3664949747) * 7.19607610311'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.84704783417 - exp(-pt / 3.32529515837) * 9.38050947827', 
                        '2.03833922005 - exp(-pt / 1.93288758682) * 15.364588247', 
                        '1.82704158461 - exp(-pt / 1.89796754399) * 19.1236071158', 
                        '6.12931925263 - exp(-pt / 13.281753835) * 8.71138432196', 
                        '5.26289004857 - exp(-pt / 13.2154971491) * 8.0997882835', 
                        '4.37338792902 - exp(-pt / 14.0776094696) * 8.48513324496'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '1.26402092475', 
                        '1.17808089508', 
                        '1.33051972806', 
                        '2.36464785939', 
                        '2.07880614597', 
                        '1.08080644615'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpHZZ'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.700642584415', 
                        '0.739335420875', 
                        '1.45390456109', 
                        '-0.146270871164', 
                        '-0.0315850882679', 
                        '-0.0321841194737'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.105),
                        hadronicOverEMCutValueEE = cms.double(0.029),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0276),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.839),
                        C1_EE = cms.double(2.15),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(9.188),
                        C1_EE = cms.double(10.471),
                        C2_EB = cms.double(0.0126),
                        C2_EE = cms.double(0.0119),
                        C3_EB = cms.double(2.6e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.956),
                        C1_EE = cms.double(4.895),
                        C2_EB = cms.double(0.0035),
                        C2_EE = cms.double(0.004),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('45515ee95e01fa36972ff7ba69186c97'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.035),
                        hadronicOverEMCutValueEE = cms.double(0.027),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.416),
                        C1_EE = cms.double(1.012),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.491),
                        C1_EE = cms.double(9.131),
                        C2_EB = cms.double(0.0126),
                        C2_EE = cms.double(0.0119),
                        C3_EB = cms.double(2.6e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.952),
                        C1_EE = cms.double(4.095),
                        C2_EB = cms.double(0.004),
                        C2_EE = cms.double(0.004),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('772f7921fa146b630e4dbe79e475a421'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02),
                        hadronicOverEMCutValueEE = cms.double(0.025),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.158),
                        C1_EE = cms.double(0.575),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.267),
                        C1_EE = cms.double(8.916),
                        C2_EB = cms.double(0.0126),
                        C2_EE = cms.double(0.0119),
                        C3_EB = cms.double(2.6e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.065),
                        C1_EE = cms.double(3.272),
                        C2_EB = cms.double(0.0035),
                        C2_EE = cms.double(0.004),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('e260fee6f9011fb13ff56d45cccd21c5'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.67, 0.54),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('56138c4a3ac3c0bffc7f01c187063102'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.27, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1120f91d15f68bf61b5f08958bf4f435'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0481),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01031),
                        cutValueEE = cms.double(0.03013),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.295),
                        C1_EE = cms.double(1.011),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(10.91),
                        C1_EE = cms.double(5.931),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(3.63),
                        C1_EE = cms.double(6.641),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('d6ce6a4f3476294bf0a3261e00170daf'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0396),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01022),
                        cutValueEE = cms.double(0.03001),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.441),
                        C1_EE = cms.double(0.442),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.725),
                        C1_EE = cms.double(1.715),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.571),
                        C1_EE = cms.double(3.863),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c739cfd0b6287b8586da187c06d4053f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0269),
                        hadronicOverEMCutValueEE = cms.double(0.0213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00994),
                        cutValueEE = cms.double(0.03),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.202),
                        C1_EE = cms.double(0.034),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.264),
                        C1_EE = cms.double(0.586),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.362),
                        C1_EE = cms.double(2.617),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('bdb623bdb1a15c13545020a919dd9530'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.68, 0.6),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('beb95233f7d1e033ad9e20cf3d804ba0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.2, 0.2),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('36efe663348f95de0bc1cfa8dc7fa8fe'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(0.42, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('3013ddce7a3ad8b54827c29f5d92282e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(-0.02, -0.26),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('5c06832759b1faf7dd6fc45ed1aef3a2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.04596),
                        hadronicOverEMCutValueEE = cms.double(0.059),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.694),
                        C1_EE = cms.double(2.089),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(24.032),
                        C1_EE = cms.double(19.722),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.876),
                        C1_EE = cms.double(4.162),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4578dfcceb0bfd1ba5ac28973c843fd0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02197),
                        hadronicOverEMCutValueEE = cms.double(0.0326),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01015),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.141),
                        C1_EE = cms.double(1.051),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.189),
                        C1_EE = cms.double(2.718),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.08),
                        C1_EE = cms.double(3.867),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('28b186c301061395f394a81266c8d7de'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02148),
                        hadronicOverEMCutValueEE = cms.double(0.0321),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00996),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.65),
                        C1_EE = cms.double(0.517),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.317),
                        C1_EE = cms.double(2.716),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.044),
                        C1_EE = cms.double(3.032),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('6f4f0ed6a8bf2de8dcf0bc3349b0546d'),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h+'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        )
    ),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronMVAVariableHelper = cms.EDProducer("GsfElectronMVAVariableHelper",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    beamSpotMiniAOD = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    vertexCollectionMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
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


process.heepIDVarValueMaps = cms.EDProducer("ElectronHEEPIDValueMapProducer",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    candVetosAOD = cms.vstring(
        'ELES', 
        'NONE', 
        'NONELES'
    ),
    candVetosMiniAOD = cms.vstring(
        'ELES', 
        'NONE', 
        'NONELES'
    ),
    candsAOD = cms.VInputTag("packedCandsForTkIso", "lostTracksForTkIso", "lostTracksForTkIso:eleTracks"),
    candsMiniAOD = cms.VInputTag("packedPFCandidates", "lostTracks", "lostTracks:eleTracks"),
    dataFormat = cms.int32(2),
    ebRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    ebRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    eeRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    elesAOD = cms.InputTag("gedGsfElectrons"),
    elesMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    trkIsoConfig = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    )
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
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            ebeeSplit = cms.double(1.479),
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring16NonTrigV1'),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            ebeeSplit = cms.double(1.479),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1'),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            ebeeSplit = cms.double(1.479),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1p1'),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            ebeeSplit = cms.double(1.479),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v2'),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonRegressionValueMapProducer = cms.EDProducer("PhotonRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
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
        modifications = cms.VPSet(
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepTrkPtIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    PhotonMVAEstimatorRunIIFall17v1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                    PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                    phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            )
        )
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepTrkPtIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    PhotonMVAEstimatorRunIIFall17v1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                    PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                    phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            )
        )
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
    RunOnMC = cms.bool(False),
    ak4jetsSrc = cms.InputTag("cleanAK4Jets"),
    beamSpot = cms.InputTag("offlineBeamSpot","","RECO"),
    conversions = cms.InputTag("reducedEgamma","reducedConversions","RECO"),
    crossSectionPb = cms.double(1),
    effAreaChHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
    effAreaNeuHadFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
    effAreaPhoFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
    elPaths1 = cms.vstring('HLT_Ele23_WPTight_Gsf_v*'),
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
        'Fall17_17Nov2017B_V32_DATA_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L3Absolute_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2L3Residual_AK4PFchs.txt'
    ),
    jecAK4chsPayloadNames = cms.vstring(
        'Fall17_17Nov2017B_V32_DATA_L1FastJet_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2Relative_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L3Absolute_AK4PFchs.txt', 
        'Fall17_17Nov2017B_V32_DATA_L2L3Residual_AK4PFchs.txt'
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
    noiseFilter = cms.InputTag("TriggerResults","","RECO"),
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
            reportEvery = cms.untracked.int32(10)
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
    globaltag = cms.string('102X_dataRun2_v13'),
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

process.egmPhotonIsolationMiniAODTask = cms.Task(process.egmPhotonIsolation)


process.egammaUpdatorTask = cms.Task()


process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer, process.electronMVAVariableHelper, process.electronRegressionValueMapProducer)


process.egmPhotonIDTask = cms.Task(process.egmPhotonIDs, process.egmPhotonIsolationMiniAODTask, process.photonIDValueMapProducer, process.photonMVAValueMapProducer, process.photonRegressionValueMapProducer)


process.patJetCorrectionsTask = cms.Task(process.patJetCorrFactors)


process.egammaPostRecoPatUpdatorTask = cms.Task(process.slimmedElectrons, process.slimmedPhotons)


process.pileUpJetIDTask = cms.Task(process.pileupJetId, process.pileupJetIdCalculator, process.pileupJetIdEvaluator)


process.egammaVIDTask = cms.Task(process.egmGsfElectronIDTask, process.egmPhotonIDTask, process.heepIDVarValueMaps)


process.egammaScaleSmearTask = cms.Task()


process.egammaUpdatorSeq = cms.Sequence(process.egammaUpdatorTask)


process.patJetCorrections = cms.Sequence(process.patJetCorrectionsTask)


process.NJetsSequence = cms.Sequence(process.goodAK4Jets+process.cleanAK4Jets)


process.leptonicVSequence = cms.Sequence(process.Wtomunu+process.Wtoenu+process.leptonicV)


process.cleanJets = cms.Sequence(process.NJetsSequence)


process.photonSequence = cms.Sequence(process.goodPhotons)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIDTask)


process.egmGsfElectronIDSequence = cms.Sequence(cms.Task(process.heepIDVarValueMaps), process.egmGsfElectronIDTask)


process.makeUpdatedPatJets = cms.Sequence(process.updatedPatJetCorrFactors+process.updatedPatJets)


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolationMiniAODTask)


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


