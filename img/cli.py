import glob, os
import click
from PIL import Image


width = 960

@click.command()
def cli():
    for infile in glob.glob("*.png"):
        file, _ = os.path.splitext(infile)
        with Image.open(infile) as im:
            im = im.convert('RGB')
            im.thumbnail((width,width / im.size[0] * im.size[1]))
            im.save(file + ".jpeg", "JPEG")
            
            


if __name__ == '__main__':
    cli()
