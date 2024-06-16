Barang=input('masukan nama barang')
harga=int(input('masukan harga barang'))
jumlah_barang=int(input('masukan jumlah_barang'))

text= f'''===NOTA KASIR===
barang: {Barang}
harga: {harga}
jumlah_barang: {jumlah_barang}
total {harga*jumlah_barang}
'''
file = open('nota.txt', 'a')
file.write(text)
file.close()


