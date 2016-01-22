
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse("cisco_ipsec.txt", factory=True)

def print_children(parse_object):
	for parent in parse_object:
		print parent.text
		for child in parent.children:
			print child.text

crypto_map = parse.find_objects(r"^crypto map CRYPTO")
print_children(crypto_map)


pfs_group_2 = parse.find_objects_w_child(parentspec=r"^crypto map CRYPTO", 
	childspec=r"set pfs group2")



def not_in_parent(parent, search_term):
	for line in range(len(parent)):
		parent_child = parent[line]
		if search_term not in parent_child.children[1].text:
			print parent_child.text
			print parent_child.children[1].text

no_AES = parse.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set")
not_in_parent(no_AES, 'AES')
