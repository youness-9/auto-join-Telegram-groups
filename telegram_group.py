from telethon.sync import TelegramClient
from telethon import functions, types
import requests
from PIL import Image
from colorama import Fore

print('''
     ___   .___________.  ______   .___  ___.  __    ______ 
    /   \  |           | /  __  \  |   \/   | |  |  /      |
   /  ^  \ `---|  |----`|  |  |  | |  \  /  | |  | |  ,----'
  /  /_\  \    |  |     |  |  |  | |  |\/|  | |  | |  |     
 /  _____  \   |  |     |  `--'  | |  |  |  | |  | |  `----.
/__/     \__\  |__|      \______/  |__|  |__| |__|  \______|
                                                            

''')

ascii_chars = '@%#*+=-:. '


def image_to_ascii(image_path, width):
    image = Image.open(image_path)
    aspect_ratio = image.width / float(image.height)
    height = int(width / aspect_ratio / 2)
    resized_image = image.resize((width, height))
    resized_image = resized_image.convert('L')
    ascii_image = ''

    for y in range(resized_image.height):
        line = ''
        for x in range(resized_image.width):
            pixel_value = resized_image.getpixel((x, y))
            ascii_index = int(pixel_value / 256 * len(ascii_chars))
            line += ascii_chars[ascii_index]

        line = ' ' * 10 + line

        ascii_image += line + '\n'

    return ascii_image


image_url = "https://source.unsplash.com/random/900%C3%97700/?face"
try:
    response = requests.get(image_url)
    if response.status_code == 200:
        image_path = "image/2.jpg"
        with open(image_path, "wb") as f:
            f.write(response.content)
    else:
        image_path = "image/1.jpg"
except requests.exceptions.RequestException:
    image_path = "image/1.jpg"

width = 50

ascii_image = image_to_ascii(image_path, width)

ascii_lines = ascii_image.strip().split('\n')

red_link = Fore.GREEN + "https://t.me/atomic_9" + Fore.RESET
combined_lines = [line + ' ' * (50 - len(line)) + ' my group telegram: ' + red_link for line in ascii_lines]

for line in combined_lines:
    print(line)

with open("token.txt", "r") as file:
    lines = file.readlines()
    api_id = lines[0].strip().split('=')[1].strip()
    api_hash = lines[1].strip().split('=')[1].strip()

print("\n\n" + Fore.RED + "1. Join a group (put 1)")
print("2. Get group links (put 2)")
choice = input("\n#Enter the corresponding number for the action you want to take (1 or 2): " + Fore.RESET)
if choice == '1':
    file_name = input("Please enter the name of the file that contains the group links: ")

    with open(file_name, 'r') as file:
        group_links = file.readlines()

    for group_link in group_links:
        group_link = group_link.strip()
        group_username = group_link.split('/')[-1]

        with TelegramClient('session_name', api_id, api_hash) as client:
            try:
                result = client(functions.channels.JoinChannelRequest(channel=group_username))
                if isinstance(result.chats[0], types.Chat):
                    print("Successfully joined the group!")
                    print("Group Title:", result.chats[0].title)
                else:
                    print("Successfully joined the group!")
                    print("Group Title:", result.chats[0].title)
            except Exception as e:
                print("Failed to join the group:", str(e))
elif choice == '2':
    with TelegramClient('session_name', api_id, api_hash) as client:
        group_links = []
        for dialog in client.iter_dialogs():
            entity = dialog.entity
            if isinstance(entity, (types.Channel, types.Chat)):
                if hasattr(entity, 'username') and entity.username:
                    invite_link = f"https://t.me/{entity.username}"
                else:
                    invite_link = f"https://t.me/joinchat/{entity.id}"
                group_links.append(invite_link)

        for link in group_links:
            print(link)

    with open('your_telegram_link.txt', 'w', encoding='utf-8') as aotofile:
        for link in group_links:
            aotofile.write(link + '\n')
else:
    print("Invalid choice!")