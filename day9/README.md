# Day 9｜taibun 台語文字處理功能測試

這個資料夾放的是 Day 9 文章中，針對 Python 台語文字處理套件 `taibun` 進行的幾個基本功能測試。

本次主要測試：

- 台語漢字轉臺羅
- 自動連讀變調（sandhi）
- 台語漢字轉臺語方音符號
- 不同腔調（dialect）設定

## 包含的測試程式

### 1. `tailo.py`

將台語漢字轉換成臺羅。

程式使用：

```python
Converter(system='Tailo')
```

以「癩哥蛾仔」作為輸入範例，觀察 `taibun` 的臺羅轉換結果。



### 2. `tailoSandhi.py`

測試 `taibun` 的自動連讀變調功能。

程式使用：

```python
Converter(system='Tailo', sandhi='auto')
```

本次使用「癩哥蛾仔」測試自動變調結果。


### 3. `zhuyin.py`

將台語漢字轉換成臺語方音符號。

程式使用：

```python
Converter(system='Zhuyin')
```

---

### 4. `dialect.py`

測試 `taibun` 的不同腔調設定。

程式可以透過：

```python
dialect='south'
```

指定偏漳州腔的設定。

`taibun` 目前也提供其他 dialect 選項，如 `north`、`singapore`。

## 安裝

請先安裝 `taibun`：

```bash
pip install taibun
```

## 執行方式

四支程式都可以直接透過 Python 執行：

```bash
python tailo.py
python tailoSandhi.py
python zhuyin.py
python dialect.py
```

