import json
import os
import hashlib


def block_dir():
    return os.path.dirname(os.path.abspath(__file__)) + '/blockchain/'


def sorted_files():
    files = os.listdir(block_dir())
    files = sorted([int(i) for i in files])
    return files


# hashing last filename
def get_hash(filename):
    file = open(block_dir() + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_integrity():
    files = sorted_files()
    results = []
    for file in files[1:]:
        h = json.load(open(block_dir()+str(file)))['hash']
        p_file = str(file-1)
        act_hash = get_hash(p_file)
        if h == act_hash:
            result = 'OK'
        else:
            result = 'Corrupted'
        #print('block {} is: {}'.format(p_file, result))
        results.append({'block': p_file, 'result': result})
    return results


# it writes new blocks
def write_block(name, p_id, passport, phone, p_hash=''):

    last_file = sorted_files()[-1]
    filename = str(last_file + 1)

    p_hash = get_hash(str(last_file))

    data = {
        'name': name,
        'id': p_id,
        'passport': passport,
        'phone': phone,
        'hash': p_hash
    }

    with open(block_dir() + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # write_block(name='dokov', p_id='P11', passport='AB1111', phone='+99899')
    check = check_integrity()
    # print(check)


if __name__ == '__main__':
    main()
