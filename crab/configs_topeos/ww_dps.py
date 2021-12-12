from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName = 'WW_DPS'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script.sh'
# hadd nano will not be needed once nano tools are in cmssw
config.JobType.inputFiles = ['crab_script.py', '../scripts/haddnano.py','keep_and_drop.txt']
config.JobType.sendPythonFolder = True

config.section_("Data")
config.Data.inputDataset = '/WWTo2L2Nu_TuneCP5_DoubleScattering_13TeV-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_top/ExtraYukawa/TTC_newLeptonID/'
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'WW_DPS'

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
