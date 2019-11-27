#!usr/bin/env python3

queue = [-1, -1, -1, -1, -1, -1, -1, -1]

def cal8queues(row):
    if row == 8:
        printQueues()
        return

    for column in range(0, 8):
        if isOk(row, column):
            queue[row] = column
            cal8queues(row + 1)


def isOk(row, column):
    leftUp = column - 1
    rightUp = column + 1

    for i in range(row - 1, -1, -1):
        if queue[i] == column:
            return False
        if leftUp >= 0 and queue[i] == leftUp:
            return False
        if rightUp < 8 and queue[i] == rightUp:
            return False
        
        leftUp = leftUp - 1
        rightUp = rightUp + 1
        
    return True


def printQueues():
    for row in range(0, 8):
        line = ''
        for column in range(0, 8):
            if queue[row] == column:
                line += 'Q '
            else:
                line += '* '
        print(line)
    print('\n')


if __name__ == '__main__':
    cal8queues(0)