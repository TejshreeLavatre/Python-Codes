# IP address segment number and segment length checker

ip_address = input('Enter a valid IP address: \n')
if ip_address[-1] != '.':
    ip_address += '.'

seg_num = 1
seg_len = 0
# character = ' '

for character in ip_address:
    if character == '.':
        print('Segment number {} contains {} elements'.format(seg_num, seg_len))
        seg_num += 1
        seg_len = 0
    else:
        seg_len += 1
