def get_box_area(width,length,height):
    if width < 0 or length < 0 or height < 0 :
        return 0
    box_area = width * length * height
    return box_area

box1 = get_box_area(5,5,5) 
box2 = get_box_area(3,3,3)
box3 = get_box_area(-4,5,6)

print(box1,box2,box3)
