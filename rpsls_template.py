#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 = ʯͷ
# 1 = ʷ����
# 2 = ֽ
# 3 = ����
# 4 = ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(number):
	
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if number=="ʯͷ":
        return 0
    elif number=="ʷ����":
        return 1
    elif number=="ֽ":
        return 2
    elif number=="����":
	    return 3
    elif number=="����":
        return 4
    pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
	    return "����"
    elif number==4:
        return "����"

    pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    player_choice=input("����ѡ����")
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(0,5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�������ѡ����",comp_choice)# ����Ļ����ʾ�����ѡ����������
    result=(comp_number-player_choice_number)%5
    if result==1 or result==2:
        print("�����Ӯ��")		
    elif result==3 or result==4:
        print("��Ӯ��")
    elif result==0:
        print("���ͼ������ƽ��Ŷ")

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


