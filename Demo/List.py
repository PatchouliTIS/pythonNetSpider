# List �б�
# ���������ƣ������Դ洢�����ͬ�������͵�Ԫ��


# ��������
a = ["a", "b", "c", "a", "d", "e"]
# ����
x = a[-1]
y = a[len(a)-1]       # ���ߵȼ�  �����ø��Ž��е���ķ���


# ��
target = input("��������Ĳ������ݣ�")
if target in a:
    x = a.index(target, 0, len(a))        # ~.index(str, start, end) ??~?��????��?start????end(??????)??��?????str??????
    print("�����������У����±�Ϊ��%d" % x)
else:
    print("��������������")


# ����
a.reverse()     # ��ת
a.sort()
a.sort(reverse=True)      # ����

# �б��Ƕ�� Ҳ���Ƕ�ά����
Office = [[], [], []]   # �������б���ɵ�һ���б�


# ��ö������enumerate()����������б��е�ֵ�е�ֵ
myList = ["a", "b", "c", "d"]       # �б�

for i, x in enumerate(myList):
    print(i + 1, x)
