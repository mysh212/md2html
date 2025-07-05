from core.general import *

import lib.export as export

import argparse


def init():
    ps = argparse.ArgumentParser()

    sp = ps.add_subparsers(title = 'Actions', description = 'Actions you\'d like me to do')

    ep = sp.add_parser('export', help = 'Export Markdown files into HTML')
    # ep.add_argument('-e', '--export', action = 'store_true', help = 'Export Markdown files into HTML')
    ep.set_defaults(check = export.export)
    ep.add_argument('-f', '--path', type = str, default = 'source', nargs = '?')
    ep.add_argument('-o', '--output-path', type = str, default = 'public', nargs = '?')

    pt = sp.add_parser('print', help = 'Export single Markdown file to HTML')
    # ep.add_argument('-p', '--print', action = 'store_true', help = 'Export single Markdown file to HTML')
    pt.set_defaults(check = export.encode)
    pt.add_argument('-f', '--path', type = str, required = True,  nargs = '+')
    pt.add_argument('-o', '--output-path', type = str, required = True, nargs = '+')

    val = ps.parse_args()
    debug(val)
    return val, val.check

if __name__ == '__main__':
    val, check = init()
    check(val)
