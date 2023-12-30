import os
import re
import datetime
from pathlib import Path
import subprocess as sp
import pytz
import xml.etree.ElementTree as ET
import click
import shutil
from tqdm import tqdm


@click.group
def cli():
    pass


@click.command
def migrate_to_jekyll():
    for post in tqdm(list(Path('.').iterdir())):
        if post.suffix != '.org':
            continue
        ctime = datetime.date.fromtimestamp(post.stat().st_ctime)
        output = f'_org/_posts/{ctime:%Y-%m-%d}-{post.stem}.org'
        #sp.run(['docker', 'run', '--rm', '--volume', '.:/data', 'pandoc/core', '-i', post.name, '-o', output], check=False)
        # shutil.move(output, '/home/chen/Code/html/chanmo/_posts/')
        shutil.copyfile(post, output)


@click.command
def generate_jekyll_header():
    for post in tqdm(list(Path('_org/_posts/').iterdir())):
        with post.open() as f:
            text = f.read()
            try:
                title = re.search(r'#\+TITLE:(.*)', text).group(0)[8:]
                excerpt = re.search(r'#\+DESCRIPTION:(.*)', text).group(0)[15:]
                keywords = ' '.join([i.strip() for i in re.search(r'#\+KEYWORDS:(.*)', text).group(0)[11:].split(',')])

                text = f"""---
layout: post
title: {title}
excerpt: {excerpt}
keywords: {keywords}
---
"""
                #print(text)
                outfile = Path(f'_posts/{post.stem}.html')
                html = ''
                with outfile.open('r') as f:
                    html = f.read()
                    html = text + html

                if html:
                    with outfile.open('w') as f:
                        f.write(html)

            except Exception as e:
                print(post, e)


@click.command
def generate_sitemap():
    " Generate sitemap.xml"
    root = ET.Element('urlset')
    root.attrib['xmlns'] = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    timezone = pytz.timezone('Asia/Shanghai')
    for f in os.listdir("."):
        if not f.endswith(".html"):
            continue
        url = ET.SubElement(root, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = f'https://www.chanmo.me/{f}'
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = timezone.localize(datetime.datetime.fromtimestamp(os.path.getmtime(f))).isoformat(timespec='seconds')

    with open('sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(ET.tostring(root, encoding='utf-8'))

    click.echo('done')


cli.add_command(generate_sitemap)
cli.add_command(migrate_to_jekyll)
cli.add_command(generate_jekyll_header)

if __name__ == '__main__':
    cli()
