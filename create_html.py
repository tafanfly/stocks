from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

# headers = ["City name", "Area", "Population", "Annual Rainfall"]
# rows = [
#     ["Brisbane", 5905, 1857594, 1146.4],
#     ["Adelaide", 1295, 1158259, 600.5],
#     ["Darwin", 112, 120900, 1714.7],
#     ["Hobart", 1357, 205556, 619.5],
#     ["Sydney", 2058, 4336374, 1214.8],
#     ["Melbourne", 1566, 3806092, 646.9],
#     ["Perth", 5386, 1554769, 869.4],
# ]
class renderHtmlTable(object):
    def __init__(self):
        self.table = Table()
        self.html_name = "table_base.html"
        self.title = ""
        self.subtitle = ""

    def set_html_name(self, name):
        self.html_name = name

    def set_html_header(self, header):
        self.header = header

    def set_html_body(self, body):
        self.body = body

    def set_table_title(self, title):
        self.title = title

    def set_table_subtitle(self, subtitle):
        self.subtitle = subtitle

    def render_table(self):
        self.table.add(self.header, self.body)
        self.table.set_global_opts(
            title_opts=ComponentTitleOpts(title=self.title, subtitle=self.subtitle))
        self.table.render(self.html_name)
