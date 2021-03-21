import requests
import re
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    # 创建一个文件夹，保存所有图片
    if not os.path.exists('./表情包'):
        os.mkdir('./表情包')

    # 使用通用爬虫对url对应的一整张页面进行爬取
    url = 'https://www.doutula.com/photo/list/?page=%d'
    for pageNum in  range(1,3):
        #对应页码的url
        new_url = format(url%pageNum)
        page_text = requests.get(url=new_url,headers=headers).text
        # 使用聚焦爬虫将页面中所有糗图进行提取/解析
        ex = 'data-original="(.*?)"'
        img_src_list = re.findall(ex,page_text,re.S)
        #print(img_src_list)
        for src in img_src_list:
            # 请求到图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储的路径
            imgPath = './表情包/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！！')