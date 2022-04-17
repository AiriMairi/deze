import os
import requests as r

cur = os.getcwd() + "\\users_data\\"

if not os.path.exists(cur):
    os.makedirs(cur)

url = "https://reqres.in/api/users?page=2"
data = r.get(url).json()["data"]
for i in range(len(data)):
    new_cur = cur + str(data[i]["id"])
    if not os.path.exists(new_cur):
        os.makedirs(new_cur)
    file_dir = new_cur + "\\user_info.txt"

    name, surname, email, url = data[i]["first_name"], data[i]["last_name"], data[i]["email"], data[i]["avatar"]
    with open(file_dir, mode="w") as f:
        f.write("Name: {}\nSurname: {}\nEmail: {}".format(name, surname, email))

    image = r.get(url)
    image_dir = new_cur + "\\avatar.jpg"
    with open(image_dir, "wb") as f:
        f.write(image.content)



