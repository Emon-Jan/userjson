import json
from random import choice, randrange

userFirstNameSeq = ['Jhon', 'Kart', 'Ross', 'Mike', 'Phillip', 'Elita', 'Monica', 'Gart', 'Poly']
userlastNameSeq = ['Martin', 'Hannigen', 'Geller', 'Morgan', 'Donglas', 'Loki', 'Tinda', 'Nambi', 'Albart', 'Pop']
userMailSeq = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@custommail.com']
otherSeq = ['_', '321', '568', '23', '100']
phoneSeq = ['+093', '+084', '+076', '+037', '+068']
addressSeq = ['-a, Dhanmondi', '/1, Motijheel', '-c, Mohakhali', '/12, Gulshan', '-d, Banani', '/25, Firmgate']

def randomJson(index):
    use = dict(id=1, userId=1, firstname="Jhon", lastname="Martin", email="jhonmartin@gmail.com", phone="+8801700000001",
    address="23-a,dhaka,bangladesh", imgURL='https://via.placeholder.com/400x400')
    use["id"] = use["id"] + index
    use["userId"] = use["userId"] + (index+1)
    use["firstname"] = choice(userFirstNameSeq)
    use["lastname"] = choice(userlastNameSeq)
    use["email"] = use["firstname"] + choice(otherSeq) + use["lastname"] + choice(userMailSeq)
    use["phone"] = choice(phoneSeq) + str(randrange(11111111, 99999999))
    use["address"] = str(randrange(0, 100)) + choice(addressSeq) + ", dhaka,bangladesh"
    use["imgURL"] = use["imgURL"] + "?text=" + str(use["userId"]) + "-" + use["firstname"]
    return use

userList = []
dict_user = dict(users= userList)
with open("fakejson/db.json", "w") as fs:
    i = 0
    while i<10000:
        userList.append(randomJson(i))
        i += 1  
    fs.write(json.dumps(dict_user, indent=4, sort_keys=True).encode())
