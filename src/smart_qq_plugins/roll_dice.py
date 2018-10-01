# coding: utf-8
from random import randint

from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited
from smart_qq_bot.logger import logger

import re, time

@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("Plugin Manager is available now:)")

@on_all_message(name="RollDice")
def rool_dice(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """
    msg_id = randint(1, 10000)
    rdre = re.compile("^!roll.?\{(.*?)\}\{(.*?)\}\{(.*?)\}")
    rdfind = rdre.findall(msg.content)
    if len(rdfind) > 0:
        rd = rdfind[0]
        if len(rd) > 0:
            times_roll = int(rd[0])
            dicetype_roll = int(rd[1])
            result_list = [0] * (times_roll)
            for i in range(times_roll):
                result_list[i] = randint(1, dicetype_roll)
            result_sum = sum(result_list)
            output = rd[2] + ':' + str({result_sum:result_list})
            if isinstance(msg, GroupMsg):
                bot.send_group_msg(output, msg.from_uin, msg_id)
            elif isinstance(msg, PrivateMsg):
                bot.send_friend_msg(output, msg.from_uin, msg_id)
        else:
            print('input error')

    