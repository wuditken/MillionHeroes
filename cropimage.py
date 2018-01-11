from PIL import Image

def crop(file):
	im = Image.open(r"D:\million\origin\\"+file)   
	img_size = im.size
	w = im.size[0]
	h = im.size[1]

	print("xx:{}".format(img_size))

	region = im.crop((70/1080*w,220/1920*h, w-70/1080*w,600/1920*h))    #裁剪的区域——问题
	saved_name_question = 'crop_question_'+file
	region.save("D:\million\crop\\"+saved_name_question)

	region = im.crop((70/1080*w,600/1920*h, w-70/1080*w,800/1920*h))    #裁剪的区域——选项
	saved_name_op_a = 'crop_op_a_'+file
	region.save("D:\million\crop\\"+saved_name_op_a)

	region = im.crop((70/1080*w,800/1920*h, w-70/1080*w,1000/1920*h))    #裁剪的区域——选项
	saved_name_op_b = 'crop_op_b_'+file
	region.save("D:\million\crop\\"+saved_name_op_b)

	region = im.crop((70/1080*w,1000/1920*h, w-70/1080*w,1200/1920*h))    #裁剪的区域——选项
	saved_name_op_c = 'crop_op_c_'+file
	region.save("D:\million\crop\\"+saved_name_op_c)

	return [saved_name_question, saved_name_op_a, saved_name_op_b, saved_name_op_c]