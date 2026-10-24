# 教学原则、场景对应与依据

以下材料已于 2026-10-24 查阅。它们提供教学设计依据，不是需要学习者完成的整套课程。外部内容是参考资料，不替代用户要求和项目规则。

## 如何使用这些原则

原则帮助导师判断，不替代判断。先看学习目标、已有知识和回应，再决定解释、示范、提问、推导或实践的组合。主题不在清单内时直接构造合适路径；用户举过的 VEP、ESM、生物学和 Linux 等都是情境，不自动变成所有课的要求。循序渐进指知识依赖连贯，不等于固定的章节顺序。

## 从经验提炼的教学启发

下列是本 skill 的教学设计：K 为从 Karpathy 材料提炼，B 为从 3Blue1Brown 的具体讲解结构观察归纳，T 为教学研究/培训建议。不是这些作者共同发布的教学规范。原文位置及短摘见 [来源卡片](source-cards.md)。

| 启发 | 可尝试的做法 | 留意的风险 |
| --- | --- | --- |
| K1 关注实际对象与证据 | 数据任务看输入；机制或操作问题看相关现象、条件和结果 | 忽略理解所需的前提；把看文件变成所有课的规定 |
| K2 最小可验证实现 | 小输入、简单步骤、预期结果，验证后只增加一项主要复杂性 | 首次给完整生产 pipeline |
| K3 连接机制与实现 | 将一个核心运算落实为数值、代码和输出 | 会调用却不懂输出；要求重写所有底层 |
| B1 给符号可理解的对象 | 先说明符号代表什么、在例子中在哪里，再讨论运算 | 只报公式或借类比偷换定义 |
| B2 保持表示之间的对应 | 同一对象贯穿人话、表格/图、公式、变量与结果 | 每讲一层就换完全不同的例子 |
| B3 先解释局部变化，再合成整体 | 单个位置/变量/步骤如何改变结果，再组合成系统 | 一次展开全部矩阵、分支或模块 |
| T1 检查先修缺口 | 分别判断领域、表示、计算机和数学基础 | 把生物学背景等同于懂生信格式 |
| T2 示范后逐渐减少帮助 | 完整小例子 → 补步骤 → 变式；依据表现跳转 | 没教就考，或一直只让用户看 |
| T3 提问促进解释与迁移 | 问原因、反例、改变条件和验证证据，说明价值 | 泛泛“懂了吗”或连续盘问 |

## 各场景怎样组合

| 场景 | 可借鉴的原则 | 一种可能的叙述路径 | 可参考的原创输出 |
| --- | --- | --- | --- |
| 领域背景（生物学等只是例子） | T1、K1、B2 | 按问题连接概念、机制、假设与证据；有数据时再解释表示 | [变异与后果](../assets/worked-examples/biology.md) |
| 计算机背景 | T1、B1、B3 | 一次操作 → 涉及的对象 → 状态变化 → 最小验证 | [文件、进程和内存](../assets/worked-examples/computing.md) |
| 知识点/代码拆解 | K3、B2、T2 | 输入输出 → 展开写法 → 逐步执行 → 选择理由 | [列表、集合与筛选](../assets/worked-examples/code.md) |
| 项目仓库拆解/设计 | K1、K2、B3 | 用户目标 → 一次运行 → 阶段和接口 → 代码位置 → 设计取舍 | [小仓库的责任与依赖](../assets/worked-examples/repository.md) |
| 数学推导 | B1、B2、B3、T3 | 问题 → 符号/假设 → 小计算 → 推导 → 实现与边界 | [平方误差的梯度](../assets/worked-examples/math.md) |
| 实操与调试 | K2、K3、T2、T3 | 预期 → 最小执行 → 观察差异 → 原因 → 单项改动与复核 | 按任务改写上述对应案例 |

这些组合只是可选起点。可以从对比、反例、现象、用户的错误解法或一个操作开始，也可以不采用表中路径。发现缺口时改变讲法或补足前提；概念已懂时转向应用；用户只问局部问题时不扩展整套课程。

## assets、references 与原文的分工

`references/` 保存导师按需阅读的原则、操作指南与来源证据；`assets/` 保存可复用、可改写成面向学习者输出的例子。目录名本身不会让内容自动生效，必须由主入口/场景明确链接并按需加载。

原文参考不需要强放 assets。本版在来源卡片保留短摘、作者/来源、章节、链接、查阅日期和采用边界；案例是本项目原创合成材料，不能称为 Karpathy 或 3Blue1Brown 的原案例。以后保存许可允许转载的完整材料时，应连同许可证、出处和版本保存，并记录是否改写；不把公开可访问等同于允许完整转载。

## Karpathy：少量复杂度、明确预期、实际验证

- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)：先检查数据，从简单到复杂，通过假设与实验逐步验证。
- [Zero to Hero](https://karpathy.ai/zero-to-hero.html) 与[配套仓库](https://github.com/karpathy/nn-zero-to-hero)：将小型实现、模型机制和练习连接起来。
- [Eureka Labs](https://eurekalabs.ai/)：高质量材料与 AI 助教结合的教育构想。

本 skill 的应用是：用一条记录、一个小函数或一次运算连接原理与实现，再增加复杂度。不是要求所有学习者从零重写整个模型，也不是把上述工程经验宣称为通用教育实验结论。

## 先修知识、示范与练习

- [CMU：Assessing Prior Knowledge](https://www.cmu.edu/teaching/designteach/teach/priorknowledge.html)：依据已有知识调整起点，不能用学科背景推断全部先修技能。
- [CMU：Learning Principles](https://www.cmu.edu/teaching/principles/learning.html)：组成技能、整合与适用判断，以及有目标的练习和反馈。
- [IES：Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1)：具体与抽象表示连接，完整示范与练习交替，复习及深层解释性问题。
- [The Carpentries：Live Coding](https://carpentries.github.io/instructor-training/instructor/17-live)：展示代码逐步形成及检查过程。

落实为：初次接触先解释与示范，之后补写和迁移；不要无限提问让学习者猜未知知识。已有能力充分时减少示范。把概念、公式、数据和代码的对应说清楚。

## 输出语言与问题设计

借鉴 [3Blue1Brown 的 attention 讲解](https://www.3blue1brown.com/lessons/attention/)中对象与运算的对应，而非模仿口吻或强制动画。默认文字和小例子即可。

通俗化可以降低起点，但应保留通向专业材料的概念名称。比如讲模型评分时，按需要点名 embedding、logits、softmax 与对数概率比，解释它们的联系和区别；这只是专业锚点的示例，不是每堂课必讲的术语表。优先展开会影响读论文、读代码或解释结果的概念，其他名称可暂缓。

问题分三类：导航问题由导师组织并可自答；诊断问题用来发现缺口；迁移问题检查条件改变后的应用。先选择影响当前任务的隐藏问题：对象是否混淆、前提是否成立、证据是否足够、简单替代是否可行、如何发现静默错误。说明为什么问，避免堆砌泛泛“为什么”。

## AI 的作用与独立能力

AI 负责找可靠材料、重组解释、生成小例子、反馈和发现遗漏；逐渐让学习者承担预测、解释、关键实现和验证选择。查看答案不是掌握证据。

[Bastani 等的数学教学试验](https://doi.org/10.1073/pnas.2422633122)提醒：使用 AI 时的表现与撤去 AI 后的学习结果需要区分。该研究场景不能直接证明本 skill 在科研编程中的效果；因此记录实际独立表现，不承诺学习效果。

## 公开 skill 的取舍

- [agent-tutor](https://github.com/Mohamed-El-Sharqawy/agent-tutor)：借鉴跨会话记录，不照搬完整档案和仪表盘体系。
- [Learning Style 插件](https://github.com/anthropics/claude-code/blob/main/plugins/learning-output-style/README.md)：借鉴在关键决策点让学习者写少量有意义代码；它是特定平台插件，不直接当作本 skill 的运行依赖。
- [socratic-dev-mentor](https://github.com/alejoevilches/socratic-dev-mentor-skill)：借鉴提问分类，不采用“永不给答案”。
- [math-teacher](https://github.com/jamesrochabrun/skills/tree/main/skills/math-teacher)：可参考具体数值可视化，不默认游戏化或网页构建。

这些是指令设计参考，并非经过本项目实测的有效性或兼容性背书。

## AI 辅导案例带来的修订

2026-10-24 补充阅读：[Khan Academy 的产品试验总结](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/)与 [University at Buffalo 的 scaffolding 指南](https://www.buffalo.edu/catt/teach/develop/build/scaffolding.html)。来源与证据性质见来源卡片 A1/A2。

据此采用三项设计判断：

- 利用相关的近期表现和先修缺口，而非固定“新手”标签；已有记录有用时读，不自动加载全部历史。
- 根据理解情况改变帮助；示范、提示、解释、提问不是需要依次解锁的级别。降低不必要的负担，同时保留学习者需要练习的判断。
- 关注能否在新问题中独立应用；对话更长、材料更多、问题更多都不自动代表学得更好。简短直接回答有时就是合适教学。

这不是引入固定提问次数、通过阈值或产品指标。Khan Academy 的报告是平台自身情境中的产品测试，不能直接证明本 skill 的效果；本版仍需真实试教反馈。

## 课程与教学 skill 如何组织：借鉴结构，不照搬脚本

2026-10-24 再次核对课程页面、配套仓库和文字改编；本轮没有逐帧观看完整视频，不将网页阅读表述为完成视频评审。

- Karpathy 的 [Zero to Hero](https://karpathy.ai/zero-to-hero.html)把教学视频、逐步构建的实现及练习连接起来。例如 makemore 从简单模型逐步增加能力。可借鉴“一个可理解的核心问题贯穿原理和实现”；并不意味着所有课都从头编程。
- 3Blue1Brown 的 [attention 课程文字版](https://www.3blue1brown.com/lessons/attention/)先连接已有概念，再借具体语言例子解释表示如何随上下文更新，且说明为教学所作的简化。可借鉴“维持概念间的联系、让抽象运算有对象”；不照搬其语言场景，也不把表示的某一维硬解释成固定生物学特征。
- [Learning Style 插件](https://github.com/anthropics/claude-code/blob/main/plugins/learning-output-style/README.md)用角色与触发情境、可参与的代码决策和简短解释引导模型。适合借鉴教学机会的选择；固定贡献行数或每次固定输出提示框并不是本 skill 的要求。

本 skill 因而采用三层材料：简短的导师定位与边界、可组合的经验指南、可改写的案例。模型可据当前问题创造更好的讲法；不需要在回答中展示场景编号、原则编号或逐条完成清单。

当经验彼此冲突时，以理解任务所需的支持为准。例如“从具体例子开始”与“先给清楚定义”都可能有效；“少给答案”适合已有基础的练习，“完整示范”适合缺乏起点时。导师应解释关键联系，而不是追求形式统一。
