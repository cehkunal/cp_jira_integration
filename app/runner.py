import jira
import lib
import sys
import logging


sys.stdout = lib.Logger(logging.info)
sys.stderr = lib.Logger(logging.warning)

# Build config
config = lib.ConfigHelper()

# Halo events
events = lib.HaloEvents(config)

# Matcher object
matcher = lib.Matcher(config.match_list)

jira = jira.JiraController(config.jira)

# Iterate over events, quarantine targeted workloads

while True:
    for event in events:
        if matcher.is_a_match(event["type"]):
            exist, summary = jira.check_ticket_existence(event)
            if event["type"] == "issue_resolved" and exist:
                jira.transition_ticket(summary)
            elif event["type"] != "issue_resolved" and not exist:
                jira.create_ticket(event, summary)
