from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'fullrun2_2017_version5_seleC'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.maxMemoryMB = 3000
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles =['Fall17_17Nov2017C_V32_DATA_L1FastJet_AK4PFchs.txt','Fall17_17Nov2017C_V32_DATA_L1FastJet_AK4PFPuppi.txt','Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK4PFchs.txt','Fall17_17Nov2017C_V32_DATA_L2L3Residual_AK4PFPuppi.txt','Fall17_17Nov2017C_V32_DATA_L2Relative_AK4PFchs.txt','Fall17_17Nov2017C_V32_DATA_L2Relative_AK4PFPuppi.txt','Fall17_17Nov2017C_V32_DATA_L3Absolute_AK4PFchs.txt','Fall17_17Nov2017C_V32_DATA_L3Absolute_AK4PFPuppi.txt']

config.JobType.psetName    = 'analysis_data_C.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.outputPrimaryDataset = 'VBS_WGAMMA_94X'
config.Data.inputDataset = '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 40
config.Data.lumiMask = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'fullrun2_2017_version5_seleC'

config.section_("Site")
config.Site.storageSite = 'T2_CN_Beijing'
