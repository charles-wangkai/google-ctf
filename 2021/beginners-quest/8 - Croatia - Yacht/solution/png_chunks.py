import base64
import png

chunks = list(png.Reader(filename='../resources/hideandseek.png').chunks())
edih_body = ''.join(chunk[1].decode()
                    for chunk in chunks if chunk[0] == b'eDIH')

print(base64.b64decode(edih_body).decode())
