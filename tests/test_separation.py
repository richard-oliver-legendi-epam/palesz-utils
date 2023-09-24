def test_separation_get(client):
    response = client.get('/separation')

    assert b'Alszes mennyis\xc3\xa9ge f\xc5\x91z\xc3\xa9s el\xc5\x91tt (liter)' in response.data
    assert b'Az el\xc5\x91p\xc3\xa1rlatra vonatkoz\xc3\xb3 mennyis\xc3\xa9gek:' in response.data


def test_separation_post(client):
    response = client.post('/separation', data={'volume': 80})

    assert b'4.00 dL - 16.00 dL' in response.data
    assert b'2.40 dL - 4.00 dL' in response.data
    assert b'4.00 dL - 12.00 dL' in response.data


def test_separation_errors(client):
    response = client.post('/separation', data={'volume': 0})

    assert b'A liter pozit\xc3\xadv kell legyen!' in response.data


def test_mail_link(client):
    response = client.get('/separation')

    assert b"mailto:" in response.data
