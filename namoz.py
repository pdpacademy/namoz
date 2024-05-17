import requests
def namoz_vaqtlari(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"
    r = requests.get(url).text
    ss = r.split("<script>")
    sanoq, on, rs = 0, 0, ""
    for i in ss[5]:
        if sanoq == 13: break
        if i == "'":
            sanoq += 1
            if on == 0:
                on = 1
                rs += i
            else:
                on = 0
        if on == 1: rs += i
    rs2 = rs.split("''")
    rs2.pop()
    rs2.pop(0)
    return {
    	'bomdod': rs2[1],
    	'peshin': rs2[2],
    	'asr': rs2[3],
    	'shom': rs2[4],
    	'xufton': rs2[5],
    }
