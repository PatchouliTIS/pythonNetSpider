# ��ӡ����
def printLine():
    print("-" * 30)


printLine()

# ȫ����ֲ�����
# �ں�����߶���ı�������ȫ�ֱ���
# ����ں������޸�ȫ�ֱ�������ô����Ҫʹ��global �����������������
a = 10


def aMend():
    global a
    a += 1
    print(a)


print(a)
