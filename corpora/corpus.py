# -*- coding: utf-8 -*-

import os
import yaml
import cPickle as pickle

class Corpus:
    CHUNK_PREFIX="chunk"
    CONFIG_FILE="config"
    IDX_FILE="idx"
    RIDX_FILE="ridx"
    
    def __init__(self, path):
        self.corpus_path = path
        self.chunks = {}
        self.idx = pickle.load(file(os.path.join(self.corpus_path, Corpus.IDX_FILE ), 'rb'))
        self.ridx = pickle.load(file(os.path.join(self.corpus_path, Corpus.RIDX_FILE ), 'rb'))
        self.properties = yaml.load(file(os.path.join(self.corpus_path, Corpus.CONFIG_FILE), 'r'))
    
    def __len__(self):
        return len(self.idx)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __iter__(self):
        for e in self.idx:
            yield self.get_by_idx(e)
            
    
    def get_property(self, prop):
        return self.properties[prop]
    def set_property(self, prop, val):
        self.properties[prop] = val

    @staticmethod
    def create( path, **properties ):
        os.makedirs(path)
        if not properties.has_key('chunk_size') :
            properties['chunk_size'] = 1024
        if not properties.has_key('encoding') :
            properties['encoding'] = 'utf-8'
        properties['current_chunk'] = 0
        
        yaml.dump(properties, file(os.path.join(path, Corpus.CONFIG_FILE), 'w'), default_flow_style=False)
        file(os.path.join(path, Corpus.CHUNK_PREFIX + "0"), 'w').close()
        
        pickle.dump([], file(os.path.join(path, Corpus.IDX_FILE ), 'wb'))
        pickle.dump({}, file(os.path.join(path, Corpus.RIDX_FILE ), 'wb'))
      
    
    def save_config(self):
        yaml.dump(self.properties, file(os.path.join(self.corpus_path, Corpus.CONFIG_FILE), 'w'), default_flow_style=False)

    def save_indexes(self):
        pickle.dump(self.idx, file(os.path.join(self.corpus_path, Corpus.IDX_FILE ), 'wb'))
        pickle.dump(self.ridx, file(os.path.join(self.corpus_path, Corpus.RIDX_FILE ), 'wb'))        
    
    def make_new_chunk(self):
        self.set_property('current_chunk' , self.get_property('current_chunk') + 1 )
        self.set_property('current_chunk_size', 0 )
            
        file(os.path.join(self.corpus_path, Corpus.CHUNK_PREFIX + str(self.get_property('current_chunk'))), 'w').close()
        self.save_config()
    
    def test_chunk_size(self, new_size):
        chunk = self.get_chunk()
        chunk.seek(0,2)
        chunk_size = chunk.tell()
        if new_size > self.get_property('chunk_size'):
            raise Corpus.ExceptionTooBig()
        return chunk_size + new_size <=  self.get_property('chunk_size')
        
    def get_chunk(self, number=None):
        if number is None:
            number = self.get_property('current_chunk')
        try:
            return self.chunks[number]
        except:
            self.chunks[number] = file(os.path.join(self.corpus_path, Corpus.CHUNK_PREFIX + str(number)), 'r+b')
            return self.chunks[number]
    
    def add(self, text, ident, **headers):
        if self.ridx.has_key(ident):
            raise Corpus.ExceptionDuplicate()
        
        headers['id'] = ident
        headers_str = yaml.dump(headers, default_flow_style=False) 
        text_str = text.encode(self.get_property('encoding'))  + "\n\n"

        if not self.test_chunk_size(len(headers_str) + len(text_str)) :
            self.make_new_chunk()
        
        chunk = self.get_chunk()
        chunk.seek(0,2)
        self.idx.append((self.get_property('current_chunk') , chunk.tell(), len(headers_str), len(text_str)))
        self.ridx[ident] = len(self.idx)-1
        chunk.write(headers_str)
        chunk.write(text_str)
        chunk.flush()

    def get(self, ident):
        if not self.ridx.has_key(ident):
            raise IndexError('Not found')
        return self.get_by_idx(self.idx[self.ridx[ident]])
        
    def get_by_idx(self, idx):
        (chunk_number, offset, head_len, text_len) = idx
        chunk = self.get_chunk(chunk_number)
        chunk.seek(offset,0)
        head = chunk.read(head_len)
        text = chunk.read(text_len)[:-2]
        return (yaml.load(head) , text.decode(self.get_property('encoding')))
        
            
    class ExceptionTooBig(Exception):
        pass
    class ExceptionDuplicate(Exception):
        pass    