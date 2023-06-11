import random
import string

def ref_gen(stringLength=16):
	ref_char = string.ascii_letters + string.digits
	ref = ''.join(random.sample(ref_char, stringLength))
	ref_id = "-".join([ref[i:i+4] for i in range(0, len(ref), 4)])
	print(ref_id)

ref_gen()


#Output
#H3yI-97PF-ubk2-Uv8V
