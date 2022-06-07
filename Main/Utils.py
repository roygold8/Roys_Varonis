import hashlib


def get_sha256(file_path):
    '''
    :param file_path:
    :return:hash string of input file
    '''
    with open(file_path, "rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()


def get_file_of_hash_from_file(input_file, output_file):
    '''
    :param input_file: file to hash
    :param output_file: file with outputed hash
    :return:
    '''
    hash_value = get_sha256(input_file)
    with open(output_file, 'w') as file:
        file.write(hash_value)
    return None
