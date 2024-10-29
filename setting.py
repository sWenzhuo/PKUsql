import pymysql.cursors

Patents = {
    '专利公开号': 'publication_number',
    '专利名称': 'patent_name',
    '专利类型': 'patent_type',
    '专利摘要': 'abstract',
    '申请⼈': 'applicant',
    '专利申请号': 'application_number',
    '申请⽇': 'application_date',
    '申请公布⽇': 'publication_date',
    '授权公布号': 'grant_publication_number',
    '授权公布⽇': 'grant_publication_date',
    '申请地址': 'application_address',
    '主权项': 'claims',
    '发明⼈': 'inventor',
    '分类号': 'classification_number',
    '主分类号': 'main_classification_number',
    '代理机构': 'agency',
    '分案原申请号': 'original_application_number',
    '优先权': 'priority',
    '国际申请': 'international_application',
    '国际公布': 'international_publication',
    '代理⼈': 'agent',
    '省份或国家代码': 'province_or_country_code',
    '法律状态': 'legal_status',
    '专利领域': 'patent_field',
    '专利学科': 'patent_subject',
    '多次公布': 'multiple_publications'
}
Companies = {
    "公司名称": "company_name",
    "英文名称": "english_name",
    "统一社会信用代码": "unified_social_credit_code",
    "公司类型": "company_type",
    "经营状态": "business_status",
    "成立日期": "establishment_date",
    "核准日期": "approval_date",
    "法定代表人": "legal_representative",
    "注册资本": "registered_capital",
    "实缴资本": "paid_in_capital",
    "参保人数": "insured_number",
    "公司规模": "company_size",
    "经营范围": "business_scope",
    "注册地址": "registered_address",
    "营业期限": "business_period",
    "纳税人识别号": "taxpayer_identification_number",
    "工商注册号": "business_registration_number",
    "组织机构代码": "organization_code",
    "纳税人资格": "taxpayer_qualification",
    "曾用名": "former_name",
    "省份": "province",
    "城市": "city",
    "区域": "district",
    "官网链接": "website_link",
    "行业": "industry",
    "主要行业类别": "primary_industry_category",
    "次要行业类别": "secondary_industry_category",
    "第三行业类别": "tertiary_industry_category",
    "登记机关": "registration_authority",
    "经度": "longitude",
    "纬度": "latitude",
    "网站": "website"
}


#创建connection对象
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Srits0ft",
    db="industry",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

