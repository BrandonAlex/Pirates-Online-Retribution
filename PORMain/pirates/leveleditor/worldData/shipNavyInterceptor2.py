from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Objects': {
        '1189043565.22gjeon': {
            'Type': 'Ship Part',
            'Name': 'shipNavyInterceptor2',
            'Category': '2: Sloop',
            'File': '',
            'Flagship': True,
            'Objects': {
                '1189043669.81gjeon': {
                    'Type': 'Spawn Node',
                    'Aggro Radius': '12.0000',
                    'AnimSet': 'default',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-0.47798, -16.46, 20.716),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Area',
                    'Start State': 'Patrol',
                    'Team': 'default',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley' } },
                '1189043707.47gjeon': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(20.385, 11.228, 20.748),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1189043711.91gjeon': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-20.933, 10.802, 20.741),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1189043715.06gjeon': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(0.35698, 26.544, 20.963),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1189043719.16gjeon': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(19.372, -28.727, 20.716),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1189043723.09gjeon': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-16.780, -28.9258, 20.718),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } } },
            'Respawns': True,
            'Team': 'EvilNavy',
            'Visual': {
                'Model': [
                    'models/shipparts/interceptorL2-geometry_High',
                    'models/shipparts/interceptorL2-collisions'] } } },
    'Node Links': [
        [
            '1189043669.81gjeon',
            '1189043711.91gjeon',
            'Bi-directional'],
        [
            '1189043711.91gjeon',
            '1189043715.06gjeon',
            'Bi-directional'],
        [
            '1189043707.47gjeon',
            '1189043715.06gjeon',
            'Bi-directional'],
        [
            '1189043669.81gjeon',
            '1189043707.47gjeon',
            'Bi-directional'],
        [
            '1189043711.91gjeon',
            '1189043723.09gjeon',
            'Bi-directional'],
        [
            '1189043719.16gjeon',
            '1189043707.47gjeon',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1189043565.22gjeon': '["Objects"]["1189043565.22gjeon"]',
        '1189043669.81gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043669.81gjeon"]',
        '1189043707.47gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043707.47gjeon"]',
        '1189043711.91gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043711.91gjeon"]',
        '1189043715.06gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043715.06gjeon"]',
        '1189043719.16gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043719.16gjeon"]',
        '1189043723.09gjeon': '["Objects"]["1189043565.22gjeon"]["Objects"]["1189043723.09gjeon"]' } }
