# 狼人杀游戏在AgentScope中的实现

这是一个关于如何使用AgentScope玩狼人杀游戏的演示，其中六个代理扮演狼人和村民进行对抗。
在这个示例中，你可以学习到AgentScope中的以下特性。

- **_快速设置_**：如何通过代理配置文件初始化代理
- **_语法糖_**：如何使用msghub和pipeline用不到100行代码构建一个复杂的工作流
- **_提示转变量_**：如何从代理的提示中获取变量

**查看[werewolf.py](werewolf.py)以获取完整代码并亲自体验。**

```bash
# 注意：首先在./configs/model_configs.json中设置你的api_key
python werewolf.py
```

## 代码片段

### 快速设置

以下代码读取模型和代理配置，并自动初始化代理。

```python
# 读取模型和代理配置，并自动初始化代理
survivors = agentscope.init(
    model_configs="./configs/model_configs.json",
    agent_configs="./configs/agent_configs.json",
)
```

在代理配置中，你只需要指定`agentscope.agents`下的代理类和所需的参数。以Player1为例，其配置如下

```json
{
    "class": "DictDialogAgent",
    "args": {
        "name": "Player1",
        "sys_prompt": "扮演狼人杀游戏中的一名玩家。你是Player1，总共有6名玩家，分别是Player1、Player2、Player3、Player4、Player5和Player6。\n\n玩家角色:\n在狼人杀游戏中，玩家分为两个狼人、两个村民、一个预言家和一个女巫。只有狼人知道自己的队友是谁。\n狼人：他们知道自己队友的身份，并试图在夜晚淘汰一名村民，同时尝试保持不被发现。\n村民：他们不知道谁是狼人，必须在白天一起工作，推断出谁可能是狼人，并投票淘汰他们。\n预言家：一名具有每晚了解一名玩家真实身份能力的村民。这个角色对村民获得信息至关重要。\n女巫：一个角色，拥有一次在夜间保存一名玩家免于被淘汰的能力（有时是生命药水）和一次在夜间淘汰一名玩家的能力（死亡药水）。\n\n游戏规则:\n游戏由夜晚和白天两个阶段组成。这两个阶段重复进行，直到狼人或村民赢得游戏。\n1. 夜晚阶段：在夜晚，狼人讨论并投票淘汰一名玩家。特殊角色也在此时执行他们的动作（例如，预言家选择一名玩家以了解其角色，女巫决定是否救这名玩家）。\n2. 白天阶段：在白天，所有幸存的玩家讨论他们怀疑可能是狼人的人。除非出于战略目的，否则没有人揭露自己的角色。讨论后，进行投票，得票最多的玩家被“处决”或从游戏中淘汰。\n\n胜利条件:\n对于狼人来说，如果狼人的数量等于或大于剩余村民的数量，他们赢得游戏。\n对于村民来说，如果他们识别并

淘汰了小组中所有的狼人，他们就赢了。\n\n约束:\n1. 你的回应应该使用第一人称。\n2. 这是一场对话游戏。你应该仅根据对话历史和你的策略做出回应。\n\n你正在这个游戏中玩狼人杀。\n",
        "model_config_name": "gpt-3.5-turbo",
        "use_memory": true
    }
}
```

### 语法糖

以下代码是狼人杀中白天讨论的实现。使用msghub和pipeline，编程代理之间的讨论非常简单。

```python
    # ...
    with msghub(survivors, announcement=hints) as hub:
        # 讨论
        x = sequentialpipeline(survivors)
    # ...
```

### 提示转变量

有时候，我们需要从代理响应中提取所需的变量。以讨论为例，我们希望代理确定他们在讨论中是否达成了协议。

以下提示要求代理响应时包含一个“agreement”字段，以表示他们是否达成了协议。

```text
... 请按照以下格式回应，该格式可以通过python的json.loads()加载
{{
    "thought": "思考",
    "speak": "对他人说的思考总结",
    "agreement": "讨论是否达成一致(true/false)"
}}
```

使用[`DictDialogAgent`](../../src/agentscope/agents/dict_dialog_agent.py)中的`parse_func`、`fault_handler`和`max_retries`参数，我们可以直接使用变量`x.agreement`来知道讨论是否达成了协议。

更多详情，请参考[`DictDialogAgent`](../../src/agentscope/agents/dict_dialog_agent.py)的代码和我们的文档。

```python
    # ...
    with msghub(wolves, announcement=hint) as hub:
        for _ in range(MAX_WEREWOLF_DISCUSSION_ROUND):
            x = sequentialpipeline(wolves)
            if x.get("agreement", False):
                break
    # ...
```