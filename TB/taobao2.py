import  re



def main():
    with open("g_page_config.txt","r",encoding="utf-8") as file1:
       g_page_config = re.search(r"g_page_config = (.*?);\n",file1.read())
       with open("g_page_config.txt", "w", encoding="utf-8") as file2:
        file2.write(g_page_config.group())
if __name__ =="__main__":
    main()