def wrap(text, charactersPerBlock):
    import math
    numberOfBlocks = math.ceil(len(text) / charactersPerBlock)
    block = [''] * numberOfBlocks
    for x in range(numberOfBlocks):
        block[x] = text[charactersPerBlock - 50: charactersPerBlock]
        charactersPerBlock += 50

    return block


def makeBlock(message):
    blocks = wrap(message, 50)
    blockInt = 0
    i = 0

    for b in range(len(blocks)):
        for x in blocks[b]:
            blockInt += ord(x) * (1114111 ** i)
            i += 1
        blocks[b] = blockInt
        blockInt = 0
        i = 0

    return blocks


def blockTotext(integer):
    NumberOfcharacterInBlock = 49  # counting from zero
    blocks = len(integer)
    symbols = 1114111
    block = [''] * blocks
    blockposition = 0
    counter = 0
    while counter < 50 + (50*(blocks-1)):
        unicodeNumber = integer[blockposition] // (symbols ** NumberOfcharacterInBlock)
        block[blockposition] = chr(unicodeNumber) + block[blockposition]
        integer[blockposition] = integer[blockposition] % (symbols ** NumberOfcharacterInBlock)
        NumberOfcharacterInBlock = NumberOfcharacterInBlock - 1
        counter += 1
        if NumberOfcharacterInBlock < 0:
            NumberOfcharacterInBlock = 49
            blockposition += 1

    return ''.join(block)




