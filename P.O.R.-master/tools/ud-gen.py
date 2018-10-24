import sys, os

UD = """from direct.distributed import DistributedObjectUD\n\nclass {0}(DistributedObjectUD.DistributedObjectUD):\n\n\tdef ___init___(self, air):\n\t\tDistributedObjectUD.DistributedObjectUD.__init__(self, air)\n\n\tdef announceGenerate(self):\n\t\tDistributedObjectUD.DistributedObjectUD.announceGenerate(self)\n\n\tdef generate(self):\n\t\tDistributedObjectUD.DistributedObjectUD.generate(self)\n\n\tdef delete(self):\n\t\tDistributedObjectUD.DistributedObjectUD.delete(self)\n\n\tdef disable(self):\n\t\tDistributedObjectUD.DistributedObjectUD.disable(self)\n""".expandtabs(4)

if '--directory' in sys.argv:
    dir = os.path.dirname(os.path.abspath(__file__))

    for distributed in os.listdir(dir):
        print 'file: ' + distributed

        if distributed.startswith("Distributed"):
            print 'Generating UD...'

            distributed = os.path.splitext(distributed)[0]

            with open(distributed + "UD.py", "w") as f:
                f.write(UD.format(distributed + "UD"))
        else:
            print 'Not Distributed!'

else:
    client = sys.argv[1] + "UD"

    with open(client + ".py", "w") as f:
        f.write(UD.format(client))