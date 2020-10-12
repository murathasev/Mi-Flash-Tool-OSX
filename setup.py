from setuptools import setup

OPTIONS = {
 'iconfile':'logoapp.icns',
 'argv_emulation': True,
}

setup(
app=["miflashtool.py"],
setup_requires=["py2app"],
options={'py2app': OPTIONS},
)