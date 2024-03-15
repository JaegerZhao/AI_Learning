# -*- coding: utf-8 -*-
"""实用工具模块。"""
import re  # 导入正则表达式模块
from typing import Union, Any, Sequence  # 导入类型注解模块

import numpy as np  # 导入NumPy模块，用于数据处理
from loguru import logger  # 导入loguru模块，用于日志记录

from prompt import Prompts  # 从prompt模块导入Prompts类
from agentscope.agents import AgentBase  # 从agentscope.agents模块导入AgentBase类
from agentscope.message import Msg  # 从agentscope.message模块导入Msg类


def check_winning(alive_agents: list, wolf_agents: list, host: str) -> bool:
    """检查哪一组获胜"""
    if len(wolf_agents) * 2 >= len(alive_agents):  # 如果狼人数量的两倍大于等于存活玩家数量
        msg = Msg(host, Prompts.to_all_wolf_win)  # 创建一个表示狼人胜利的消息
        logger.chat(f"{host}: {msg.content}")  # 记录日志
        return True  # 返回True表示狼人获胜
    if alive_agents and not wolf_agents:  # 如果还有存活的玩家但没有狼人
        msg = Msg(host, Prompts.to_all_village_win)  # 创建一个表示村民胜利的消息
        logger.chat(f"{host}: {msg.content}")  # 记录日志
        return True  # 返回True表示村民获胜
    return False  # 否则返回False，表示游戏继续

def update_alive_players(
    survivors: Sequence[AgentBase],
    wolves: Sequence[AgentBase],
    dead_names: Union[str, list[str]],
) -> tuple[list, list]:
    """更新存活玩家的列表"""
    if not isinstance(dead_names, list):  # 如果dead_names不是列表
        dead_names = [dead_names]  # 将其转换为列表
    return [_ for _ in survivors if _.name not in dead_names], [  # 返回更新后的存活玩家列表和狼人列表
        _ for _ in wolves if _.name not in dead_names
    ]

def majority_vote(votes: list) -> Any:
    """多数投票函数"""
    unit, counts = np.unique(votes, return_counts=True)  # 获取票数中各元素的出现次数
    return unit[np.argmax(counts)]  # 返回出现次数最多的元素

def extract_name_and_id(name: str) -> tuple[str, int]:
    """从字符串中提取玩家名和ID"""
    name = re.search(r"\bPlayer\d+\b", name).group(0)  # 通过正则表达式匹配玩家名
    idx = int(re.search(r"Player(\d+)", name).group(1)) - 1  # 通过正则表达式提取ID并转换为整数
    return name, idx  # 返回玩家名和ID

def n2s(agents: Sequence[Union[AgentBase, str]]) -> str:
    """将代理名称组合成一个字符串，使用“和”连接最后两个名称。"""
    def _get_name(agent_: Union[AgentBase, str]) -> str:  # 定义一个内部函数来获取代理名称
        return agent_.name if isinstance(agent_, AgentBase) else agent_  # 返回代理名称

    if len(agents) == 1:  # 如果代理列表只有一个元素
        return _get_name(agents[0])  # 直接返回该元素的名称

    # 否则，返回一个由代理名称组成的字符串，最后两个名称之间用“和”连接
    return (
        ", ".join([_get_name(_) for _ in agents[:-1]])
        + " 和 "
        + _get_name(agents[-1])
    )
