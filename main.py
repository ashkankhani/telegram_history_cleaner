from pyrogram import Client
from pyrogram.types import Dialog,Message
from config import *


app = Client('myacc' , api_id=api_id , api_hash=api_hash)
async def main():
    async with app:
        contacts = await app.get_contacts()
        async for dialog in app.get_dialogs():
            dialog:Dialog
            if(dialog.chat.first_name is None):
                continue
            ok = True
            for user in contacts:
                if(dialog.chat.id == user.id):
                    ok = False
                    break
            if(ok):
                print(f'deleting {dialog.chat.id!r} messages!')
                message_ids = []

                message : Message
                async for message in app.get_chat_history(dialog.chat.id):
                    message_ids.append(message.id)
                await app.delete_messages(dialog.chat.id,message_ids,revoke=False)
                    

app.run(main())
