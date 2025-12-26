# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['../app/main.py'],  # script principal
    pathex=['..'],       # racine du projet
    binaries=[],
    datas=[
        ('../app/*.py', 'app'),  # tous les fichiers .py de app/ sont inclus
    ],
    hiddenimports=[
        'smartcard.System',
        'smartcard.util',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'unittest',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CARTEIDLECTEUR',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='CARTEIDLECTEUR',
)
