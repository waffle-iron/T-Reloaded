from setuptools import setup

about = {}
with open('reloaded/__about__.py') as f:
    exec(f.read(), about)

packages = [
    about['__title__'],
]

setup(
    author=about['__author__'],
    author_email=about['__author_email__'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 10'
        'Programming Language :: Python',
        'Topic :: Office/Business',
    ],
    description=about['__description__'],
    license=about['__license__'],
    long_description=open('README.rst').read(),
    name=about['__title__'],
    version=about['__version__'],
    packages=packages,
    platforms='any',
    url=about['__url__'],
)
