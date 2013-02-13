from heapq import heapify, heappop, heappush

def Huffman(freqList):
	"""Input：An list with n pairs of (freq, char)
Output: An encoding tree with n leaves
	"""
    trees = list(freqList)
    heapify(trees)
    while len(trees) > 1:
        childL, childR = heappop(trees), heappop(trees)
        parent = (childL[0] + childR[0], childL, childR)
        heappush(trees, parent)
    return trees[0]

def printHuffman(huffTree, prefix = ''):
	"""Input: An Huffman encoding tree
Output: the character with its coding every line
	"""
    if len(huffTree) == 2:
        print huffTree[1], prefix
    else:
        printHuffman(huffTree[1], prefix + '0')
        printHuffman(huffTree[2], prefix + '1')