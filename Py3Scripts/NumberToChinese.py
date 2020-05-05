def digital_to_chinese(digital):
    str_digital = str(digital)
    chinese = {
        "1": "壹",
        "2": "贰",
        "3": "叁",
        "4": "肆",
        "5": "伍",
        "6": "陆",
        "7": "柒",
        "8": "捌",
        "9": "玖",
        "0": "零",
    }
    chinese2 = ["拾", "佰", "仟", "万", "厘", "分", "角"]
    jiao = ""
    bs = str_digital.split(".")
    yuan = bs[0]
    if len(bs) > 1:
        jiao = bs[1]
    r_yuan = [i for i in reversed(yuan)]
    count = 0
    for i in range(len(yuan)):
        if i == 0:
            r_yuan[i] += "圆"
            continue
        r_yuan[i] += chinese2[count]
        count += 1
        if count == 4:
            count = 0
            chinese2[3] = "亿"

    s_jiao = [i for i in jiao][:3]  # 去掉小于厘之后的

    j_count = -1
    for i in range(len(s_jiao)):
        s_jiao[i] += chinese2[j_count]
        j_count -= 1
    last = [i for i in reversed(r_yuan)] + s_jiao

    last_str = "".join(last)
    print(str_digital)
    print(last_str)
    for i in range(len(last_str)):
        digital = last_str[i]
        if digital in chinese:
            last_str = last_str.replace(digital, chinese[digital])
    print(last_str)
    return last_str


# number = float(input("输入需要转换的数字："))
number = float(3000)

if __name__ == "__main__":
    digital_to_chinese(number)
