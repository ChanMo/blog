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
    for f in os.listdir("."):
        if not f.endswith(".html"):
            continue
        url = ET.SubElement(root, "url")
        url.attrib['loc'] = f
        url.attrib['lastmod'] = datetime.datetime.fromtimestamp(os.path.getmtime(f)).isoformat()

    with open('sitemap.xml', 'wb') as f:
        f.write(ET.tostring(root, encoding='utf-8'))

    click.echo('done')


cli.add_command(generate_sitemap)


if __name__ == '__main__':
    cli()
