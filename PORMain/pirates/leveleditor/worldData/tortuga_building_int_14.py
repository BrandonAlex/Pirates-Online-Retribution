from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Interact Links': [
        [
            '1186512896.0dxschafe',
            '1186513024.0dxschafe',
            'Bi-directional']],
    'Objects': {
        '1156267951.67dzlu0': {
            'Type': 'Building Interior',
            'Name': '',
            'AdditionalData': [
                'interior_spanish_office_b'],
            'Instanced': True,
            'Objects': {
                '1186512896.0dxschafe': {
                    'Type': 'Searchable Container',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-0.576, -4.7358, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/props/desk_gov' },
                    'searchTime': '6.0',
                    'type': 'Desk' },
                '1186513024.0dxschafe': {
                    'Type': 'Spawn Node',
                    'Aggro Radius': '12.0000',
                    'AnimSet': 'idleB',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '2.7892',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(11.587, -10.981, 0.0),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Navy - Guard',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley' } },
                '1209159389.84dxschafe': {
                    'Type': 'Door Locator Node',
                    'Name': 'door_locator',
                    'Hpr': VBase3(178.916, 0.0, 0.0),
                    'Pos': Point3(-13.404, 47.298, 5.0380),
                    'Scale': VBase3(1.0, 1.0, 1.0) },
                '1209159457.0dxschafe': {
                    'Type': 'Interior_furnishings',
                    'DisableCollision': False,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(0.98198, 25.722, 5.264),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/props/interior_wall_spanish' } } },
            'Visual': {
                'Model': 'models/buildings/interior_spanish_store' } } },
    'Node Links': [],
    'Layers': { },
    'ObjectIds': {
        '1156267951.67dzlu0': '["Objects"]["1156267951.67dzlu0"]',
        '1186512896.0dxschafe': '["Objects"]["1156267951.67dzlu0"]["Objects"]["1186512896.0dxschafe"]',
        '1186513024.0dxschafe': '["Objects"]["1156267951.67dzlu0"]["Objects"]["1186513024.0dxschafe"]',
        '1209159389.84dxschafe': '["Objects"]["1156267951.67dzlu0"]["Objects"]["1209159389.84dxschafe"]',
        '1209159457.0dxschafe': '["Objects"]["1156267951.67dzlu0"]["Objects"]["1209159457.0dxschafe"]' } }
extraInfo = {
    'camPos': Point3(4.40847, -60.5987, 22.7239),
    'camHpr': VBase3(3.5387, -10.686, 2.06348e-006),
    'focalLength': 1.3999999761599999,
    'skyState': -1,
    'fog': 0 }
