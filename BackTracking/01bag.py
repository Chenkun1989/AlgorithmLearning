#!usr/bin/env python3

# 当前最大重量
maxW = 0

# i: 表示当前考察到哪个物品
# cw: 表示当前背包中的重量
# items: 物品重量的集合
# w: 背包所能承受的总重量
def f_bag(i, cw, items, w):
    global maxW
    if i == len(items) or cw >= w:
        if maxW < cw:
            maxW = cw
        return
    
    # 回溯的关键
    f_bag(i + 1, cw, items, w)

    if cw + items[i] <= w:
        f_bag(i + 1, cw + items[i], items, w)
    
if __name__ == "__main__":
    items = [61, 13, 28, 30, 49]
    w = 100

    f_bag(0, 0, items, w)

    print("maxW = %d" %(maxW))