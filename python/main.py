import numpy as np

# 초기 데이터를 설정
standard_v_data = {"v1":(1,0,0), "v2":(0,1,0), "v3":(0,0,1), "v4":(-1,0,0), "v5":(0,-1,0), "v6":(0,0,-1)}

# 데이터 규율 설정(삼각형으로 Vertex 구성)
triangle_info = {"t1":("v1","v2","v3"), "t2":("v4","v2","v3"), "t3":("v4","v5","v3"), "t4":("v1","v5","v3"), "t5":("v1","v2","v6"), "t6":("v4","v2","v6"), "t7":("v4","v5","v6"), "t8":("v1","v5","v6")}

# 학습 부위 설정 (다수의 삼각형으로 구성된 하나의 부위)
object_info = {"UP":("t1", "t2", "t3", "t4"), "DOWN":("t5", "t6", "t7", "t8")}

# 데이터 움직임 종류 개수 설정
DNA_TYPE_NUM = 10

# 부위 하나의 여러개의 삼각형이 있으니 (n개의 삼각형) 오브젝트의 길이는 1:n
# 삼각형은 3개의 점 좌표 규칙을 가지니 1:3
# 좌표 규칙은 1개당 DNA_TYPE_NUM(DNA)의 좌표를 가짐 1:DNA
# 즉 좌표 규칙 하나당 좌표 * DNA개수를 가짐 -> 위와 같은 경우는 6개의 좌표규칙이 DNA_TYPE_NUM=10이므로 60개의 좌표가 나옴
# 삼각형은 3개의 좌표 규칙을 가지니 나올 수 있는 모든 가짓 수는 DNA^3개 -> 위와 같은 경우는 10^3=1,000개 (0~999)
# 부위별 설정은 n개의 삼각형을 가지니 나올 수 있는 모든 가짓 수는 (DNA^3)^n개 -> 위와 같은 경우는 1,000^4 = 1,000,000,000,000개
# 부위개수를 m개라고 하면, 나올 수 있는 모든 가짓 수는 ((DNA^3)^n)^m개 -> 위와 같은 경우는 1,000,000,000,000^2 => 그냥 너무 많음

def vDNACalculator(v_tuple, DNA_TYPE_NUM, DNA):
    x, y, z = v_tuple[0], v_tuple[1], v_tuple[2]
    x = x - DNA*(x/DNA_TYPE_NUM)
    y = y - DNA*(y/DNA_TYPE_NUM)
    z = z - DNA*(z/DNA_TYPE_NUM)
    return (x, y, z)
    
def generateVertexData(standard_v_data, DNA_TYPE_NUM):
    for k,v in zip(standard_v_data.keys(),standard_v_data.values()):
        v_data = {}
        index = 1
        for DNA in range(0, DNA_TYPE_NUM):
            key_name = "p" + str(index)
            v_data[key_name] = vDNACalculator(v, DNA_TYPE_NUM, DNA)
            index += 1
        standard_v_data[k] = v_data
    return standard_v_data