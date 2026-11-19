# Obsidian 适配

只在目标为 Obsidian 或材料含其特有语法时读取。核心笔记写作要求与普通 Markdown 相同。

用户指定的 vault 或文件优先。未指定时可用已明确的当前 vault，再查本机 `~/.config/research-skill-kit/local.json` 的 `obsidian.vault`。这一默认值仅用于对应本机环境，不适用于其他服务器。

编辑时保留 `[[双链]]`、`![[附件]]`、标题链接、`^块ID`、callout、任务状态和现有 YAML。表格中的双链别名使用 `[[笔记\|显示名]]`。改标题或文件名时检查受影响的入链和文内链接，语法参考 [Obsidian 内部链接](https://help.obsidian.md/links)。

需要输出可移植 Markdown 时，解析双链的实际目标和显示名，转为普通相对链接；附件路径随笔记保存，块引用和 callout 按目标环境改为可读表达。核对迁移后的引用。仅整理内容时沿用已有语法即可。
