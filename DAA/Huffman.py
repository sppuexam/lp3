from collections import Counter

# Node class for the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Count character frequencies
    frequency = Counter(text)
    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]

    # Build the tree by sorting and merging nodes
    while len(nodes) > 1:
        # Sort nodes by frequency
        nodes = sorted(nodes, key=lambda node: node.freq)

        # Merge two nodes with the lowest frequency
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the merged node back to the list
        nodes.append(merged)

    # The final node is the root of the Huffman Tree
    return nodes[0]

# Recursive function to generate Huffman codes
def generate_codes(root, current_code, codes):
    if root is None:
        return
    if root.char is not None:  # Leaf node
        codes[root.char] = current_code
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Main function to get Huffman codes for each character in the text
def huffman_codes(text):
    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)
    return codes

# Example usage with the specified string
text = "BCAADDDCCACACAC"
codes = huffman_codes(text)
print("Huffman Codes for each character:", codes)
