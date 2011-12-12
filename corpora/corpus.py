import os
import yaml
class Corpus:
	CHUNK_PREFIX="chunk"
	CONFIG_FILE="config"
	IDX_FILE="idx"
	
	def __init__(self, path):
		self.corpus_path = path
		self.chunks = {}
		self.properties = yaml.load(file(os.path.join(self.corpus_path, Corpus.CONFIG_FILE), 'r'))
	@staticmethod
	def create( path, **properties ):
		os.mkdir(path)
		if not properties.has_key('chunk_size') :
			properties['chunk_size'] = 1024
		properties['current_chunk'] = 0
		properties['current_chunk_size'] = 0
		
		yaml.dump(properties, file(os.path.join(path, Corpus.CONFIG_FILE), 'w'))
		file(os.path.join(path, Corpus.CHUNK_PREFIX + "0"), 'w').close()
	
	def save_config(self):
		yaml.dump(self.properties, file(os.path.join(self.corpus_path, Corpus.CONFIG_FILE), 'w'))
	
	def make_new_chunk(self):
		self.properties['current_chunk'] += 1
		self.properties['current_chunk_size'] = 0		
		file(os.path.join(self.corpus_path, Corpus.CHUNK_PREFIX + str(self.properties['current_chunk'])), 'w').close()
		self.save_config()
	
	def test_chunk_size(self):
		pass
	def get_chunk(self, number=None):
		if is_none(number):
			number = self.current_chunk
		try:
			return self.chunks[number]
		except:
			self.chunks[number] = file(os.path.join(self.corpus_path, Corpus.CHUNK_PREFIX + str(number)), 'rw')
			return self.chunks[number]
	
	def add(self, text, ident, **headers):
		headers['id'] = ident
		text_str = text.encode('utf-8')  + '\n\n'
		headers_str = yaml.dump(headers) + '\n'
		chunk = get_chunk()
		