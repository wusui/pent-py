# (c) 2022 Warren Usui MOPFPPP
# This code is licensed under the MIT license (see LICENSE.txt for details)
"""
Remove duplicate paths
"""
def tree_rm_dup_paths(node_list):
    """
    Remove full paths to leaves that duplicate the path of an earlier
    leaf node

    @param {tuple} node_list tree nodes
    @return {tuple} tree nodes with duplicate figure nodes removed
    """
    return tuple([iter1[1] for iter1 in enumerate(node_list)
                  if _not_in_list_so_far(node_list, iter1)])

def _not_in_list_so_far(node_list, enum_data):
    return enum_data[1]['figure'] not in [
        iter1['figure'] for iter1 in node_list[0:enum_data[0]]
    ]
