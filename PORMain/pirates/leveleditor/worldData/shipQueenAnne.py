from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
objectStruct = {
    'Objects': {
        '1302550960.6jubutler': {
            'Type': 'Ship Part',
            'Name': 'shipQueenAnne',
            'Category': "55: Queen Anne's Revenge",
            'Flagship': False,
            'LogoOverride': '-1: Default',
            'Objects': {
                '1302551043.33jubutler': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'AuraFX': 'None',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(1.39, -20.734, 25.053),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropFXLeft': 'None',
                    'PropFXRight': 'None',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'VoodooZombie T4',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley' },
                    'spawnTimeBegin': 0.0,
                    'spawnTimeEnd': 0.0 },
                '1302551224.75jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-11.023, -45.302, 24.596),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551245.21jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(7.6059, -45.433, 24.594),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551263.39jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-8.734, 6.623, 25.561),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551267.54jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(7.827, 5.195, 25.535),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } } },
            'Respawns': True,
            'StyleOverride': '-1: Default',
            'Team': 'Player',
            'VisSize': '',
            'Visual': {
                'Model': [
                    'models/shipparts/interceptorL1-geometry_High',
                    'models/shipparts/interceptorL1-collisions'] } } },
    'Node Links': [
        [
            '1302551267.54jubutler',
            '1302551245.21jubutler',
            'Bi-directional'],
        [
            '1302551267.54jubutler',
            '1302551263.39jubutler',
            'Bi-directional'],
        [
            '1302551267.54jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551245.21jubutler',
            '1302551224.75jubutler',
            'Bi-directional'],
        [
            '1302551245.21jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551224.75jubutler',
            '1302551263.39jubutler',
            'Bi-directional'],
        [
            '1302551224.75jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551263.39jubutler',
            '1302551043.33jubutler',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1302550960.6jubutler': '["Objects"]["1302550960.6jubutler"]',
        '1302551043.33jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551043.33jubutler"]',
        '1302551224.75jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551224.75jubutler"]',
        '1302551245.21jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551245.21jubutler"]',
        '1302551263.39jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551263.39jubutler"]',
        '1302551267.54jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551267.54jubutler"]' } }
extraInfo = {
    'camPos': Point3(86.5114, -47.7759, 129.218),
    'camHpr': VBase3(69.1049, -42.2173, 0),
    'focalLength': 1.39951908588,
    'skyState': 2,
    'fog': 0 }
