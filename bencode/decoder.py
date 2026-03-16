
def decode(txt):
    if txt[0] == "l":
        return decode_list(txt)
    
    if txt[0] == "i":
        return decode_int(txt)

    if txt[0].isdigit():
        return decode_str(txt)

class MalformedTorrent(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
# d7:meaningi42e4:wiki7:bencodee

#l...e
#li42ei43ee
#7:meaning
#i42e


#le
#li43ee -> [42]

#li42ei43ee
#i42ei43e
def decode_list(encoded_list):
    if encoded_list.startswith("l") and encoded_list.endswith("e"):
        content = encoded_list[1:-1]
        if content[0] == "i":
            head, rest = content.split("e")
            return decode_int(head) + decode("l"+ rest + "e")















            # for i in content[1:]:
            #     n += i
            #     if i == "e":
            #         decode_int(n)
            #         break
                    


def decode_int(encoded_int):
    if encoded_int.startswith("i") and encoded_int.endswith("e"):
        return encoded_int[1:-1]
    else:
        raise MalformedTorrent(f"Malformed integer: {encoded_int}")

def decode_str(encoded_str):
    size, word = encoded_str.split(":")
    if size.isdigit() and len(word) == int(size):
        return word
    raise MalformedTorrent(f"Malformed string: {encoded_str}")

a = "i42e"
print(a)
print(decode_int(a))
print("---")

# b = "i42"
# print(b)
# print(decode_int(b))
# print("---")

string = "1:a"
print(string)
print(decode_str(string))
print("---")

string = "10:aaaaaaaaaa"
print(string)
print(decode_str(string))
print("---")

# string = "1a:a"
# print(string)
# print(decode_str(string))
# print("---")

string = "li42ee"
print(string)
print(decode_list(string))
print("---")