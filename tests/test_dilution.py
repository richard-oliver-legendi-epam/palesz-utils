import pytest


def test_dilution_get(client):
    response = client.get('/dilution')

    assert b'Mennyis\xc3\xa9g (liter)' in response.data
    assert b'Mostani alkoholszint (%)' in response.data
    assert b'El\xc3\xa9rni k\xc3\xadv\xc3\xa1nt alkoholszint (%)' in response.data
    assert (b'A k\xc3\xadv\xc3\xa1nt alkoholszint el\xc3\xa9r\xc3\xa9s\xc3\xa9hez '
            b'sz\xc3\xbcks\xc3\xa9ges v\xc3\xadz mennyis\xc3\xa9ge:') in response.data


def test_dilution_post(client):
    response = client.post('/dilution', data={'volume': 50, 'act_alcohol_level': 65,
                                              'target_alcohol_level': 45})

    assert (b'(50.00L * 65.00% / 45.00%) - 50.00L == 22.22 Liter v\xc3\xadzre van sz\xc3\xbcks\xc3\xa9g'
            in response.data)


@pytest.mark.parametrize(('volume', 'act_alcohol_level', 'target_alcohol_level', 'message'), (
        ('0', '2', '1', b'A liter pozit\xc3\xadv kell legyen!'),
        ('3', '0', '1', b'A mostani alkoholszint pozit\xc3\xadv kell legyen!'),
        ('3', '2', '0', b'Az el\xc3\xa9rni k\xc3\xadv\xc3\xa1nt alkoholszint pozit\xc3\xadv kell legyen!'),
        ('3', '101', '1', b'Na azt hogy csin\xc3\xa1ltad, h 100%-n\xc3\xa1l nagyobb az alkoholszint?!'),
        ('3', '1', '2', b'Az el\xc3\xa9rni k\xc3\xadv\xc3\xa1nt alkoholszint kisebb kell legyen, mint a mostani!')
))
def test_dilution_errors(client, volume, act_alcohol_level, target_alcohol_level, message):
    response = client.post('/dilution', data={'volume': volume, 'act_alcohol_level': act_alcohol_level,
                                              'target_alcohol_level': target_alcohol_level})

    assert message in response.data
