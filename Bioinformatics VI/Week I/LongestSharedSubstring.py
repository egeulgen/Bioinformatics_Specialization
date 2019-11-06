import sys
import Tree_Trie_classes

def backtrace_path_from_node(tree, node, Text):
    # if root is reached, stop
    if node.label == 0: 
        return ''

    for edge in tree.all_edges:
        if edge.target_node == node:
            incoming_edge = edge
            break

    path_substring = Text[incoming_edge.position : incoming_edge.position + incoming_edge.length]
    path_substring = backtrace_path_from_node(tree, incoming_edge.from_node, Text) + path_substring
    return path_substring

def LongestSharedSubstring(Text1, Text2):
    ''' Longest Shared Substring
    Input: Strings Text1 and Text2.
    Output: The longest substring that occurs in both Text1 and Text2.
    '''
    suffix_tree = Tree_Trie_class.Tree()
    combined_Text = Text1 + '#' + Text2 + '$'
    suffix_tree.PopulateSuffixTree(combined_Text)
    suffix_tree.add_indicators()

    ## Find deepest common internal node
    max_dep = -1   
    for node in suffix_tree.all_nodes:
        if node.indicator == '*':
            # print(str(node.label) + ': '+ str(node.indicator) + ': ' + str(node.depth))
            if len(node.edges) != 0 and node.depth >= max_dep:
                max_dep = node.depth
                max_dep_node = node

    longest_substring = backtrace_path_from_node(suffix_tree, max_dep_node, combined_Text)
    return longest_substring


if __name__ == "__main__":
    tmp = sys.stdin.read().splitlines()
    Text1 = tmp[0]
    Text2 = tmp[1]
    print(LongestSharedSubstring(Text1, Text2))