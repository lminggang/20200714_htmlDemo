from lxml import etree


# 1. 获取 html 结构文本
html = '''
		<!DOCTYPE html>
		<html>
		<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>百度离线版DEMO</title>
		<script type="text/javascript" src="apiv3.0.min.js"></script>
		<meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'>
		</head>
		<body>
		<style>
		html,body{
		  margin:0;
		  padding:0
		}

		</style>
		<!--can u get me, bitch?-->
		<div style="width:100%;height:100%;position:absolute;" id="container">
			哈哈哈哈哈
		</div>

		</body>
		</html>
	'''

# 2. 将 html 转换成 etree 对象
dom = etree.HTML(html)

# 3. 解析 html
# 获取所有内容
all_text = dom.xpath('//text()')
# 获取所有注释
all_comment = dom.xpath('//comment()')
print(all_text)
print(all_comment)