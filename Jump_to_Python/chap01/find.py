# coding: cp949

a="hobby"

print("find�� index�Լ��� ������ ��")

print(a.find('y'))
print("a.find('y') ����Ϸ�")
if a.find('c'):
    print("���ϴ� ������� ����")
print("a.find('c') ����Ϸ�")
print(a.index('y'))
print("a.index('y') ����Ϸ�")
try:
    print(a.index('c'))
    print("a.index('c') ����Ϸ�")
except ValueError as e:
    print("���ϴ� ������� ����")
    print(e)
finally:
    print("c.index('c') ����Ϸ�")
print("\n 12���� �������� 13���� ���Ĵ� �����")
