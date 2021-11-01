#!/usr/bin/env python3
"""
This adds Ansible filters from https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html

And Ansible tests from https://docs.ansible.com/ansible/latest/user_guide/playbooks_tests.html

"""
import jinja2
from j2lint import main, AbsolutePathLoader

FILTER = ['b64decode', 'basename', 'bool', 'combinations', 'combine', 'comment', 'dict2items', 'difference', 'dirname', 'expanduser', 'expandvars', 'flatten', 'from_json', 'from_yaml', 'from_yaml_all', 'hash', 'int', 'intersect', 'ipaddr', 'ipv4', 'ipv6', 'items2dict', 'join', 'k8s_config_resource_name', 'log', 'map', 'max', 'min', 'omandatory', 'parse_cli', 'parse_xml', 'password_hash', 'path_join', 'permutations', 'pow', 'product', 'quote', 'realpath', 'regex_escape', 'regex_findall', 'regex_replace', 'regex_search', 'root', 'shuffle', 'split', 'splitext', 'strftime', 'subelements', 'symmetric_difference', 'ternary', 'to_datetime', 'to_json', 'to_nice_json', 'to_nice_yaml', 'to_uuid', 'to_yaml', 'type_debug', 'union', 'unique', 'urlencode', 'urlsplit', 'vlan_parser', 'win_basename', 'win_dirname', 'win_splitdrive', 'zip', 'zip_longest']

TEST = ['all', 'any', 'contains', 'directory', 'exists', 'falsy', 'file', 'human_readable', 'human_to_bytes', 'link', 'match', 'mount', 'regex', 'same_file', 'search', 'subset', 'superset', 'truthy', 'vault_encrypted', 'version']


ENV = jinja2.Environment(loader=AbsolutePathLoader())
ENV.filters.update({name: lambda: None for name in FILTER})
ENV.tests.update({name: lambda: None for name in TEST})

main(env=ENV)
