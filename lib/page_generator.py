import os
import datetime

import lib.settings


class HtmlPageGenerator(object):

    def __init__(self, successes, failures, host_count):
        self.success = successes
        self.fails = failures
        self.host_count = host_count
        self.html_template = lib.settings.HTML_PAGE_TEMPLATE
        self.attacked_hosts_list = open(lib.settings.HOST_FILE).readlines()

    def _generate_html_table(self, headers):
        retval = '<table id="generatedExploitTable"><tr>'
        for header in headers:
            retval += "<th>{}</th>".format(header)
        retval += "</tr><tr>"
        for value in self.success:
            retval += "<td>{}</td>".format(value)
        retval += "</tr></table>"
        return retval

    def _generate_drop_down_menu(self):
        retval = ""
        for host in self.attacked_hosts_list:
            retval += """<a href="#">{}</a><br>""".format(host.strip())
        return retval

    def generator(self):
        if not os.path.exists(lib.settings.HTML_PAGE_PATH):
            os.makedirs(lib.settings.HTML_PAGE_PATH)
        with open(self.html_template, 'r') as template, open(lib.settings.HTML_PAGE_GENERATION_FILE_PATH, 'a+') as out:
            to_format = template.read()
            out.write(
                to_format.format(
                    date_of_attack=str(datetime.datetime.today()).split(".")[0],
                    exploit_table=self._generate_html_table(["Exploit Paths"]),
                    amount_of_hosts=self.host_count,
                    all_hosts_attacked=self._generate_drop_down_menu()
                )
            )
        return lib.settings.HTML_PAGE_GENERATION_FILE_PATH
