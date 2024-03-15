# -*- coding: utf-8 -*-
"""Used to record prompts, will be replaced by configuration"""


class Prompts:
    """狼人杀游戏提示"""

    to_wolves = (
        "{}, 如果你是唯一的狼人，请淘汰一名玩家。否则，请与你的队友讨论并达成一致。请按照以下格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考",\n'
        '    "speak": "对他人说的思考总结",\n'
        '    "agreement": "讨论是否达成一致(true/false)"\n'
        "}}"
    )

    to_wolves_vote = (
        "你投票要淘汰哪位玩家？请按照以下格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '   "thought": "思考" ,\n'
        '   "speak": "玩家姓名"\n'
        "}}"
    )

    to_wolves_res = "得票最多的玩家是{}。"

    to_witch_resurrect = (
        "{witch_name}，你是女巫。今晚{dead_name}被淘汰。你想要复活{dead_name}吗？请按照以下格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考",\n'
        '    "speak": "要说的思考总结",\n'
        '    "resurrect": true/false\n'
        "}}"
    )

    to_witch_poison = (
        "你想要淘汰一名玩家吗？请按照以下json格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考", \n'
        '    "speak": "要说的思考总结",\n'
        '    "eliminate": true/false\n'
        "}}"
    )

    to_seer = (
        "{}, 你是预言家。今晚你想要查验{}中的哪位玩家？请按照以下json格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考" ,\n'
        '    "speak": "玩家姓名"\n'
        "}}"
    )

    to_seer_result = "好的，{}的角色是{}。"

    to_all_danger = (
        "白天来临，所有玩家睁开眼睛。昨夜，以下玩家被淘汰：{}。"
    )

    to_all_peace = (
        "白天来临，所有玩家睁开眼睛。昨夜是平安夜，没有玩家被淘汰。"
    )

    to_all_discuss = (
        "现在活着的玩家是{}。根据游戏规则和你的角色，基于现状和你获得的信息，为了赢得游戏，在活着的玩家中投票淘汰一名玩家，你想对其他人说些什么？你可以决定是否揭露你的角色。请按照以下JSON格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考" ,\n'
        '    "speak": "对他人说的思考总结"\n'
        "}}"
    )

    to_all_vote = (
        "现在活着的玩家是{}。根据游戏规则和你的角色，基于现状和你获得的信息，为了赢得游戏，在活着的玩家中投票淘汰一名玩家，你认为是狼人的玩家。请按照以下格式回应，该格式可以被python json.loads()加载\n"
        "{{\n"
        '    "thought": "思考",\n'
        '    "speak": "玩家姓名"\n'
        "}}"
    )

    to_all_res = "{}被投票淘汰了。"

    to_all_wolf_win = (
        "狼人获胜，接管了村庄。祝你下次好运！"
    )

    to_all_village_win = (
        "游戏结束。狼人被击败，村庄再次安全了！"
    )

    to_all_continue = "游戏继续。"
