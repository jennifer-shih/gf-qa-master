import com.cwctravel.hudson.plugins.extended_choice_parameter.ExtendedChoiceParameterDefinition

def ALL_WORKSPACE = "C:/Jenkins/workspace/${JOB_NAME}"
def MY_WORKSPACE = "${ALL_WORKSPACE}/${BUILD_NUMBER}"
def TEST_TRIGGER = env.test_trigger
def SERVER = env.test_server
def TAGS = env.tags
def COMPANY = env.company
def MONITOR = env.monitor
def LOG_LEVEL = env.log_level
def WORKER = env.worker != null ? env.worker : 'win-worker'
def TEST_CASES = env.test_cases
def MANUAL_INPUT_TEST_CASES = env.manual_input_test_cases
def PARALLEL_CNT = env.parallel_cnt
def TIMEOUT_RATIO = env.timeout_ratio
def DEF_RUNTIME = env.def_runtime

// msg color
def INFO = "\033[34mINFO\033[0m:"

// slack environment variables
def SLACK_TOKEN = "qa-slack-robot"
def SLACK_CHANNEL = "#feed-qa-jenkins"
def SLACK_MSG_DESC = """company: ${COMPANY}
test_trigger: ${TEST_TRIGGER}
server: ${SERVER}
"""

// jenkins build msg
def trigger_by_timer = currentBuild.getBuildCauses('org.jenkinsci.plugins.parameterizedscheduler.ParameterizedTimerTriggerCause')
def trigger_by_indexing = currentBuild.getBuildCauses('jenkins.branch.BranchIndexingCause')
def trigger_by_user = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')

if (trigger_by_timer) {
    currentBuild.displayName = "#${currentBuild.number}-${COMPANY}-SCH"
    currentBuild.description = """
<b>test_trigger:</b> ${TEST_TRIGGER} <br>
<b>server:</b> ${SERVER} <br>
"""
}
else if (trigger_by_user) {
    def user_id = trigger_by_user.userId
    currentBuild.displayName = "#${currentBuild.number}-${COMPANY}-${user_id}"
    currentBuild.description = """
<b>test_trigger:</b> ${TEST_TRIGGER} <br>
<b>server:</b> ${SERVER} <br>
"""
}
else if (trigger_by_indexing) {
    currentBuild.displayName = "#${currentBuild.number}-INDEX"
    currentBuild.description = ""
}


// settings of build periodically with parameters
def CRON_SETTINGS = ""
switch(BRANCH_NAME) {
    case "develop":
        CRON_SETTINGS = '''
            0 3 * * 1,3,5 % test_server=https://fms-autotest.gofreight.co; company=SFI; tags=SFI; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=intergration_with_reset_db; parallel_cnt=1
            0 3 * * 2,4,6 % test_server=https://fms-autotest.gofreight.co; company=LOHAN; tags=LOHAN; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 3 * * 1,3,5 % test_server=https://fms-autotest-2.gofreight.co; company=OLC; tags=OLC; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 3 * * 2,4,6 % test_server=https://fms-autotest-2.gofreight.co; company=MASCOT; tags=MASCOT; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            0 7 * * 1,3,5 % test_server=https://fms-autotest-2.gofreight.co; company=OLC; tags=OLC_TPE; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 7 * * * % test_server=https://fms-autotest-3.gofreight.co; company=BugRegression; tags=BugRegression; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=bug_regression; parallel_cnt=1
            0 9 * * 1,3,5 % test_server=https://fms-autotest-4.gofreight.co; company=SFI; tags=SFI; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
            0 9 * * 2,4,6 % test_server=https://fms-autotest-4.gofreight.co; company=LOHAN; tags=LOHAN; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
            30 10 * * 1,3,5 % test_server=https://fms-autotest-4.gofreight.co; company=OLC; tags=OLC; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
        '''
        break
    case "master":
        CRON_SETTINGS = '''
            0 17 * * 1,3,5 % test_server=https://fms-autotest.gofreight.co; company=SFI; tags=SFI; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=intergration_with_reset_db; parallel_cnt=1
            0 17 * * 2,4,6 % test_server=https://fms-autotest.gofreight.co; company=LOHAN; tags=LOHAN; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 17 * * 1,3,5 % test_server=https://fms-autotest-2.gofreight.co; company=OLC; tags=OLC; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 16 * * 2,4,6 % test_server=https://fms-autotest-2.gofreight.co; company=MASCOT; tags=MASCOT; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            0 21 * * 1,3,5 % test_server=https://fms-autotest-2.gofreight.co; company=OLC; tags=OLC_TPE; log_level=DEBUG; monitor=0; worker=win-worker2; test_trigger=intergration_with_reset_db; parallel_cnt=1
            1 21 * * * % test_server=https://fms-autotest-3.gofreight.co; company=BugRegression; tags=BugRegression; log_level=DEBUG; monitor=0; worker=win-worker1; test_trigger=bug_regression; parallel_cnt=1
            2 17 * * 1,3,5 % test_server=https://fms-autotest-4.gofreight.co; company=SFI; tags=SFI; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
            2 17 * * 2,4,6 % test_server=https://fms-autotest-4.gofreight.co; company=LOHAN; tags=LOHAN; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
            30 18 * * 1,3,5 % test_server=https://fms-autotest-4.gofreight.co; company=OLC; tags=OLC; log_level=DEBUG; monitor=0; worker=win-worker3; test_trigger=acct_report_with_reset_db; parallel_cnt=1
        '''
        break
}

