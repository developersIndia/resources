#!/usr/bin/env python

''' Simple script to auto-generate the README.md file for developersIndia Wiki'''

from __future__ import print_function
import os

EMOJIS = {
    "development": ':man_technologist:',
    "languages": ':computer:',
    "jobs": ':file_cabinet:',
    "miscellaneous": ':large_blue_circle:',
}


HEADER = '''# Developers India Wiki

> The Developers India Wiki for some cool & useful resources.


![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![open-source-love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges)
[![GitHub license](https://img.shields.io/github/license/developersIndia/wiki)](https://github.com/developersIndia/wiki/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/developersIndia/wiki?color=purple)](https://github.com/developersIndia/wiki/graphs/contributors)
[![Discord](https://img.shields.io/discord/669880381649977354?color=blue)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/developersIndia?style=social)](https://www.reddit.com/r/developersIndia/)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Furl%3Dhttps%3A%2F%2Fgithub.com%2FdevelopersIndia%2Fwiki%26text%3DThe%2520Developers%2520India%2520Wiki%2520is%2520full%2520of%2520cool%2520resources%2520to%2520learn%2520new%2520things)](https://twitter.com/intent/tweet?url=https://github.com/developersIndia/wiki&text=Developers%20India%20Wiki%20has%20some%20cool%20resources%20!!)

Find below some of the best and popular resources for learning new technologies/programming languages.
'''

FOOTER = '''# 📜 License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

# 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.

'''


def get_contributors():
    with open('CONTRIBUTORS.md') as file:
        return str(file.read())


def get_list_of_categories():
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and
            '.git' not in x and x != '.github']
    return dirs


def get_title(function_file):
    with open(function_file) as _file:
        for line in _file:
            line = line.strip()
            if line.startswith('#'):
                return line[1:].lstrip()  # text after # and whitespace


def get_subcategories(category):
    files = [x for x in os.listdir(category)]
    titles = []
    for filename in files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith('.md'):
            title = get_title(fullname)
            titles.append((title, fullname))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_subcategories(category)
        categories[category] = titles
        count += len(titles)
    return count, categories


def print_file(category_names, count, categories):
    with open('README.md', 'w') as file_:
        file_.write(HEADER)
        file_.write('\n')

        for category in sorted(category_names):
            file_.write('* [{0}](#{1}) '.format(category,
                                                category))
            file_.write(EMOJIS[category] + '\n')

        file_.write('''
---

''')
        for category in sorted(category_names):
            file_.write('### {0} '.format(category.capitalize()))
            file_.write('\n')
            file_.write('<details><summary>View contents</summary>\n<ol>\n')
            tils = categories[category]
            for (title, filename) in sorted(tils):
                file_.write(
                    '<li><a href="{0}"><code>{1}</code></a></li>\n'.format(filename, title))
            file_.write('\n</ol>\n</details>\n\n')

        file_.write(FOOTER)
        file_.write('\n')
        file_.write(get_contributors())


def create_readme():
    category_names = get_list_of_categories()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)


if __name__ == '__main__':
    create_readme()
