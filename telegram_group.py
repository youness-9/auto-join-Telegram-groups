from telethon.sync import TelegramClient
from telethon import functions, types
import requests
from PIL import Image
from colorama import Fore

print('''


 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░ 
                                                                   
                                                                   
                                                      
''')

ascii_chars = '@%#*+=-:. '
def send_file_to_group(client):
    send_links = input("\nDo you want to send these links to a group to share them for benefit? (yes/no): ").strip().lower()
    if send_links == 'yes':
        group_username = 'arabebug'  # Username of the group (https://t.me/arabebug)
        file_path = 'your_telegram_link.txt'

        try:
            client.send_file(group_username, file_path, caption="Here are the extracted group links 📎")
            print(Fore.GREEN + "File was successfully sent to the group.")
        except Exception as e:
            print(Fore.RED + "Failed to send the file to the group:", str(e))



with open("token.txt", "r") as file:
    lines = file.readlines()
    api_id = lines[0].strip().split('=')[1].strip()
    api_hash = lines[1].strip().split('=')[1].strip()

print("\n\n" + "1. Join a group (Type 1)")
print("2. Extract group links (Type 2)")
choice = input("\n#Enter the number(1 or 2): ")
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

    # 📤 Call the new function to send file from user account
    send_file_to_group(client)
