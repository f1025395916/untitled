import re
import json

def get_space_end(level):
    return '   '* level+ '-'
def get_space_end(level):
    return '    '*level +'-'


def find_keys(targets):
    keys =iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            print(each)
        else:
            print(each)
            find_keys(targets[each])


def main():
    with open("items.txt","r",encoding="utf-8") as file:
        g_page_config = re.search(r'g_page_config = (.*?);\n',file.read())
        # 从字符串当中，获取第一组数据
        page_config_json =   json.loads(g_page_config.group(1))
        find_keys(page_config_json)

if __name__ =="__main__":
    main()