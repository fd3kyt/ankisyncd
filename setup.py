from setuptools import setup


def get_anki_bundled_files():
    import os
    data_files = []
    for root, dirs, files in os.walk('anki-bundled'):
        data_files.append((root, [os.path.join(root, f) for f in files]))
    return data_files


setup(
    name="ankisyncd",
    version="2.1",
    description="A personal Anki sync server" +
    "(so you can sync against your own server rather than AnkiWeb)",
    license='COPYING',
    author="David Snopek",
    author_email="dsnopek@gmail.com",
    url="https://github.com/fd3kyt/ankisyncd",
    install_requires=[
        "WebOb>=0.9.7",
    ],
    data_files=get_anki_bundled_files()+["ankisyncd.conf"],
    zip_safe=False,
    scripts=['ankisyncctl.py'],
    packages=['ankisyncd'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Utilities',
    ],
)
