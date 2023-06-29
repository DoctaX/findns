import argparse


def get_args() -> dict:
    parser = argparse.ArgumentParser(description='Request a domains DNS info')
    parser.add_argument('-d', '--domain', help='The target domain', required=True)
    parser.add_argument('-a', '--allrecords', help='Specify this argument to return all found records for this domain',
                        action='store_true')
    parser.add_argument('-A', '--arecords', help='Specify this argument to return the domains A records',
                        action='store_true')
    parser.add_argument('-MX', '--mxrecords', help='Specify this argument to return the domains MX records',
                        action='store_true')
    parser.add_argument('-PTR', '--ptrrecords', help='Specify this argument to return the domains PTR records',
                        action='store_true')
    parser.add_argument('-CNAME', '--cnamerecords', help='Specify this argument to return the domains CNAME records',
                        action='store_true')
    parser.add_argument('-TXT', '--txtrecords', help='Specify this argument to return the domains TXT records',
                        action='store_true')
    parser.add_argument('-SRV', '--srvrecords', help='Specify this argument to return the domains SRV records',
                        action='store_true')
    parser.add_argument('-NS', '--nsrecords', help='Specify this argument to return the domains NS records',
                        action='store_true')

    args = vars(parser.parse_args())

    return args
