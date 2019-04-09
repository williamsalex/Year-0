profiles = [[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,1,2],[0,3,2,1],[1,0,2,3],[1,0,3,2],[1,2,0,3],[1,2,3,0],[1,3,0,2],[1,3,2,0],[2,0,1,3],[2,0,3,1],[2,1,0,3],[2,1,3,0],[2,3,0,1],[2,3,1,0],[3,0,1,2],[3,0,2,1],[3,1,0,2],[3,1,2,0],[3,2,0,1],[3,2,1,0]]


connection = pymysql.connect(host='127.0.0.1',
                             user='awilliams',
                             passwd='C6Kb9_9l',
                             port=3310,
                             db='safe_water')
try:
    with connection.cursor() as cursor:
        sql =


with open('ws3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
