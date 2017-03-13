# unichain-client

####1.[`create_account.py`](./create_account.py)

The role of this module is to create an account and write to the '.account' file

```
~/unichain-account$ python3 create_account.py MIKE
{
    "username": "MIKE",
    "verifying_key": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
    "signing_key": "3JMBk1Qsrj6psv697CLVNxS7C3t9ZW4Zf5aweHVZCMZz"
}
```


####2.[`create_asset_tx.py`](./create_asset_tx.py)

A simple way to generate a `CREATE` transaction.

```
~/unichain-account$ python3 create_asset_tx.py 1000
{
    "transaction": {
        "metadata": {
            "id": "d06368b3-b72f-4f39-bede-ecca4f8bab96",
            "data": {
                "planet": "earth"
            }
        },
        "timestamp": "1489373697905",
        "fulfillments": [
            {
                "fulfillment": "cf:4:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aME_LdhO4-yM-CK2qyKcFy7llAB5pSbMa2NFWDHTLd3WminowKHAotztu8bpwQX9-buPH9Ha79poFRTOa1luswL",
                "input": null,
                "owners_before": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ],
                "fid": 0
            }
        ],
        "operation": "CREATE",
        "conditions": [
            {
                "owners_after": [
                    "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y"
                ],
                "amount": 1000,
                "cid": 0,
                "condition": {
                    "details": {
                        "type": "fulfillment",
                        "signature": null,
                        "public_key": "3yLFxcMPnc3ozT82Csn9EDbw1vBVSqYJq6oxF9FHwF7Y",
                        "bitmask": 32,
                        "type_id": 4
                    },
                    "uri": "cc:4:20:LCWslQuppEihgphGm0R7v0jHLd67v4JIQGvuQqbo6aM:96"
                }
            }
        ],
        "asset": {
            "id": "1",
            "updatable": false,
            "refillable": false,
            "divisible": true,
            "data": {
                "money": "RMB"
            }
        }
    },
    "id": "573fbfdc672714fbb4318e61f704d7ab479faa1319ba831b5f2015b03e4cf8dd",
    "version": 1
}
```

####3.[`transfer_asset_tx.py`](./transfer_asset_tx.py)

A simple way to generate a `TRANSFER` transaction.

```
~/unichain-account$ python3 transfer_asset_tx.py
Please input 'owners_after':
>>>5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X
Please input the amount(int):
>>>2000
{
    "id": "a784445834b37caf74af8ad3a88f7b64c1e0b80c0235b08a5673957f02842c00",
    "version": 1,
    "transaction": {
        "fulfillments": [
            {
                "fid": 0,
                "input": {
                    "cid": 0,
                    "txid": "e02afde589b67bc5ee8bc1eb455609ba2f00e990227fedf4de22ff33ac641867"
                },
                "fulfillment": "cf:4:XjXJ9clYCIKLHf8CdAfLfw5BYPzweeqXU1BbJCUD30IPMO2epCdl30CIiNMYSWXq56sEaxm4nkXYw8gJHck_kzdSoLA1ahJg6kG54SHYLYLKaDNw3aMPl0Ge94tHLzEA",
                "owners_before": [
                    "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1"
                ]
            }
        ],
        "operation": "TRANSFER",
        "conditions": [
            {
                "cid": 0,
                "condition": {
                    "uri": "cc:4:20:PsiwZR_uYx613wh4xbPSpdZ_Xzdu1gZQEqgWAk9w11Y:96",
                    "details": {
                        "signature": null,
                        "type_id": 4,
                        "type": "fulfillment",
                        "bitmask": 32,
                        "public_key": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
                    }
                },
                "amount": 2000,
                "owners_after": [
                    "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X"
                ]
            },
            {
                "cid": 1,
                "condition": {
                    "uri": "cc:4:20:XjXJ9clYCIKLHf8CdAfLfw5BYPzweeqXU1BbJCUD30I:96",
                    "details": {
                        "signature": null,
                        "type_id": 4,
                        "type": "fulfillment",
                        "bitmask": 32,
                        "public_key": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1"
                    }
                },
                "amount": 8000,
                "owners_after": [
                    "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1"
                ]
            }
        ],
        "asset": {
            "id": "1"
        },
        "metadata": null,
        "timestamp": "1487918371022"
    }
}
```

####4.[`tx_record.py`](./tx_record.py)

The role of this module is to get transaction list of the account

```
~/unichain-account$ python3 tx_record.py
[
    {
        "timestamp": "2017-02-24 14:34:12",
        "owner_before": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "amount": 10000,
        "owners_after": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "operation": "CREATE"
    },
    {
        "timestamp": "2017-02-24 14:39:31",
        "owner_before": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "amount": 2000,
        "owners_after": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
        "operation": "TRANSFER"
    }

]
```

####5.[`UTXO.py`](./UTXO.py)

The role of this module is to get UTXO(unspent transaction output) of the account

```
~/unichain-account$ python3 UTXO.py
[
    {
        "txid": "a784445834b37caf74af8ad3a88f7b64c1e0b80c0235b08a5673957f02842c00",
        "cid": 1,
        "amount": 8000
    }
]
```