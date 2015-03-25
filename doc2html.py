import csv
import json
import lxml


class doc2html(object):
	def __init__(self, doclocation, docname, doctype):
		self.doclocation = doclocation
		self.docname = docname
		self.doctype = doctype
		self.html_header = '<doctype! html>\n<head>\n<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.3.min.js"></script>\n<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.21.2/js/jquery.tablesorter.min.js"></script>\n<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.21.2/css/theme.blue.min.css" />\n<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.21.2/css/theme.green.min.css" />\n<style>tr:nth-child(even) {background: #CCC} tr:nth-child(odd) {background: #FFF}</style>\n<title>' + docname.split('.')[0] + '</title>\n<script>$(document).ready(function(){$("#myTable").tablesorter();});</script>\n</head>\n<body>\n<table id="myTable" class="tablesorter" border="1" cellpadding="5" style="width:100%">'
		self.html_footer = "</table>\n</body>\n<footer>\n<p>Created using htmlsheets</p>\n<p>Software Written By: Jake Sawyer 2105</p>\n</footer>"
		self.html_body = ''

	def create_html(self):
		html_body = ""
		if self.doctype == 'CSV':
			f = open(str(self.doclocation))
			csv_f = csv.reader(f)
			for i, row in enumerate(csv_f):
				if i == 0:
					html_body += "<tr>\n<thead>\n"
					for x in row:
						html_body += '<th>%s</th>\n' % x
					html_body += "</thead>\n</tr>\n<tbody>\n"
				elif i>0:
					html_body += '<tr>\n'
					for x in row:
						html_body += '<td>%s</td>\n' % x
					html_body += '</tr>\n'
			html_body += "</tbody>"
			self.html_body = html_body

		elif self.doctype == 'JSON':
			pass

		elif self.doctype == 'XML':
			pass

	def write_html(self, write_name):
		write_name += ".html"
		with open(write_name, 'w') as f:
			f.write(self.html_header + self.html_body + self.html_footer)
			print("Write complete\nFile Name:\n    %s" % write_name)


