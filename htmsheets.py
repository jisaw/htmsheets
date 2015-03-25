import argparse
from doc2html import doc2html


FILE_TYPES = ['XML', 'JSON', 'CSV', 'XLS']

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action='store', dest='file_name', help='File name for the csv/json/xml document.')
	parser.add_argument('-n', action='store', dest='name', help='What the output html file will be named')

	return parser.parse_args()


def create_html(location, fname, ftype):
	pass


def main():
	p = parse_arguments()
	if not p.file_name:
		print("Please give the path to the file using the -f flag")
	if p.file_name:
		file_name_list = p.file_name.split('/')
		location = "/".join(file_name_list)
		fname = file_name_list[-1]
		ftype = file_name_list[-1].split('.')[-1].upper()
		if ftype in FILE_TYPES:
			d2h = doc2html(location, fname, ftype)
			d2h.create_html()
			d2h.write_html(p.name)
		#with open(p.file_name, 'r') as f:


if __name__=="__main__":
	main()