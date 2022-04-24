from random import choice
from string import ascii_letters


class Codec:
    alphabet = ascii_letters + '0123456789'

    def __init__(self) -> None:
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl: str) -> str:
        code = ''.join(choice(Codec.alphabet) for _ in range(6))
        if code not in self.code2url:
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.code2url[shortUrl[-6:]]


codec = Codec()
url = "https://www.url.com"
tinyurl = codec.encode(url)
assert codec.decode(tinyurl) == url
