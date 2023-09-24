def test_index(client):
    response = client.get('/')
    assert b'Kalkul\xc3\xa1torok' in response.data
    assert (b'Ezeket meguntam k\xc3\xa9zzel sz\xc3\xa1molgatni, ink\xc3\xa1bb csin\xc3\xa1ltam egy appot :-)'
            in response.data)


def test_mail_link(client):
    response = client.get('/')

    assert b"mailto:" in response.data
