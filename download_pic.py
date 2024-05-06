import requests
import os
import random
import time
import faker


base_url = "https://img1.doubanio.com/view/status/raw/public/"
jpg_extension = ".jpg"
root_path = r'C:\Users\Auime\Pictures\鹿丸酱（豆瓣）'
save_path = r'C:\Users\Auime\Pictures\鹿丸酱（豆瓣）jpg'
fake = faker.Faker()

for root, dirs, files in os.walk(root_path):
    for file in files:
        file_name, file_extension = file.split('.')
        if file_extension == "jpg":
            continue
        
        image_url = base_url + file_name + jpg_extension
        print(fake.user_agent())
        headers = {'user_agent': fake.user_agent()}
        r = requests.get(image_url, headers=headers)
        print(r.status_code)
        with open(f"{save_path}\\{file_name}{jpg_extension}",'wb') as f:
            f.write(r.content)
            
        time.sleep(random.random()+2)
