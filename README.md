# unichain-client

####1.[`create_account.py`](./create_account.py)

The role of this module is to create an account and write to the '.account' file

```
~/unichain-account$ python3 create_account.py
Pick your username:
>>>Mike
{
    "username": "Mike",
    "verifying_key": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
    "signing_key": "HStrGbff99t69ipzqw9q6JzqjMSF9UaMGHwJ2qmCWMwo"
}
```


####2.[`create_asset_tx.py`](./create_asset_tx.py)

A simple way to generate a `CREATE` transaction.

```
:~/unichain-account$ python3 create_asset_tx.py
Please input an integer:
>>>10000
{
    "id": "e02afde589b67bc5ee8bc1eb455609ba2f00e990227fedf4de22ff33ac641867",
    "transaction": {
        "asset": {
            "divisible": true,
            "id": "1",
            "data": {
                "money": "RMB"
            },
            "updatable": false,
            "refillable": false
        },
        "timestamp": "1487918052087",
        "conditions": [
            {
                "cid": 0,
                "condition": {
                    "uri": "cc:4:20:XjXJ9clYCIKLHf8CdAfLfw5BYPzweeqXU1BbJCUD30I:96",
                    "details": {
                        "type_id": 4,
                        "public_key": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
                        "type": "fulfillment",
                        "signature": null,
                        "bitmask": 32
                    }
                },
                "owners_after": [
                    "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1"
                ],
                "amount": 10000
            }
        ],
        "operation": "CREATE",
        "metadata": {
            "id": "99e26e5a-46db-43d2-936c-7e7d1b274013",
            "data": {
                "planet": "earth"
            }
        },
        "fulfillments": [
            {
                "fid": 0,
                "fulfillment": "cf:4:XjXJ9clYCIKLHf8CdAfLfw5BYPzweeqXU1BbJCUD30IYu1QGxAOT-upQL1lVgi--Dx3R4r_7uoiGgRyIpmWAfR3nR73N8-AqBR2PiEM71ESwlsz4B3sVeSKJsF4NAqcM",
                "owners_before": [
                    "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1"
                ],
                "input": null
            }
        ]
    },
    "version": 1
}
```

####3.[`transfer_asset_tx.py`](./transfer_asset_tx.py)

A simple way to generate a `TRANSFER` transaction.

```
~/unichain-account$ python3 transfer_asset_tx.py
Please input an after:
>>>5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X
Please input an integer:
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
        "timestamp": "2017-02-24 14:39:31",
        "owner_before": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "amount": 2000,
        "owners_after": "5E5mXSHUX4mLJyL3jpbNhpoNputENJ9Wud7wyhBjT31X",
        "operation": "TRANSFER"
    },
    {
        "timestamp": "2017-02-24 14:34:12",
        "owner_before": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "amount": 10000,
        "owners_after": "7Lktu1cbgTwLHVGXw64AVnRjZwr5Yp9fSdwu7T8dggt1",
        "operation": "CREATE"
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