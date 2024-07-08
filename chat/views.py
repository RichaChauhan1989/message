import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def sumNumbers(start_num, end_num):
    if start_num > end_num:
        start_num, end_num = end_num, start_num
    sum = 0
    for i in range(start_num, end_num + 1):
        sum += i
    return sum




@api_view(['Post'])
def sumNumbersView(request):
    if request.method == 'POST':
        # 增加调试记录：
        print("!!!Request Headers!!!:", request.headers)
        print("!!!Request Data!!!:", request.data)
        print("!!!Request POST!!!:", request.POST)

        # V1：以下为替代为get方法
        # start_num = request.data['start_num']
        # end_num = request.data['end_num']

        # V2 修改为判断
        start_num = request.data.get('start_num')
        end_num = request.data.get('end_num')

        # V3增加判断是否Json
        # if request.content_type == 'application/x-www-form-urlencoded':
        #     start_num = request.POST.get('start_num')
        #     end_num = request.POST.get('end_num')
        # else:
        #     start_num = request.data.get('start_num')
        #     end_num = request.data.get('end_num')

        # V4 根据 Content-Type 解析请求数据
        if request.content_type == 'application/x-www-form-urlencoded':
            # 处理 URL 编码的数据
            try:
                body = json.loads(list(request.POST.keys())[0])
                start_num = body.get('start_num')
                end_num = body.get('end_num')
            except (json.JSONDecodeError, IndexError):
                return Response({'error': 'Invalid form data'}, status=400)
        else:
            # 处理 JSON 编码的数据
            start_num = request.data.get('start_num')
            end_num = request.data.get('end_num')

        # 已下到result上面为新增
        if start_num is None or end_num is None:
            return Response({'error': 'start_num and end_num are required.'}, status=400)

        try:
            start_num = int(start_num)
            end_num = int(end_num)
        except ValueError:
            return Response({'error': 'start_num and end_num must be integers.'}, status=400)

        result = sumNumbers(start_num, end_num)
        return Response({'result': result})

    # def sorting_number(number_list):
    #     sorted_list = []
    #     while number_list:
    #         # find the minimum number
    #         min_num = number_list[0]
    #         while number_list:
    #             if number_list[0] < min_num:
    #                 min_num = number_list[0]
    #             number_list.pop(0)
    #         sorted_list.append(min_num)
    #         number_list.remove(min_num)
    #     return sorted_list

    def sorting_number(number_list):
        sorted_list = []
        while number_list:
            # find the minimum number
            min_num = min(number_list)
            sorted_list.append(min_num)
            number_list.remove(min_num)
        return sorted_list

    def add_numbers(number_list):
        sum = 0
        for number in number_list:
            sum += number
        return sum




