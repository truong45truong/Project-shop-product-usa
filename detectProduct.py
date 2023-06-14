import cv2
import numpy as np

image = cv2.imread('./sg-11134201-22120-w4it0uurvklvbd.jpeg')
image_test = cv2.imread('./sg-11134201-22120-w4it0uurvklvbd.jpeg')
min_x = 0
max_x = 500
min_y = 0
max_y = 500
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)  # Tách các kênh L, a, b

# Áp dụng phép biến đổi vào kênh L
l_equ = cv2.equalizeHist(l)

# Kết hợp lại các kênh L, a, b
lab_equ = cv2.merge((l_equ, a, b))

# Chuyển lại ảnh gốc từ không gian màu LAB sang BGR
result = cv2.cvtColor(lab_equ, cv2.COLOR_LAB2BGR)

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

# Phát hiện cạnh của ./nh
# image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
# blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(image, 30, 150)
# Tìm các đường thẳng trong ảnh
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
point_line = []
distinct_lines = []
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        current_line = [rho, theta]

        # Kiểm tra góc của đường thẳng hiện tại với các đường thẳng đã lưu trữ
        is_distinct = True
        for line in distinct_lines:
            delta_theta = abs(current_line[1] - line[1])
            if delta_theta < 0.15:  # Điều kiện: góc khác nhau dưới 1 độ
                is_distinct = False
                break

        # Nếu đường thẳng hiện tại có góc khác nhau với các đường thẳng đã lưu trữ,
        # thì thêm nó vào danh sách đường thẳng đã lưu trữ
        if is_distinct:
            distinct_lines.append(current_line) 
            point_line.append({
                'x1' : x1,
                'x2' : x2,
                'y1' : y1, 'y2' : x2,
            })
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
         
def group_intersecting_lines(lines):
    groups = [] # Danh sách các nhóm đường thẳng
    point = []
    threshold_rho = 10 # Giảm ngưỡng khoảng cách rho
    threshold_theta = np.pi/180 * 10
    height, width, _ = image.shape
    print("height: ", height)
    print("width :",width)
    # for line in lines:
    rho, theta = lines[0] # Lấy rho và theta của đường thẳng
    # Tìm các nhóm có đường thẳng gần nhất
    found_group = False
    # for group in groups:
    for group_line in lines:
        group_rho, group_theta = group_line # Lấy rho và theta của đường thẳng trong nhóm
        
        a_line_current = -np.cos(theta)/np.sin(theta)
        b_line_current = rho / np.sin(theta)
    
        a_group_line = -np.cos(group_theta) / np.sin(group_theta)   
        b_group_line = group_rho / np.sin(group_theta)
        
        
        try :
            Y_intersection = ( b_group_line - b_line_current) / ( a_line_current - a_group_line )
            X_intersection = ( Y_intersection - b_group_line) / a_group_line
            if( np.abs(X_intersection) <= width and np.abs(Y_intersection) <= height):
                print("interSection = ",(X_intersection,Y_intersection))
                point.append((X_intersection,Y_intersection))
                groups.append(group_line)
        except Exception as e:
            print("Ex",e)
            # Kiểm tra xem điểm giao điểm có nằm trên cả hai đường thẳng hay không
            # if x >= 0 and y >= 0 and y <= height and x <= max(rho, group_rho) and y <= max(rho, group_rho):
            #     found_group = True
            #     group.append(line) # Thêm đường thẳng vào nhóm
            #     point.append((x,y))
            #     print((x,y))
            # else:
            #     found_group = False
    # if not found_group:
    #     groups.append([line]) # Tạo nhóm mới chứa đường th
    return groups,point
group_lines,point_intersection = group_intersecting_lines(distinct_lines)
print(group_lines)
# Hiển thị ảnh với các đường thẳng và điểm giao nhau đã được vẽ lên
line_check = distinct_lines[0]
rho_line_check,theta_line_check = line_check
a_line_check = -np.cos(theta_line_check)/np.sin(theta_line_check)
b_line_check = rho_line_check / np.sin(theta_line_check)
a = np.cos(theta_line_check)
b = np.sin(theta_line_check)
x0 = a * rho_line_check
y0 = b * rho_line_check
x1 = int(x0 + 1024 * (-b))
y1 = int(y0 + 1024 * (a))
x2 = int(x0 - 1024 * (-b))
y2 = int(y0 - 1024 * (a))
img_test = image_test
cv2.line(image_test, (x1, y1), (x2, y2), (160, 100, 100), 2)
for lines in group_lines:
    print(lines)
    # for line in lines:
    rho, theta = lines
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1024 * (-b))
    y1 = int(y0 + 1024 * (a))
    x2 = int(x0 - 1024 * (-b))
    y2 = int(y0 - 1024 * (a))
    current_line = [rho, theta]
    a_line_current = -np.cos(theta)/np.sin(theta)
    b_line_current = rho / np.sin(theta)
    X_point_intersection = (b_line_current - b_line_check) / (a_line_check - a_line_current)
    Y_point_intersection = a_line_current*X_point_intersection + b_line_current
    cv2.circle(img_test, (int(X_point_intersection), int(Y_point_intersection) ), 5, (160, 100, 100), -1)
    cv2.putText(img_test,str((int(X_point_intersection), int(Y_point_intersection))), (int(X_point_intersection), int(Y_point_intersection)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(160, 100, 100), 1, cv2.LINE_AA)
    text_line = "y = {a}x + {b}".format( a = a_line_current , b = b_line_current)
    point_text = (  500, int(a_line_current*500 + b_line_current) )
    cv2.putText(img_test,text_line, point_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5,(251, 192, 65), 1, cv2.LINE_AA)
    cv2.circle(img_test, point_text, 5, (9, 255, 0), -1)
    # cv2.putText(img_test,str(point_text), point_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5,(251, 0, 65), 1, cv2.LINE_AA)
    cv2.line(img_test, (x1, y1), (x2, y2), (0, 0, 255), 2)
for point in range(0,1024):
    if point % 50 == 0:
        color = (0, 25, 0)
        cv2.putText(img_test, str(point), (30,point), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
        cv2.putText(img_test, str(point), (point,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
    cv2.circle(img_test, (0,point), 5, (9, 255, 0), -1)
    cv2.circle(img_test, (point,0), 5, (9, 255, 0), -1)    
for point in point_intersection:
    x = int(point[0])
    y = int(point[1])
    cv2.circle(img_test, (x,y), 5, (9, 255, 0), -1)
    text = "(" + str(x) + "," + str(y) + ")"
    cv2.putText(img_test, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow("Original Image", img_test)
while True:
    # Chờ và kiểm tra sự kiện phím được nhấn
    key = cv2.waitKey(1) & 0xFF

    # Nếu phím ESC (key code 27) được nhấn, hoặc nút Cancel được nhấn
    if key == 27 or key == ord('c'):
        break
cv2.destroyAllWindows()