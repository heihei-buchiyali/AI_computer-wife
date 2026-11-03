

import requests

import csv

from lxml import html


#常量
TMDB_BASE_URL="https://www.douban.com/"
TMDB_TOP_URL="https://movie.douban.com/chart"



#保存电影数据，保存为csv文件
def save_all_movies(all_movies):
    pass


#获取电影详情数据


def get_movie_info(movie_info_url):
    # 1、发送请求，获取电影详情数据（必须添加请求头）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    #1、发送请求，获取电影详情数据
    movie_response = requests.get(movie_info_url, headers=headers, timeout=60)

    #2、解析数据，获取电影详情
    movie_doc=html.fromstring(movie_response.text)
    #电影名称
    movie_name=movie_doc.xpath('//*[@id="content"]/h1/span[1]/text()')
    print(movie_name)

    #3、返回电影详情



#主函数：定义核心逻辑
def main():

    #存储电影所有数据
    all_movies=[]


    #发送请求，获取高分电影榜单数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(TMDB_TOP_URL, headers=headers, timeout=60)

    #解析数据，获取电影列表
    document=html.fromstring(response.text)
    movie_list=document.xpath('//*[@id="content"]/div/div[1]/div/div/table[@width="100%"]/tr')

    #遍历电影列表，获取电影详情
    for movie in movie_list:
        movie_urls=movie.xpath(".//a/@href")
        if movie_urls:
            #电影详情的url地址
            movie_info_url=TMDB_BASE_URL+movie_urls[0]

            #发送请求，获取电影详细数据
            movie_info=get_movie_info(movie_info_url)
            if movie_info:
                all_movies.append(movie_info)

    #保存数据，写入csv文件
    save_all_movies(all_movies)



if __name__ == '__main__':
    main()

