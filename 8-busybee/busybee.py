import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un_decompressor = bz2.BZ2Decompressor()

username = un_decompressor.decompress(un)
print(username)

pw_decompressor = bz2.BZ2Decompressor()

password = pw_decompressor.decompress(pw)
print(password)