import hashlib
file_path = r"E:\Python\example.txt" 
with open(file_path, "rb") as file:
    content = file.read()
    print(f"content in file:{content}")
hash_value = hash(content)
print(f"hash_value={hash_value}")
sha256_hash = hashlib.sha256(content).hexdigest()
print(f"sha256={sha256_hash}")
