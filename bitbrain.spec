from kivy.deps import sdl2, glew

# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\spark\\OneDrive\\Desktop\\SheInnovatesHackathon\\main.py'],
             pathex=['C:\\Users\\spark\\OneDrive\\Desktop\\SheInnovatesHackathon'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='bitbrain',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          )
coll = COLLECT(exe, Tree('C:\\Users\\spark\\OneDrive\\Desktop\\SheInnovatesHackathon'), 
               a.binaries,
               a.zipfiles,
               a.datas,*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='bitbrain')
