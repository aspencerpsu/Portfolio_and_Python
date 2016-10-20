import logging

log = logging.getLogger(__name__)

log.addHandler(logging.StreamHandler())

def app_factory(global_options, **local_options):
	return app

def app(environ, start_response):
	start_response("200 OK", [])
	log.debug("DEBUG INFORMATION!")
	log.info("Information!")
	log.warn("Warning!")
	log.error("ERROR PROCESSED!")
	return ["\nCHECK SETTINGS WITHIN FRAMEWORK\n"]
