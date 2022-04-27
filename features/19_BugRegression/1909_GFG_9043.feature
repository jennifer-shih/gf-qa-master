Feature: [Bug Regression] GFG_9043

[TNR] For Balance Sheet & Aging Report, 同日期區間下, AR <=> Accounts Receivable & AP <=> Accounts Payable 金額應一致
https://hardcoretech.atlassian.net/browse/GFG-9043

# Scenario: For Balance Sheet & Aging Report, when in the same date interval, Accounts Receivable = AR & Accounts Payable = AP
#     Given DB is reset to aws-sfi-gofreight / fms / backup.sql.gz-20210127
#      When the user go to Balance Sheet page, click print button and 'As of' date is today
#       And the user go to Aging Report page, only select 'A/R' for 'Aging Report Type', choose 'Post Date' for 'Ending Date' and click Print button
#       And the user go to Aging Report page, only select 'A/P' for 'Aging Report Type', choose 'Post Date' for 'Ending Date' and click Print button
#      Then 'ACCOUNTS RECEIVABLE' of Balance Sheet should equal to A/R 'Balance Amount' of Aging Report
#       And 'ACCOUNTS PAYABLE' of Balance Sheet should equal to A/P 'Balance Amount' of Aging Report
