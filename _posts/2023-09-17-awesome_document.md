---
layout: post
title: "Awesome Document: Dockerize Document Processing"
description: "Dockerize document processing with three awesome Docker images: docker-pandoc, docker-unoserver, and docker-poppler. These images make it easy to convert documents between different formats, refresh the TOC in LibreOffice, and extract text from PDF files."
keywords: docker,pandoc,libreoffice,unoserver,poppler
tags: docker pandoc libreoffice popper
---

Document processing is a common task in many industries, but it can be
time-consuming and complex. Docker can be used to simplify and
streamline document processing by providing a containerized environment
for each tool.

This article will introduce three Docker images for document processing:

[docker-pandoc:](https://github.com/ChanMo/docker-pandoc) A Docker image
for Pandoc, a universal document converter.
[docker-unoserver](https://github.com/ChanMo/docker-unoserver): A Docker
image for LibreOffice, a free and open-source office suite.
[docker-poppler](https://github.com/ChanMo/docker-poppler): A Docker
image for Poppler, a PDF library.

## docker-pandoc

docker-pandoc is a Docker image for Pandoc, a universal document
converter. Pandoc can convert between many different document formats,
including Markdown, HTML, PDF, and LaTeX.

Start the API server

``` {.bash}
docker run --rm -p 5000:5000 chanmo/pandoc
```

Convert the DOCX file to HTML format, by httpie

``` {.bash}
http -f POST :5000/convert/html file@~/demo.docx
```

[github](https://github.com/ChanMo/docker-poppler),
[docker](https://hub.docker.com/r/chanmo/poppler)

## docker-unoserver

docker-unoserver is a Docker image for LibreOffice, a free and
open-source office suite. LibreOffice includes a variety of applications
for word processing, spreadsheets, presentations, and more.

Start the API server

``` {.bash}
docker run -p 5000:5000 chanmo/unoserver  
```

convert a docx file to the pdf format

``` {.bash}
http -f POST :5000/convert/pdf file@/path/to/demo.docx -o demo.pdf
```

If you just want to refresh the TOC in a docx file.

``` {.bash}
http -f POST :5000/convert/docx file@/path/to/demo.docx -o demo.docx
```

[github](https://github.com/ChanMo/docker-unoserver),
[docker](https://hub.docker.com/r/chanmo/unoserver)

## docker-poppler

docker-poppler is a Docker image for Poppler, a PDF library. Poppler can
be used to render, split, and merge PDF files.

Start the API server

``` {.bash}
docker run --rm -p 5000:5000 chanmo/poppler
```

convert a pdf file to the html format

``` {.bash}
http -f POST :5000/pdftohtml file@/path/to/file.pdf -o demo.html
```

convert a pdf file to the text string

``` {.bash}
http -f POST :5000/pdftotext file@/path/to/file.pdf
```

convert a pdf file to multiple images

``` {.bash}
http -f POST :5000/pdftocairo file@/path/to/file.pdf
```

get a pdf file information

``` {.bash}
http -f POST :5000/pdfinfo file@/path/to/file.pdf  
```

[github](https://github.com/ChanMo/docker-poppler),
[docker](https://hub.docker.com/r/chanmo/poppler)

## Conclusion

Docker can be used to simplify and streamline document processing by
providing a containerized environment for each tool. The three Docker
images introduced in this article can be used to perform a variety of
document processing tasks, including converting documents between
different formats, refresh the TOC in LibreOffice, and extracting text
from PDF files.
