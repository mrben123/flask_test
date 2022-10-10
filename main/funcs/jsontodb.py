import pathlib
import re
import json
import os


from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import docx

def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)
        # else:
        #     yield child


def doc_content_list(doc):
    list = []
    for block in iter_block_items(doc):
        list.append(block)
    return list


def check_table_style1(table):
    return format_cell_text(table.cell(0, 0).text) == "乡镇(街道)" and \
           format_cell_text(table.cell(0, 1).text).endswith("业")

def check_table_style2(index, block, content_list):
    table_name = content_list[index - 3].text
    return "乡镇监管机构负责人信息表" in table_name

def check_table_style3(index, block, content_list):
    table_name = content_list[index - 3].text
    return "安全工作负责人信息表" in table_name

# support multiple Industry
class Industry:

    def __init__(self, start_index=0, end_index=0, name=None, keys=None):
        self.start_index = start_index
        self.end_index = end_index
        self.name = name
        self.keys = keys


def format_cell_text(text):
    return re.sub(r'\s|\(\d+\)|\n', '', text)


def parse_industry(table):
    pre_category_temp = None
    start_temp = 1
    key_temp = []
    category_list = []

    for index, cell in enumerate(table.rows[0].cells):
        if index == 0:
            continue

        if pre_category_temp is not None and pre_category_temp != format_cell_text(cell.text):
            category_list.append(Industry(start_temp, index - 1, pre_category_temp, key_temp))
            start_temp = index
            key_temp = [format_cell_text(table.rows[1].cells[index].text)]
        else:
            next_key = format_cell_text(table.rows[1].cells[index].text)
            if len(key_temp)> 0 and next_key == key_temp[len(key_temp)-1]:
                next_key = next_key+"-1"
            key_temp.append(next_key)

        if index == len(table.rows[0].cells) - 1:
            category_list.append(Industry(start_temp, index, format_cell_text(cell.text), key_temp))

        pre_category_temp = format_cell_text(cell.text)

    return category_list


def parse_table_data(industry_list, table, city_and_area, word_file_name):
    data_list = []
    # data like: file_name, city_and_area, 乡镇 (街 道), industry, [industry keys]
    for index, row in enumerate(table.rows):
        if index < 2:
            continue
        cells = row.cells
        for industry in industry_list:
            data = {"file_name": word_file_name,
                    "city_and_area": city_and_area,
                    "town": format_cell_text(cells[0].text),
                    "industry": industry.name
                    }
            for i in range(industry.start_index, industry.end_index+1):
                industry_key = industry.keys[i - industry.start_index]
                display_key = re.sub(r'[\s]+', '', industry_key)
                if "主导产业和重点治理品种" == display_key:
                    display_key = "main_product"
                elif "主导产业和重点治理品种-1" in display_key:
                    display_key = "product"
                elif "面积" in display_key:
                    display_key = "area"
                elif "年均总产" in display_key:
                    display_key = "productivity"
                elif "主要风险点" in display_key:
                    display_key = "risk_points"
                data[display_key] = cells[i].text
            data_list.append(data)
        # for index, cell in enumerate(row.cells):
    return data_list


def parse_table(table, city_and_area, word_file_name):
    industrys = parse_industry(table)
    return parse_table_data(industrys, table, city_and_area, word_file_name)


def parse_table_data2(industry_list, table, city_and_area, word_file_name):
    data_list = []
    # data like: file_name, city_and_area, 乡镇 (街 道), industry, [industry keys]
    for index, row in enumerate(table.rows):
        if index < 2:
            continue
        cells = row.cells
        for industry in industry_list:
            data = {"file_name": word_file_name,
                    "city_and_area": city_and_area,
                    "town": format_cell_text(cells[0].text)
                    }

            type_name = re.sub(r'[\s]+', '', industry.name)
            name_key = None
            tel_key = None
            owner_dic = {}
            if type_name == "农业分管负责人":
                type_name = "agriculture_owner"
                name_key = "agriculture_owner_name"
                tel_key = "agriculture_owner_tel"
                owner_dic[name_key] = cells[1].text
                owner_dic[tel_key] = cells[2].text
            elif type_name == "水产业分管负责人":
                type_name = "aquatic_owner"
                name_key = "aquatic_owner_name"
                tel_key = "aquatic_owner_tel"
                owner_dic[name_key] = cells[3].text
                owner_dic[tel_key] = cells[4].text
            elif type_name == "监管机构(种植业)负责人":
                type_name = "agriculture_mechanism"
                name_key = "agriculture_mechanism_name"
                tel_key = "agriculture_mechanism_tel"
                owner_dic[name_key] = cells[5].text
                owner_dic[tel_key] = cells[6].text
            elif type_name == "监管机构(水产业)负责人":
                type_name = "aquatic_mechanism"
                name_key = "aquatic_mechanism_name"
                tel_key = "aquatic_mechanism_tel"
                owner_dic[name_key] = cells[7].text
                owner_dic[tel_key] = cells[8].text

            data[type_name] = owner_dic
            data_list.append(data)
        # for index, cell in enumerate(row.cells):
    return data_list

