import os
import datetime
import xml.etree.ElementTree as ET
import click


@click.group
def cli():
    pass


@click.command
def generate_sitemap():
    " Generate sitemap.xml"
    root = ET.Element('urlset')
    root.attrib['xmlns'] = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    for f in os.listdir("."):
        if not f.endswith(".html"):
            continue
        url = ET.SubElement(root, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = f'https://www.chanmo.me/{f}'
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = datetime.datetime.fromtimestamp(os.path.getmtime(f)).isoformat(timespec='seconds')

    with open('sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(ET.tostring(root, encoding='utf-8'))

    click.echo('done')


cli.add_command(generate_sitemap)


if __name__ == '__main__':
    cli()
