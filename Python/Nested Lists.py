if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score]) 
    minn = sorted(set([b for a,b in students]))[1]
    print('\n'.join([a for a,b in sorted(students) if b==minn ]))        
                  

