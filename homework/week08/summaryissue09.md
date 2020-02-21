时间过得好快，转眼间三个月的算法训练营就要结束了，通过这三个月的学习，我感觉个人的编程内功加深了，第一次做LeetCode的两数之和的题目就被虐的好惨，连两层嵌套for循环解题的代码都写不出来，曾经以为只要努力了就会有收获，但是没有方向的努力都是低效的和无效的。   
自从和覃超老师一起学习算法之后，才知道了想要解决leetcode上面的题目是需要方法的，五毒神掌、不要死磕、和优秀的题解提高代码质量，这些都让我受益良多，相当于给迷茫假努力的自己找到了一条出路，起初坚持五毒也并没有明显感觉，但是有一次解决业务问题，因长期刷题的积累虽然还是默写不下来，但是确让我有了解决的思路，参考前中后序遍历那三道leetcode题目，我写出了一维父子关系数组生成树型结构的代码，突然感觉好有成就感   

### 工作中解决实际问题示例
__背景：__ 某项目页面上需要提供 N 叉树的数据    
+ 已实现的javascript版本       
```javascript
let deptInfo = [
    {deptname: '一级部门-1', deptlevel: 0, parentid: 0, deptid: 1},
    {deptname: '二级部门-1', deptlevel: 1, parentid: 1, deptid: 2},
    {deptname: '二级部门-2', deptlevel: 1, parentid: 1, deptid: 3},
];
const changeArrayToTree = (root, sources,childrenKey, idKey, parentKey) => {
    const helper = (tree, childrenKey, idKey, parentKey, sources) => {
        if (!tree) {
            return tree;
        }
        tree[childrenKey] = sources.filter(sc=> sc[parentKey] === tree[idKey]) || [];
        for (let child of tree[childrenKey]) {
            helper(child, childrenKey, idKey, parentKey, sources);
        }
        return tree;
    };
    return helper(root, childrenKey, idKey, parentKey, sources);
};


let tree = changeArrayToTree(deptInfo[0], deptInfo, 'children', 'deptid', 'parentid');

console.log(JSON.stringify(tree, null, 4));
```
+ 仿照js版本实现的python版本       
```python
# -*- coding: utf-8 -*-#
import json

import itertools

def helper(tree, children, idname, pidname, sources):
    """
    将存在父子关系的一维数组 list[dict] 转成树状
    :param tree: 树状数据的根节点                                       :type tree: dict
    :param children: 存放当前节点的子节点list                            :type children: list
    :param idname: 一维数组中每个节点唯一标识，例如：'id'                   :type idname: str
    :param pidname: 一维数组中每个节点的父节点唯一标识，例如：'parentid'      :type pidname: str
    :param sources: 一维数组源数据
    :return: dict
    """
    if isinstance(sources, list) and len(sources) > 0 and tree and tree.get('mold', '') != 'pers':
        children = list(itertools.ifilter(lambda d: d[pidname] == tree[idname], sources))
        if len(children) > 0:
            for child in children:
                helper(child, [], idname, pidname, sources)
    tree['children'] = children if isinstance(children, list) else []
    return tree

if __name__ == '__main__':
    tests = [
        {'projectid': '1', 'parentid': '0', 'projectname': '测试父级项目节点-1'},
        {'projectid': '2', 'parentid': '1', 'projectname': '测试【A】级项目节点-1-1'},
        {'projectid': '3', 'parentid': '1', 'projectname': '测试【B】级项目节点-1-1'},
        {'projectid': '4', 'parentid': '2', 'projectname': '测试子级项目节点-A-1'},
        {'projectid': '5', 'parentid': '2', 'projectname': '测试子级项目节点-A-2'},
        {'projectid': '6', 'parentid': '3', 'projectname': '测试子级项目节点-B-1'},
        {'projectid': '7', 'parentid': '3', 'projectname': '测试子级项目节点-B-2'},
    ]
    with open('F:\\mytest\\test.json', 'w') as jsonfile:
        json.dump(helper(tests[0], [], 'projectid', 'parentid', tests), jsonfile, ensure_ascii=False)
```
__python 示例代码执行结果__      
```json
{
	"projectid": "1",
	"children": [{
		"projectid": "2",
		"children": [{
			"projectid": "4",
			"children": [],
			"projectname": "测试子级项目节点-A-1",
			"parentid": "2"
		}, {
			"projectid": "5",
			"children": [],
			"projectname": "测试子级项目节点-A-2",
			"parentid": "2"
		}],
		"projectname": "测试【A】级项目节点-1-1",
		"parentid": "1"
	}, {
		"projectid": "3",
		"children": [{
			"projectid": "6",
			"children": [],
			"projectname": "测试子级项目节点-B-1",
			"parentid": "3"
		}, {
			"projectid": "7",
			"children": [],
			"projectname": "测试子级项目节点-B-2",
			"parentid": "3"
		}],
		"projectname": "测试【B】级项目节点-1-1",
		"parentid": "1"
	}],
	"projectname": "测试父级项目节点-1",
	"parentid": "0"
}
```

### 总结  
通过三个月的刻意训练，按照老师传授的五毒神掌和寻找最近重复子问题等方法，在不断刷题积累中，个人编程能力得到了很大的提高，面对各种复杂的业务问题也可以有了一些思路，能更好的设计数据结构和写出简洁高效的代码，总之三个月的算法训练营都是干货很值得购买。