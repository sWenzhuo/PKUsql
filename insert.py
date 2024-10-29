import os
import re
import pymysql
import pandas as pd
from tqdm import tqdm
from setting import Patents, connection, Companies

import logging
logging.basicConfig(filename='insert_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 专利字段映射
Patent_Mapping_Column = {
    "专利申请人": "applicant",
    "专利公开号": "publication_number",
    '申请⽇': 'application_date',
    '申请公布⽇': 'publication_date',
    '授权公布⽇': 'grant_publication_date',
}

def filter_company(applicant):
    """
    提取中文公司名称，并去除空格
    """
    applicants_str = applicant.replace(" ", "")
    applicants = re.findall(r'[\u4e00-\u9fa5()（）]+', applicants_str)
    return applicants

def process_result(res):
    """
    处理查询结果，针对多个申请人进行拆分并赋予评分
    """
    df = pd.DataFrame(res)
    new_rows = []
    for idx, row in df.iterrows():
        applications = filter_company(row["applicant"])
        for i, applicant in enumerate(applications):
            score = 1 / (i + 1)
            new_row = row.copy()
            new_row["applicant"] = applicant
            new_row['score'] = score
            new_rows.append(new_row)
    new_df = pd.DataFrame(new_rows)
    return new_df

def insert_to_new_db(df, offset, batch_size):
    """
    插入数据到数据库的search表
    """
    try:
        with connection.cursor() as cursor:
            for _, row in df.iterrows():
                sql = """
                    INSERT INTO search (applicant, publication_number, application_date, publication_date, grant_publication_date, score) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    row['applicant'],
                    row['publication_number'],
                    row['application_date'],
                    row['publication_date'],
                    row['grant_publication_date'],
                    row['score']
                ))
            connection.commit()
            logging.info(f"成功插入 {batch_size} 条记录，当前偏移量 {offset}")
    except Exception as e:
        connection.rollback()
        logging.error(f"最后成功插入的偏移量: {offset}, 错误: {e}")
        raise

def insert(connection):
    """
    从专利表中批量读取并处理数据后插入到目标表中
    """
    try:
        offset = 0
        batch_size = 500
        with connection.cursor() as cursor:
            while True:
                columns = ', '.join(Patent_Mapping_Column.values())
                sql = f"SELECT {columns} FROM patents LIMIT %s OFFSET %s"
                cursor.execute(sql, (batch_size, offset))
                res = cursor.fetchall()
                if not res:
                    break
                df = process_result(res)
                insert_to_new_db(df, offset, batch_size)
                offset += batch_size
    except Exception as e:
        connection.rollback()
        logging.error(f"插入失败，错误: {e}")
    else:
        logging.info("写入成功")
        connection.close()

if __name__ == "__main__":
    insert(connection)

