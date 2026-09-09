# Taiwanese ASR Lab

歡迎來到 **Taiwanese ASR Lab**！

這個專案紀錄我參加 **2026 iThome 鐵人賽**期間的相關程式碼與技術筆記。

## 專案簡介

「為什麼英文有成熟的發音檢測工具，臺語卻沒有？」

本專案源自於我的大學畢專，以及一路踩坑後產生的技術問題。

在主流語言 AI 蓬勃發展的今天，臺語語音技術仍充滿挑戰。本系列文章與程式碼將探索臺語自動語音辨識（ASR）的技術細節，並逐步朝「臺語發音檢測」的目標邁進。

在這個專案中，不只會探討現有的臺語語音模型，也會深入挖掘以下主題：

- **模型內部觀察**：剖析模型推論過程中的 Hidden States、Logits 與 Frame-level 資訊，為後續的發音檢測探索可能的方法。

- **資料整理實戰**：從臺語字典、臺羅拼音出發，建構與清理適合模型使用的資料。

- **踩坑實錄與微調經驗**：紀錄模型微調過程中遇到的各種狀況，例如看似完美的 99.34% 準確率背後隱藏的問題。

目前系列文章正在 [Medium](https://medium.com/@yifyu1122) 上先行連載中，未來也會同步發布至 iThome。

## 文章索引

### Day 01: 為什麼英文有發音檢測，台語卻沒有？
* [Medium 連結](https://medium.com/@yifyu1122/day-1-為什麼英文有發音檢測-台語卻沒有-ae6c2ea62e6d)
* iThome 連結 (待釋出)

### Day 02: 台語 AI 到底已經發展到哪裡？從資料、ASR 到模型選擇
* [Medium 連結](https://medium.com/@yifyu1122/day-2-台語-ai-到底已經發展到哪裡-從資料-asr-到模型選擇-ba7685fca5af)
* iThome 連結 (待釋出)

### Day 03: 從字典到模型輸入：台語 ASR 的資料整理實戰
* [Medium 連結](https://medium.com/@yifyu1122/day-3-從字典到模型輸入-台語-asr-的資料整理實戰-b6630d5ca349)
* iThome 連結 (待釋出)

### Day 04: 人生中第一次微調 99.34%？然後我發現事情不太對...
* [Medium 連結](https://medium.com/@yifyu1122/day-4-大學生畢專實錄-人生中第一次微調-99-34-然後我發現事情不太對-59eaa5a625f3)
* iThome 連結 (待釋出)

### Day 05: Colab GPU 額度沒了，還有其他資源嗎？
* [Medium 連結](https://medium.com/@yifyu1122/day-5-%E5%A4%A7%E5%AD%B8%E7%94%9F%E7%95%A2%E5%B0%88%E5%AF%A6%E9%8C%84-colab-gpu-%E9%A1%8D%E5%BA%A6%E6%B2%92%E4%BA%86-%E9%82%84%E6%9C%89%E5%85%B6%E4%BB%96%E8%B3%87%E6%BA%90%E5%97%8E-59d9c774efe7)
* iThome 連結 (待釋出)

### Day 06: 多音節資料到底怎麼建立？
* [Medium 連結](https://medium.com/@yifyu1122/day-6-%E5%A4%A7%E5%AD%B8%E7%94%9F%E7%95%A2%E5%B0%88%E5%AF%A6%E9%8C%84-%E5%A4%9A%E9%9F%B3%E7%AF%80%E8%B3%87%E6%96%99%E5%88%B0%E5%BA%95%E6%80%8E%E9%BA%BC%E5%BB%BA%E7%AB%8B-f0e77c4682b6)
* iThome 連結 (待釋出)

### Day 07: Unicode 危機：[UNK] 是什麼？NFC、NFD 又是什麼？怎麼沒人跟我說模型訓練還要管這些？
* [Medium 連結](https://medium.com/@yifyu1122/day-7-%E5%A4%A7%E5%AD%B8%E7%94%9F%E7%95%A2%E5%B0%88%E5%AF%A6%E9%8C%84-unicode-%E5%8D%B1%E6%A9%9F-unk-%E6%98%AF%E4%BB%80%E9%BA%BC-nfc-nfd-%E5%8F%88%E6%98%AF%E4%BB%80%E9%BA%BC-%E6%80%8E%E9%BA%BC%E6%B2%92%E4%BA%BA%E8%B7%9F%E6%88%91%E8%AA%AA%E6%A8%A1%E5%9E%8B%E8%A8%93%E7%B7%B4%E9%82%84%E8%A6%81%E7%AE%A1%E9%80%99%E4%BA%9B-bff02724677b?postPublishedType=initial6)
* iThome 連結 (待釋出)

### Day 08: 模型訓練場目睹之怪現狀
* [Medium 連結](https://medium.com/@yifyu1122/day-8-%E5%A4%A7%E5%AD%B8%E7%94%9F%E7%95%A2%E5%B0%88%E5%AF%A6%E9%8C%84-%E6%A8%A1%E5%9E%8B%E8%A8%93%E7%B7%B4%E5%A0%B4%E7%9B%AE%E7%9D%B9%E4%B9%8B%E6%80%AA%E7%8F%BE%E7%8B%80-0ce56c1725a2)
* iThome 連結 (待釋出)

---
*更多文章與程式碼實驗將隨賽程持續更新，敬請期待！*
