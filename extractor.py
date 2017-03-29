import requests

class Extractor:

	def __init__(self, URL):
		self.originalURL = URL
		self.queryURL = URL
		self.firstURL = ""
		self.prevURL = ""
		self.nextURL = ""
		self.lastURL = ""


	def __extractPaginationURLs(self, responseLink):
		print(responseLink)
		nextURL = ""
		prevURL = ""
		lastURL = ""
		firstURL = ""
		a = responseLink

		try:
			aSplitList = a.split(", ")
			for s in aSplitList:
				if 'rel="next"' in s:
					nextStr = s.split("; ")[0]
					nextURL = nextStr[1:-1]
				if 'rel="last"' in s:
					lastStr = s.split("; ")[0]
					lastURL = lastStr[1:-1]
				if 'rel="prev"' in s:
					prevStr = s.split("; ")[0]
					prevURL = prevStr[1:-1]
				if 'rel="first"' in s:
					firstStr = s.split("; ")[0]
					firstURL = firstStr[1:-1]
		except Exception as e:
			print("error", e)
			pass

		self.firstURL = firstURL
		self.prevURL = prevURL
		self.nextURL = nextURL
		self.lastURL = lastURL

	def request(self):
		response = requests.get(self.queryURL)
		self.__extractPaginationURLs(response.headers['link'])
		return response.json()

	def next(self):
		pass

	def previous(self):
		pass
