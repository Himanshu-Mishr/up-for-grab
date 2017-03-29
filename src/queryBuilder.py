ROOT_URL = "https://api.github.com"

API_PATH = "/search/issues"


class QueryBuilder:

	def __init__(self, ROOT_URL=ROOT_URL, API_PATH=API_PATH):
		self.ROOT_URL = ROOT_URL
		self.API_PATH = API_PATH

	def printParam(self):
		print(self.ROOT_URL, self.API_PATH)

	def getQueryURL(self, queryList=list()):
		"""
		@brief      Gets the query url.

		@param      self       The object
		@param      queryList  ['is:issue', 'label:open']

		@return     The query url.
		"""
		queryStr = ""
		queryListLength = len(queryList)
		count = 0
		for param in queryList:
			count += 1
			if count ==  queryListLength:
				queryStr += param
			else:
				queryStr += param + "+"

		queryURL = self.ROOT_URL + self.API_PATH + "?q=" + queryStr
		return queryURL
