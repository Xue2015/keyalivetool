import base64

with open("golive.ico","rb") as i:
    b64str = base64.b64encode(i.read())
    with open("goliveicon.py","ab+") as f:
        f.write("img=b'" +  str(b64str))
with open("goliveicon.py","a") as f:
    f.write("'")
