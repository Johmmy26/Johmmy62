#coding:gbk
"""
���������Ľֵ�
���ߣ��м���
"""



import codecs
import jieba.posseg as pseg
import jieba

names = {}#  ���������Ϊ�������ƣ�ֵΪ��������ȫ���г��ֵĴ���
relationships = {}#���������ϵ������ߣ���Ϊ����ߵ���㣬ֵΪһ���ֵ� edge ��edge �ļ�Ϊ����ߵ��յ㣬ֵ������ߵ�Ȩֵ
lineNames = []# ��������������ÿһ�ηִʵõ���ǰ���г��ֵ���������

jieba.load_userdict("name.txt")#���������
with codecs.open("limingpoxiaodejiedao.txt", 'r', 'utf8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)  # �ִʣ����ش���
        lineNames.append([])  # Ϊ��������һ�������б�
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue  # ���ִʳ���С��2��ôʴ��Բ�Ϊnr��������ʱ��Ϊ�ôʲ�Ϊ����
            lineNames[-1].append(w.word)  # Ϊ��ǰ�εĻ�������һ������
            if names.get(w.word) is None:  # ���ĳ���w.word�����������ֵ���
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

            # ���������ִ���ͳ�ƽ��
# for name, times in names.items():
#    print(name, times)

# ���� lineNames ��ÿһ�У�����Ϊ�����г��ֵ������������������������������֮����δ�б߽��������½��ı�Ȩֵ��Ϊ 1��
# �����Ѵ��ڵıߵ�Ȩֵ�� 1�����ַ����������ܶ������ߣ���Щ����߽��������
for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

                # ���ڷִʵĲ�׼ȷ����ֺܶ಻�������ġ����������Ӷ����³��ֺܶ�����ߣ�
                # Ϊ�˿�������ֵΪ10�������߳���10����������Ϊ��������

with codecs.open("People_node.txt", "w", "utf8") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")



with codecs.open("People_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
f=open('People_edge.txt','r',encoding='utf-8')
f2=open('name.txt','r',encoding='utf-8').read()
lines=f.readlines()


A=[]
for line in lines:
    A.append([])
    m=line.strip('\n').split(' ')
    for x in m:
        A[-1].append(x)
for items in A:
    if items[0]and items[1] not in f2:
        del(items)

f.close()

print(A)
