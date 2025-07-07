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
        # 'add_preview': True
    }
})

def make_css():
    ans = []
    for i in [i for i in ls('data') if i.endswith('.css')]:
        ans.append(read_from_file(f'data/{i}'))
    return '\n\n'.join(ans)

def make_html(html: str, template: str = read_from_file('data/template.html') if exist('data/template.html') else '[html]') -> str:
    return template.replace('[html]', html).replace('[style]', make_css())

def export(val):
    source = val.path
    filename = val.output_path
    info(f'Exporting from [{source}] to [{filename}]')

    if not exist(source):
        error(f'{source} not exist')
        exit(-1)

    mkdir(filename)
    q = [i for i in ls(source) if i.endswith('.md')]
    t = 0
    for i in q:
        t = t + 1
        info(f'[{t}/{len(q)}] Exporting {i}', end = '\r')

        des = i.replace('.md', '.html')
        write_to_file(f'{filename}/{des}', make_html(md.convert(read_from_file(f'{source}/{i}'))))

    info(f'Finished exporting {len(q)} Files')
    
    return

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
        else: write_to_file(filename[0], make_html(md.convert(pre)));

    info('ouob')