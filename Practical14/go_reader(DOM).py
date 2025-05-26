import xml.dom.minidom
import datetime

# 记录开始时间
start_time = datetime.datetime.now()

# 加载并解析 XML 文件
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement

# 获取所有 'term' 元素
terms = collection.getElementsByTagName("term")

# 用于存储每个命名空间的最大 is_a 数量和对应的 term id
max_is_a = {
    "molecular_function": {"id": [], "count": 0},
    "biological_process": {"id": [], "count": 0},
    "cellular_component": {"id": [], "count": 0},
}

def output(list):
    s = ''
    for i in list:
        s = s + i + ', '
    s = s[:-2]
    print(s)

# 遍历每个 term
for term in terms:
    # 获取 namespace
    namespace_node = term.getElementsByTagName("namespace")[0]
    namespace = namespace_node.firstChild.nodeValue

    # 检查是否是我们关心的命名空间之一
    if namespace in max_is_a:
        # 获取所有的 is_a 元素
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)

        # 获取 term id
        id_node = term.getElementsByTagName("id")[0]
        term_id = id_node.firstChild.nodeValue

        # 检查是否需要更新最大 is_a 计数
        if is_a_count > max_is_a[namespace]["count"]:
            max_is_a[namespace]["id"] = [term_id]
            max_is_a[namespace]["count"] = is_a_count
        elif is_a_count == max_is_a[namespace]["count"]:
            max_is_a[namespace]["id"].append(term_id)

# 记录结束时间
end_time = datetime.datetime.now()
dom_duration = end_time - start_time

# 打印结果
print("DOM API Results:")
for namespace in max_is_a:
    term_data = max_is_a[namespace]
    print(f"Namespace: {namespace}")
    print(f"Term ID with most is_a elements:",end='' )
    output(max_is_a[namespace]["id"])
    print(f"Number of is_a elements: {term_data['count']}\n")

print(f"DOM API Execution Time: {dom_duration}")