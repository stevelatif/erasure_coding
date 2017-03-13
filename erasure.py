#!/usr/bin/env python

import numpy as np
import random
import hashlib


'''
 Reed Solomon Encoding
   data - column vector array
   sz - integer length of data

   Encodes data and returns a code that can be decoded

'''
class ErasureCoding():
    def __init__(self):
        pass

    def _encode(self, x_vector, xform):
        '''Do a Reed Solomon encoding of a vector of data

        Keyword Arguemts:
        x_vector -- numpy vector of data
        xform    -- numpy array to transform data

        returns transformed vector
        '''
        res =  np.dot(xform, x_vector)
        return res

    def _decode(self, code, inv):
        '''Decode data that has been transfomed by 
        Reed Solomon transformation

        Keyword Arguments:
        code -- Encodeing data in a numpy array
        inv  -- Inverse Reed Solomon transformation in 
        numpy matrix

        returns transformed vector
        '''
        return(np.dot(inv, code))

    def chunks(self, data, ch_sz):
        '''Convert an array of data into chunks

        Keywords arguments:
        data -- the data to be converted
        ch_sz -- chunk size

        returns a generator with the chunk 
        '''
        for ii in xrange(0, len(data), ch_sz):
            yield data[ii:ii + ch_sz]

    def rs_read(self, _dd):
        _out = []
        _buf = []
        for ii in  self.chunks(_dd, self.ndim):
            data = np.array(ii)
            _buf[:] = [ chr(x) for x in data]
            _out += _buf

        output =  "".join(_out)
        output = output[:-self.pad_len -1 or None]
        return output


    def rs_write(self, _data):
        '''
        '''
        Id = np.identity(self.ndim)
        b = np.array([[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1]]) 
        B = np.vstack((Id, b))
        bad_rows = [2,3,4]
        B_prime = np.delete(B, bad_rows , 0)
        B_prime_inv = np.linalg.inv(B_prime)
        m = hashlib.md5()
        m.update(_data)
        print m.hexdigest()
        _d_len = len(_data)
        self.pad_len = _d_len % self.ndim
        for ii in xrange(0, self.pad_len + 1):
            _data += '0'
        _dd = []
        _dd[:] = [ ord(x) for x in _data ]
        #self.dest_arr.node
        return _dd

    def rs(self, _data):
        '''

        '''
        self.ndim = 5
        self.mdim = 3
        dd = self.rs_write(_data)
        print self.rs_read(dd)

def main():
    ec = ErasureCoding()
    ec.dest_arr = []

    node_1 = {}
    node_2 = {}
    node_3 = {}
    node_4 = {}
    node_5 = {}

    ec.dest_arr.append(node_1)
    ec.dest_arr.append(node_2)
    ec.dest_arr.append(node_3)
    ec.dest_arr.append(node_4)
    ec.dest_arr.append(node_5)
    
    ec.rs("holy smokes bat man! would you look at that!")
    ec.rs("The ugly man rides a big motorcycle")
    ec.rs("There has also been White House conflict with Cabinet members such as Treasury Secretary Steven Mnuchin, who has vented to friends that Priebus has blocked his choice for deputy secretary, Goldman Sachs managing director Jim Donovan, according to one person familiar with the talks. Secretary of State Rex Tillerson, meanwhile, has complained that the chief of staff is picking who will get plum ambassador posts without always consulting others, said another person familiar with that situation.")
if __name__ == '__main__':
    main()
