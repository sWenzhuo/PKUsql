from setting import connection


createsql= """
CREATE TABLE IF NOT EXISTS search (
    id INT AUTO_INCREMENT PRIMARY KEY,
    applicant VARCHAR(255),
    publication_number VARCHAR(31),
    application_date DATE,
    publication_date DATE,
    grant_publication_date DATE,
    score DOUBLE
);
"""

#只运行一次
def create_table():
    try:
        print("开始建立表")
        with connection.cursor() as cursor:
            cursor.execute(createsql)
            connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"error:{e}")


    else:
        print("创建表成功")
        connection.close()



if __name__=="__main__":
    create_table()


