# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dota2_pre_check.py'],
             pathex=['C:\\Users\\hzq\\Desktop\\Conda_Projects\\dota2'],
             binaries=[],
             datas=[('dota2.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='dota2_pre_check',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='dota2.ico')
