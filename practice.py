from optparse import OptionParser 
parser= OptionParser()

parser.add_option("-n","--names", dest="name_arg", help="")

(options, args) = parser.parse_args()

print options.name_arg






