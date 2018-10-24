import sys, os

AI = """from direct.distributed import DistributedObjectAI\n\nclass {0}(DistributedObjectAI.DistributedObjectAI):\n\n\tdef ___init___(self, air):\n\t\tDistributedObjectAI.DistributedObjectAI.__init__(self, air)\n\n\tdef announceGenerate(self):\n\t\tDistributedObjectAI.DistributedObjectAI.announceGenerate(self)\n\n\tdef generate(self):\n\t\tDistributedObjectAI.DistributedObjectAI.generate(self)\n\n\tdef delete(self):\n\t\tDistributedObjectAI.DistributedObjectAI.delete(self)\n\n\tdef disable(self):\n\t\tDistributedObjectAI.DistributedObjectAI.disable(self)\n""".expandtabs(4)

if '--directory' in sys.argv:
    dir = os.path.dirname(os.path.abspath(__file__))

    for distributed in os.listdir(dir):
        print 'file: ' + distributed

        if distributed.startswith("Distributed"):
            print 'Generating AI...'

            distributed = os.path.splitext(distributed)[0]

            with open(distributed + "AI.py", "w") as f:
                f.write(AI.format(distributed + "AI"))
        else:
            print 'Not Distributed!'

else:
    client = sys.argv[1] + "AI"

    with open(client + ".py", "w") as f:
        f.write(AI.format(client))