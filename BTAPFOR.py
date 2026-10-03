"""
01. Nhập vào một số nguyên dương N với N ∈ [10000, 99999]. Hãy cho biết trong số N vừa nhập có bao nhiêu chữ
số chẵn, bao nhiêu chữ số lẻ?
"""
import math
from idlelib.debugger_r import restart_subprocess_debugger


def bai_1():
    cntc = 0
    cntl = 0
    n = -1
    while True:
        nhap = input("Nhap(10000, 99999): ")
        if nhap.isdigit() and 10000 <= int(nhap) <= 99999:
            n = nhap
            break
        else:
            print("Vui lòng nhap lại: ")
    for i in n:
        i = int(i)
        if i % 2 == 0:
            cntc +=1
        else:
            cntl +=1
    print(cntc, cntl)


"""
02. Viết chương trình kiểm tra một số nguyên có phải SỐ CHÍNH PHƯƠNG không? Nếu không phải xuất SỐ CHÍNH
PHƯƠNG gần nó nhất.
"""

def bai_2():
    nhap = int(input("Nhap so can kiem tra: "))
    for i in range(nhap + 1):
        tmp = i * i
        if tmp == nhap:
            print("Đây là số chinh phương")
            break
    else:
        for i in range(nhap+1):
            a = i * i
            b = (i+1) * (i+1)
            if a < nhap <b:
                if nhap - a < b - nhap:
                    print(f"Số chính phương gần nhất là {a}")
                else:
                    print(f"Số chính phương gần nhất là {b}")
                    break

"""
03. Nhập vào số dương, nếu nhập sai nhập lại cho đến khi đúng, nếu nhập đúng thì
xuất số đã nhập.
"""
def bai_3():
    while True:
        n = int(input("Nhap: "))
        if n > 0:
            print(n)
            break
        else:
            print("VUi long nhap lai")

""""
04. Nhập điểm lý thuyết, thực hành; kiểm tra riêng từng điểm phải trong khoảng từ [0 .. 10],
nếu không đúng phải nhập lại cho đến khi nào hợp lệ thì xuất điểm trung bình cộng.
"""
def bai_4():
    while True:
        a, b = map(int, input("Nhap: ").split())
        if 0 <= a <= 10 and 0 <= b <= 10:
            dtb = (a+b)/2
            print(dtb)
            break
        else:
            print("Vui long nhap lai")

def bai_5():
    n = int(input("Nhap: "))
    for i in range(1, n+1):
        print(i, end=" ")

""""
06. Nhập vào tháng trong năm, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 12) nếu sai yêu cầu nhập lại cho đúng. Khi
đã nhập đúng thì xuất ra mùa của tháng đã nhập
"""
def bai_6():
    while True:
        thang = int(input("Nhap thang trong nam: "))
        if 1<= thang <= 12:
            if 1<= thang <=3:
                print("Mua xuan")
            elif 4<= thang <=6:
                print("Mua ha")
            elif 7<= thang <=9:
                print("Mua thu")
            else:
                print("Mua dong")

""""
07. Nhập vào thứ trong tuần, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 7) nếu sai yêu cầu nhập lại cho đúng. Khi đã
nhập đúng thì xuất ra tên của thứ trong tuần là tiếng anh.
"""
def bai_7():
    days = {1: "Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday",5:"Thursday", 6:"Friday", 7:"Saturday"}
    while True:
        n = int(input("Nhap thu trong tuan(1-7): "))
        if 1 <= n <= 7:
            print(days[n])
            break
        else:
            print("Thu khong hop le")

def bai_8():
    while True:
        a = int(input("Nhap: "))

""""
09. Nhập vào 2 số nguyên khác 0 là tử và mẫu của một phân số, xuất ra giá trị thập phân của phân số, ví dụ nhập tử
là 5, nhập mẫu là 8 thì xuất ra giá trị phân số dạng thập phân là 0.625, và cho nhập tiếp hai số khác để tính. Chương
trình ngừng khi một trong hai số nhập vào là số 0.
"""
def bai_9():
    while True:
        tu, mau = map(int, input("Nhap tu va mau so(0 de thoat): ").split())
        if tu == 0 or mau == 0:
            break
        else:
            ans = tu/mau
            print(f"{ans:.3f}")
            break


""""
10. Nhập vào một số nguyên dương, kiểm tra nếu nhập không đúng phải nhập lại cho đúng. Tính tổng các chữ số
trong số nguyên và xuất kết quả. (Ví dụ nhập 307 thì xuất tổng là 10)
"""
def bai_10():
    ans = 0
    while True:
        n = input("Nhap so nguyen duong: ")
        if not n.isdigit() or int(n) < 0:
            print("Gia tri khong hop le")
            continue
        else:
            tmp = str(n)
            for i in tmp:
                i = int(i)
                ans += i
            break
    print(ans)

