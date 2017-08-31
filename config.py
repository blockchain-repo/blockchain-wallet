import collections
import copy
import json
import os

from collections import namedtuple
from cryptoconditions import crypto

CryptoKeypair = namedtuple('CryptoKeypair', ('private', 'public'))

config = {
    'server': {
        'host': 'localhost',
        'port': '9984'
    },
    'keypair': {
        'public': '',
        'private': ''
    },
    'username': 'user'
}

_config = copy.deepcopy(config)


def generate_keypair():
    """Generates a cryptographic key pair."""
    return CryptoKeypair(
        *(k.decode() for k in crypto.ed25519_generate_key_pair()))


def create_config():
    keypair = generate_keypair()
    if os.path.exists('.unichain-account'):
        return
    f = open('.unichain-account', 'w')
    config['keypair']['private'] = keypair.private
    config['keypair']['public'] = keypair.public
    json_account = json.dumps(config)
    f.write(json_account)
    f.close()


def set_config():
    fileconfig = file_config('.unichain-account')
    update(config, fileconfig)


def file_config(filename=None):
    """Returns the config values found in a configuration file.
    Args:
        filename (str): the JSON file with the configuration values.
            If ``None``, CONFIG_DEFAULT_PATH will be used.
    Returns:
        dict: The config values in the specified config file (or the
              file at CONFIG_DEFAULT_PATH, if filename == None)
    """
    with open(filename) as f:
        try:
            configs = json.load(f)
            return configs
        except ValueError as err:
            raise err


# Thanks Alex <3
# http://stackoverflow.com/a/3233356/597097
def update(d, u):
    """Recursively update a mapping (i.e. a dict, list, set, or tuple).
    Conceptually, d and u are two sets trees (with nodes and edges).
    This function goes through all the nodes of u. For each node in u,
    if d doesn't have that node yet, then this function adds the node from u,
    otherwise this function overwrites the node already in d with u's node.
    Args:
        d (mapping): The mapping to overwrite and add to.
        u (mapping): The mapping to read for changes.
    Returns:
        mapping: An updated version of d (updated by u).
    """
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


def update_types(config, reference, list_sep=':'):
    """Return a new configuration where all the values types
    are aligned with the ones in the default configuration"""

    def _coerce(current, value):
        # Coerce a value to the `current` type.
        try:
            # First we try to apply current to the value, since it
            # might be a function
            return current(value)
        except TypeError:
            # Then we check if current is a list AND if the value
            # is a string.
            if isinstance(current, list) and isinstance(value, str):
                # If so, we use the colon as the separator
                return value.split(list_sep)

            try:
                # If we are here, we should try to apply the type
                # of `current` to the value
                return type(current)(value)
            except TypeError:
                # Worst case scenario we return the value itself.
                return value

    def _update_type(value, path):
        current = reference

        for elem in path:
            try:
                current = current[elem]
            except KeyError:
                return value

        return _coerce(current, value)

    return map_leafs(_update_type, config)


def map_leafs(func, mapping):
    """Map a function to the leafs of a mapping."""

    def _inner(mapping, path=None):
        if path is None:
            path = []

        for key, val in mapping.items():
            if isinstance(val, collections.Mapping):
                _inner(val, path + [key])
            else:
                mapping[key] = func(val, path=path + [key])

        return mapping

    return _inner(copy.deepcopy(mapping))
