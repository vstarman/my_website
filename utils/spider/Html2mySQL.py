"""
将编程派网的html文件,信息过滤,保存到mySQL中
"""
import os
import django
# 防止django报错
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_website.settings")
django.setup()
import re
import json
from bs4 import BeautifulSoup
from apps.blog.models import ArticleInfo


def parse_html_to_json():
    """
    # title:标题
    author:作者
    # img_url:首页图片链接   article-thumb dimmable lazy-hidden   (/static/.+.[jpg|png])
    # content_url:文章原始链接
    # page_view:浏览量
    like_num:喜欢数量
    # abstract:文章摘要
    # label:标签
    """
    # 创建bs对象
    soup = BeautifulSoup(open("CodingPython.html"), "lxml")
    # 创建json文件对象
    f_writ = open("CodingPython.json", "a")

    class_list = soup.find_all(class_="js-infinite-item")
    f_writ.write("[")
    # 遍历DOM,找出需要的字段值
    for tag in class_list:
        item = dict()
        item["label"] = tag.a.get_text()
        tag_list = tag.find_all(class_=["header",          # content_url, title
                                        "article-thumb",   # img_url
                                        "description",     # abstract
                                        "share-article"])  # int page_view
        # 获取不同格式图片url
        img_attr = tag_list[1].attrs
        if "style" in img_attr:
            img_url = img_attr["style"]
        else:
            img_url = img_attr["data-bg"]

        item["content_url"] = tag_list[0].a.attrs["href"]
        item["title"] = tag_list[0].get_text()
        item["img_url"] = "http://codingpy.com" + re.findall(r"(/static/.+.[jpg|png])", img_url)[0]
        item["abstract"] = tag_list[2].get_text()
        item["page_view"] = int(tag_list[3].get_text())
        # item["author"] = ""
        # item["like_num"] = ""
        f_writ.write(json.dumps(item) + ",\n")

        # 存到数据库
        save_to_mysql(item)

    f_writ.write("]")
    f_writ.close()


def save_to_mysql(item):
    try:
        article_info = ArticleInfo.objects.create(
            title=item['title'],
            img_url=item['img_url'],
            content_url=item['content_url'],
            page_view=item['page_view'],
            abstract=item['abstract'],
            label=item['label'],
        )
        article_info.save()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parse_html_to_json()
