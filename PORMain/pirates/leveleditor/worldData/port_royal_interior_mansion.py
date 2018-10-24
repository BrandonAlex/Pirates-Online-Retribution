from pandac.PandaModules import Point3, VBase3
objectStruct = {
    'Interact Links': [],
    'Objects': {
        '1168033330.17kmuller0': {
            'Type': 'Building Interior',
            'Name': 'port_royal_interior_mansion',
            'AdditionalData': [
                'interior_mansion'],
            'Instanced': True,
            'Objects': {
                '1171325040.86MAsaduzz': {
                    'Type': 'Townsperson',
                    'Category': 'Cast',
                    'AnimSet': 'sit_write',
                    'CustomModel': 'models/char/es_2000',
                    'Hpr': VBase3(-27.527, 0.0, 0.0),
                    'Pos': Point3(-0.101, -8.0860, -0.0280),
                    'Private Status': 'All',
                    'Respawns': True,
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Start State': 'Idle',
                    'Team': 'Villager' },
                '1176937728.0dxschafe': {
                    'Type': 'Interactive Prop',
                    'Hpr': VBase3(179.866, 0.0, 0.0),
                    'Objects': { },
                    'Pos': Point3(0.274, -9.202, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/props/chair_fancy' },
                    'interactAble': 'npc',
                    'interactType': 'sit_write' } },
            'Visual': {
                'Model': 'models/buildings/interior_mansion_gov' } } },
    'Node Links': [],
    'Layers': { },
    'ObjectIds': {
        '1168033330.17kmuller0': '["Objects"]["1168033330.17kmuller0"]',
        '1171325040.86MAsaduzz': '["Objects"]["1168033330.17kmuller0"]["Objects"]["1171325040.86MAsaduzz"]',
        '1176937728.0dxschafe': '["Objects"]["1168033330.17kmuller0"]["Objects"]["1176937728.0dxschafe"]' } }
