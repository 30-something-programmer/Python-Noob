import os
#Types of file opening:
# r = reading only
# w = writing only
# w+ = reading & writing

kitteh_file = os.path.join('Random Files','cat_names.txt')

kitteh_file_open = open(kitteh_file,'w')
kittehs = ['Link','Kylo','Eris','Luna']
for kitteh in kittehs:
    kitteh_file_open.write(kitteh)
kitteh_file_open.close()


#another way
with open (kitteh_file,'w') as f:
    for kitteh in kittehs:
        f.write(kitteh)

with open(kitteh_file,'r') as f:
    kittehs.append(f.read())
print(kittehs)