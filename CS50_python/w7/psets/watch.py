"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        id = re.search(
            r"<iframe.*?src=\"(?:https?://)?(?:www.)?youtube\.com/embed/(\w+)\".*?>.*?</iframe>", s)
        return f"https://youtu.be/{id.group(1)}"
    except AttributeError:
        pass


...


if __name__ == "__main__":
    main()
