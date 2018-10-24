To use the production Astron, you must have these things:

1. A Linux distro that uses apt-get.

2. Panda3D for Linux (make sure it supports .deb files): http://loudstore.s3.amazonaws.com/panda3d1.9_1.9.0_amd64.deb (NOTE: This is so that the uberdog and ai servers work.)

3. The Mongo driver (you only really need the .so file in lib): http://loudstore.s3.amazonaws.com/mongo-driver.zip

4. Boost. To get this run: sudo apt-get install libboost1.55-all-dev

You also need an Astron configuration that has a valid string to connect to Mongo.

EXAMPLE: 
	backend: mongodb
	server: mongodb://127.0.0.1:27017/test
	
127.0.0.1 being the address of your running Mongo database, 27017 being the port, and test being the database name.

If Panda3D says dependencies are missing, then apt-get those dependencies. I expect you to have basic knowledge of how to do these things.

You also of course need MongoDB: sudo apt-get install mongodb

I am unsure whether or not we will be using PyMongo, but we may need that eventually: sudo pip install pymongo

If you don't have pip: sudo apt-get install pip

However, if you're running Linux, you don't have to! The Astron files are already there in the Astron directory.
