from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Objects': {
        '1195522163.95gjeon': {
            'Type': 'Ship Part',
            'Name': 'shipGoliath',
            'Category': '53: The Goliath',
            'File': '',
            'Flagship': True,
            'Objects': {
                '1204765119.55piwanow': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(8.7731, 145.617, 94.688),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Noob Skeleton',
                    'Start State': 'Patrol',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley' } } },
            'Respawns': False,
            'Team': 'Player',
            'Visual': {
                'Model': [
                    'models/shipparts/goliath-geometry_High',
                    'models/shipparts/goliath-collisions',
                    'models/shipparts/goliath-collisions',
                    'models/shipparts/goliath-geometry_High'] } } },
    'Node Links': [
        [
            '1197502455.56piwanow',
            '1197507700.02piwanow',
            'Bi-directional'],
        [
            '1197502504.69piwanow',
            '1197502455.56piwanow',
            'Bi-directional'],
        [
            '1197502504.69piwanow',
            '1197507764.84piwanow',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1195522163.95gjeon': '["Objects"]["1195522163.95gjeon"]',
        '1197502455.56piwanow': '["Objects"]["1195522163.95gjeon"]["Objects"]["1197502455.56piwanow"]',
        '1197502504.69piwanow': '["Objects"]["1195522163.95gjeon"]["Objects"]["1197502504.69piwanow"]',
        '1197507700.02piwanow': '["Objects"]["1195522163.95gjeon"]["Objects"]["1197507700.02piwanow"]',
        '1197507764.84piwanow': '["Objects"]["1195522163.95gjeon"]["Objects"]["1197507764.84piwanow"]',
        '1204765119.55piwanow': '["Objects"]["1195522163.95gjeon"]["Objects"]["1204765119.55piwanow"]' } }
extraInfo = {
    'camPos': Point3(539.557, -352.226, 493.809),
    'camHpr': VBase3(57.1946, -30.6598, 0),
    'focalLength': 1.3999999761599999 }
