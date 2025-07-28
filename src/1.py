import cv2

# 마우스 이벤트 처리 함수
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'좌표: ({x}, {y})')

# 흑백 이미지 하나 생성
image=cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image,dsize=None,fx=2,fy=2,)
  # 또는 np.zeros((500,500,3), dtype=np.uint8)

cv2.imshow('Image', image_big)

# 마우스 이벤트 등록
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
