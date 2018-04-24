# CloudPassage - Jira Integration

Version: *1.0*


## Purpose

This integration tool monitors the /v1/events endpoint in the Halo API,
looking for software vulnerabilities, configuration management and issue resolved events.
If a targeted event is matched, the tool will automatically create a jira ticket with revelant
information or resolved a jira ticket.

## How it works

When the end of the events stream is reached, this tool continue to query
until more events arrive.  If you do not set the `HALO_EVENTS_START`
environment variable, the tool will start at the beginning of the current day.

## Prerequisites

* You'll need an account with CloudPassage Halo.
* Make sure that your policies are configured to create events on failure.
* You'll need an auditor (read) API key for your Halo account.
* You'll need a JIRA account

## Using the tool
Clone the code:

        git clone https://github.com/cloudpassage-community/cp_jira_integration
        cd cp_jira_integration
        python app/runner.py

Configure your JIRA information in `configs/config.yml`

Set these environment variables:

| Variable            | Purpose                                              |
|---------------------|------------------------------------------------------|
| HALO_API_KEY        | Halo API key ID                                      |
| HALO_API_SECRET_KEY | Halo API key secret                                  |


Optionally, define these as well:

| Variable            | Purpose                                   |
|---------------------|-------------------------------------------|
| HALO_EVENTS_START   | ISO8601 timestamp for starting event      |



## Setup Config.yml
| Variable            | Purpose                                                  |
|---------------------|-----------------------------------------    |
| url                 | Jira Cloud url. i.e. https://cloudpassagecs.atlassian.net|
| user                | Jira Username                                                          |
| password            | Jira Password                                                     |
| project_key         | Jira Project Key                                                      |
| issue_name          | Jira Issue Name. i.e. Bug, Improvement                                                     |
| auto_resolved       | Boolean. Auto-resolved ticket based on CloudPassage Scan result                                                     |
| supress_threshold   | Integer. Surppress ticket creation if CVSS score is lower than supress_threshold                                                  |
| sva_severity        | Key-value pair (Priority: CVSS score). Associate CVSS score with your Jira priorities. i.e. Highest: 9, High: 7, Medium: 4, Low: 2                                                      |
| event_severity      | Key-value pair (Critical: Priority). Associate event criticality with your Jira priorities. i.e. critical: High, non_critical: Low                                                     |
| resolution_workflow | This section is highly customized. Auto-resolved will read this setting and perform based on your project workflow. You will be able to set comment and Jira transition id.                                                     |


<!---
#CPTAGS:community-supported automation
#TBICON:images/python_icon.png
-->
