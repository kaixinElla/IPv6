# -------------------------------------#
#       对单张图片进行预测
# -------------------------------------#
from retinaface import Retinaface
import cv2
# import pymysql

# db = pymysql.connect(host="localhost",
#                      user="root",
#                      password="123456",
#                      db="students",
#                      port=3306)
# cursor = db.cursor()

retinaface = Retinaface()
img = "./img/2.jpg"

image = cv2.imread(img)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r_image, num = retinaface.detect_image(image)
print(num)

# sql = """INSERT INTO stu(stu_num)
#         VALUE('%s')"""
# cursor.execute(sql, num)
# db.commit()
# db.close()
#
##r_image = cv2.cvtColor(r_image, cv2.COLOR_RGB2BGR)
##cv2.imshow("after", r_image)
##cv2.waitKey(0)
