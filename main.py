import requests
import os
import aiohttp
import html
import textwrap
import jikanpy
import bs4 
import asyncio

from asyncio import sleep


from telethon import events
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, run_async
from telegram import ParseMode
from alternation import typing_action

bot = Client(
    "notesbot",
    api_id=os.environ['5441410'],
    api_hash=os.environ['a1a4fe7d23328f419d98a58339fd9980'],
    bot_token=os.environ['5574259099:AAHwaZrsBAqmATzCjVplU2Ayy053VKFeJMc'],

)

CHAT_ID = os.environ.get('-1001745028967')
owner = int(os.environ.get('1451257129'))


def call_back_in_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )


@bot.on_message(filters.command('start'))
def start(_,message): 
    keyboard = [] 
    keyboard.append([InlineKeyboardButton ("Our Channel", url="https://t.me/pokesensei")])
    message.reply_text(text =f""" **Hello dear**,\n\n Tell your cartoon request, query and other prblm. You tell directly to lord sushanth to resolve problem.\n\n Use = /request (query) """ , reply_markup=InlineKeyboardMarkup(keyboard))


@bot.on_message(filters.command('request'))
def req_(_, message):
    if len(message.command) != 2:
        message.reply_text("Format : /request < query >")
        return
    else:
        message.reply('Your request have been sent')
        global req_
    req_ = message.text.replace(message.text.split(' ')[0] , '')
    keyboard = []
    keyboard.append([InlineKeyboardButton("✅ Accept" , callback_data=f"request:accept:{message.from_user.id}")])
    keyboard.append([InlineKeyboardButton("❌ Reject" , callback_data=f'request:reject:{message.from_user.id}')])
    bot.send_message(int(CHAT_ID) , f'#Request \n\n **• Requestor Info:-\n ID - {message.from_user.id} \n Username - @{message.from_user.username} \n\n Requested for** -{req_}' , reply_markup=InlineKeyboardMarkup(keyboard))


@bot.on_callback_query(call_back_in_filter('request'))
def botreq(_,query):
    result = query.data.split(':')

    if result[1] == "accept" and query.from_user.id == owner:
        bot.send_message(result[2] , "**Your Request has been Approved!**")
        query.message.edit('Request approved\n\n{}'.format(req_))

    elif result[1] == "reject" and query.from_user.id == owner:
        bot.send_message(result[2] , "Sorry your Request has been decline.! ")
        query.message.edit('Rejected!')

    else:
        query.answer('You are not allowed') 

from pyrogram import Client, filters
app = Client("my_account")


@app.on_message(filters.private)
def hello(client, message):
    message.reply("Hello from Pyrogram!")

     
        



bot.run()
