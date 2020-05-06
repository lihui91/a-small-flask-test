# -*- coding :utf-8 -*-


#用列表存储书籍信息
import numpy as np
import os
from flask import Flask,render_template
app = Flask(__name__)
with open('E:/flask/flask_template_demo/book.txt','r', encoding='utf-8') as file:
    lines = file.readlines()

    books = []

    for line in lines:

        result_dict = {}
        if line != '\n':
            line = line.strip()
            list = line.split()
            arr = np.array(list)

            if arr[0].isdigit():
                k1 = 'book_num'
                k2 = 'book_name'
                k3 = 'book_class'
                result_dict[k1] = arr[0]
                result_dict[k2] = arr[1]
                result_dict[k3] = arr[2]
                books.append(result_dict)
    # print(books)

# books=[
#     {'book_num':'1','book_name':'HTML5+CSS3+JavaScript从入门到精通（标准版）','book_class':'计算机'},
#     {'book_num':'2','book_name':'JavaWeb项目开发实战入门（全彩版）','book_class':'计算机'},
# ]




@app.route('/')
def book():
    return render_template('book.html',books=books)


if __name__ == '__main__':
    app.run()
