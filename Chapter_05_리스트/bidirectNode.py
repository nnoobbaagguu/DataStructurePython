class BidirectNode:
    def __init__(self, item, prev_node: 'BidirectNode', next_node: 'BidirectNode'):
        self.item = item
        self.prev = prev_node
        self.next = next_node