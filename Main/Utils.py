import hashlib


def get_sha256(file_path):
    with open(file_path, "rb") as file:
        bytes = file.read()
    return hashlib.sha256(bytes).hexdigest()

def get_file_of_hash_from_file(input_file,output_file):
    hash = get_sha256(input_file)
    with open (output_file,'w') as file:
        file.write(hash)
    return None