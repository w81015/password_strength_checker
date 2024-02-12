import re

def check_password(password):
    # 五個檢查的條件，存成布林值
    min_length = 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', password))
    
    error = ['低強度：']  # 一個空清單儲存錯誤的訊息。因為錯誤就會回傳「低強度」，所以先在清單中放入。

    # 依序檢查每個條件，有錯誤就先錯誤訊息加到error清單中。
    if len(password) < int(min_length):
        error.append('密碼的最小長度應為 8 個字符。')
    if has_uppercase == False:
        error.append('密碼應包含至少一個大寫字母（`A-Z`）。')
    if has_lowercase == False:
        error.append('密碼應包含至少一個小寫字母（`a-z`）。')
    if has_digit == False:
        error.append('密碼應包含至少一個數字（`0-9`）。')
    if has_special_char == False:
        error.append('密碼應包含至少一個特殊字符（`!@#$%^&*()_+{}\[\]:;<>,.?~\\/-`）。')
    if True:  # 檢查是否有連續字符，因為一定要檢查，用if True進入檢查程序
        check_list = []  # 空清單儲存檢查結果
        for i in range(len(password)):  # 以password的長度，產出一個數列
            if i+1 >= len(password):  # 最後一個字符不用檢查，確認是最後一字後，跳出迴圈
                break
            elif ord(password[i]) == ord(password[i+1]):  # 檢查第一個字符是否和第二個字符的編碼相同
                check_list.append(False)
            elif ord(password[i]) + 1 ==  ord(password[i+1]): # 檢查第一個字符是否和第二個字符的編碼相鄰
                check_list.append(False)
            elif ord(password[i]) - 1 == ord(password[i+1]): # 檢查第一個字符是否和第二個字符的編碼相同鄰
                check_list.append(False)
            else:  # 如果上述檢查都通過，代表這兩個字符沒有連續
                check_list.append(True)
        if False in check_list:  # 檢查完每一個字符後，只要有一個沒有符合，就代表有錯誤
            error.append('密碼不應包含連續字符。')
    if len(error) <= 1:
        return '高強度：密碼滿足所有條件。'
    else:
        return ''.join(error) + f'不符合條件的數量：{len(error)-1}'


password = input('請輸入密碼：')  # 要檢查的密碼，使用者自行輸入
# password = 'abckauKAti'  # 要檢查的密碼，範例密碼
strength = check_password(password)
print(strength)