// a list for 'Build with Parameters' UI
PREFIX_PATH = "features/"
TEST_CASE_LIST = [
    '00_InitialSetup/0001_InitialSetup.feature',
    '01_Role/0101_CreateRoles.feature',
    '02_TradePartner/0201_CreateTradePartners.feature',
    '02_TradePartner/0202_CreateQuotation.feature',
    '04_OceanImport/0401_CreateOIMBLShipment.feature',
    '04_OceanImport/0402_AddOIHBLToShipment.feature',
    '04_OceanImport/0403_AddOIContainer.feature',
    '04_OceanImport/0414_OIMBLLinkedFields.feature',
    '04_OceanImport/0415_OIMBLAndHBLLinkedFields.feature',
    '04_OceanImport/0417_OIHBLToolCopyTo.feature',
    '04_OceanImport/0418_OIDirectMaster.feature',
    '05_OceanExport/0501_CreateOEMBLShipment.feature',
    '05_OceanExport/0502_AddOEHBLToShipment.feature',
    '05_OceanExport/0517_OEHBLToolCopyTo.feature',
    '05_OceanExport/0518_OEDirectMaster.feature',
    '06_AirImport/0601_CreateAIMAWBShipment.feature',
    '06_AirImport/0602_AddAIHAWBToShipment.feature',
    '06_AirImport/0611_AIMAWBFunction.feature',
    '06_AirImport/0612_AIMAWBAndHAWBFunction.feature',
    '06_AirImport/0617_AIHAWBToolCopyTo.feature',
    '06_AirImport/0618_AIDirectMaster.feature',
    '07_AirExport/0701_CreateAEMAWBShipment.feature',
    '07_AirExport/0702_AddAEHAWBToShipment.feature',
    '07_AirExport/0710_AEMAWBFunction.feature',
    '07_AirExport/0711_AEMAWBAndHAWBFunction.feature',
    '07_AirExport/0717_AEHAWBToolCopyTo.feature',
    '07_AirExport/0718_AEDirectMaster.feature',
    '08_Truck/0801_CreateTKShipment.feature',
    '08_Truck/0802_AddTKContainer.feature',
    '08_Truck/0803_TKAccounting.feature',
    '08_Truck/0804_TKDocCenterAndWorkOrder.feature',
    '08_Truck/0805_TKStatus.feature',
    '09_Warehouse/0901_CreateWHReceipt.feature',
    '09_Warehouse/0902_CreateWHReceipAMBasic.feature',
    '09_Warehouse/0906_CreateWHReceipOTBasic.feature',
    '09_Warehouse/0909_CreateWHReceiving.feature',
    '09_Warehouse/0915_CreateWHShipping.feature',
    '09_Warehouse/0920_CopyWHReceipt.feature',
    '09_Warehouse/0921_CreateWHReceiptAdvanced.feature',
    '10_Misc/1001_CreateMiscShipment.feature',
    '14_Accounting/1403_AccountingReportBalanceSheet.feature',
    '14_Accounting/1404_AccountingReportTrialBalance.feature',
    '14_Accounting/1405_AccountingReportGLReport.feature',
    '14_Accounting/1406_AccountingReportWithLargePeriod.feature',
    '14_Accounting/1419_AccountingReportBSMonthly.feature',
    '14_Accounting/1420_AccountingReportTBMonthly.feature',
    '14_Accounting/1421_AccountingReportISMonthly.feature',
    '19_BugRegression/GFG_8412.feature',
    '19_BugRegression/GFG_8542.feature',
    '19_BugRegression/GFG_9043.feature',
    '19_BugRegression/1901_GQT_255.feature',
    '19_BugRegression/1902_GQT_256.feature',
    '19_BugRegression/1903_GQT_258.feature',
    '19_BugRegression/1904_GFACCT_1290.feature',
    '19_BugRegression/1905_GQT_333.feature',
    '19_BugRegression/1906_GQT_301.feature',
    '20_AccountingWizard/2001_OIAcceptanceTest.feature',
    '20_AccountingWizard/2002_OEAcceptanceTest.feature',
    '20_AccountingWizard/2003_AIAcceptanceTest.feature',
    '20_AccountingWizard/2004_AEAcceptanceTest.feature',
    '20_AccountingWizard/2005_TKAcceptanceTest.feature',
    '20_AccountingWizard/2006_WHReceivingAcceptanceTest.feature',
    '20_AccountingWizard/2007_WHShippingAcceptanceTest.feature',
    '20_AccountingWizard/2008_MSAcceptanceTest.feature',
    '20_AccountingWizard/2009_OEBKAcceptanceTest.feature',
    '20_AccountingWizard/2010_OEVSAndBKAcceptanceTest.feature',
    '20_AccountingWizard/2011_OEVSAndHBLAcceptanceTest.feature',
    '21_FrontDesk/2101_AcceptanceTest.feature',
    '22_AWBNoManagement/2201_AcceptanceTest.feature',
    '22_AWBNoManagement/2202_PermissionTest.feature',
    '22_AWBNoManagement/2203_AdvancedTest.feature',
    '23_CostShare/2301_CostShare.feature',
    '24_LoadAndLink/2401_LoadAndLink.feature',
    '24_LoadAndLink/2402_LoadAndLinkMatch.feature',
    '25_PaymentPlan/2501_PaymentPlanList.feature',
    '26_Tracking/2601_EnableGFTracking.feature',
]


