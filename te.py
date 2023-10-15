import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeStudio 2023.10")
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # 创建菜单栏
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # 创建文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="新建", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="打开", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="保存", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="另存为", accelerator="Ctrl+Shift+S", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", accelerator="Ctrl+Q", command=self.exit_app)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)

        # 创建编辑菜单
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="撤销", accelerator="Ctrl+Z", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="重做", accelerator="Ctrl+Y", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="剪切", accelerator="Ctrl+X", command=self.cut_text)
        self.edit_menu.add_command(label="复制", accelerator="Ctrl+C", command=self.copy_text)
        self.edit_menu.add_command(label="粘贴", accelerator="Ctrl+V", command=self.paste_text)
        self.menu_bar.add_cascade(label="编辑", menu=self.edit_menu)

        # 创建操作菜单
        self.sef_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.sef_menu.add_command(label="启动终端", command=self.run_terminal)
        self.sef_menu.add_command(label="启动文件管理器", command=self.launch_fm)
        self.sef_menu.add_separator()
        self.sef_menu.add_command(label="构建(gcc)", command=self.gcc_compile)
        self.sef_menu.add_command(label="构建(javac)", command=self.javac_compile)
        self.menu_bar.add_cascade(label="操作", menu=self.sef_menu)
        """
        # 高亮
        self.style_menu = tk.Menu(self.menu_bar, tearoff=0)
        style = tk.StringVar()
        style.set("friendly")
        self.style_menu.add_radiobutton(label="默认", variable=style)
        self.style_menu.add_radiobutton(label="友好", variable=style)
        self.style_menu.add_radiobutton(label="炫彩", variable=style)
        self.menu_bar.add_cascade(label="主题", menu=self.style_menu)

        # 高亮-选择部分
        self.language_menu = tk.Menu(self.menu_bar, tearoff=0)
        language_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="语法", menu=language_menu)
        language = tk.StringVar()
        language.set("python")
        self.language_menu.add_radiobutton(label="Python", variable=language)
        self.language_menu.add_radiobutton(label="C", variable=language)
        self.language_menu.add_radiobutton(label="C++", variable=language)
"""
        # 创建帮助菜单
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="关于", command=self.show_about)
        self.menu_bar.add_cascade(label="帮助", menu=self.help_menu)

        # 状态栏
        self.status_bar = tk.Label(self.root, text="就绪", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # 绑定快捷键
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-S>", self.save_file_as)
        self.root.bind("<Control-q>", self.exit_app)
        self.root.bind("<Control-z>", lambda event: self.text_area.edit_undo())
        self.root.bind("<Control-y>", lambda event: self.text_area.edit_redo())
        self.root.bind("<Control-x>", self.cut_text)
        self.root.bind("<Control-c>", self.copy_text)
        self.root.bind("<Control-v>", self.paste_text)

    def new_file(self, event=None):
        self.text_area.delete(1.0, tk.END)

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

    def save_file(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))

    def save_file_as(self, event=None):
        file_path = filedialog.asksaveasfilename(filetypes=[("文本文件", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))

    def exit_app(self, event=None):
        if messagebox.askokcancel("退出", "确定要退出吗?"):
            self.root.destroy()

    def cut_text(self, event=None):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self, event=None):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self, event=None):
        self.text_area.event_generate("<<Paste>>")

    def run_terminal(self):
        subprocess.call(["x-terminal-emulator"])
    
    def launch_fm(self):
        subprocess.call(['xdg-open', '.'])

    def gcc_compile(self):
        file_path = filedialog.askopenfilename(filetypes=[("C语言文件", "*.c")])
        os.system(f"gcc {file_path}")

    def javac_compile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Java文件", "*.java")])
        os.system(f"javac {file_path}")

    def show_about(self):
        messagebox.showinfo("关于","CodeStudio 23.10")

root = tk.Tk()
editor = TextEditor(root)
root.iconbitmap('')
# while True:
#     root.highlight_code()
root.mainloop()
