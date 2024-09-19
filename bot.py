import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQGrZw0AumVJSRytUsHsbDl75FbK628R5FydCV4hu7UfPEeiATewad3BmUhGPxtgfSR4OR3JxTNhbdHq8M9gItLcEzB2hhuQfuHtytkvAm3x7N-Hwkkp9434hPQlxTMsdRj7X-uNMovWr_1wdh-8YsYCAu96Y7BjbFmXMvioetDzEQ-uLvI5_ylvnEH05UO_DLE5gQslN163zoUPhgJ3EFtDJgTd3AeVD0czEyF9UDRnp6HLiz40bRzDAlhiMy8smilwrJhl6MCZxR03kVkgLRZ1ld4Cg0I1XtWvR6UEITxLnbIh_SsuHFV30_FVk5zaRgLoBrhxhHaRfsBylG3ugsyW9pmuuwAAAAF28Sj4AA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







