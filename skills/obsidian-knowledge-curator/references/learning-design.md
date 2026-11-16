# 学习笔记设计与参考

## 从检索中采用的原则

- **先建立知识框架：** 根据现有知识和学习目的选择主题边界及顺序；复杂主题可以按概念、因果、步骤或问题—方案组织，而不是照搬原材料的出现顺序。依据：[Carnegie Mellon 学习原则](https://www.cmu.edu/teaching/principles/learning.html)、[Indiana University 教学设计](https://ctl.indianapolis.iu.edu/Resources/Preparing-to-Teach/Planning-a-Learning-Session)。
- **写清内容之间的关系：** 父段概括要展开的方面，转向新的主题时说明与前文的联系；过渡要传达具体关系，不能只堆“此外、因此、综上”。依据：[Harvard 写作中心：Transitions](https://writingcenter.fas.harvard.edu/transitions)。
- **概念与实例互相解释：** 抽象概念、公式与小例子按需要紧邻；案例展示输入、关键过程或结果之一，不重复整段定义。根据读者已有知识调整解释深度。依据：[CUNY 教学实践](https://www.cuny.edu/wp-content/uploads/sites/4/page-assets/publications/cuny-publications/best_teach_practice.pdf)。
- **知识库既要聚合也要保持上下文：** 按概念建立可复用连接，但不是把每个小知识点都拆成新文件；笔记过宽和过碎都会妨碍使用。依据：[Evergreen notes 的粒度讨论](https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic)、[概念导向](https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented)。
- **复习提示按需提供：** 如果用户需要复习或自测，可依据笔记内容提出少量问题，不强加固定栏目。参考：[Cornell 笔记法](https://lsc.cornell.edu/notes.html)。

这些资料用于指导取舍，不证明某个固定笔记模板适合所有人；实际笔记要根据主题和用户目标调整。

## 示例：用一句承接总论与小节

材料已有一段解释蛋白质序列的进化信息，接下来分述结构、功能、相互作用等六个方面。若直接从概念定义跳到第一个标题，读者不容易看出后面六节属于同一组。可保留或补充：

> 蛋白质序列中的进化信息可用于分析结构、功能、相互作用、变异效应、进化历程和环境适应；下面依次介绍这六个方面。

这句话交代了总分关系；它不是要求每组标题都写“以下几点”，也不应凭空发明分类或因果。

## 示例：概念、公式与案例

```markdown
## 1. Phred 质量分数

质量分数 $Q$ 表示碱基判读的可靠程度；$P$ 是估计的判读错误概率。

$$
Q = -10\log_{10}(P)
$$

例如 Q30 对应 $P = 0.001$，即估计错误概率约为 0.1%。
```

此例无需再加代码重复计算。公式来源：[Illumina Q-score 说明](https://knowledge.illumina.com/instrumentation/general/instrumentation-general-reference_material-list/000006557)。

## 笔记工具方案

- [Obsidian Markdown skill](https://github.com/obsidianmd/obsidian-skills/blob/main/plugins/obsidian/skills/obsidian-markdown/SKILL.md)：双链、嵌入、数学与属性语法。
- [Obsidian Vault Skill 样式说明](https://github.com/Asul1n/obsidian-vault-skill/blob/main/styles/style-b.md)、[Course Noter](https://github.com/tuan3w/obsidian-vault-agent/blob/main/skills/course/agents/course-noter.md)：按主题组织概念、机制和实例；不照搬固定篇幅和强制章节。
- [Capture Concept](https://github.com/lionellau/capture-concept) 与 [Cobsidian](https://github.com/Totoro-qaq/Cobsidian)：先查找已有知识，再形成可复用的关联。
