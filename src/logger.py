import datetime

class Logger:
	"""
	@brief      Class for logger.

	@example :
		l = Logger()
		l.log("this is msg", "{this_is_data}")
		l.info("this is msg", "{this_is_data}")
		l.error("this is msg", "{this_is_data}")
		l.warn(data="{this_is_data}")
		l.success("this is msg")
	"""

	def __init__(self):
		pass

	def _printLogDict(self, logDict):
		print('{timestamp} : {level:7} : {msg} : {data}'.format(**logDict))

	def _makeLogDict(self, level, msg, data):
		logDict = {}
		logDict["timestamp"] = datetime.datetime.utcnow()
		logDict["level"]	 = level
		logDict["msg"]   = msg
		logDict["data"]		 = data
		return logDict

	def log(self, msg="", data="{}"):
		logDict = self._makeLogDict("log", msg, data)
		self._printLogDict(logDict)

	def info(self, msg="", data="{}"):
		logDict = self._makeLogDict("info", msg, data)
		self._printLogDict(logDict)


	def error(self, msg="", data="{}"):
		logDict = self._makeLogDict("error", msg, data)
		self._printLogDict(logDict)


	def warn(self, msg="", data="{}"):
		logDict = self._makeLogDict("warn", msg, data)
		self._printLogDict(logDict)


	def success(self, msg="", data="{}"):
		logDict = self._makeLogDict("success", msg, data)
		self._printLogDict(logDict)

