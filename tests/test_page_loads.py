def test_index(client):
    response = client.get('/')
    assert b'Kalkul\xc3\xa1torok' in response.data


def test_dilution(client):
    response = client.get('/dilution')
    assert (b'A k\xc3\xadv\xc3\xa1nt alkoholszint el\xc3\xa9r\xc3\xa9s\xc3\xa9hez '
            b'sz\xc3\xbcks\xc3\xa9ges v\xc3\xadz mennyis\xc3\xa9ge:') in response.data


def test_separation(client):
    response = client.get('/separation')
    assert b'Az el\xc5\x91p\xc3\xa1rlatra vonatkoz\xc3\xb3 mennyis\xc3\xa9gek:' in response.data
