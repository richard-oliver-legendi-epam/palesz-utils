def test_dilution(client):
    assert client.get('/dilution').status_code == 200
    response = client.get('/dilution')
    assert (b'A k\xc3\xadv\xc3\xa1nt alkoholszint el\xc3\xa9r\xc3\xa9s\xc3\xa9hez '
            b'sz\xc3\xbcks\xc3\xa9ges v\xc3\xadz mennyis\xc3\xa9ge:') in response.data
