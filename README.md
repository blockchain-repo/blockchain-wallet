# unichain-client

####1.[`create_account.py`](./create_account.py)

The role of this module is to create an account and write to the '.account' file

```
~/unichain-account$ python3 create_account.py
Pick a username:
mike
{
    'username': 'mike',
    'verifying_key': '5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X',
    'signing_key': '8BzfpzwgBxJrCFZuvPVY48N3Lf8WCcXpDDJwrTNfxxwd'
}
```


####2.[`create_asset_tx.py`](./create_asset_tx.py)

A simple way to generate a `CREATE` transaction.

```
~/unichain-account$ python3 create_asset_tx.py
Please input an integer:
100
{
    "version": 1,
    "id": "092c913f16c658de429912a47ef1989dcfc51897ba76395c843cbdb01480cbcb",
    "transaction": {
        "fulfillments": [
            {
                "owners_before": [
                    "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
                ],
                "fid": 0,
                "fulfillment": "cf:4:PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11aE61aNwAXcQeXiGXh2iTJ8CqJYm0SebTCwJYYl93iAohwjd5d6S-7wc90A2QDGJcbEg6q8-A5pdsGIMzpr_AgL",
                "input": null
            }
        ],
        "conditions": [
            {
                "amount": 100,
                "owners_after": [
                    "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
                ],
                "cid": 0,
                "condition": {
                    "details": {
                        "bitmask": 32,
                        "signature": null,
                        "type_id": 4,
                        "public_key": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
                        "type": "fulfillment"
                    },
                    "uri": "cc:4:20:PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11Y:96"
                }
            }
        ],
        "asset": {
            "divisible": true,
            "refillable": false,
            "id": "1",
            "data": {
                "money": "RMB"
            },
            "updatable": false
        },
        "metadata": {
            "id": "af688338-f24a-4354-a16a-4beb9b96ab22",
            "data": {
                "planet": "earth"
            }
        },
        "timestamp": "1487914832286",
        "operation": "CREATE"
    }
}
```

####3.[`transfer_asset_tx.py`](./transfer_asset_tx.py)

A simple way to generate a `TRANSFER` transaction.

```
~/unichain-account$ python3 transfer_asset_tx.py
Please input an after:
CShGVt5vTN3g3S14QcnWoVcsEMMkvznWJ8nPfef7T78b
Please input an integer:
20
{
    'version': 1,
    'transaction': {
        'asset': {
            'id': '1'
        },
        'fulfillments': [
            {
                'owners_before': [
                    '5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X'
                ],
                'fid': 0,
                'fulfillment': 'cf: 4: PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11aqhxjgLIyEdP3ZWDNjLqXVIQiK7tWI2wJsCY5BxNiPMfpT-ohDIPaEWo-33gGKicacrktoae_L4sIwhIGTkh8A',
                'input': {
                    'cid': 0,
                    'txid': '092c913f16c658de429912a47ef1989dcfc51897ba76395c843cbdb01480cbcb'
                }
            }
        ],
        'operation': 'TRANSFER',
        'timestamp': '1487914964611',
        'metadata': None,
        'conditions': [
            {
                'cid': 0,
                'amount': 20,
                'owners_after': [
                    'CShGVt5vTN3g3S14QcnWoVcsEMMkvznWJ8nPfef7T78b'
                ],
                'condition': {
                    'details': {
                        'type_id': 4,
                        'type': 'fulfillment',
                        'signature': None,
                        'bitmask': 32,
                        'public_key': 'CShGVt5vTN3g3S14QcnWoVcsEMMkvznWJ8nPfef7T78b'
                    },
                    'uri': 'cc: 4: 20: qgWbUCT_00Iax4kkeworDvHvrV4qorXIQUmnfMQMrwA: 96'
                }
            },
            {
                'cid': 1,
                'amount': 80,
                'owners_after': [
                    '5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X'
                ],
                'condition': {
                    'details': {
                        'type_id': 4,
                        'type': 'fulfillment',
                        'signature': None,
                        'bitmask': 32,
                        'public_key': '5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X'
                    },
                    'uri': 'cc: 4: 20: PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11Y: 96'
                }
            }
        ]
    },
    'id': '22845202130f3712bdf1fb3c1e4f63cade679b3386f15686e5e8a2ec04005b25'
}
```

####4.[`tx_record.py`](./tx_record.py)

The role of this module is to get transaction list of the account

```
~/unichain-account$ python3 tx_record.py
[
    {
        "amount": 20,
        "owner_before": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
        "timestamp": "1487914964611",
        "operation": "TRANSFER",
        "id": "22845202130f3712bdf1fb3c1e4f63cade679b3386f15686e5e8a2ec04005b25",
        "owners_after": "CShGVt5vTN3g3S14QcnWoVcsEMMkvznWJ8nPfef7T78b"
    },
    {
        "amount": 100,
        "owner_before": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
        "timestamp": "1487914832286",
        "operation": "CREATE",
        "id": "092c913f16c658de429912a47ef1989dcfc51897ba76395c843cbdb01480cbcb",
        "owners_after": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
    }
]
```

####5.[`UTXO.py`](./UTXO.py)

The role of this module is to get UTXO(unspent transaction output) of the account

```
~/unichain-account$ python3 UTXO.py
[
    {
        "details": {
            "bitmask": 32,
            "signature": null,
            "public_key": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
            "type_id": 4,
            "type": "fulfillment"
        },
        "amount": 80,
        "cid": 1,
        "txid": "22845202130f3712bdf1fb3c1e4f63cade679b3386f15686e5e8a2ec04005b25"
    }
]
```