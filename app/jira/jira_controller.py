from jira_lib import JiraApi
from jira_form import JiraForm


class JiraController(object):
    def __init__(self, jira_config):
        self.config = jira_config
        self.existing_tickets = {}
        self.summary = ""
        self.fmt = JiraForm(self.config)
        self.jira_api = JiraApi(self.config)

    def check_ticket_existence(self, event):
        summary = self.fmt.form_summary(event)
        if summary not in self.existing_tickets.keys():
            resp = self.exist_in_jira(summary)
            if resp['issues']:
                self.existing_tickets[summary] = resp["issues"][0]["key"]
            else:
                return False, summary
        print "Ticket: %s already exists in Jira. Ticket id: %s" % (summary,
                                                                    self.existing_tickets[summary])
        return True, self.existing_tickets[summary]

    def create_ticket(self, event, summary):
        ticket = self.fmt.form_ticket(event, summary)
        if ticket:
            resp = self.jira_api.post("/rest/api/2/issue/", ticket)
            try:
                self.existing_tickets[summary] = resp["key"]
            except:
                return None

    def transition_ticket(self, issuekey):
        if not self.config["auto_resolved"]:
            return None
        trans_endpoint = "/rest/api/2/issue/%s/transitions?expand=transitions.fields" % issuekey
        comment_endpoint = "/rest/api/2/issue/%s/comment" % issuekey
        self.jira_api.post(comment_endpoint, self.fmt.form_transition(comment=True))
        self.jira_api.post(trans_endpoint, self.fmt.form_transition())
        return None

    def exist_in_jira(self, summary):
        endpoint = "/rest/api/2/search?jql=summary~'%s'" % (summary)
        return self.jira_api.get(endpoint)

