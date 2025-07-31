# XSS_Scan
a script used to scan xss in Python
# XSS Scanner 🔍💥

A simple Python script to detect reflected Cross-Site Scripting (XSS) vulnerabilities in URLs by injecting payloads into query parameters and checking for reflections.

---

## 📌 Features

- Parses query parameters from a given URL
- Injects customizable XSS payloads into each parameter
- Sends modified requests and checks if the payload is reflected in the response
- Highlights potentially vulnerable parameters
- Easy to extend with your own payloads

---

## 📁 File

- `xss_scanner.py` — main script for scanning URLs for XSS

---

## 🛠️ Requirements

- Python 3.x
- No external libraries (uses only built-in modules: `urllib`, `http`, `sys`)

---

## 🚀 Usage

```bash
python xss_scanner.py "http://example.com/search?q=test"
# XSS 扫描器 🔍💥

一个使用 Python 编写的轻量级反射型 XSS（跨站脚本）漏洞检测脚本。通过向 URL 查询参数注入 XSS payload，并检测是否在响应中被反射，从而发现潜在的漏洞点。

---

## 📌 功能特点

- 自动提取 URL 中的查询参数（Query Parameters）
- 向每个参数注入可定制的 XSS payload
- 发起请求，检查 payload 是否出现在响应内容中
- 标记可能存在 XSS 漏洞的参数
- 使用标准库实现，无需额外依赖

---

## 📁 文件结构

- `xss_scanner.py`：主程序脚本

---

## 🛠️ 环境要求

- Python 3.x
- 使用内置标准库（无需安装第三方库）

---

## 🚀 使用方法

```bash
python xss_scanner.py "http://example.com/search?q=test"

