import time,os,requests

def get_page(folder_name,front_url,start_page,end_page,normal_page_number,url_numbers,url_rear,nap,sleep,ini_count,arith_url_numbers):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    current_time = time.strftime(' Time  %Y.%m. %d %H_%M_%S')
    sub_folder_name = str(ini_count) + '. ' + str(current_time)

    if not os.path.exists(folder_name + '/' + sub_folder_name):
        os.mkdir(folder_name + '/' + sub_folder_name)

    if start_page =='' and end_page =='':

        f = open(folder_name + '/' + sub_folder_name + '/' + 'page.html', 'w', encoding='utf-8')
        url = front_url
        r = requests.get(url, headers=headers)
        html = r.text
        f.write(html)
        f.close()
        print("Finish downloading html file!")
        time.sleep(nap)

    else:

        if normal_page_number == True:

            for page_number in range(start_page,end_page+1):
                f = open(folder_name + '/' + sub_folder_name + '/' +'page # ' + str(page_number) + '.html', 'w', encoding = 'utf-8')
                url = front_url + str(page_number) + url_rear
                r = requests.get(url,headers = headers)
                html  = r.text
                f.write(html)
                f.close()
                print ('Finish downloading page # ' + str(page_number) + '......')
                time.sleep(nap)

        else:
            if type(url_numbers) is list:

                for page_number in url_numbers:
                    f = open(folder_name + '/' + sub_folder_name + '/' + 'page # ' + str(page_number) + '.html', 'w', encoding='utf-8')
                    url = front_url + str(page_number) + url_rear
                    r = requests.get(url, headers=headers)
                    html = r.text
                    f.write(html)
                    f.close()
                    #print(url)
                    print('Finish downloading page # ' + str(page_number) + '......')
                    time.sleep(nap)

            elif str(type(url_numbers)) == "<class 'generator'>":

                for arith_number in arith_url_numbers:
                    f = open(folder_name + '/' + sub_folder_name + '/' + 'page # ' + str(arith_number) + '.html', 'w', encoding='utf-8')
                    url = front_url + str(arith_number) + url_rear
                    r = requests.get(url, headers=headers)
                    html = r.text
                    f.write(html)
                    f.close()
                    print(url)
                    print('Finish downloading page # ' + str(arith_number) + '......')
                    time.sleep(nap)

            else:
                print("Error! 'url_numbers' must be a list or generator type.")


    time.sleep(sleep)



def auto_requests(folder_name,url,start_page = '',end_page = '',normal_page_number = True,url_numbers='',url_rear = '/',nap = 0,sleep = 0,ini_count = 0):

    front_url = url
    arith_url_numbers = []

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    if str(type(url_numbers)) == "<class 'generator'>":

        for x in range(start_page, end_page + 1):
            x = url_numbers.__next__()
            arith_url_numbers.append(x)
    else:
        pass

    if sleep == 0:

        get_page(folder_name,front_url,start_page,end_page,normal_page_number,url_numbers,url_rear,nap,sleep,ini_count,arith_url_numbers)

    else:
        while True:
            print('Start downloading Round # ' + str(ini_count) + '\n')
            get_page(folder_name,front_url,start_page,end_page,normal_page_number,url_numbers,url_rear,nap,sleep,ini_count,arith_url_numbers)
            ini_count += 1




