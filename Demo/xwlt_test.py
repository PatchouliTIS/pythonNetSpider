import xlwt

workbook = xlwt.Workbook(encoding='utf-8')   # 创建workbook对象
worksheet = workbook.add_sheet('Sheet_1')    # 在workbook中创建一个表单sheet_1

for i in range(1, 10):
    for j in range(1, i+1):
        i_str = str(i)
        j_str = str(j)
        mq_str = str(i*j)
        cur = i_str + " * " + j_str + " = " + mq_str
        worksheet.write(i-1, j-1, cur)
        # 输入格式可以直接(i-1,j-1,"%d * %d = %d"%(i,j,i*j))
    #     print(cur, end="\t")
    # print("\n")
# worksheet.write(0, 0, cur)
# worksheet.write(0, 0, "hello")                 # 在第0行第0列写入数据

workbook.save('test_arr.xls')