def get_run_test_set(){
    def run_test_set = ""

    switch(TEST_TRIGGER) {
        case 'reset-db':
            run_test_set = "RESET_DB"
            break
        case 'intergration':
            run_test_set = "INTERGRATION"
            break
        case 'intergration_with_reset_db':
            run_test_set = "RESET_DB INTERGRATION"
            break
        case 'acct_report':
            run_test_set = "ACCT_REPORT"
            break
        case 'acct_report_with_reset_db':
            run_test_set = "RESET_DB ACCT_REPORT"
            break
        case 'bug_regression':
            run_test_set = "BUG_REGRESSION"
            break
        case 'hotfix':
            run_test_set = "RESET_DB INTERGRATION"
            break
        default:
            echo "ERROR: test_trigger is NOT existed."
            throw new Exception("Please check the test_trigger is correct.")
    }

    return run_test_set
}


def get_feature_file_path(){
    def paths = []

    if (TEST_CASES != ''){
        echo "INFO: specify test cases... ${TEST_CASES}"
        without_prefix_paths = TEST_CASES.split(',')
        for (p in without_prefix_paths) {
            paths.add(PREFIX_PATH + p)
        }
    }
    else if (MANUAL_INPUT_TEST_CASES != ''){
        echo "INFO: manual input test cases... ${MANUAL_INPUT_TEST_CASES}"
        without_prefix_paths = MANUAL_INPUT_TEST_CASES.split('\n')
        for (p in without_prefix_paths) {
            paths.add(PREFIX_PATH + p)
        }
    }
    else{
        echo "ERROR: No any test_case is selected"
        throw new Exception("Please check feature files have been selected.")
    }

    return paths.join(' ')
}


