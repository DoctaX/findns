import main
import args
from logo import logo

print(logo)

# Get command line arguments
args = args.get_args()

domain = args['domain']

if args['allrecords'] is True:
    for key in args.keys():
        args[key] = True

if args['arecords'] is True:
    print("\n" + domain, "A Records:\n")
    records = main.return_records(domain, 'A')

if args['mxrecords'] is True:
    print("\n" + domain, "MX Records:\n")
    records = main.return_records(domain, 'MX')

if args['ptrrecords'] is True:
    print("\n" + domain, "PTR Records:\n")
    records = main.return_records(domain, 'PTR')

if args['cnamerecords'] is True:
    print("\n" + domain, "CNAME Records:\n")
    records = main.return_records(domain, 'CNAME')

if args['txtrecords'] is True:
    print("\n" + domain, "TXT Records:\n")
    records = main.return_records(domain, 'TXT')

if args['srvrecords'] is True:
    print("\n" + domain, "SRV Records:\n")
    records = main.return_records(domain, 'SRV')

if args['nsrecords'] is True:
    print("\n" + domain, "NS Records:\n")
    records = main.return_records(domain, 'NS')

