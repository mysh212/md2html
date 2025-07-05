# Author : ysh
# 2025/07/06 Sun 00:05:22
from core.general import *

import markdown

md = markdown.Markdown(extensions=[
    'extra',
    'toc',
    'codehilite',
    'pymdownx.emoji',
    'mdx_math',
    'customblocks'
], extension_configs={
    'mdx_math': {
        'enable_dollar_delimiter': True,
        'add_preview': True
    }
})

def export(val):
    source = val.path
    filename = val.output_path
    info(f'Exporting from [{source}] to [{filename}]')

def encode(val):
    source = val.path
    filename = val.output_path

    if (filename != ['-'] and len(source) != len(filename)) or (source == ['-'] and len(filename) != 1):
        error('The number of input files does not equals to the output ones')
        quit(-1)

    if source == ['-']:
        pre = []
        while True:
            try:
                pre.append(input())
            except:
                break
        pre = '\n'.join(pre)
        if filename == ['-']: print(md.convert(pre));
        else: write_to_file(filename[0], md.convert(pre));

    info('ouob')