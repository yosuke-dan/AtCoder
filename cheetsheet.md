# 文字列操作

## 文字列の中の文字が大文字か小文字かを判定する
```
print("apple".islower())
>> True

print("Hello".islower())
>> False

print("APPLE".isupper())
>> True

print("Hello".isupper())
>> False
```


# List操作

## 各要素の個数（要素ごとの出現回数）をカウント: count()メソッド

```
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

print(l.count('a'))
# 4

print(l.count('b'))
# 1

print(l.count('c'))
# 2

print(l.count('d'))
# 0
```

# Dictionary操作

## setdefault(key, default)

 - 指定したキーに対応する値を取得します。キーが存在しない場合はキーとデフォルト値を辞書に追加します。

```
my_dict = {"name": "John", "age": 25, "city": "Tokyo"}
name = my_dict.setdefault("name", "Unknown")
country = my_dict.setdefault("country", "Japan")
print(name)  # 出力: John
print(country)  # 出力: Japan
print(my_dict)  # 出力: {'name': 'John', 'age': 25, 'city': 'Tokyo', 'country': 'Japan'}
```

## 辞書の値が最大・最小となるキーを取得

```
d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d, key=d.get))
# a

print(min(d, key=d.get))
# b
```