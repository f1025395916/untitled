from lxml import  etree

html = etree.parse("./32.html")

print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)


rst= html.xpath('//book[@category="sport"]')
print(rst)

rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)

# Css 选择器   BeautifulSoup4