def parse_table2(table, city_and_area, word_file_name):
    industrys = parse_industry(table)
    return parse_table_data2(industrys, table, city_and_area, word_file_name)


def parse_table_data3(industry_list, table, city_and_area, word_file_name):
    data_list = []
    # data like: file_name, city_and_area, 乡镇 (街 道), industry, [industry keys]
    for index, row in enumerate(table.rows):
        if index < 2:
            continue
        cells = row.cells
        for industry in industry_list:
            data = {"file_name": word_file_name,
                    "city_and_area": city_and_area,
                    "company": format_cell_text(cells[0].text)
                    }

            type_name = re.sub(r'[\s]+', '', industry.name)
            name_key = None
            tel_key = None
            owner_dic = {}
            if type_name == "分管负责人":
                type_name = "admin"
                name_key = "admin_name"
                title_key = "admin_title"
                tel_key = "admin_tel"
                mobile_key = "admin_mobile"
                owner_dic[name_key] = cells[1].text
                owner_dic[title_key] = cells[2].text
                owner_dic[tel_key] = cells[3].text
                owner_dic[mobile_key] = cells[4].text
            elif type_name == "具体工作负责人":
                type_name = "staff"
                name_key = "staff_name"
                title_key = "staff_title"
                tel_key = "staff_tel"
                mobile_key = "staff_mobile"
                owner_dic[name_key] = cells[5].text
                owner_dic[title_key] = cells[6].text
                owner_dic[tel_key] = cells[7].text
                owner_dic[mobile_key] = cells[8].text
            data[type_name] = owner_dic
            data_list.append(data)
        # for index, cell in enumerate(row.cells):
    return data_list

def parse_table3(table, city_and_area, word_file_name):
    industrys = parse_industry(table)
    return parse_table_data3(industrys, table, city_and_area, word_file_name)


# def listToJson(lst):
#     import json
#     import numpy as np
#     keys = [str(x) for x in np.arange(len(lst))]
#     list_json = dict(zip(keys, lst))
#     str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
#     return list_json

def write_list_to_json(data, json_path):
    jsonArr = json.dumps(data, ensure_ascii=False)
    if os.path.exists(json_path):
        os.remove(json_path)

    result_f = open(json_path, mode = 'w', encoding= 'utf-8')
    # result_str = json.dumps(dic)
    # result_str = result_str.encode('utf-8').decode('unicode_escape')

    result_f.write(jsonArr)

    result_f.close()


def do_one_file(file_path):
    try:
        print('123321')
        # file = "乡镇分配试剂-泰安.docx"
        file_name = os.path.basename(file_path).split('.')[0]
        if file_name.startswith("~$"):
            return
        print("do file" + file_path)
        path_dir = os.path.dirname(file_path) + "/"
        doc = docx.Document(file_path)
        content_list = doc_content_list(doc)
        data_list1 = []
        data_list2 = []
        data_list3 = []
        for index, block in enumerate(content_list):
            if "Table" in block.style.name:
                if check_table_style1(block):
                    city_and_area = format_cell_text(content_list[index - 2].text)
                    datalist = parse_table(block, city_and_area,file_name)
                    data_list1.extend(datalist)
                elif check_table_style2(index, block, content_list):
                    city_and_area = format_cell_text(content_list[index - 2].text)
                    datalist = parse_table2(block, city_and_area, file_name)
                    data_list2.extend(datalist)
                elif check_table_style3(index, block, content_list):
                    city_and_area = format_cell_text(content_list[index - 2].text)
                    datalist = parse_table3(block, city_and_area, file_name)
                    data_list3.extend(datalist)

        write_list_to_json(data_list1, path_dir + file_name + "_1.json")
        write_list_to_json(data_list2, path_dir + file_name + "_2.json")
        write_list_to_json(data_list3, path_dir + file_name + "_3.json")
    except Exception as e:
        print('!!!!')
        print(e)


def go(url):
    from os import path

    print("start...")
    file = os.listdir(url)
    for f in file:
        file_path = path.join ("./local/trash/docxs/" , f)
        if file_path.endswith(".docx"):
            do_one_file(file_path)

    print("finish...")

    return url

