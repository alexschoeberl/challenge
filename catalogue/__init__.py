from catalogue import setup

application = setup.application()
database = setup.database(application)
interface = setup.interface(application)
