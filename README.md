# 書本文本分析器
這個專案是一個簡單的書本文本分析器，由 Python 實現。它會讀取書本文本，計算單字數量，並分析書本中每個字母的出現頻率。以下是主要功能的摘要：

## 功能
- **單字計算**：計算書本中的總單字數量。
- **字母頻率分析**：確定每個字符在書本文本中出現的次數，忽略非字母字符，並將大寫和小寫字母視為相同字符。

## 工作原理
- **讀取書本**：get_book_text 函數從指定的文件路徑讀取書本文本。
- **單字計算**：get_num_words 函數將文本拆分為單字並計算它們的數量。
- **字母計算**：get_chars_dict 函數創建一個字典，以字母為鍵，以它們的出現次數為值。
- **字符排序**：chars_dict_to_sorted_list 函數按字符的頻率降序排序。
- **生成報告**：main 函數統籌整個過程，生成報告並印出結果。

## 使用方法
要運行分析器，執行 main() 函數。書本文本應放在 books 目錄中，並更改 main() 函數的 book_path 為當前的書本路徑。比如：文件名為 frankenstein.txt，book_path 應為 'books/frankenstein.txt'。腳本將印出一份報告，顯示總單字數量和每個字母的出現頻率。
1. **準備書本文本**
- 將書本文本文件放在 books 目錄中。
- 假設文件名為 frankenstein.txt。

2. **修改程式碼**
- 更改 main() 函數中的 book_path 為當前的書本文本路徑。
- 例如，設置 book_path 為 'books/frankenstein.txt'。

3. **運行分析器**
- 執行 main() 函數。

4. **查看報告**
- 腳本將印出一份報告，顯示單字總數量和每個字母的出現頻率。

## 範例輸出
```
--- Begin report of books/frankenstein.txt ---
7185 words found in the document

The e character was found 1045 times
The t character was found 850 times
...
--- End report ---

````
