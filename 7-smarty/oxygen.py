import png

reader = png.Reader(filename='smarty/smarty_files/oxygen.png')

chunkit = reader.chunks()

for chunk_type, chunk_data in chunkit:
    if chunk_type == b'IHDR':
        print(chunk_data)