""""
11. Nhập vào lần lượt các số và tính tổng các số dương, nếu nhập vào số 0 thì kết thúc việc nhập số. Xuất ra tổng các
số dương. Ví dụ: nhập 3 8 -2 7 -5 1 0, dừng và xuất ra 19)
"""
def bai_11():
    n = -1
    ans= 0
    while n != 0:
        n = int(input("Nhap n: "))
        if n > 0:
            ans += n
        else:
            continue
    print(ans)

"""
12. Nhập vào các số nguyên hoặc nhập 0 để kết thúc. Đếm số lượng các số âm có trong dãy số vừa nhập.
Ví dụ: nhập 3 8 -2 7 -5 1 0, dừng và xuất ra “Co 2 so am”
"""
def bai_12():
    n = -1
    cnt = 0
    while n != 0:
        n = int(input("Nhap n: "))
        if n < 0:
            cnt += 1
        else:
            continue
    print(f"Co {cnt} so am")

"""
13. Nhập vào một số nguyên dương. Đếm xem có bao nhiêu ký số 7 trong số vừa nhập.
Ví dụ: nhập 37577 0, xuất ra “Co 3 so 7”
"""
def bai_13():
    n = input("Nhap so nguyen: ")
    cnt = 0
    for i in n:
        if i == '7':
            cnt += 1
        else:
            continue
    print(f"Co {cnt} so 7")

"""
16. Sử dụng vòng lặp while tính các tổng sau, với n là một số nguyên dương nhập bởi người dùng:
"""
def bai_16():
    ans = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    i1 = 1
    i2 = 1
    i3 = 1
    i4 = 1
    mau1 = 0
    mau2 = 1
    mau3 = 0
    mau4 = 0
    n = int(input("Nhap n: "))
    while(i1<=n):
        mau1 += i1
        ans += 1/mau1
        i1+=1
    while(i2<=n):
        ans2 += 1/(i2 * (i2 + 1))
        i2+=1
    while(i3<=n):
        ans3 += i3/(i3+1)
        i3 += 1
    while(i4<=n):
        ans4 += (2*i4 + 1)/(2*i4 + 2)
        i4 += 1
    print(f"tong 1: {ans:.2f}")
    print(f"tong 2: {ans2:.2f}")
    print(f"tong 3: {ans3:.2f}")
    print(f"tong 4: {ans4:.2f}")

"""
17. Cho người dùng nhập số nguyên dương N. Nếu nhập sai thì cho nhập lại đến khi đúng. Sau đó cho người dùng
nhập N số nguyên và in ra số lẻ lớn nhất trong những số được nhập. Cuối cùng, hỏi người dùng có muốn tiếp tục
không, nếu người dùng nhấn ‘c’ thì tiếp tục, nhấn phím khác thì thoát chương trình.
"""
def bai_17():
    while True:
        while True:
            try:
                n = int(input("Nhap so n: "))
                if n > 0:
                    break
                else:
                    print("Vui long nhap lai")
            except:
                print("Gia tri khong hop le")
        for i in range(1, n+1):
            val = int(input("Nhap so nguyen thu {i}"))
            maxVal = None
            if val % 2 != 0:
                if maxVal is None or val > maxVal:
                    maxVal = val
        if maxVal is not None:
            print(f"Số lẻ lớn nhất là: {maxVal}")
        else:
            print("Không có số le")
        chon = input("bạn có muốn tiếp tục(c de thoat): ")
        if chon.lower() == 'c':
            print("Tam biet")
            break

"""
18. In ra tất cả ước số của một số nguyên N nhập bởi người dùng.
"""
def bai_18():
    n = int(input("Nhap n: "))
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end=" ")
            print(-i, end=" ")

"""
21. Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp for tìm phần tử chia hết cho 5 lớn nhất.
"""
def bai_21():
    n = input("Nhap list danh sach(cach nhau boi dau cach): ")
    numbers = [int(x) for x in n.split()]
    max_val = None
    for x in numbers:
        if x%5 == 0:
            if max_val is None or x > max_val:
                max_val = x
    if max_val is not None:
        print(f"So chia het cho 5 lon nhat la {max_val}")
    else:
        print("Khong co so chia het cho 5")

"""
22. Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp for xóa các phần tử lớn hơn A trong list, với A
là một số thực nhập bởi người dùng.
Gợi ý: Có thể tạo list mới chứa phần tử không bị xóa. Nếu muốn xóa bằng lệnh del thì cần dùng vòng lặp while.
"""

def bai_22():
    ans = []
    a = float(input("Nhap so thuc A: "))
    numbers = input("Nhap list so: ")
    tmp = [float(x) for x in numbers.split()]
    for i in tmp:
        if i < a:
            ans.append(i)
    print(*ans)

"""
23. Tạo một list có độ dài tùy ý chứa các phần tử đã sắp tăng dần. Dùng vòng lặp for chèn một số B vào list sao cho
list vẫn tăng dần, với B là một số thực nhập bởi người dùng.
Gợi ý: dùng vòng lặp tìm ra vị trí (index) thích hợp cần chèn, sau đó dùng hàm insert() để chèn B vào list. Có thể tìm
hiểu từ khóa break trong vòng lặp để sử dụng.
"""
def bai_23():
    b = float(input("Nhap b: "))
    numbers = input("Nhap list so (da sap xep tang dan): ")
    tmp = [float(x) for x in numbers.split()]
    inserted = False
    for i in range(len(tmp)):
        if b <= tmp[i]:
            tmp.insert(i, b)
            inserted = True
            break
    if not inserted:
        tmp.append(b)
    for ans in tmp:
        print(ans, end=" ")

