# Django练手测试练手项目

## 开始

Django是Python程序员的福利，python程序员编写Django代码就如同福利的制作。——海明斯基 威尔

## 结构设计草稿

https://www.figma.com/file/Qg7812JrvDEAJmoYTnic0J/fulimake%E6%B5%8B%E8%AF%95?type=whiteboard&node-id=0-1&t=IDBbDpmvCY8QbbNe-0

## 记录目前的开发体验困惑

- objects.filter   .all这个点儿之后是一点提示都没有

- 创建一条模型数据的时候，参数字段也没有提示，属性名写错了就会报错

- except UnionExamCourseScore.DoesNotExist  这个代码在写的时候也抱错

```python
except UnionExamCourseScore.DoesNotExist:
    return JsonResponse({
        'status': False,
        'text': '学生不存在',
        'data': {}
    }, status=404)  #.DoesNotExit属性会抱错
```
