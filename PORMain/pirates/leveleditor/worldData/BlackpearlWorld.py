from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Objects': {
        '1171761196.78sdnaik': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1171761224.13sdnaik': {
                    'Type': 'Island',
                    'Name': 'Black Pearl Island',
                    'File': 'BlackpearlIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1171940948.2sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(0.0, 0.0, 210.853),
                            'Radi': [
                                9000.0,
                                25000.0,
                                40000.0],
                            'Scale': VBase3(1.0, 1.0, 1.0) } },
                    'Pos': Point3(0.0, 0.0, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/pir_m_are_isl_pearl' } },
                '1205374848.0jubutler1': {
                    'Type': 'Avoid Sphere',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Object Avoided': '1171761224.13sdnaik',
                    'Pos': Point3(200.698, -2705.773, 0.0),
                    'Scale': VBase3(4778.850, 4778.850, 4778.850) } },
            'Visual': { } } },
    'Layers': { },
    'ObjectIds': {
        '1171761196.78sdnaik': '["Objects"]["1171761196.78sdnaik"]',
        '1171761224.13sdnaik': '["Objects"]["1171761196.78sdnaik"]["Objects"]["1171761224.13sdnaik"]',
        '1171940948.2sdnaik': '["Objects"]["1171761196.78sdnaik"]["Objects"]["1171761224.13sdnaik"]["Objects"]["1171940948.2sdnaik"]' } }
extraInfo = {
    'camPos': Point3(-10992.9, 77281.3, 67183.3),
    'camHpr': VBase3(-170.958, -41.2584, 0),
    'focalLength': 1.3999999761599999 }
