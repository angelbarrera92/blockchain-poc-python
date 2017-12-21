import hashlib
import time


class BlockChain:
    def __init__(self, debug=False, difficulty='0000'):
        self.difficulty = difficulty
        self._blocks = list()
        self._debug = debug
        self._do_genesis()

    def _do_genesis(self):
        index = 0
        prev_hash = 0
        timestamp = int(time.time())
        data = 'GENESIS-BLOCK'
        self._do_hash(data, timestamp, prev_hash, index)

    def _do_hash(self, data, timestamp, prev_hash, index):
        nonce = 0
        hash = ''
        while not self._valid_hash(hash):
            input = '%s%s%s%s%s' % (data, timestamp, prev_hash, index, nonce)
            hash = hashlib.sha256(input.encode('utf-8')).hexdigest()
            nonce += 1
        if self._debug:
            print('Hash: %s' % hash)
            print('Nonce: %d' % nonce)
        self._blocks.append(hash)

    def _valid_hash(self, hash):
        return hash.startswith(self.difficulty)

    def _last_hash(self):
        return self._blocks[-1]

    def new_block(self, data):
        index = len(self.blocks())
        prev_hash = self._last_hash()
        timestamp = int(time.time())
        self._do_hash(data, timestamp, prev_hash, index)

    def blocks(self):
        return self._blocks
