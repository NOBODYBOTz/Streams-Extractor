#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "17983098"))
    API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6234365091").split())
    
