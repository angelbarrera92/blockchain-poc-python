from blockchain import BlockChain

if __name__ == '__main__':
    my_block_chain = BlockChain(debug=True)
    my_block_chain.new_block('Second Block')
    my_block_chain.new_block('Third Block')
    for block in range(0, 10):
        my_block_chain.new_block('Block %d' % block)
    print(my_block_chain.blocks())
