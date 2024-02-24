import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from screenshot import screenshot

def select_folder():
    folder_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)  # パス入力欄をクリア
    path_entry.insert(tk.END, folder_path)  # 選択されたフォルダのパスを挿入

def select_file():
    file_path = filedialog.askopenfilename()
    driver_entry.delete(0, tk.END)  # パス入力欄をクリア
    driver_entry.insert(tk.END, file_path)  # 選択されたファイルのパスを挿入

def submit():
    url = str(url_entry.get())
    save_folder = str(path_entry.get())
    driver_path = str(driver_entry.get())
    print(url, save_folder, driver_entry)
    sc = screenshot(driver_path, url, save_folder)
    sc.run()

# ウィンドウを作成
window = tk.Tk()
window.title("URLとパス入力")

# URL入力欄を作成
url_label = tk.Label(window, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# パス選択ボタンを作成
select_button = tk.Button(window, text="フォルダを選択", command=select_folder)
select_button.grid(row=1, column=0, padx=5, pady=5)

# パス入力欄を作成
path_entry = tk.Entry(window, width=50)
path_entry.grid(row=1, column=1, padx=5, pady=5)

# driverパス選択ボタン
select_button = tk.Button(window, text="ドライバーを選択", command=select_file)
select_button.grid(row=2, column=0, padx=5, pady=5)

# driverパス入力欄
driver_entry = tk.Entry(window, width=50)
driver_entry.grid(row=2, column=1, padx=5, pady=5)

# 提出ボタンを作成
submit_button = tk.Button(window, text="開始", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# ウィンドウを表示
window.mainloop()
