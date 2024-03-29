---
layout: post
title: Write Your Blog Faster and Smarter with Org Mode
description: How to use Org Mode to write a blog website that is both readable and SEO-friendly. Learn how to create a blog website with Org Mode, including tips on how to optimize your posts for search engines.
keywords: org mode, blog website, seo, blogging, emacs, writing, readability, keywords, metadata, search engines
tags: orgmode, emacs, web, blog
---

Org Mode is a powerful tool that can be used to write blog posts, manage
projects, and track tasks. In this blog post, I will show you how to use
Org Mode to create a blog website that is both readable and
SEO-friendly.

## What is Org Mode

Org Mode is a mode for Emacs that allows you to create structured notes.
These notes can be organized into headings, lists, and tables. You can
also use Org Mode to track tasks, set deadlines, and attach files.

## Why Use Org Mode for a Blog Website?

There are many reasons why you might want to use Org Mode for a blog
website. Here are a few of the benefits:

-   **Powerful and flexible**: Org Mode is a very powerful tool that can
    be used to do a variety of things. It is also very flexible, so you
    can customize it to fit your needs.
-   **Extensible**: Org Mode is extensible, so you can add new features
    and functionality. There are many plugins available that can extend
    Org Mode\'s capabilities.
-   **Easy to use**: Org Mode is relatively easy to learn. The syntax is
    simple, and there are many resources available to help you get
    started.
-   **SEO-friendly**: Org Mode can be used to create blog posts that are
    both readable and SEO-friendly. This is because Org Mode allows you
    to easily add keywords and other metadata to your posts.

## How to Use Org Mode for a Blog Website

### Write an article

Create a new Org file and set the properties for your blog. This
includes the title of your blog, the author name, and the base directory
for your blog posts.

### Export your Org file to HTML

Use `C-c C-e h h` to generate a html file, that you can host on your own
server or on a service like GitHub Pages.

### Publish to the web

create a public repository in github, then add your html files, enable
to use github page, and your articles are published.

## SEO Tips for Org Mode Blog Posts

Here are some additional tips to make your Org Mode blog posts more
SEO-friendly:

-   Use relevant keywords throughout your blog posts.
-   Optimize the title and meta description for search engines.
-   Internally link to other relevant blog posts on your site.
-   Promote your blog website on social media and other channels.

### \[Optional\] create the sitemap.xml file

A sitemap is a file that provides a map of a website\'s pages to search
engines. It helps search engines crawl and index your website more
efficiently, which can improve your website\'s search engine ranking.

You can use this script to generate the file sitemap.xml

``` {.python}
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
```

You can download this script directly from
[cli.py](https://github.com/ChanMo/blog/blob/main/cli.py) on Github.
Remember to replace `https://www.chanmo.me/` with your domain.

``` {.bash}
python cli.py generate-sitemap
```

## Make your blog more modern and mobile-friendly

### Add a css file

you can use [Bulma.css](https://bulma.io/documentation/), a simple and
great CSS framework.

Edit `init.el`, add this

    (setq org-html-head "<link rel='stylesheet' href='app.css'>")

### Create a beautiful home page

You can use orgmode to generate an index.html file to list your
articles. However, the index.html file may not look good as a blog home
page.

You can create a beautiful index.html file by using HTML, CSS, and
Javascript.

## Links

-   [The Org Manual](https://orgmode.org/manual/)
-   [cli.py](https://github.com/ChanMo/blog/blob/main/cli.py)
