# Copyright (c) 2021 Itz-fork
import os
from config import Config


class Defaults():
    """
    Harley Chat botunun tüm varsayılan verileri

     Değişkenler:
         Chat_Log - Varsayılan sohbet günlüğü
         Motor - Varsayılan OpenAI Yapay Zeka Motoru
         Max_Tokens - Varsayılan Maksimum jeton sayısı
         CHAT_LOG_DB - Kullanıcıların sohbet günlüklerini kaydetmeyi söyle (geçici)
         Engines_list - OpenAI'de kullanılabilen motor adlarının listesi """
    Chat_Log = f"""
You: Hey, neler oluyor?
{Config.CHAT_BOT_NAME}: Merhaba!
You: Ben""" + " {uname} " + f"""!
{Config.CHAT_BOT_NAME}:
"""
    Engine = "text-davinci-002"
    Max_Tokens = int(os.environ.get("MAX_TOKENS", 100))
    CHAT_LOG_DB = {}
    Engines_list = ["davinci", "curie", "babbage", "ada", "text-davinci-002",
                    "text-curie-001", "text-babbage-001", "text-ada-001", ]
