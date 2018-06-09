import uuid, re, magic, os
from django.conf import settings



def handle_uploaded_file(f):
    INVALID_TYPES=['jpg','png','jepg']
    name = str(uuid.uuid4().fields[-1])[:15]

    with open('./public/images/'+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    m = magic.open(magic.MAGIC_MIME)
    m.load()
    type_file=m.file('./public/images/'+name)

    type_file=type_file.split(';')[0].split('/')[1] ;

    if type_file in INVALID_TYPES :
           return name; # hints that it is valid type
    else:
       os.remove(os.path.join('./public/images/'+name))

    return "null";
