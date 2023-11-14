n = 300 # meng inisiasi variabel n dengan value 300

print(n) # menampilkan value n

n = 1000 # reassignment atau mengisi ulang atau mereplace value n dengan 1000

print(n) # menampilkan value n

number = 300 # meng inisiasi variabel n dengan value 300

# ini tidak bisa, 
# karena nama variabel selalu dimulai dengan alfabet
# 1number = 300

# nama variable bisa mengandung numeric 
# jika pada posisi character ke 2 atau lebih
num1 = 300

# nama variable juga bisa mengandung symbol 
# tetapi hanya simbol '_' (underscore)
num_1 = 300

# nama variable juga bisa diawali dengan symbol '_' (underscore)
# tetapi biasanya untuk case tertentu
_num1 = 300
print(_num1)


numb1 = 300 # tipe data integer

print(type(numb1))

numb1 = 'saya' # tipe data string

print(type(numb1))

# tampilkan hasil 1 di tambah 2 dikali 3 dibagi 4 dikurang 5
print(1 + 2 * 3 / 4 - 5)

print (2342 / 6) # hasil bagi
print (2342 % 6) # sisa bagi (modulus)

print(2 ** 12) # 2 pangkat 12

print(2342 % 2 == 0 )

number = 1231231
if number % 2 == 0:
    print('Genap')
else:
    print('Ganjil')
    
result = 8 / 2
result = int(result)

print (result)

# + Operators
s = 'Saya'
t = 'Anak'
u = 'Kuat'

print(s, t, sep=' ')

# separator tidak berfungsi, karena tidak pisah menggunakan koma
print(s + t, sep=' ')

print(s + ' ' + t + ' ' + u)
print(f'{s} {t} {u}')

print('bla ' * 30) # menulis kata bla sebanyak 30 kali

text = 'SaYa AnAk kUaT'

print(text.capitalize()) # Saya anak kuat
print(text.upper()) # SAYA ANAK KUAT
print(text.lower()) # saya anak kuat
print(text.title()) # Saya Anak Kuat
print(text.swapcase()) # sAyA aNaK KuAt
print(text.replace('AnAk', 'manusia')) # SaYa manusia kUaT

students = ['Ade', 'Gilbert', 'Mardhya'] 
students.append('Agus')

# print(students)
students[2] = 'Qais'

print(students)


students1 = ['Ade', 'Gilbert', 'Mardhya'] 
print(students1)
# ini error 
students1[2] = 'Qais'

print(students1)

# tuple biasanya digunakan untuk konstan data
jabodetabek = ('Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi')

# dictionary
# key indexing
MLB_team = {
    'Colorado': 'Rockies', # key nya adalah Colorado, Valuenya Rockies
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

print(MLB_team['Boston'])

print(MLB_team.keys())
print(MLB_team.values())

for key in MLB_team.keys():
    print(MLB_team[key])
    
# dictionary
# key indexing
MLB_team = {
    'Colorado': 'Rockies', # key nya adalah Colorado, Valuenya Rockies
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

MLB_team['Jakarta'] = 'Ersapta Team' # menambahkan element / item

print(MLB_team)

# dictionary
# key indexing
MLB_team = {
    'Colorado': 'Rockies', # key nya adalah Colorado, Valuenya Rockies
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

MLB_team['Jakarta'] = 'Ersapta Team' # menambahkan element / item
print('Before: ', MLB_team)

MLB_team.pop('Jakarta') # menghapus element / item berdasarkan key
print('After: ', MLB_team)
