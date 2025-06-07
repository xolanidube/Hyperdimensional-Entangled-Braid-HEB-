class HEBNode:
    def __init__(self):
        self.children = {}
        self.value = None

class HEB:
    """Minimal Hyperdimensional Entangled Braid prototype."""

    def __init__(self, branch_factor=3, depth=3):
        self.branch_factor = branch_factor
        self.depth = depth
        self.root = HEBNode()

    def _hash(self, key):
        """Generate fractal coordinates for a key."""
        h = hash(key)
        coords = []
        for _ in range(self.depth):
            coords.append(h % self.branch_factor)
            h //= self.branch_factor
        return coords

    def insert(self, key, value):
        node = self.root
        for idx in self._hash(key):
            node = node.children.setdefault(idx, HEBNode())
        node.value = value

    def search(self, key):
        node = self.root
        for idx in self._hash(key):
            node = node.children.get(idx)
            if node is None:
                return None
        return node.value
