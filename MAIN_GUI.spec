# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\MAIN_GUI.py', 
    'C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\Build\\MAIN_GUI.spec'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\alterCommand.dat', 'Data\\database') ,
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\attributeList.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\attributeType.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\databaseName.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\indexChange.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\selectCommand.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\database\\tableList.dat', 'Data\\database'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\columnName.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\command.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\constraints.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\fk.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\tableName.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\createTable\\type.dat', 'Data\\createTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\Data\\user\\login.dat', 'Data\\user'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\SignInWindow\\SignIn.ui', 'GUI\\SignInWindow'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\DatabaseWindow\\CreateDatabase.ui', 'GUI\\DatabaseWindow'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\DatabaseWindow\\CreateDatabaseMenu.ui', 'GUI\\DatabaseWindow'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\DatabaseWindow\\CreateDatabaseMenu.ui', 'GUI\\DatabaseWindow'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Main.ui', 'GUI\\CrudWindow'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Grouping\\Grouping.ui', 'GUI\\CrudWindow\\Grouping'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Grouping\\SelectAttribute.ui', 'GUI\\CrudWindow\\Grouping'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\SelectTable.ui', 'GUI\\CrudWindow\\Table'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\MainTable\\CreateTable.ui', 'GUI\\CrudWindow\\Table\\MainTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\MainTable\\CreateTable_ColProperties.ui', 'GUI\\CrudWindow\\Table\\MainTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\MainTable\\CreateTable_FK.ui', 'GUI\\CrudWindow\\Table\\MainTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\MainTable\\CreateTableMenu.ui', 'GUI\\CrudWindow\\Table\\MainTable'),
            ('C:\\Users\\wcbre\\Documents\\MAPUA\\Q3\\IT131L\\CRUD-PROJECT\\GUI\\CrudWindow\\Table\\ModifyTable\\ModifyTable.ui', 'GUI\\CrudWindow\\Table\\ModifyTable')
            ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MAIN_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MAIN_GUI',
)
