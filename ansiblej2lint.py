#!/usr/bin/env python3
"""
This adds Ansible filters from https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html

And Ansible tests from https://docs.ansible.com/ansible/latest/user_guide/playbooks_tests.html

"""
import jinja2
from j2lint import main, AbsolutePathLoader

FILTER = ['b64decode', 'basename', 'bool', 'combinations', 'combine', 'comment', 'dict2items', 'difference', 'dirname', 'expanduser', 'expandvars', 'flatten', 'from_json', 'from_yaml', 'from_yaml_all', 'hash', 'int', 'intersect', 'ipaddr', 'ipv4', 'ipv6', 'items2dict', 'join', 'k8s_config_resource_name', 'log', 'map', 'max', 'min', 'omandatory', 'parse_cli', 'parse_xml', 'password_hash', 'path_join', 'permutations', 'pow', 'product', 'quote', 'realpath', 'regex_escape', 'regex_findall', 'regex_replace', 'regex_search', 'root', 'shuffle', 'split', 'splitext', 'strftime', 'subelements', 'symmetric_difference', 'ternary', 'to_datetime', 'to_json', 'to_nice_json', 'to_nice_yaml', 'to_uuid', 'to_yaml', 'type_debug', 'union', 'unique', 'urlencode', 'urlsplit', 'vlan_parser', 'win_basename', 'win_dirname', 'win_splitdrive', 'zip', 'zip_longest', 'ansible.builtin.b64decode', 'ansible.builtin.basename', 'ansible.builtin.bool', 'ansible.builtin.combinations', 'ansible.builtin.combine', 'ansible.builtin.comment', 'ansible.builtin.dict2items', 'ansible.builtin.difference', 'ansible.builtin.dirname', 'ansible.builtin.expanduser', 'ansible.builtin.expandvars', 'ansible.builtin.flatten', 'ansible.builtin.from_json', 'ansible.builtin.from_yaml', 'ansible.builtin.from_yaml_all', 'ansible.builtin.hash', 'ansible.builtin.int', 'ansible.builtin.intersect', 'ansible.builtin.ipaddr', 'ansible.builtin.ipv4', 'ansible.builtin.ipv6', 'ansible.builtin.items2dict', 'ansible.builtin.join', 'ansible.builtin.k8s_config_resource_name', 'ansible.builtin.log', 'ansible.builtin.map', 'ansible.builtin.max', 'ansible.builtin.min', 'ansible.builtin.omandatory', 'ansible.builtin.parse_cli', 'ansible.builtin.parse_xml', 'ansible.builtin.password_hash', 'ansible.builtin.path_join', 'ansible.builtin.permutations', 'ansible.builtin.pow', 'ansible.builtin.product', 'ansible.builtin.quote', 'ansible.builtin.realpath', 'ansible.builtin.regex_escape', 'ansible.builtin.regex_findall', 'ansible.builtin.regex_replace', 'ansible.builtin.regex_search', 'ansible.builtin.root', 'ansible.builtin.shuffle', 'ansible.builtin.split', 'ansible.builtin.splitext', 'ansible.builtin.strftime', 'ansible.builtin.subelements', 'ansible.builtin.symmetric_difference', 'ansible.builtin.ternary', 'ansible.builtin.to_datetime', 'ansible.builtin.to_json', 'ansible.builtin.to_nice_json', 'ansible.builtin.to_nice_yaml', 'ansible.builtin.to_uuid', 'ansible.builtin.to_yaml', 'ansible.builtin.type_debug', 'ansible.builtin.union', 'ansible.builtin.unique', 'ansible.builtin.urlencode', 'ansible.builtin.urlsplit', 'ansible.builtin.vlan_parser', 'ansible.builtin.win_basename', 'ansible.builtin.win_dirname', 'ansible.builtin.win_splitdrive', 'ansible.builtin.zip', 'ansible.builtin.zip_longest']

TEST = ['all', 'any', 'contains', 'directory', 'exists', 'falsy', 'file', 'human_readable', 'human_to_bytes', 'link', 'match', 'mount', 'regex', 'same_file', 'search', 'subset', 'superset', 'truthy', 'vault_encrypted', 'version']


ENV = jinja2.Environment(loader=AbsolutePathLoader())
ENV.filters.update({name: lambda: None for name in FILTER})
ENV.tests.update({name: lambda: None for name in TEST})

main(env=ENV)
