# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

from roach import aes, rc4, rsa

def test_aes():
    # Note that ECB doesn't use the IV.
    assert aes.ecb.decrypt("A"*16, "B"*16, "C"*32) == (
        "I\x96Z\xe4\xb5\xffX\xbdT]\x93\x03\x96\xfcw\xd9"
        "I\x96Z\xe4\xb5\xffX\xbdT]\x93\x03\x96\xfcw\xd9"
    )
    assert aes.ecb.decrypt("A"*16, data="C"*32) == (
        "I\x96Z\xe4\xb5\xffX\xbdT]\x93\x03\x96\xfcw\xd9"
        "I\x96Z\xe4\xb5\xffX\xbdT]\x93\x03\x96\xfcw\xd9"
    )

    assert aes.cbc.decrypt("A"*16, "B"*16, "C"*32) == (
        "\x0b\xd4\x18\xa6\xf7\xbd\x1a\xff\x16\x1f\xd1A\xd4\xbe5\x9b"
        "\n\xd5\x19\xa7\xf6\xbc\x1b\xfe\x17\x1e\xd0@\xd5\xbf4\x9a"
    )

def test_rc4():
    assert rc4.encrypt("Key", "Plaintext") == "bbf316e8d940af0ad3".decode("hex")
    assert rc4.decrypt("Wiki", "pedia") == "1021bf0420".decode("hex")
    assert rc4.decrypt("Secret", "Attack at dawn") == (
        "45a01f645fc35b383552544b9bf5".decode("hex")
    )
    assert rc4("hello", "world") == "783ecd96cf".decode("hex")

def test_rsa():
    assert rsa.import_key("""
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5cagCPVB7LiX3UI5N3WRQJqTLe5RPrhFj79/U
7AY+ziYQrKhSaIQG7KWuLAZj4sKRyRyZK1te0Ekb1UGkYn3b1YTQtXojaakq5p4WyHFvhfNPjSlJ
ClIt4QC/NZ9uS2FRee8ONEKODrcgevzcd+lbNy/mGAB7yW9XgP06YzfOyQIDAQAB
    """.decode("base64")) == """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5cagCPVB7LiX3UI5N3WRQJqTL
e5RPrhFj79/U7AY+ziYQrKhSaIQG7KWuLAZj4sKRyRyZK1te0Ekb1UGkYn3b1YTQ
tXojaakq5p4WyHFvhfNPjSlJClIt4QC/NZ9uS2FRee8ONEKODrcgevzcd+lbNy/m
GAB7yW9XgP06YzfOyQIDAQAB
-----END PUBLIC KEY-----
""".strip()

    assert rsa.import_key("""
BwIAAACkAABSU0EyAAQAAAEAAQCxTx++ykWtb2UaYFYQLt1yM893SV/wLehU2DwzeAMpxq5MsOF5
XVAd1qSElMN8Uqxdn7FXuT4XFJjH2o6MsnkheoWKPmIC357IUk/N/49dyjtk14In+HdxWKKoguXd
lOfGoriyieo8cr4kYCoYGPpHNv50NlZi3jkzQvW+hVK6v/ufshtYBRd/+NjecYVQlt7ivap8d/9g
szM+eSC91zZm8OPUCmfQX8AJOq9r7LUB/tS5DLswtJZdDDmpjhbGf/ZDg+YhHFPYvRlnGP4PlXBW
Qds44ZlSJJ780+tDuxP3Zn1Nfch4IZjkATGx7Zd9tzr8iLDe0zAGzJDaV92qHR7Hn5V5VGH1dZk2
DMiR1893vJfuE9RwDja6hUycXNjj9Y1fCYGK3rsVGO7+Dg9xab3HFqueydlMgir8MD4jShsaXk2P
jUYp2KdJuyN6BZP1oorUntgJIJGeoK59w5Vxni64rJp6KKhsKiOWM37cWAVYmd3dc0PeF3R9s/1Y
nTMtXoo1r77CjBv5q+zvMSzeFUl+ji9beSZbzl9rAvJOBw4v1Bj8EzPq5aYvEs7h9M66BbZjuyeH
zp2sRBuxE6K13j1AIVHCK7gbVwlieHWKuE5d45ealzSsChwoxGlJcHlHBI62zQqo7SHbb2An72IS
XtyKY18/3bYV4nv6ydeC9zgpVlNfGwgwP05Rkp7ldJsCz7uT6RAANV86JIp+65SCKs4gcgWWPIbn
KJ4s7fs/3oy7tUSTdviZShGj2cJGiEIyIiA=
    """.decode("base64")) == """
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC/ulKFvvVCMzneYlY2dP42R/oYGCpgJL5yPOqJsriixueU3eWC
qKJYcXf4J4LXZDvKXY//zU9SyJ7fAmI+ioV6IXmyjI7ax5gUFz65V7GfXaxSfMOU
hKTWHVBdeeGwTK7GKQN4MzzYVOgt8F9Jd88zct0uEFZgGmVvrUXKvh9PsQIDAQAB
AoGAICIyQohGwtmjEUqZ+HaTRLW7jN4/++0snijnhjyWBXIgziqClOt+iiQ6XzUA
EOmTu88Cm3TlnpJRTj8wCBtfU1YpOPeC18n6e+IVtt0/X2OK3F4SYu8nYG/bIe2o
Cs22jgRHeXBJacQoHAqsNJeal+NdTriKdXhiCVcbuCvCUSECQQD2f8YWjqk5DF2W
tDC7DLnU/gG17GuvOgnAX9BnCtTj8GY2170geT4zs2D/d3yqveLellCFcd7Y+H8X
BVgbsp/7AkEAxx4dqt1X2pDMBjDT3rCI/Dq3fZftsTEB5JgheMh9TX1m9xO7Q+vT
/J4kUpnhONtBVnCVD/4YZxm92FMcIeaDQwJAXhobSiM+MPwqgkzZyZ6rFse9aXEP
Dv7uGBW73oqBCV+N9ePYXJxMhbo2DnDUE+6XvHfP15HIDDaZdfVhVHmVnwJBAIpe
LTOdWP2zfXQX3kNz3d2ZWAVY3H4zliMqbKgoepqsuC6ecZXDfa6gnpEgCdie1Iqi
9ZMFeiO7SafYKUaNj00CQEA93rWiE7EbRKydzocnu2O2BbrO9OHOEi+m5eozE/wY
1C8OB07yAmtfzlsmeVsvjn5JFd4sMe/sq/kbjMK+rzU=
-----END RSA PRIVATE KEY-----
""".strip()

    assert rsa.import_key("""
BgIAAACkAABSU0ExAAQAAAEAAQChEcfAbVoL/jUnFMxI+xsR0zZUvMZ+9pgkLGpaxTiLRP6PZqx8
lDdwqdb7gC+m5aOz+Uwms6RHrY/xRMYEXopj877qLancMtsiqcpASOYJWxWSgW+gQMJGldwn2H97
AaHoqFlbn7NW6oNtpz4C7NotiggtVnqLdE8YyNfO6/gEpQ==
""".decode("base64")) == """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClBPjrztfIGE90i3pWLQiKLdrs
Aj6nbYPqVrOfW1mo6KEBe3/YJ9yVRsJAoG+BkhVbCeZIQMqpItsy3Kkt6r7zY4pe
BMZE8Y+tR6SzJkz5s6Plpi+A+9apcDeUfKxmj/5EizjFWmosJJj2fsa8VDbTERv7
SMwUJzX+C1ptwMcRoQIDAQAB
-----END PUBLIC KEY-----
""".strip()
