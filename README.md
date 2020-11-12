cmsrel CMSSW_10_2_18

cd CMSSW_10_2_18/src

cmsenv

git cms-init

git cms-merge-topic cms-egamma:EgammaPostRecoTools

git-cms-addpkg RecoEgamma/PhotonIdentification

git cms-addpkg RecoMET/METFilters

git clone -b 94X_weights_DYJets_inc_v2 git@github.com:cms-jet/PUjetID.git PUJetIDweights/ git-cms-addpkg RecoJets/JetProducers

cp PUJetIDweights/weights/pileupJetId_94X_Eta* $CMSSW_BASE/src/RecoJets/JetProducers/data/

git cms-merge-topic singh-ramanpreet:PUID_102_15_v2

git clone -b 17_pujetID https://github.com/JINGFFF/fullRun2VBSWG.git VAJets
