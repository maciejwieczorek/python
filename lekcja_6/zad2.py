import re

class Mail(Exception):
    pass

class mailContainer:
    def __init__(self, mail):
        regex = re.compile(
            r'''\w+(.\w)+@\w+(\.\W+)+''',
            re.IGNORECASE | re.VERBOSE
        )

        matches = list(regex.finditer(mail))
        if(len(matches) !=1):
            raise mailContainer("Zly adres")
        else:
            self.address=mail

