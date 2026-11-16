# 本仓库维护约定

- `skills/<name>/` 是唯一源码；安装目录只链接到此处。新增 skill 保持独立任务，不默认让所有任务先经过一个总控 skill。
- 入口使用标准 YAML `name` / `description`；名称与目录一致。统一封装和元数据，不要求各 skill 使用同一种输出结构或教学流程。
- 详细指导放在 skill 自己的 `references/` 并从入口或相关引用提供按需索引；范例放 `assets/`。不依赖仓库根部文档或另一个 skill 才能运行。
- 修改教学 skill 时保留适应性与任务边界；修改笔记 skill 时保留精简、系统、概念关联、公式/代码保护和用户确定的两级编号。
- 个人路径、笔记、学习记录和备份放仓库外。本机可选配置为 `~/.config/research-skill-kit/local.json`，不得写入密钥。
- 完成后运行 `scripts/validate.py`；修改管理脚本时运行 `python3 -m unittest discover -s tests -v`。行为变更使用相关真实或最小示例验收，不把结构通过宣称为学习效果已验证。
- 更新 README 索引和必要来源记录。保持原有引用和来源边界；不要自动选择新的开源许可证。远端推送和发布依照用户授权。
