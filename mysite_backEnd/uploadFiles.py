import uuid

def handle_uploaded_file(f):

    name = str(uuid.uuid4().fields[-1])[:15]
    with open('./public/images/'+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return name;
