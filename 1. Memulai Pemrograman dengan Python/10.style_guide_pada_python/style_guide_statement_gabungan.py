""" 
Style Guide Statement Gabungan
Setelah mengetahui aplikasi untuk pengecekan dan memformat kode, kali ini kita akan belajar cara membuat kode yang baik dan benar. Perhatikan bahwa materi ini akan menunjukkan sintaks yang disarankan dan tidak disarankan.

"""
# Statement Gabungan
# Saat Anda membuat program dengan banyak statement, usahakan untuk tidak menggabungkan >1 statement pada baris yang sama.

# Disarankan seperti ini:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Tidak disarankan seperti ini:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


# Tidak disarankan seperti ini:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# Sangat tidak disarankan seperti ini:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()
try: something()
finally: cleanup()
do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()