"""
24. Tìm N số nguyên tố đầu tiên và lưu vào 1 list. N là một số nguyên dương nhập bởi người dùng.
Yêu cầu: dùng vòng lặp for kết hợp với vòng lặp while.
"""
def bai_24():
    n = int(input("Nhap n: "))
    list = []
    num = 2
    while len(list) < n:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            list.append(num)
        num += 1
    print(f"{n} so nguyen to dau tien la: ")
    print(*list)


"""
25. Viết chương trình tính căn bậc hai của một số x. Sử dụng phương pháp Newton để tính toán và hiển thị căn bậc
hai của một số x được nhập bởi người dùng. Thuật toán Newton như sau:
Đọc số x từ bàn phím
Khởi tạo guess bằng x/2
While guess không thỏa điều kiện do
Cập nhật giá trị guess bằng với trung bình của guess và x/guess.
Khi thuật toán chạy hoàn chỉnh thì guess chứa một giá trị xấp xỉ với căn bậc hai của x, giá trị của phép xấp xỉ sẽ phụ
thuộc vào điều kiện thỏa mãn mà người dùng đặt. Trong bài tập này thì guess được xem là thỏa mãn khi giá trị tuyệt
đối của guess*guess so với x nhỏ hơn hoặc bằng 10-12.
"""


def bai_25():
    x = float(input("Nhập số x: "))
    if x < 0:
        print("Không thể tính căn bậc hai của số âm.")
        return
    elif x == 0:
        print("Căn bậc hai của 0 là: 0.0")
        return
    guess = x / 2.0
    epsilon = 1e-12
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    print(f"Căn bậc hai xấp xỉ của {x} là: {guess:.12f}")

"""
26. Viết chương trình thực hiện chuyển đổi một số nhị phân (binary) sang hệ thập phân (decimal). Chương trình sẽ
đọc một chuỗi các số nhị phân. Sau đó, chương trình sẽ tính toán một số hệ thập phân tương đương. Cuối cùng,
chương trình sẽ hiển thị số thập phân tương ứng lên màn hình
"""
def bai_26():
    binary_str = input("Nhập chuỗi số nhị phân: ").strip()
    decimal_val = 0
    power = 0
    for digit in reversed(binary_str):
        if digit not in ('0', '1'):
            print("Lỗi: Chuỗi nhập vào không phải số nhị phân hợp lệ!")
            return
        decimal_val += int(digit) * (2 ** power)
        power += 1

    print(f"Số thập phân tương ứng là: {decimal_val}")

def bai_14():
    first_x_str = input("Enter the first x-coordinate: ")
    first_y_str = input("Enter the first y-coordinate: ")
    first_x = float(first_x_str)
    first_y = float(first_y_str)
    prev_x = first_x
    prev_y = first_y
    perimeter = 0.0
    while True:
        line_x = input("Enter the next x-coordinate (blank to quit): ")
        if line_x.strip() == "":
            break
        line_y = input("Enter the next y-coordinate: ")
        curr_x = float(line_x)
        curr_y = float(line_y)
        distance = math.sqrt((curr_x - prev_x) ** 2 + (curr_y - prev_y) ** 2)
        perimeter += distance
        prev_x = curr_x
        prev_y = curr_y
    perimeter += math.sqrt((prev_x - first_x) ** 2 + (prev_y - first_y) ** 2)
    print(f"The perimeter of that polygon is {perimeter}")


def bai_15():
    while True:
        line = input("Nhập chuỗi 8 bit nhị phân (nhấn Enter hoặc khoảng trắng để dừng): ")
        if line.strip() == "":
            print("Đã dừng chương trình.")
            break
        if len(line) > 8:
            print("CẢNH BÁO: Chuỗi nhập vào có nhiều hơn 8 bit! Vui lòng nhập lại.")
            continue
        if len(line) < 8:
            print("Lỗi: Chuỗi phải có đúng 8 bit. Vui lòng nhập lại.")
            continue
        if not all(c in '01' for c in line):
            print("Lỗi: Chuỗi chỉ được chứa các ký tự 0 và 1.")
            continue
        count_ones = line.count('1')
        if count_ones % 2 == 1:
            parity_bit = '1'
        else:
            parity_bit = '0'
        print(f"-> Chế độ: Parity chẵn | Bit parity cần thêm: {parity_bit} (Chuỗi đầy đủ: {line}{parity_bit})")

def bai_16():
    q = int(input("Nhap q: "))
    res = ""
    if q < 0:
        print("Nhap so nguyen lon hon > 0: ")
        return
    while True:
        r = q % 2
        res = str(r) + res
        q //= 2
        if q == 0:
            break
    print(res)
bai_16()






