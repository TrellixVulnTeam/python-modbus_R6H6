# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\大炮\\PycharmProjects\\大作业\\server_\\main.py'],
             pathex=['C:\\Users\\大炮\\PycharmProjects\\大作业\\server_'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas +=(('off.ico','C:\\Users\\大炮\\PycharmProjects\\大作业\\server_\\off.ico','DATA'),
('on.ico','C:\\Users\\大炮\\PycharmProjects\\大作业\\server_\\on.ico','DATA'),
('led_off.ico','C:\\Users\\大炮\\PycharmProjects\\大作业\\server_\\led_off.ico','DATA'),
('led_on.ico','C:\\Users\\大炮\\PycharmProjects\\大作业\\server_\\led_on.ico','DATA'))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
