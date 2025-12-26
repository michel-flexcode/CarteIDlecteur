from PyKCS11 import PyKCS11Lib, CKF_SERIAL_SESSION, CKF_RW_SESSION

PKCS11_LIB = "/usr/lib/x86_64-linux-gnu/libbeidpkcs11.so"

ATTR_MAP = {
    "surname": "BEID_CARD_SURNAME",
    "givenname": "BEID_CARD_GIVENNAME",
    "birthdate": "BEID_CARD_BIRTHDATE",
}

def read_eid_identity():
    pkcs11 = PyKCS11Lib()
    pkcs11.load(PKCS11_LIB)

    slot = pkcs11.getSlotList(tokenPresent=True)[0]
    session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)

    session.login("")  # PIN NON requis pour lecture identité

    objects = session.findObjects()
    result = {}

    for obj in objects:
        attrs = session.getAttributeValue(
            obj,
            [
                getattr(pkcs11, attr)
                for attr in ATTR_MAP.values()
                if hasattr(pkcs11, attr)
            ],
            allAsBinary=True,
        )

        for key, value in zip(ATTR_MAP.keys(), attrs):
            if value:
                result[key] = bytes(value).decode("utf-8").strip()

    session.logout()
    session.closeSession()

    return result


if __name__ == "__main__":
    data = read_eid_identity()
    print("Nom      :", data.get("surname"))
    print("Prénom   :", data.get("givenname"))
    print("Naissance:", data.get("birthdate"))
