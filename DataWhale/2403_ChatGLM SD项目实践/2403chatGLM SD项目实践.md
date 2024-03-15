# 用免费GPU线上跑chatGLM、SD项目实践

​	DataWhale组织了一个线上白嫖GPU跑chatGLM与SD的项目活动，我很感兴趣就参加啦。之前就对chatGLM有所耳闻，是去年清华联合发布的开源大语言模型，可以用来打造个人知识库什么的，一直没有尝试。而SD我前两天刚跟着B站秋叶大佬和Nenly大佬的视频学习过，但是生成某些图片显存吃紧，想线上部署尝试一下。

> 参考：DataWhale [学习手册链接](https://datawhaler.feishu.cn/docx/BwjzdQPJRonFh8xeiSOcRUI3n8b)

## 1 学习简介

本文以趋动云平台为例，详细介绍下如何通过平台提供的在线开发环境，**<font color='red'>直接在云端编写</font>**、运行代码，并使用**<font color='red'>GPU资源进行加速</font>**。本教程将学习云算力资源的使用方式，并给出了两个AI项目实践：

- 用免费GPU创建属于自己的聊天GPT
- 用免费GPU部署自己的stable-diffusion

**平台注册：**

- 注册即送168元算力金
- Datawhale专属注册链接：https://growthdata.virtaicloud.com/t/SA

**适用人群**：

- 新手开发者、快速原型设计者；
- 需要协作和分享的团队；
- 对大模型部署感兴趣的人；
- 深度学习入门学习者；
- 对使用GPU资源有需求的人。

**优势：**

无需进行本地环境配置，简单易用，便于分享和协作。

**组织方：**Datawhale x 趋动云

## 2 云端部署chatGLM3-6B模型

> ***ChatGLM3 是智谱AI和清华大学 KEG 实验室联合发布的新一代对话预训练模型。***
>
> ***推理速度比上一代提高了很多，虽然本教程有两种启动方式，但教程作者强烈推荐使用streamlit体验，效果极佳。***

### 2.1 项目配置

本项目采用 **趋动云** 云端配置，环境采用 `Pytorch2.0.1、python3.9、cuda11.7` 的镜像，在公开模型选择 <u>葱姜蒜上传的这个ChtaGLM3-6B模型</u> 。

资源配置采用拥有24G显存的 **B1.large** ，最好设置一个最长运行时间，以免忘关环境，导致资源浪费。我这里选择了24h的最长运行时间。

### 2.2 环境配置

成功配置好项目基本资源后，就可以进入JupyterLab开发环境了。现在需要在终端进一步配置环境，通过我们选择的模型资源中的加载的文件，我们首先要设置镜像源、克隆ChatGLM项目。

1. 升级apt，安装unzip

   ```shell
   apt-get update && apt-get install unzip
   ```

2. 设置镜像源，升级pip

   ```shell
   git config --global url."https://gitclone.com/".insteadOf https://
   pip config set global.index-url https://pypi.virtaicloud.com/repository/pypi/simple
   python3 -m pip install --upgrade pip
   ```

3. 克隆项目，并进入项目目录

   ```shell
   git clone https://github.com/THUDM/ChatGLM3.git
   cd ChatGLM3
   ```

4. 安装项目依赖与peft

   > 可以先把requirements.txt中的torch删掉，避免重复安装

   ```shell
   pip install -r requirements.txt
   pip install peft
   ```

### 2.2 镜像发布

​	通过以上步骤，项目环境已部署完成啦。但是为了防止下次加载还得重新装载镜像，此时可以将镜像封装发布。

1. 点击右上角将当前环境制作为镜像

   ![image-20240311114056429](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311114056429.png)

2. 填写镜像名称，构建镜像

   填写自定义镜像名称后，在Dockerfile中，填写以下内容，以之前选择的基础镜像，创建镜像。

   ![image-20240311171511654](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311171511654.png)

   ```dockerfile
   RUN apt-get update && apt-get install unzip
   
   RUN git config --global url."https://gitclone.com/".insteadOf https://
   RUN pip config set global.index-url https://pypi.virtaicloud.com/repository/pypi/simple
   RUN python3 -m pip install --upgrade pip
   
   RUN pip install  accelerate==0.27.2  \ 
    aiofiles==23.2.1  \ 
    altair==5.2.0  \ 
    annotated-types==0.6.0  \ 
    arxiv==2.1.0  \ 
    blinker==1.7.0  \ 
    colorama==0.4.6  \ 
    cpm-kernels==1.0.11  \ 
    dataclasses-json==0.6.4  \ 
    distro==1.9.0  \ 
    fastapi==0.110.0  \ 
    feedparser==6.0.10  \ 
    ffmpy==0.3.2  \ 
    gitdb==4.0.11  \ 
    GitPython==3.1.42  \ 
    gradio==4.21.0  \ 
    gradio_client==0.12.0  \ 
    greenlet==3.0.3  \ 
    h11==0.14.0  \ 
    httpcore==1.0.4  \ 
    httpx==0.27.0  \ 
    huggingface-hub==0.21.4  \ 
    jsonpatch==1.33  \ 
    jupyter_client==8.6.0  \ 
    langchain==0.1.11  \ 
    langchain-community==0.0.27  \ 
    langchain-core==0.1.30  \ 
    langchain-text-splitters==0.0.1  \ 
    langchainhub==0.1.15  \ 
    langsmith==0.1.23  \ 
    latex2mathml==3.77.0  \ 
    loguru==0.7.2  \ 
    markdown-it-py==3.0.0  \ 
    marshmallow==3.21.1  \ 
    mdtex2html==1.3.0  \ 
    mdurl==0.1.2  \ 
    openai==1.13.3  \ 
    orjson==3.9.15  \ 
    packaging==23.2  \ 
    peft==0.9.0  \ 
    protobuf==4.25.3  \ 
    pydantic==2.6.3  \ 
    pydantic_core==2.16.3  \ 
    pydeck==0.8.1b0  \ 
    pydub==0.25.1  \ 
    PyJWT==2.8.0  \ 
    python-multipart==0.0.9  \ 
    regex==2023.12.25  \ 
    requests==2.31.0  \ 
    rich==13.7.1  \ 
    ruff==0.3.2  \ 
    safetensors==0.4.2  \ 
    semantic-version==2.10.0  \ 
    sentence-transformers==2.5.1  \ 
    sentencepiece==0.2.0  \ 
    sgmllib3k==1.0.0  \ 
    shellingham==1.5.4  \ 
    smmap==5.0.1  \ 
    SQLAlchemy==2.0.28  \ 
    sse-starlette==2.0.0  \ 
    starlette==0.36.3  \ 
    streamlit==1.32.0  \ 
    tenacity==8.2.3  \ 
    tiktoken==0.6.0  \ 
    timm==0.9.16  \ 
    tokenizers==0.15.2  \ 
    toml==0.10.2  \ 
    tomlkit==0.12.0  \ 
    transformers==4.38.2  \ 
    typer==0.9.0  \ 
    typing_extensions==4.10.0  \ 
    urllib3==2.2.1  \ 
    uvicorn==0.28.0  \ 
    watchdog==4.0.0  \ 
    websockets==11.0.3  \ 
    zhipuai==2.0.1
   ```

3. 等待镜像构建

   ![image-20240311114257441](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311114257441.png)

   ![image-20240311114320543](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311114320543.png)

4. 在开发环境实例中修改镜像

   在构建的项目中，点击右边栏的 **开发** ，点击 **修改挂载镜像** ，在 **我的** 里选择刚才创建的镜像。

   ![image-20240311114509586](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311114509586.png)

### 2.4 通过 Gradio 创建ChatGLM交互界面

Gradio是一个开源的Python库，用于创建机器学习模型的交互式界面。其中，StableDiffusion的WebUI就是通过 Gradio 开发。

1. 修改模型目录

   将 `basic_demo` 文件夹中的 `web_demo_gradio.py` 的模型加载路径改为 `/gemini/pretrain`

   ![20240311output](https://raw.githubusercontent.com/ZzDarker/figure/main/img/20240311output.png)

2. 修改启动路径

   将代码最后一行的启动代码修改为如下代码。

   ```py
   demo.queue().launch(share=False, server_name="0.0.0.0",server_port=7000)
   ```

3. 添加外部端口映射

   在界面的右边添加外部端口：7000

4. 运行gradio界面

   返回终端，输入以下指令，运行 `web_demo_gradio.py`

   ```shell
   cd basic_demo
   python web_demo_gradio.py
   ```

   等待模型慢慢加载完毕，即可访问gradio页面。

5. 访问gradio页面

   加载完毕之后，复制外部访问的连接，到浏览器打打开

   ![](https://raw.githubusercontent.com/ZzDarker/figure/main/img/1710127591278.jpg)

   打开后界面如下，可以再input输入框进行问答测试。

   ![image-20240311124022630](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311124022630.png)

   可以看到，Gradio界面并不稳定，回答的结果有点"抽风"，回复中夹杂指令字符`<|im_end|>` 与 `<|im_start|>`，并且出现了自问自答的现象。

> 配置好环境后，再次访问，在终端输入以下指令直接运行 gradio 。
>
> ```shell
> cd ChatGLM3/basic_demo
> python web_demo_gradio.py
> ```

### 2.5 通过 streamlit 创建ChatGLM交互界面

> ***如果你运行了gradio，需要先杀掉这个进程，不然内存不够。***
>
> ***CTRL+C 可以杀掉进程***

- Streamlit是一个开源的Python库，它允许用户 **<font color='red'>快速创建</font>** 交互式的数据科学和机器学习Web应用程序。

- 与Gradio相比，Streamlit在用户体验设计上更为通用，适合广泛的应用场景，而Gradio则更专注于展示和交互机器学习模型。

根据以下步骤，创建 streamlit 交互界面。

1. 修改模型目录

   将 `basic_demo` 文件夹中的 `web_demo_streamlit.py` 的模型加载路径改为 `/gemini/pretrain`

2. 运行streamlit界面

   在终端输入以下指令，运行web_demo_stream.py并指定7000端口，这样就不用再次添加外部端口映射啦~

   ```shell
   streamlit run web_demo_streamlit.py --server.port 7000
   ```

3. 访问streamlit界面

   复制外部访问地址到浏览器打开，**之后模型才会开始加载**。（不复制在浏览器打开是不会加载的！）

   ![image-20240311131049872](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311131049872.png)

   出现以上界面，等待加载，加载结束后工作台后端画面如下。可以在输入框提问。

   ![image-20240311131208656](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311131208656.png)

   可以看到，streamlit界面的问答，比Gradio的问答稳定的多，没有多余的符号与自问自答。

   ![image-20240311131423451](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311131423451.png)

> 配置好环境后，再次访问，在终端输入以下指令直接运行 streamlit 。
>
> ```shell
> cd ChatGLM3/basic_demo
> streamlit run web_demo_streamlit.py --server.port 7000
> ```

### 2.6 chatGLM功能测试

可以看到，chatGLM侧边栏有三行可调节参数，其功能分别如下：

- **Max_length**（最大长度）: 这个参数决定了模型生成文本的最大长度。如果输入文本特别长，可能需要调整这个参数以避免截断数据，确保模型能够理解完整的上下文信息。
- **Top_P**（Top P采样）: 这是一个概率阈值，模型在生成文本时只考虑累积概率达到这个阈值的词汇。较高的Top P值意味着模型在生成时会考虑更多的词汇，从而增加文本的多样性。
- **Temperature**（温度）: 这个参数控制生成文本的随机性。较低的温度值会使模型生成更确定性、更可预测的文本，而较高的温度值则会使模型生成更多样化和创造性的文本。

下面分别测试以上3个方面对生成文本的影响。

#### 2.6.1 测试max_length对生成文本的影响

​	max_length决定了模型生成**文本的最大长度**。于是本次测试决定让模型回答固定长度的答案，一次超过max_length，一次没有对比其对生成文本的影响。

1. max_length较大时，生成500字的作文

   ![image-20240311133450424](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311133450424.png)

   可以看到成功生成了一篇大约500字的作文。

2. max_length较小时，生成500字的作文

   ![image-20240311133351286](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311133351286.png)

​	可以看到，max_length有效的控制了生成的字数，当要求生成的字数小于max_length，生成的文章将会被截断。

#### 2.6.2 测试Top_P对生成文本的影响

​	Top P影响着**文本的多样性**。即值越大用词越丰富，值越少越词穷。本次测试让模型生成一个旅游规划，对比不同Top P的值对生成文本的影响。

1. Top_P较大时，生成泰山旅游行程

   ![b58f9c8037f4f7c62dd4199eabd270d](https://raw.githubusercontent.com/ZzDarker/figure/main/img/b58f9c8037f4f7c62dd4199eabd270d.png)

2. Top_P较小时，生成泰山旅游行程

   ![001603c8a83d9a136ec4da22bbfdbe3](https://raw.githubusercontent.com/ZzDarker/figure/main/img/001603c8a83d9a136ec4da22bbfdbe3.png)

​	可以看到，在Top P值较大时，生成的旅游规划较为详细，每日都有不同的行程。而Top P较小时，生成的旅游规划十分简单，而且还出现了 "专线 bus"、"泰山 train"这种不伦不类的用词。

#### 2.6.3 测试Temperature对生成文本的影响

​	Temperature控制着生成文本的随机性。即值越小回答越死板，值越大回答越丰富。这个参数和Top P其实有点相似，经过查阅资料得知：

> 当 temperature 设置为较高值（接近1或大于1）时，模型在选择下一个 token 时，会倾向于选择概率较低的选项，从而产生更具创新性和多样性的输出。
>
> 当 temperature 设置为较低值（接近0但大于0）时，模型在选择下一个 token 时，会更偏向于选择概率较高的选项，从而产生更准确、更确定性的输出。

​	所以，本次选择一个大语言模型表现不太的领域——数学，来考察 temperature 对生成文本的影响。

1. Temperature较大时，对年龄计算题的回答

   ![a5afc2777eeceab876535f046418c19](https://raw.githubusercontent.com/ZzDarker/figure/main/img/a5afc2777eeceab876535f046418c19.png)

2. Temperature较小时，对年龄计算题的回答

   ![bf4f80b97bc9c2f6bbc06ca7d8594c2](https://raw.githubusercontent.com/ZzDarker/figure/main/img/bf4f80b97bc9c2f6bbc06ca7d8594c2.png)

​	可以看到，当 temperature 值较大时，回答的答案有推理思路，联想能力强，得到了正确的回答，而 temperature 值较小时，回答仅仅把题干中两个数字相加，未能理解题目的真正含义，死板的回复了错误的答案。

## 3 云端部署StableDiffusion模型

### 3.1 项目配置

1. 创建项目

   在趋动云用户工作台中，点击 **快速创建** ，选择 **创建项目**，创建新项目。

2. 镜像配置

   选择 **趋动云小助手** 的 `AUTOMATIC1111/stable-diffusion-webui` 镜像。

   ![image-20240311172651842](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311172651842.png)

3. 数据集配置

   在 **公开** 数据集中，选择 `stable-diffusion-models` 数据集。 

   ![1710149308792](https://raw.githubusercontent.com/ZzDarker/figure/main/img/1710149308792.jpg)

   配置完成后，点击创建，要求上传代码时，选择 **暂不上传** 。

4. 初始化开发环境

   找到最右侧 "**开发**"-> "**初始化开发环境实例**"，我这里没按教程配置，因为SD生图需要较大显存，我选择了拥有24G显存的 **B1.large**，其他按教程一样，并设置了24h的最长运行时间。

   ![image-20240311173442914](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311173442914.png)

### 3.2 环境配置

​	因为数据集代码有所变化，所以教程中有些步骤可以省略，以下为具体步骤。

1. 解压代码及模型

   ```shell
   tar xf /gemini/data-1/stable-diffusion-webui.tar -C /gemini/code/ 
   ```

2. 拷贝frpc内网穿透文件

   ```shell
   chmod +x /root/miniconda3/lib/python3.10/site-packages/gradio/frpc_linux_amd64_v0.2
   ```

3. 拷贝模型文件到项目目录下

   ```shell
   cp /gemini/data-1/v1-5-pruned-emaonly.safetensors /gemini/code/stable-diffusion-webui/
   ```

4. 更新系统httpx依赖

   ```shell
   pip install httpx==0.24.1
   ```

5. 运行项目

   ```shell
   cd /gemini/code/stable-diffusion-webui && python launch.py --deepdanbooru --share --xformers --listen
   ```

   运行项目后，点击右侧添加，创建 **外部访问链接** 。

   ![1710149802068](https://raw.githubusercontent.com/ZzDarker/figure/main/img/1710149802068.jpg)

6. 访问StableDiffusion的WebUI

   复制外部访问链接，在浏览器粘贴并访问，就成功打开WebUI界面啦。

   ![1710149919322](https://raw.githubusercontent.com/ZzDarker/figure/main/img/1710149919322.jpg)

7. 生成镜像

   点击右上角 将当前环境制作为镜像，点击 **智能生成**，在 `AUTOMATIC1111/stable-diffusion-webui`  基础镜像下生成，点击 **构建**，完成对镜像的构建。

   ![image-20240311175121573](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240311175121573.png)

   之后安装上一章的步骤，将镜像配置到你的项目里就好啦。

> 配置好环境后，再次访问，在终端输入以下指令直接运行 WebUI 。
>
> ```
> cd /gemini/code/stable-diffusion-webui && python launch.py --deepdanbooru --share --xformers --listen
> ```

### 3.3 StableDiffusion 使用

1. 生成第一张美图

   部署好了当然是要生成一张图，我选择生成一张猫猫图，结果如下。

   ![image-20240312104308881](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240312104308881.png)

   ​	库自带的模型是 `v1-5-pruned-emaonly` 模型，这个模型是官方的1.5 版本预训练模型，是在512*512的小尺寸图像上训练的，所以说如果图像尺寸超过1000的话，容易出现多头多人的情况。

   ​	在这里我选择的参数与提示词如下：

   - **提示词(prompt)**：

     ```
     1 cat
     ```

   - **负面提示词(Negative prompt)**：

     ```
     out of frame,(worst quality, low quality, normal quality:2),text,bad eyes,weird eyes closed eyes,badhandv4:0.8,OverallDetail,render,bad quality,worst quality,signature,watermark,extra limbs,
     ```

   - **迭代步数(Steps)**、**采样器(Sampler)**、**提示词相关性(CFG scale)**：

     ```
     Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, 
     ```

   - **随机种子(Seed)**、**图像尺寸(Size)**、**模型(Model)**

     ```
     Seed: 3052626755, Size: 384x512, Model hash: 6ce0161689, Model: v1-5-pruned-emaonly, Version: v1.6.0
     ```

   生成的猫猫图如下：

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00002-3052626755.png)

2. 批量生成

   我想要更多的猫猫图，于是增大了生成的 `Batch Count` 和`Batch size`，生成结果如下。

   ![image-20240312111137432](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240312111137432.png)

   可以看到一下生成了16张猫猫图，它实际上是分了两批，每批生成8张，这样生成的。`Batch count` 控制了生成批次的数量，`Batch size` 控制每批生成图片的数量。`Batch size` 越大对显卡显存要求越高，当然白嫖的24g显存不在话下了。

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/grid-0000.png)

   可以看到生成的图像各有千秋，甚至有的生成了个房子（太离谱了），所以选择合适的种子很重要。可以通过批量生成找到自己喜欢的图像风格的种子，固定下来进行进一步操作。

   我很喜欢第四张，大脸狸花猫，于是点开图片，可以在图片下方看到种子号 `2617670965`。

   ![image-20240312112233897](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240312112233897.png)

3. 图像放大

   我想放大刚才选中的大脸狸花猫图，可以通过固定种子，并通过 `Hires fix` 的方法放大生成图像。

   我想使用一个名为 **R-ESRGAN4x** 的放大算法，从云平台下载太慢了，选择从 [该github链接](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth) 本地下载，并放在`/gemini/code/stable-diffusion-webui/models/RealESRGAN/RealESRGAN_x4plus.pth`路径下。

   设置以下参数，重新生成，结果如下。

   ![image-20240312113245064](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240312113245064.png)

   成功将图像尺寸放大到原来的两倍，即 768*1024 的尺寸。图像参数如下：

   ```
   1 cat
   Negative prompt: out of frame,(worst quality, low quality, normal quality:2),text,bad eyes,weird eyes closed eyes,badhandv4:0.8,OverallDetail,render,bad quality,worst quality,signature,watermark,extra limbs,
   Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 2617670965, Size: 384x512, Model hash: 6ce0161689, Model: v1-5-pruned-emaonly, Denoising strength: 0.35, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+, Version: v1.6.0
   ```

   猫猫图如下：

   ![00019-2617670965](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00019-2617670965.png)

   效果还不错，不过我还想让他更清晰一点，于是选择让他放大4倍，结果如下。

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00020-2617670965.png)

   可以看到，真的清晰了不少。

4. 图生图

   图生图就是以给的图片为基准，生成其他的图片，我就像用刚才生成的猫猫图，来生成一个宇宙的星系，于是写了以下的提示词。

   ```
   stars,out space,galaxy,
   ```

   负面提示词不变，分两个批次生成16张星系图片，结果如下。

   ![image-20240312123732068](https://raw.githubusercontent.com/ZzDarker/figure/main/img/image-20240312123732068.png)

   可以看到，生成了具有猫猫形状的星系图案，我从中挑了一张最喜欢的，就是下面这张。

   ![img](https://raw.githubusercontent.com/ZzDarker/figure/main/img/00048-3318537879.png)

   图片参数如下：

   ```
   stars,out space,galaxy,
   Negative prompt: out of frame,(worst quality, low quality, normal quality:2),text,bad eyes,weird eyes closed eyes,badhandv4:0.8,OverallDetail,render,bad quality,worst quality,signature,watermark,extra limbs,
   Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 3, Seed: 3318537879, Size: 768x1024, Model hash: 6ce0161689, Model: v1-5-pruned-emaonly, Denoising strength: 0.7, Version: v1.6.0
   ```

   以上就尝试玩SD的基本功能啦，之后可以再玩一些进阶玩法，用更厉害的模型，添加lora、ControlNet等插件，生成更可控好看的图片。



