# 教学来源卡片

查阅日期：2026-10-24。短摘按原文保留英文；中文“提炼”是本 skill 的归纳。没有保存完整文章、视频字幕或原图。正式课若需精确技术结论，应返回对应官方文档/原论文，不用教学风格参考替代技术证据。

## K1：Karpathy 的数据与验证流程

- 作者：Andrej Karpathy；文章发表于 2019-04-25。
- 原文：[A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)。定位：The recipe；1. Become one with the data。
- 短摘：“Become one with the data”
- 提炼：先检查实际数据，再逐步增加经实验检验的复杂性。
- 应用：讲原始记录、建立最小示例、运行前说明预期。
- 边界：来自神经网络训练实践；将它用于一般科研 pipeline 是本 skill 的迁移，不是原文对所有软件教学的结论。

## K2：从小实现连接机制

- 作者：Andrej Karpathy。
- 原文：[Zero to Hero 课程页](https://karpathy.ai/zero-to-hero.html)、[课程仓库](https://github.com/karpathy/nn-zero-to-hero)。定位：课程介绍、micrograd、makemore 与练习说明。
- 短摘（课程页）：“building neural networks, from scratch, in code”
- 提炼：让机制在可运行的小实现中显现，配练习巩固。
- 应用：实现一个核心计算，再连接库函数；理解后增加规模。
- 边界：课程要求一定 Python 和数学基础。本 skill 应补先修缺口，不强制照搬课程难度或手写整个模型。

## B1：3Blue1Brown 的对象与表示

- 作者：Grant Sanderson；线性变换课发表于 2016-08-07，网页另署文字改编者。
- 原文：[Linear transformations and matrices](https://www.3blue1brown.com/lessons/linear-transformations/)。定位：开篇与 Transformations Are Functions。
- 短摘：“When you think of matrices as transforming space”
- 提炼：先给运算一个可理解的作用，再将它与符号表达连接。
- 应用：解释矩阵怎样改变向量，或者解释代码操作怎样改变数据；可使用数值表，不要求动画。
- 边界：后者是教学迁移；几何直觉不能取代证明，也不能把所有数据转换当线性变换。

## B2：从局部关系到整体反向传播

- 作者：Grant Sanderson；课发表于 2017-11-03，文字改编 Josh Pullen。
- 原文：[What is backpropagation really doing?](https://www.3blue1brown.com/lessons/backpropagation/)。定位：Quick Recap 及后续对输出、代价、权重影响的解释。
- 短摘：“the output that the network gives, along with the output you wanted it to give”
- 提炼：沿用一个例子，先理解输出差异及局部影响，再理解组合机制。
- 应用：单个变量变化 → 公式中的依赖 → 代码中的计算路径。
- 边界：这是对该课结构的观察，不宣称作者发布过通用的“B2 教学原则”。

## T1：先修知识

- 机构：[CMU Eberly Center](https://www.cmu.edu/teaching/designteach/teach/priorknowledge.html)。定位：Assessing Prior Knowledge 的开篇与评估方式。
- 提炼：已有知识和误解影响新知识整合；据此调整起点。
- 应用：分别检查生物学、文件格式、计算机、语法和数学，不用单一水平标签。

## T2：示范、具体与抽象、问题

- 机构：美国教育科学研究院 IES；指南发表于 2007-09。
- 原文：[Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1)。定位：建议 2、4、7。
- 短摘：“Interleave worked example solutions with problem-solving exercises.”
- 提炼：交替示范与练习，连接具体和抽象，用解释性问题促进理解。
- 应用：示范一个实例，再补写或变式；问题关注原因和证据。
- 边界：指南综合多个教育情境；不能据此声称本 skill 已在成人计算生物学项目中验证有效。

## T3：展示编程过程

- 来源：[The Carpentries：Live Coding is a Skill](https://carpentries.github.io/instructor-training/instructor/17-live)。定位：Why Participatory Live Coding 与实践建议。
- 短摘：“participatory live coding”
- 提炼：让学习者看到代码形成、运行和检查的过程。
- 应用：文字中展示预期、中间输出、局部修正，不只给最终脚本。
- 边界：现场教学方法迁移到文字对话，不要求同步视频或用户抄写所有操作。

## A1：AI 辅导如何利用学习上下文

- 来源：Khan Academy，2026-05 页面；[How Khan Academy Is Building a Better AI Tutor: Our Most Recent Learnings](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/)。定位：How We Measure Success、Using a student’s Khan Academy learning history to improve tutoring。
- 提炼：该平台报告比较了近期表现、先修缺口等上下文的作用，并观察下一题无辅导时的表现；不是只看聊天是否顺畅。
- 应用：参考实际表现调整教学和复习，不以身份或主题名称固定难度。
- 边界：平台自报产品测试，特定用户和练习环境；不外推数值收益，不据此要求所有问题必须做测验。查阅日期：2026-10-24。

## A2：帮助随需要改变

- 来源：[University at Buffalo：Scaffolding Content](https://www.buffalo.edu/catt/teach/develop/build/scaffolding.html)。定位：Scaffolding Through Design、Zone of Proximal Development、Scaffolding Strategies。
- 提炼：支持程度依据已有知识、任务复杂性和学习进展调整；能力提高时可以减少，遇到更难任务时可重新增加。
- 应用：相同用户在不同主题和阶段使用不同讲法，允许直接示范、短讲、反例和独立实践之间切换。
- 边界：大学教学指导材料，不是本 skill 的效果试验；不把某种支架永久固定为个人学习风格。查阅日期：2026-10-24。
