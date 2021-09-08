from setuptools import setup

APP_NAME = 'Change Cell'
APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    # 'packages': 'et-xmlfile',
    'iconfile': 'app_icon.icns',
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