pipeline {
    agent {
        node {
            label "${WORKER}"
            customWorkspace "${MY_WORKSPACE}"
        }
    }
    environment {
        PYTHONIOENCODING="UTF-8"
        COLUMNS=200
    }
    options {
        ansiColor('xterm')
        timeout(time: 8, unit: 'HOURS')
    }
    parameters {
        choice(
            name: 'test_server',
            choices: [
                'https://fms-autotest.gofreight.co',
                'https://fms-autotest-2.gofreight.co',
                'https://fms-autotest-3.gofreight.co',
                'https://fms-autotest-4.gofreight.co',
                'https://fms-stage-stress-1.gofreight.co',
                'https://fms-stage-stress-2.gofreight.co',
                'https://fms-stage-stress-3.gofreight.co',
                'https://fms-stage-olc-2.gofreight.co',
                'https://fms-hotfix-5.gofreight.co',
                'https://fms-stage-qa.gofreight.co',
                'https://fms-stage-qa-2.gofreight.co',
                'https://fms-stage-qa-3.gofreight.co',
                'https://fms-stage-qa-4.gofreight.co',
                'https://fms-stage-qa-5.gofreight.co',
                'https://fms-stage-qa-automation.gofreight.co',
                'https://fms-stage-qa-automation-2.gofreight.co',
                'https://fms-release-4.gofreight.co',
                'https://fms-stage-devops-4.gofreight.co',
                'https://fms-stage-devops-5.gofreight.co',
                'https://fms-stage-sync-tracking-auto.gofreight.co'
            ]
        )
        choice(
            name: 'company',
            choices: [
                'SFI',
                'LOHAN',
                'OLC',
                'MASCOT',
                'UCM',
                'BugRegression'
            ]
        )
        choice(
            name: 'tags',
            choices: [
                'SFI',
                'LOHAN',
                'OLC',
                'OLC_TPE',
                'MASCOT',
                'Tracking',
                'BugRegression',
            ]
        )
        choice(
            name: 'log_level',
            choices: [
                'DEBUG',
                'INFO',
                'WARNING',
                'ERROR'
            ]
        )
        choice(
            name: 'monitor',
            choices: [
                '0',
                '1'
            ],
            description: "0 => Headless mode <br>1 => Show in main window <br>"
        )
        choice(
            name: 'worker',
            choices: [
                'win-worker',
                'win-worker1',
                'win-worker2',
                'win-worker3',
                'win-worker4',
            ]
        )
        extendedChoice(
            name: 'test_cases',
            defaultValue: '',
            type: 'PT_CHECKBOX',
            groovyScript: "return [\"${TEST_CASE_LIST.join('", "')}\"]",
            visibleItemCount: 20
        )
        text(
            name: 'manual_input_test_cases',
            defaultValue: '',
            description: '''Input the test case path you want to trigger. (split them by \'\\n\')<br>
                            e.g., <br>
                                00_InitialSetup/0001_InitialSetup.feature<br>
                                01_Role/0101_CreateRoles.feature'''
        )
        choice(
            name: 'test_trigger',
            choices: [
                'specified_test',
                'reset-db',
                'intergration',
                'intergration_with_reset_db',
                'acct_report',
                'acct_report_with_reset_db',
                'bug_regression',
                'hotfix'
            ],
            description: '''when choose 'specified_test', this job will do testcases which ticked below 'test_cases'<br>
                            \"hotfix\" is for GoFreight hotfix, it will trigger autotest on https://fms-hotfix-5.gofreight.co/'''
        )

        text(
            name: 'parallel_cnt',
            defaultValue: '1',
            description: 'Enter the max parallel cnt you wish'
        )

        text(
            name: 'timeout_ratio',
            defaultValue: '3',
            description: 'Enter the ratio of expected runtime you wish for terminating subprocess, e.g., expected runtime is 10 min, timeout_ratio is 3, then the timeout is 30 min'
        )

        text(
            name: 'def_runtime',
            defaultValue: '10m 00s',
            description: 'Enter the default expected runtime you wish for a testcase (only apply when the runtime is not defined in config/test_runtime.yml)'
        )

    }
    triggers {
        parameterizedCron(CRON_SETTINGS)
    }

    stages {
        stage('Delete old build directories') {
            when {
                not {
                    triggeredBy 'BranchIndexingCause'
                }
            }
            steps {
                script {
                    echo "${INFO} Delete old build directories..."

                    try {
                        dir("${ALL_WORKSPACE}"){
                            bat (
                                script: "forfiles /d -30 /c \"cmd /c echo @file && rmdir @file /s /q\"",
                                returnStatus: false
                            )
                        }
                    }
                    catch (Exception error) {
                        echo "${INFO} Not delete any directory this time."
                    }
                }
            }
        }

        stage('Prepare environment') {
            when {
                not {
                    triggeredBy 'BranchIndexingCause'
                }
            }
            steps {
                script {
                    dir("${MY_WORKSPACE}") {
                        git (
                            credentialsId: "gf-qa-github-key",
                            url: 'git@github.com:hardcoretech/gf-qa.git',
                            branch: "${env.GIT_BRANCH}"
                        )
                    }
                    requirement_installing_status = bat (
                        script: "pip install poetry",
                        returnStatus: true
                    )
                    poetry_install_status = bat (
                        script: "poetry install --no-dev",
                        returnStatus: true
                    )
                    echo "${INFO} Requirement Installing Status: ${requirement_installing_status}, ${poetry_install_status}"

                    msg = bat (
                        script: "poetry run python .\\config\\set_variable.py ${COMPANY}.url=${SERVER}",
                        returnStdout: true
                    )
                    echo "${INFO} Set Variables:\033[0m ${msg}"
                }
            }
        }

        stage('Execute auto testing') {
            when {
                not {
                    triggeredBy 'BranchIndexingCause'
                }
            }
            steps {
                script {
                    if (TEST_TRIGGER == "specified_test") {
                        def run_feature_paths = get_feature_file_path()

                        test_trigger_status = bat (
                            script: "poetry run python test_trigger/batch_trigger.py -f ${run_feature_paths} -c ${COMPANY} --tags ${TAGS} -m ${MONITOR} -l ${LOG_LEVEL} -p ${PARALLEL_CNT} -s ${TIMEOUT_RATIO} -drt \"${DEF_RUNTIME}\"",
                            returnStatus: true
                        )
                    }
                    else {
                        def run_test_set_paths = get_run_test_set()

                        test_trigger_status = bat (
                            script: "poetry run python test_trigger/batch_trigger.py -t ${run_test_set_paths} -c ${COMPANY} --tags ${TAGS} -m ${MONITOR} -l ${LOG_LEVEL} -p ${PARALLEL_CNT} -s ${TIMEOUT_RATIO} -drt \"${DEF_RUNTIME}\"",
                            returnStatus: true
                        )
                    }
                    echo "${INFO} Test Trigger Status = ${test_trigger_status}"
                    if (test_trigger_status != 0) {
                        currentBuild.result = 'UNSTABLE'
                        echo "ERROR: There is an error when trigger tests"
                    }
                }
            }
        }

        stage('Publish report') {
            when {
                not {
                    triggeredBy 'BranchIndexingCause'
                }
            }
            steps {
                script{
                    allure ([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                    ])
                }

                publishHTML (
                    target : [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'report',
                        reportFiles: 'report.html',
                        reportName: 'Intergration Test',
                        reportTitles: "${TEST_TRIGGER}"
                    ]
                )
            }
        }
    }

    post {
        success {
            script{
                if (!trigger_by_indexing) {
                    slackSend (
                        tokenCredentialId: SLACK_TOKEN,
                        channel: SLACK_CHANNEL,
                        color: '#9de777',
                        message: "[${currentBuild.fullProjectName}] is successful. :kissing::tada::tada:\n ${SLACK_MSG_DESC} \n(${env.BUILD_URL})"
                    )
                }
            }
        }
        unstable {
            slackSend (
                tokenCredentialId: SLACK_TOKEN,
                channel: SLACK_CHANNEL,
                color: '#f6e430',
                message: "[${currentBuild.fullProjectName}] is unstable. :fearful:\n ${SLACK_MSG_DESC} \n(${env.BUILD_URL})"
            )
        }
        failure {
            slackSend (
                tokenCredentialId: SLACK_TOKEN,
                channel: SLACK_CHANNEL,
                color: '#FF0000',
                message: "[${currentBuild.fullProjectName}] is failed. :dizzy_face: \n ${SLACK_MSG_DESC} \n(${env.BUILD_URL})"
            )
        }

    }
}
